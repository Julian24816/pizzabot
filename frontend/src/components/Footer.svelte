<script>

    import {_} from "svelte-i18n";
    import {link} from "svelte-spa-router";
    import LanguageChoice from "./inputs/LanguageChoice.svelte";
</script>

<hr>
<LanguageChoice/>
<slot/>
<a href="/imprint" use:link>{ $_("links.imprint") }</a>
