<script>

    import {link, push} from 'svelte-spa-router';
    import NumberWithArrows from "./inputs/NumberWithArrows.svelte";

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
            await push('/orders');
        } else {
            alert("Error creating order: " + orderResponse.error);
        }
    }

</script>


<h1>Create Order</h1>
<input type="text" required bind:value={order.user_name} placeholder="Name"/>
<div class="numberInput">
    <NumberWithArrows bind:value={order.number_of_pieces.meat} min={ 0 } placeholder="Number of meat pieces"/>
</div>
<div class="numberInput">
    <NumberWithArrows
            bind:value={order.number_of_pieces.vegetarian} min={ 0 } placeholder="Number of vegetarian pieces"/>
</div>
<div class="numberInput">
    <NumberWithArrows bind:value={order.number_of_pieces.vegan} min={ 0 } placeholder="Number of vegan pieces"/>
</div>
<button on:click={ createOrder }>Create Order</button>

<br><br><br><br><br>
<hr>
<a href="/orders" use:link>Orders</a>
<a href="/imprint" use:link>Imprint</a>


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