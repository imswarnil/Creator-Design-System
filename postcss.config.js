import postcssImport from 'postcss-import';
import cssnano from 'cssnano';

export default (ctx) => ({
	plugins: [
		postcssImport(),
		ctx.env === 'production' && cssnano({ preset: ['default', { discardComments: { removeAll: true } }] }),
	].filter(Boolean),
});
