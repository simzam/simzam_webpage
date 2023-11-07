const path = require('path');
// const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  context: __dirname, // The base directory for resolving entry and output paths
  entry: {
    bundle: ['./assets/js/index.js'], // Entry point for your application
    style: ['./assets/styles/main.scss'],
  },
  output: {
    path: path.resolve('assets/webpack_bundles'), // Output directory for your bundle
    filename: '[name].[contenthash].js', // Output bundle file name
    clean: true
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ]
      }
    ]
  },
  plugins: [
    new BundleTracker({ filename: 'webpack-stats.json' }), // Generates a stats file for webpack-bundle-tracker
    new MiniCssExtractPlugin({ filename: 'styles.[contenthash].css' })
  ],
};
