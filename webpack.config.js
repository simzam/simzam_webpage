const HtmlWebpackPlugin = require("html-webpack-plugin");
const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  mode: "development",
  entry: {
    bundle: ["./assets/js/index.js"],
    style: "./assets/scss/main.scss",
  },
  output: {
    path: path.resolve(__dirname, "simzam", "static", "webpack_bundles"),

    filename: "[name]-[hash].js",
    chunkFilename: "[name]-[hash]",
    clean: true
  },
  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          // Creates `style` nodes from JS strings
          "style-loader",
          // Translates CSS into CommonJS
          "css-loader",
          // Compiles Sass to CSS
          "sass-loader",
        ],
      },
    ],
  },
  plugins: [
    new BundleTracker({filename:"./webpack-stats.json"}),
    new HtmlWebpackPlugin({
      title: 'Output Management',
      inject: false
    })
  ],
  watchOptions: {
    aggregateTimeout: 200,
    poll: 1000,
    ignored: /node_modules/,
  },
  optimization: {
    // TODO: for some reason the line below creates a lot of uneccessary loading
    // runtimeChunk: 'single',
    splitChunks: {
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        },
      },
    }
  }
};
