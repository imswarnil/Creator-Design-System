/* =============================================================================
   FRAME & SIGNAL — After Effects template builder
   Generates a starter .aep scaffold (colour/type style guide, background
   pattern comps, and broadcast canvas templates with safe-area guides) from
   the tokens in src/1-foundation and src/4-broadcast of this design system.

   HOW TO RUN
     After Effects → File → Scripts → Run Script File… → pick this file.
     (Or drop it in AE's Scripts/ScriptUI Panels folder and run from the menu.)

   FONTS
     Install these first so the text layers pick them up automatically —
     all free, all on Google Fonts:
       Space Grotesk  https://fonts.google.com/specimen/Space+Grotesk
       Inter          https://fonts.google.com/specimen/Inter
       IBM Plex Mono  https://fonts.google.com/specimen/IBM+Plex+Mono
     If a font isn't found the script keeps going and lists it in the
     completion alert — reassign it in the Character panel, it's one click
     per text layer.

   This script only ADDS to app.project — it never touches an existing file
   on disk. Use File → Save As afterwards to keep it.
   ========================================================================== */

function hex(h) {
	h = h.replace('#', '');
	return [
		parseInt(h.substr(0, 2), 16) / 255,
		parseInt(h.substr(2, 2), 16) / 255,
		parseInt(h.substr(4, 2), 16) / 255
	];
}

// ── Tokens, mirrored from src/1-foundation/01-color.css ──────────────────
var INK = {
	'0': hex('#ffffff'), '50': hex('#f8f8fa'), '200': hex('#e5e5ea'),
	'400': hex('#a5a5b2'), '600': hex('#55556a'), '800': hex('#272734'),
	'900': hex('#191922'), '950': hex('#101017'), '1000': hex('#08080c')
};
var SIGNAL = {
	'100': hex('#ffe1db'), '300': hex('#ff9d89'), '500': hex('#f04e2e'),
	'700': hex('#b52810'), '900': hex('#6f1f12')
};
var CRAFT = { // amber
	'100': hex('#f9ecce'), '300': hex('#e8bd5c'), '400': hex('#d9a33a'), '700': hex('#78501f')
};
var MINT = { '50': hex('#eafaf1'), '500': hex('#16a06a'), '700': hex('#0b6444') };
var AZURE = { '50': hex('#eaf3ff'), '500': hex('#2b7bef'), '700': hex('#164ea3') };
var ROSE = { '50': hex('#fdeef1'), '500': hex('#d92d4e'), '700': hex('#931832') };
var WHITE = [1, 1, 1];

// ── Fonts, mirrored from src/1-foundation/02-typography.css ──────────────
// Lists of candidate PostScript names — the script tries each in order.
var F_DISPLAY_BOLD = ['SpaceGrotesk-Bold', 'Space Grotesk Bold', 'SpaceGrotesk'];
var F_DISPLAY_MED = ['SpaceGrotesk-Medium', 'Space Grotesk Medium', 'SpaceGrotesk'];
var F_BODY = ['Inter-Regular', 'Inter Regular', 'Inter'];
var F_BODY_SEMI = ['Inter-SemiBold', 'Inter SemiBold', 'Inter-Medium'];
var F_SLATE = ['IBMPlexMono-Medium', 'IBM Plex Mono Medium', 'IBMPlexMono', 'IBM Plex Mono'];

var WARNINGS = [];
var COMPS_BUILT = [];

// ── Utility layer builders ────────────────────────────────────────────────

function addBg(comp, color, name) {
	var solid = comp.layers.addSolid(color, name || 'BG', comp.width, comp.height, 1, comp.duration);
	solid.property('Position').setValue([comp.width / 2, comp.height / 2]);
	return solid;
}

