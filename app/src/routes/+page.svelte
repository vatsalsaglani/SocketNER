<script>
    import {onMount} from "svelte"
    import TaggedText from "../components/TaggedText.svelte"
    let socket
    $: receive = 0
    $: result = []
    $: text = ""
    onMount(() => {
        socket = new WebSocket("ws://localhost:8000/ws/get-entities")
        
        receive += 1
    })
    const receiveMessages = () => {
        if (typeof socket !== "undefined") {
            console.log("RECEIVING MESSAGE")
            socket.onmessage = (event) => {
                console.log("MESSAGE: ", JSON.parse(event.data))
                result = [...JSON.parse(event.data)]
            }
        }
    }
    const sendMessage = (data) => {
        if (typeof socket !== "undefined") {
            console.log("SENDING MESSAGE")
            socket.send(data)
            receive += 1
        }
    }

    const onEnterText = (event) => {
        text = event.target.value
        if (text.length > 4){
            sendMessage(text)
        }
    }

    $: receive, receiveMessages()
</script>

<div class="px-4 py-5 mx-auto min-w-full min-h-screen flex flex-col justify-center items-center" >    
    <div
      class="rounded-2xl bg-gradient-to-r from-sky-500 via-teal-600 to-indigo-500 p-1 shadow-xl"
    >
      <div class="block rounded-xl bg-white p-6 sm:p-8">

        <div class="mt-2 sm:pr-8">
          <h3 class="text-xl font-bold text-gray-900">Blazing Fast NER with Web Sockets</h3>

          <p class="mt-2 text-sm text-gray-500">
            A WebSocket implementation of NER using FastAPI and HuggingFace transformers
          </p>
        </div>
        <div class="mt-2 sm:pr-8">
            <div class="rounded-sm bg-gradient-to-r from-sky-500 via-teal-600 to-indigo-500 py-1 shadow-xl" >
                <textarea on:input|preventDefault={(e) => onEnterText(e)} id="comment" rows="4" class="block px-1 py-1 w-full text-sm bg-white border-0 rounded-sm focus:ring-0 " placeholder="Enter Text" required></textarea>
            </div>
        </div>
        <div class="mt-2" >
            <TaggedText results={result} />
        </div>
      </div>
    </div>
</div>
