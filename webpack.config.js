const HtmlWebpackPlugin = require("html-webpack-plugin");
const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  mode: "none",
  entry: {
    bundle: "./assets/js/index.js",
    style: "./assets/scss/main.scss",
  },
  output: {
    path: path.resolve(__dirname, "simzam", "static", "webpack_bundles"),
    filename: "[name]-[fullhash].js",
    clean: true,
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
    })
  ],
};
