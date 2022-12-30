<script>
    import {_} from "svelte-i18n";
    import {push} from 'svelte-spa-router';
    import {onMount} from "svelte";
    import Footer from "./Footer.svelte";
    import OrderDeleteButton from "./inputs/OrderDeleteButton.svelte";

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

    function formatOrderedByNames(orders, targetNumber) {
        let names = {};
        for (let order of orders) names[order.user_name] = (names[order.user_name] || 0) + 1;
        const nobody = targetNumber - Object.values(names).reduce((a, b) => a + b, 0)
        if (nobody > 0) names["🗑️😉"] = nobody;
        let namesWithNumbers = Object.keys(names).map(name => `${name} ${names[name]}x`);
        return namesWithNumbers.join(", ");
    }

    function formatPizzaVariantCounts(pizzas) {
        let types = {}
        for (let pizza of pizzas) types[pizza.variant] = (types[pizza.variant] || 0) + 1;
        let typesWithNumbers = Object.keys(types).map(name => `${types[name]}x ${name}`);
        return typesWithNumbers.join(", ");
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
                <OrderDeleteButton {order} bind:orders/>
            </td>
        </tr>
    {/each}
    </tbody>
</table>

<button on:click={ () => push("/") }>➕</button>


<h1>{ $_("solved.title") }</h1>

<p>
    {#if solved.length === 0}
        { $_("solved.count.none") }
    {:else if solved.length === 1}
        { $_("solved.count.single") }
    {:else}
        { $_("solved.count.multiple", {values: {count: solved.length}}) }
    {/if}
    ({ formatPizzaVariantCounts(solved) })
</p>

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
                { formatOrderedByNames(pizza.assigned_orders, pizza.pieces) }
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