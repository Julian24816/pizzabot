<script>
    import {_} from "svelte-i18n";
    import {push} from 'svelte-spa-router';
    import {onMount} from "svelte";
    import Footer from "./Footer.svelte";

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
            alert($_("order.error"));
        }
    }

    function formatPizzaNames(orders, targetNumber) {
        let names = {};
        for (let order of orders) names[order.user_name] = (names[order.user_name] || 0) + 1;
        const nobody = targetNumber - Object.values(names).reduce((a, b) => a + b, 0)
        if (nobody > 0) names["nobody"] = nobody;
        let namesWithNumbers = Object.keys(names).map(name => `${name} ${names[name]}x`);
        return namesWithNumbers.join(', ');
    }

    onMount(() => {
        fetchOrders();
        fetchSolved();
    });
</script>


<h1>{ $_("order.title") }</h1>
<table>
    <thead>
    <tr>
        <th>{ $_("order.tableHeadings.name") }</th>
        <th>🥩</th>
        <th>🧀</th>
        <th>🍀</th>
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
                <button on:click={ () => deleteOrder(order.id) }>🗑️</button>
            </td>
        </tr>
    {/each}
    </tbody>
</table>

<button on:click={ () => push("/") }>➕</button>


<h1>{ $_("solved.title") }</h1>
<table>
    <thead>
    <tr>
        <th>{ $_("solved.tableHeadings.variant") }</th>
        <th>{ $_("solved.tableHeadings.who") }</th>
    </tr>
    </thead>
    <tbody>
    {#each solved as pizza}
        <tr>
            <td>
                { pizza.variant }
            </td>
            <td>
                { formatPizzaNames(pizza.assigned_orders, pizza.pieces) }
            </td>
        </tr>
    {/each}
    </tbody>
</table>


<br><br><br><br><br><br>
<Footer/>


<style>

    th {
        text-align: left;
    }

    td {
        padding-right: 1em;
    }

</style>