function addText(comp, str, opts) {
	opts = opts || {};
	var layer = comp.layers.addText(str);
	var textProp = layer.property('Source Text');
	var doc = textProp.value;

	if (opts.font) {
		var fonts = opts.font;
		var applied = false;
		for (var i = 0; i < fonts.length; i++) {
			try { doc.font = fonts[i]; applied = true; break; } catch (e) {}
		}
		if (!applied) WARNINGS.push('Font not installed — reassign "' + (opts.label || str) + '" manually (tried: ' + fonts.join(', ') + ')');
	}
	if (opts.size) doc.fontSize = opts.size;
	if (opts.color) doc.fillColor = opts.color;
	if (opts.tracking !== undefined) { try { doc.tracking = opts.tracking; } catch (e) {} }
	if (opts.justification) doc.justification = opts.justification;
	textProp.setValue(doc);

	if (opts.position) layer.property('Position').setValue(opts.position);
	if (opts.name) layer.name = opts.name;
	return layer;
}

function addRectGuide(comp, name, w, h, cx, cy, strokeColor, strokeWidth) {
	var layer = comp.layers.addShape();
	layer.name = name;
	try { layer.guideLayer = true; } catch (e) {}
	var root = layer.property('ADBE Root Vectors Group');
	var group = root.addProperty('ADBE Vector Group');
	var gc = group.property('ADBE Vectors Group');
	var rect = gc.addProperty('ADBE Vector Shape - Rect');
	rect.property('ADBE Vector Rect Size').setValue([w, h]);
	var stroke = gc.addProperty('ADBE Vector Graphic - Stroke');
	stroke.property('ADBE Vector Stroke Color').setValue(strokeColor);
	stroke.property('ADBE Vector Stroke Width').setValue(strokeWidth || 2);
	layer.property('Position').setValue([cx, cy]);
	return layer;
}

function addDot(comp, name, d, cx, cy, color) {
	var layer = comp.layers.addShape();
	layer.name = name;
	var root = layer.property('ADBE Root Vectors Group');
	var group = root.addProperty('ADBE Vector Group');
	var gc = group.property('ADBE Vectors Group');
	var ellipse = gc.addProperty('ADBE Vector Shape - Ellipse');
	ellipse.property('ADBE Vector Ellipse Size').setValue([d, d]);
	var fill = gc.addProperty('ADBE Vector Graphic - Fill');
	fill.property('ADBE Vector Fill Color').setValue(color);
	layer.property('Position').setValue([cx, cy]);
	return layer;
}

function addRule(comp, name, w, cx, cy, color, weight) {
	var layer = comp.layers.addShape();
	layer.name = name;
	var root = layer.property('ADBE Root Vectors Group');
	var group = root.addProperty('ADBE Vector Group');
	var gc = group.property('ADBE Vectors Group');
	var rect = gc.addProperty('ADBE Vector Shape - Rect');
	rect.property('ADBE Vector Rect Size').setValue([w, weight || 4]);
	var fill = gc.addProperty('ADBE Vector Graphic - Fill');
	fill.property('ADBE Vector Fill Color').setValue(color);
	layer.property('Position').setValue([cx, cy]);
	return layer;
}

function addEffect(layer, name) {
	try {
		return layer.property('ADBE Effect Parade').addProperty(name);
	} catch (e) {
		WARNINGS.push('Could not add effect "' + name + '" on layer "' + layer.name + '": ' + e.toString());
		return null;
	}
}

function safeSet(effect, propName, value) {
	if (!effect) return;
	try { effect.property(propName).setValue(value); } catch (e) {
		WARNINGS.push('Could not set "' + propName + '" on effect "' + effect.name + '": ' + e.toString());
	}
}

// One layer, one Grid effect, Screen-blended so only the lines show
// regardless of what the effect fills behind them (mirrors --pattern-grid).
function addGridLayer(comp, name, cellSize, lineColor, opacityPct, wide) {
	var solid = comp.layers.addSolid([0, 0, 0], name, comp.width, comp.height, 1, comp.duration);
	solid.property('Position').setValue([comp.width / 2, comp.height / 2]);
	var fx = addEffect(solid, 'Grid');
	if (fx) {
		safeSet(fx, 'Size From', 3); // "Width & Height Sliders"
		safeSet(fx, 'Width', wide ? comp.width * 4 : cellSize);
		safeSet(fx, 'Height', cellSize);
		safeSet(fx, 'Border', 1);
		safeSet(fx, 'Color', lineColor);
	}
	solid.opacity.setValue(opacityPct);
	solid.blendingMode = BlendingMode.SCREEN;
	return solid;
}

