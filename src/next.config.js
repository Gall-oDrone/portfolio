/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['localhost','127.0.0.1', 'dgallo-portfolio.netlify.app', 'https://dgallo-portfolio.netlify.app/', 'dgallov-portfolio.vercel.app','https://dgallov-portfolio.vercel.app/'],
  },
}

module.exports = nextConfig
