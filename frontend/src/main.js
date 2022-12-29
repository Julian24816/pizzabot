import App from './App.svelte';
import { initTranslations } from './translations/translationInit.js';

initTranslations();

const app = new App({
	target: document.body,
	props: {}
});

export default app;