function addFractalNoiseLayer(comp, name, opacityPct) {
	var solid = comp.layers.addSolid([0.5, 0.5, 0.5], name, comp.width, comp.height, 1, comp.duration);
	solid.property('Position').setValue([comp.width / 2, comp.height / 2]);
	var fx = addEffect(solid, 'Fractal Noise');
	if (fx) {
		safeSet(fx, 'Contrast', 140);
		safeSet(fx, 'Brightness', -25);
	}
	solid.opacity.setValue(opacityPct);
	return solid;
}

function addCellPatternLayer(comp, name, opacityPct, sizeVal) {
	var solid = comp.layers.addSolid([0, 0, 0], name, comp.width, comp.height, 1, comp.duration);
	solid.property('Position').setValue([comp.width / 2, comp.height / 2]);
	var fx = addEffect(solid, 'Cell Pattern');
	if (fx) {
		safeSet(fx, 'Contrast', 180);
		safeSet(fx, 'Size', sizeVal || 12);
	}
	solid.opacity.setValue(opacityPct);
	solid.blendingMode = BlendingMode.SCREEN;
	return solid;
}

function makeComp(project, name, w, h, dur, folder) {
	var comp = project.items.addComp(name, w, h, 1, dur, 30);
	comp.parentFolder = folder;
	COMPS_BUILT.push(name);
	return comp;
}

// =============================================================================
// BUILD
// =============================================================================

app.beginUndoGroup('Build Frame & Signal AE Template');

