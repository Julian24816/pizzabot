<script>

    import { link, push } from 'svelte-spa-router';

    let order = {
        user_name: "",
        number_of_meat_pieces: 0,
        number_of_vegetarian_pieces: 0,
        number_of_vegan_pieces: 0,
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
<input type="number" bind:value={order.number_of_meat_pieces} placeholder="Number of meat pieces"/>
<input type="number" bind:value={order.number_of_vegetarian_pieces} placeholder="Number of vegetarian pieces"/>
<input type="number" bind:value={order.number_of_vegan_pieces} placeholder="Number of vegan pieces"/>
<button on:click={ createOrder }>Create Order</button>


<a href="/orders" use:link>Orders</a>
