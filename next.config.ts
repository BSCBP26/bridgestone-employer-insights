import type { NextConfig } from 'next';
const isGithubPages = process.env.GITHUB_PAGES === 'true';
const config: NextConfig = {
  output: 'export',
  distDir: process.env.NODE_ENV === 'development' ? '.next-dev' : '.next',
  basePath: isGithubPages ? '/bridgestone-employer-insights' : '',
  assetPrefix: isGithubPages ? '/bridgestone-employer-insights/' : undefined,
  images: { unoptimized: true },
};
export default config;
