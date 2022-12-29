<script>

    import {_} from 'svelte-i18n';
    import {link, push} from 'svelte-spa-router';
    import NumberWithArrows from "./inputs/NumberWithArrows.svelte";
    import Footer from "./Footer.svelte";
    import editKeys, {saveEditKeys} from "../js/editKeys";

    let order = {
        user_name: "",
        number_of_pieces: {
            meat: 0,
            vegetarian: 0,
            vegan: 0
        },
    };

    async function createOrder() {
        const response = await fetch('/order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(order)
        });
        const orderResponse = await response.json();
        if (response.ok) {
            localStorage.setItem('orderID', orderResponse.id);
            editKeys[orderResponse.id] = orderResponse.edit_key;
            saveEditKeys();
            await push('/orders');
        } else {
            alert($_(
                `create.error.${orderResponse.error}`,
                {values: {variant: orderResponse.variant}}
            ));
        }
    }

</script>


<h1>{ $_("create.title") }</h1>
<input bind:value={order.user_name} placeholder={$_("create.placeholders.name")} required type="text"/>
<div class="numberInput">
    <label>🥩
        <NumberWithArrows bind:value={order.number_of_pieces.meat} min={ 0 }
                          placeholder={$_("create.placeholders.variants.meat")}/>
    </label>
</div>
<div class="numberInput">
    <label>🧀
        <NumberWithArrows
                bind:value={order.number_of_pieces.vegetarian} min={ 0 }
                placeholder={$_("create.placeholders.variants.vegetarian")}/>
    </label>
</div>
<div class="numberInput">
    <label>🍀
        <NumberWithArrows bind:value={order.number_of_pieces.vegan} min={ 0 }
                          placeholder={$_("create.placeholders.variants.vegan")}/>
    </label>
</div>
<button on:click={ createOrder }>✅🍕</button>

<br><br><br><br><br>
<Footer>
    <a href="/orders" use:link>{ $_("links.orders") }</a>
</Footer>


<style>

    input {
        display: block;
        margin-bottom: 10px;
        font-size: 1.5em;
    }

    .numberInput {
        margin: 8px 0;
    }

</style>