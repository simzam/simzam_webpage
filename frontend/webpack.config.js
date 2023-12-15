const path = require('path');
// const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  context: __dirname, // The base directory for resolving entry and output paths
  entry: {
    bundle: ['./assets/js/index.js'], // Entry point for your application
    style: ['./assets/style/main.scss'],
  },
  output: {
    path: path.resolve('assets/webpack_bundles'), // Output directory for your bundle
    filename: '[name]-[contenthash].js', // Output bundle file name
  },
  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          // Creates `style` nodes from JS strings
          'style-loader',
          // Translates CSS into CommonJS
          'css-loader',
          // Compiles Sass to CSS
          'sass-loader',
<<<<<<< HEAD
        ]
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        type: 'asset/resource',
=======
        ],
>>>>>>> rewrite
      }
    ]
  },
  plugins: [
    new BundleTracker({ filename: 'webpack-stats.json' }), // Generates a stats file for webpack-bundle-tracker
    new MiniCssExtractPlugin({ filename: 'style.css' })
  ],
};
