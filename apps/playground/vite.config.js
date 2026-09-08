import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
export default defineConfig({ plugins: [sveltekit()], server: { host: '127.0.0.1', port: 4179, strictPort: true, fs: { strict: true } }, preview: { host: '127.0.0.1', port: 4179, strictPort: true } });
