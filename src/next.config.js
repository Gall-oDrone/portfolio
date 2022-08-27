const withPlugins = require('next-compose-plugins')
const optimizedImages = require('next-optimized-images')
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['localhost','127.0.0.1', 'dgallo-portfolio.netlify.app/'],
  },
}

module.exports = withPlugins([optimizedImages,nextConfig]);