try {
	var project = app.project;
	var rootFolder = project.items.addFolder('Frame & Signal — AE Template');
	var folderGuide = project.items.addFolder('01 Style Guide'); folderGuide.parentFolder = rootFolder;
	var folderBG = project.items.addFolder('02 Backgrounds'); folderBG.parentFolder = rootFolder;
	var folderCanvas = project.items.addFolder('03 Canvases'); folderCanvas.parentFolder = rootFolder;
	var folderExample = project.items.addFolder('04 Examples'); folderExample.parentFolder = rootFolder;

	// ── 00 — Style Guide ─────────────────────────────────────────────────
	var guide = makeComp(project, '00 — Style Guide', 1920, 1080, 8, folderGuide);
	addBg(guide, INK['1000'], 'BG');

	addText(guide, 'DESIGN SYSTEM', {
		font: F_SLATE, size: 22, color: CRAFT['400'], tracking: 200,
		position: [100, 90], name: 'Eyebrow'
	});
	addText(guide, 'Style Guide', {
		font: F_DISPLAY_BOLD, size: 72, color: WHITE,
		position: [100, 160], name: 'Title'
	});

	function ramp(comp, label, dict, order, x, y) {
		addText(comp, label, { font: F_SLATE, size: 18, color: INK['400'], tracking: 100, position: [x, y - 24] });
		var chip = 96, gap = 12;
		for (var i = 0; i < order.length; i++) {
			var key = order[i];
			var cx = x + i * (chip + gap) + chip / 2;
			var cy = y + chip / 2;
			var solid = comp.layers.addSolid(dict[key], label + ' ' + key, chip, chip, 1, comp.duration);
			solid.property('Position').setValue([cx, cy]);
			addText(comp, key, {
				font: F_SLATE, size: 13, color: INK['400'],
				justification: ParagraphJustification.CENTER_JUSTIFY,
				position: [cx, cy + chip / 2 + 24]
			});
		}
	}

	ramp(guide, 'INK', INK, ['0', '50', '200', '400', '600', '800', '900', '950', '1000'], 100, 300);
	ramp(guide, 'SIGNAL', SIGNAL, ['100', '300', '500', '700', '900'], 100, 460);
	ramp(guide, 'CRAFT', CRAFT, ['100', '300', '400', '700'], 100, 620);
	ramp(guide, 'MINT · AZURE · ROSE', MINT, ['50', '500', '700'], 100, 780);
	ramp(guide, '', AZURE, ['50', '500', '700'], 424, 780);
	ramp(guide, '', ROSE, ['50', '500', '700'], 748, 780);

	// Typography specimen column
	var specX = 1180;
	addText(guide, 'Aa', {
		font: F_DISPLAY_BOLD, size: 140, color: SIGNAL['500'], position: [specX, 260]
	});
	addText(guide, 'DISPLAY · Space Grotesk 700', {
		font: F_SLATE, size: 16, color: INK['400'], tracking: 60, position: [specX, 300]
	});

	addText(guide, 'The quick brown fox jumps.', {
		font: F_BODY, size: 34, color: WHITE, position: [specX, 460]
	});
	addText(guide, 'BODY · Inter 400', {
		font: F_SLATE, size: 16, color: INK['400'], tracking: 60, position: [specX, 500]
	});

	addText(guide, 'TIMECODE · 00:12:04', {
		font: F_SLATE, size: 30, color: CRAFT['400'], tracking: 140, position: [specX, 640]
	});
	addText(guide, 'SLATE · IBM Plex Mono 500', {
		font: F_SLATE, size: 16, color: INK['400'], tracking: 60, position: [specX, 680]
	});

	// ── Backgrounds ──────────────────────────────────────────────────────
	var bgGrid = makeComp(project, 'BG — Grid', 1920, 1080, 10, folderBG);
	addBg(bgGrid, INK['1000'], 'BG');
	addGridLayer(bgGrid, 'Grid', 64, WHITE, 10);

	var bgBlueprint = makeComp(project, 'BG — Blueprint', 1920, 1080, 10, folderBG);
	addBg(bgBlueprint, INK['1000'], 'BG');
	addGridLayer(bgBlueprint, 'Grid Fine', 32, WHITE, 6);
	addGridLayer(bgBlueprint, 'Grid Major', 160, WHITE, 16);

	var bgDots = makeComp(project, 'BG — Dots', 1920, 1080, 10, folderBG);
	addBg(bgDots, INK['1000'], 'BG');
	addCellPatternLayer(bgDots, 'Dots', 14, 10);

	var bgScan = makeComp(project, 'BG — Scanline', 1920, 1080, 10, folderBG);
	addBg(bgScan, INK['1000'], 'BG');
	addGridLayer(bgScan, 'Scanlines', 6, WHITE, 8, true);

	var bgNoise = makeComp(project, 'BG — Noise', 1920, 1080, 10, folderBG);
	addBg(bgNoise, INK['1000'], 'BG');
	addFractalNoiseLayer(bgNoise, 'Grain', 18);

	// ── Canvases (broadcast safe areas, from src/4-broadcast) ───────────
	var thumb = makeComp(project, 'YouTube Thumbnail — 1280x720', 1280, 720, 6, folderCanvas);
	addBg(thumb, INK['1000'], 'BG');
	addBg(thumb, SIGNAL['900'], 'BloomTint').opacity.setValue(18);
	addRectGuide(thumb, 'GUIDE — safe (5.5% inset)', 1280 * 0.89, 720 * 0.89, 640, 360, CRAFT['400'], 2);
	addRectGuide(thumb, 'GUIDE — subject zone (right 36%)',
		1280 * 0.36, 720 * 0.89,
		1280 * (1 - 0.055) - (1280 * 0.36) / 2,
		360, AZURE['500'], 2);
	addDot(thumb, 'Channel mark', 20, 90, 660, SIGNAL['500']);
	addText(thumb, 'BUILD LOG', {
		font: F_SLATE, size: 18, color: CRAFT['400'], tracking: 160, position: [70, 590]
	});
	addText(thumb, 'Your Title Here', {
		font: F_DISPLAY_BOLD, size: 68, color: WHITE, position: [70, 640]
	});

	var banner = makeComp(project, 'YouTube Banner — 2560x1440', 2560, 1440, 6, folderCanvas);
	addBg(banner, INK['1000'], 'BG');
	addRectGuide(banner, 'GUIDE — TV crop (2560x1440, full canvas)', 2560 - 8, 1440 - 8, 1280, 720, INK['600'], 1);
	addRectGuide(banner, 'GUIDE — safe box (mobile crop, 1546x423)', 1546, 423, 1280, 720, SIGNAL['500'], 2);
	addText(banner, 'swarnil', {
		font: F_DISPLAY_BOLD, size: 90, color: WHITE,
		justification: ParagraphJustification.CENTER_JUSTIFY,
		position: [1280, 700]
	});
	addText(banner, 'BUILD · CREATE · SHIP', {
		font: F_SLATE, size: 22, color: INK['400'], tracking: 200,
		justification: ParagraphJustification.CENTER_JUSTIFY,
		position: [1280, 750]
	});

	var igPost = makeComp(project, 'Instagram Post — 1080x1080', 1080, 1080, 6, folderCanvas);
	addBg(igPost, INK['1000'], 'BG');
	addRectGuide(igPost, 'GUIDE — safe (5.5% inset)', 1080 * 0.89, 1080 * 0.89, 540, 540, CRAFT['400'], 2);
	addText(igPost, 'Your Headline', {
		font: F_DISPLAY_BOLD, size: 64, color: WHITE,
		justification: ParagraphJustification.CENTER_JUSTIFY,
		position: [540, 540]
	});

	var igStory = makeComp(project, 'Instagram Story — 1080x1920', 1080, 1920, 6, folderCanvas);
	addBg(igStory, INK['1000'], 'BG');
	// Top/bottom ~250px are covered by platform UI (profile bar, reply field).
	addRectGuide(igStory, 'GUIDE — UI-safe zone', 1080 - 120, 1920 - 500, 540, 960, CRAFT['400'], 2);
	addText(igStory, 'Your Headline', {
		font: F_DISPLAY_BOLD, size: 64, color: WHITE,
		justification: ParagraphJustification.CENTER_JUSTIFY,
		position: [540, 960]
	});

	// ── Example — composed title card ───────────────────────────────────
	var example = makeComp(project, 'Example — Title Card', 1920, 1080, 8, folderExample);
	var bgLayer = example.layers.add(bgGrid);
	bgLayer.property('Position').setValue([960, 540]);
	addRule(example, 'Accent rule', 6, 100 + 3, 470, SIGNAL['500'], 90);
	addText(example, 'BUILD LOG · EPISODE 04', {
		font: F_SLATE, size: 20, color: CRAFT['400'], tracking: 160, position: [130, 450]
	});
	addText(example, 'The headline that\rsells the video', {
		font: F_DISPLAY_BOLD, size: 76, color: WHITE, position: [130, 540]
	});
	addDot(example, 'Record dot', 16, 130, 640, SIGNAL['500']);
	addText(example, 'swarnil', {
		font: F_BODY_SEMI, size: 24, color: INK['400'], position: [155, 650]
	});

	var msg = 'Built ' + COMPS_BUILT.length + ' compositions:\n  ' + COMPS_BUILT.join('\n  ');
	if (WARNINGS.length) {
		msg += '\n\nWarnings (' + WARNINGS.length + '):\n  ' + WARNINGS.join('\n  ');
	} else {
		msg += '\n\nNo warnings — all fonts and effects applied cleanly.';
	}
	msg += '\n\nNow: File → Save As to keep this project.';
	alert(msg);

} catch (err) {
	alert('Script stopped with an error:\n' + err.toString() + (err.line ? ('\nLine: ' + err.line) : ''));
} finally {
	app.endUndoGroup();
}
