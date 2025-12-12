import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react-swc';
import path from 'path';

export default defineConfig({
    plugins: [react()],
    test: {
        environment: 'jsdom',
        setupFiles: ['./src/setupTests.ts'],
        globals: true,
        coverage: {
            provider: 'v8',
            reporter: ['text', 'json', 'html'],
        },
    },
    resolve: {
        alias: {
            'src': path.resolve(__dirname, './src'),
            '@': path.resolve(__dirname, './src'),
        },
    },
});