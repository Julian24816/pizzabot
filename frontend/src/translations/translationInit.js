import { addMessages, init, getLocaleFromNavigator } from 'svelte-i18n';

import de from './de.json';
import en from './en.json';

const AVAILABLE_LANGUAGES = { en, de };
export const LANGUAGE_NAMES = {
    en: 'English',
    de: 'Deutsch (German)',
};

export function initTranslations() {
    for (const [locale, messages] of Object.entries(AVAILABLE_LANGUAGES)) {
        addMessages(locale, messages);
    }
    init({
        fallbackLocale: 'en',
        initialLocale: getLocaleFromNavigator(),
    });
}