<script>

    import {LANGUAGE_NAMES} from "../../translations/translationInit";
    import {locale} from "svelte-i18n";

    $: localStorage.setItem("locale", $locale);

</script>

{#each Object.keys(LANGUAGE_NAMES) as lang}
    <button on:click={ () => $locale = lang }>{LANGUAGE_NAMES[lang]}</button>
{/each}