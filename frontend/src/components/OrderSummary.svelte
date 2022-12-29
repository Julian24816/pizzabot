<script>
    import {link} from 'svelte-spa-router';
    import {onMount} from "svelte";

    let orders = [];
    let solved = [];

    async function fetchOrders() {
        const response = await fetch('/order');
        orders = await response.json();
    }

    async function fetchSolved() {
        const response = await fetch('/solved');
        solved = await response.json();
    }

    async function deleteOrder(id) {
        const resp = await fetch(`/order/${id}`, {method: 'DELETE'});
        if (resp.ok) {
            orders = orders.filter(order => order.id !== id);
        } else {
            alert('Error deleting order');
        }
    }

    function formatPizzaNames(orders) {
        let names = {};
        for (let order of orders) names[order.user_name] = (names[order.user_name] || 0) + 1;
        let namesWithNumbers = Object.keys(names).map(name => `${name} ${names[name]}x`);
        return namesWithNumbers.join(', ');
    }

    onMount(() => {
        fetchOrders();
        fetchSolved();
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
                { order.number_of_pieces.meat }
            </td>
            <td>
                { order.number_of_pieces.vegetarian }
            </td>
            <td>
                { order.number_of_pieces.vegan }
            </td>
            <td>
                <button on:click={ () => deleteOrder(order.id) }>Delete</button>
            </td>
        </tr>
    {/each}
    </tbody>
</table>


<h1>Solved</h1>
<table>
    <thead>
    <tr>
        <th>Variant</th>
        <th>Who?</th>
    </tr>
    </thead>
    <tbody>
    {#each solved as pizza}
        <tr>
            <td>
                { pizza.variant }
            </td>
            <td>
                { formatPizzaNames(pizza.assigned_orders) }
            </td>
        </tr>
    {/each}
    </tbody>
</table>


<a href="/" use:link>Create</a>
<a href="/imprint" use:link>Imprint</a>