<script>
    import {link} from 'svelte-spa-router';

    async function fetchOrders() {
        const response = await fetch('/order');
        return await response.json();
    }
</script>


<a href="/" use:link>Create</a>


{#await fetchOrders() then orders}
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
            </tr>
        {/each}
        </tbody>
    </table>
{:catch error}
    <p>Failed to load orders</p>
{/await}