const path = require('path');
// const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname, // The base directory for resolving entry and output paths
  entry: {
    main: './assets/js/index.js', // Entry point for your application
  },
  output: {
    path: path.resolve('assets/webpack_bundles'), // Output directory for your bundle
    filename: 'bundle.[contenthash].js', // Output bundle file name
  },
  plugins: [
    new BundleTracker({ filename: 'webpack-stats.json' }), // Generates a stats file for webpack-bundle-tracker
  ],
};
