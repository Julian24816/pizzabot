<script>

    import {_} from "svelte-i18n";
    import {link} from "svelte-spa-router";
    import LanguageChoice from "./inputs/LanguageChoice.svelte";

    async function clear() {
        if (!confirm("do you really want to clear all orders?")) return;
        const password = prompt("please enter the password:");
        const response = await fetch('/clear', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"password": password})
        });
        if (response.ok) {
            location.reload() // TODO JM -> PS any better ideas?
        } else {
            alert($_(
                `footer.clearError`,
                {values: {message: (await response.json()).error}}
            ));
        }
    }
</script>

<hr>
<LanguageChoice/>
<slot/>
<a href="/imprint" use:link>{ $_("footer.imprint") }</a>
<button on:click={ clear }>{ $_("footer.clearButton") }</button>
