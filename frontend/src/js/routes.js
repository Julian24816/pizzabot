import CreateOrder from "../components/CreateOrder.svelte";
import OrderSummary from "../components/OrderSummary.svelte";

const routes = {
    '/': CreateOrder,
    '/orders': OrderSummary
};

export default routes;