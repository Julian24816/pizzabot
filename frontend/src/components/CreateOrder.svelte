<script>

    import {link, push} from 'svelte-spa-router';

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
<input bind:value={order.number_of_pieces.meat} placeholder="Number of meat pieces" type="number"/>
<input bind:value={order.number_of_pieces.vegetarian} placeholder="Number of vegetarian pieces" type="number"/>
<input bind:value={order.number_of_pieces.vegan} placeholder="Number of vegan pieces" type="number"/>
<button on:click={ createOrder }>Create Order</button>


<a href="/orders" use:link>Orders</a>
<a href="/imprint" use:link>Imprint</a>
