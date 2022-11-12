import { sveltekit } from '@sveltejs/kit/vite';

const config = {
	plugins: [sveltekit()],
	server: {
		host: true,
		port: 5173
	}
};

export default config;
