<script>
    import Router from 'svelte-spa-router';
    import routes from './js/routes.js';
</script>

<main>
    <Router { routes }/>
</main>


<style>

    main {
        padding: 24px 16px;
    }

</style>
