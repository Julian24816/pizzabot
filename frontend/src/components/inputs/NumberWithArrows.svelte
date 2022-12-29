<script>

    export let value;
    export let placeholder = undefined;
    export let min = undefined;
    export let max = undefined;

    function up() {
        if (max === undefined || value < max) {
            value++;
        }
    }

    function down() {
        if (min === undefined || value > min) {
            value--;
        }
    }

</script>


<button on:click={ up }>⬆️</button>
<input { max } { min } { placeholder } bind:value type="number"/>
<button on:click={ down }>⬇️</button>
