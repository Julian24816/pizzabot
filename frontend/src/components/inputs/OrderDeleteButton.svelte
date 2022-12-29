<script>
    import {_} from 'svelte-i18n';
    import editKeys from "../../js/editKeys";

    export let order;
    export let orders; // binding so that updates can be noticed

    async function deleteOrder(id) {
        const resp = await fetch(
            `/order/${id}`,
            {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({edit_key: editKeys[id]})
            }
        );
        if (resp.ok) {
            orders = orders.filter(order => order.id !== id);
        } else {
            alert($_("order.error"));
        }
    }
</script>


{#if editKeys[order.id]}
    <button on:click={() => deleteOrder(order.id)}>🗑️</button>
{/if}