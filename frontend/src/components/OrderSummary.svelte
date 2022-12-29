<script>
    import {link} from 'svelte-spa-router';
    import {onMount} from "svelte";

    let orders = [];

    async function fetchOrders() {
        const response = await fetch('/order');
        orders = await response.json();
    }

    async function deleteOrder(id) {
        const resp = await fetch(`/order/${id}`, {method: 'DELETE'});
        if (resp.ok) {
            orders = orders.filter(order => order.id !== id);
        } else {
            alert('Error deleting order');
        }
    }

    onMount(() => {
        fetchOrders();
    });
</script>


<table>
    <thead>
    <tr>
        <th>Name</th>
        <th>Meat</th>
        <th>Vegetarian</th>
        <th>Vegan</th>
    </tr>
    </thead>
    <tbody>
    {#each orders as order}
        <tr>
            <td>
                { order.user_name }:
            </td>
            <td>
                { order.number_of_meat_pieces }
            </td>
            <td>
                { order.number_of_vegetarian_pieces }
            </td>
            <td>
                { order.number_of_vegan_pieces }
            </td>
            <td>
                <button on:click={ () => deleteOrder(order.id) }>Delete</button>
            </td>
        </tr>
    {/each}
    </tbody>
</table>


<a href="/" use:link>Create</a>
<a href="/imprint" use:link>Imprint</a>