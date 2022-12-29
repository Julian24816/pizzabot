import CreateOrder from "../components/CreateOrder.svelte";
import OrderSummary from "../components/OrderSummary.svelte";
import Imprint from "../components/Imprint.svelte";

const routes = {
    '/': CreateOrder,
    '/orders': OrderSummary,
    '/imprint': Imprint
};

export default routes;