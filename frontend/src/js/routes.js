import CreateOrder from "../components/CreateOrder.svelte";
import OrderSummary from "../components/OrderSummary.svelte";
import Imprint from "../components/Imprint.svelte";
import Admin from "../components/Admin.svelte";

const routes = {
    '/': CreateOrder,
    '/admin': Admin,
    '/orders': OrderSummary,
    '/imprint': Imprint
};

export default routes;