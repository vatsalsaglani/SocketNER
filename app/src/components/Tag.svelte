<script>
    export let word
    export let tag

    let tag2color = {
        MIS: "red-200",
        PER: "green-300",
        ORG: "pink-300",
        LOC: "sky-300"
    }
</script>

<span class="space-y-2 space-x-1">
{#if tag === "other" }
    <span
    class={`inline-flex -mr-2 mb-0.5 items-center justify-center rounded-full px-2.5 py-0.5 text-sm text-gray-500`}
    >
        
        <p class="whitespace-nowrap text-sm">{word}</p>
    </span>
    {:else if tag === "MIS"}
    <span
    class={`inline-flex items-center mb-0.5 justify-center rounded-full bg-red-400 px-2.5 py-0.5 text-gray-500 shadow-lg`}
    >
    <p class="whitespace-nowrap rounded-full bg-red-200 px-2 text-sm mr-0.5 py-0.5" >{tag}</p>
    <p class="whitespace-nowrap text-md">{word}</p>
    </span>
    {:else if tag === "PER"}
    <span
    class={`inline-flex items-center mb-0.5 justify-center rounded-full bg-green-400 px-2.5 py-0.5 text-gray-500 shadow-lg`}
    >
        <p class="whitespace-nowrap rounded-full bg-green-200 px-2 text-sm mr-0.5 py-0.5" >{tag}</p>
        <p class="whitespace-nowrap text-md">{word}</p>
    </span>
    {:else if tag === "ORG"}
    <span
    class={`inline-flex items-center mb-0.5 justify-center rounded-full bg-pink-400 px-2.5 py-0.5 text-gray-500 shadow-lg`}
    >
    <p class="whitespace-nowrap rounded-full bg-pink-200 px-2 text-sm mr-0.5 py-0.5" >{tag}</p>
        <p class="whitespace-nowrap text-md">{word}</p>
    </span>
    {:else if tag === "LOC"}
    <span
    class={`inline-flex items-center mb-0.5 justify-center rounded-full bg-sky-400 px-2.5 py-0.5 text-gray-500 shadow-lg`}
    >
        <p class="whitespace-nowrap rounded-full bg-sky-200 px-2 text-sm mr-0.5 py-0.5" >{tag}</p>
        <p class="whitespace-nowrap text-md">{word}</p>
    </span>
{/if}
</span>