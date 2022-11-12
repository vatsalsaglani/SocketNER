<script>
	import { each } from "svelte/internal";

    import Tag from "./Tag.svelte";

    // export let text
    export let results
</script>

<div class=" max-w-screen-md">
    <!-- <h5>{text}</h5> -->
    <div class="">

        { #each results as result, i}
            <Tag word={result.text.trim()} tag={result.entity} />
        {/each}
    </div>
</div>