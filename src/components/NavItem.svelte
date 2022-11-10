<a on:click={update_page} class={active ? "active" : "inactive"} href={url}>
    <span>{name}</span>
</a>

<script>
    import { page, menu_open } from "../stores/store.js"

    export let name = "Home"
    export let url = "/"
    export let prevent_default = false;

    let active = $page == name;
    $: {
        active = $page == name;
    }


    const update_page = () => {
        if (prevent_default !== true){
            page.set(name)
        }
    }
</script>


<style>
    a {
        text-decoration: none;
        color: white;
        flex-grow: 1;
        min-width: 9vw;
        max-width: 13vw;
        padding: 10px;
        border-radius: 5px;
        margin-left: 5px;
        margin-right: 5px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    a:hover {
        background-color: var(--bg);
        color: var(--nav);
    }

    .active {
        background-color: var(--bg);
        color: var(--nav);
    }  

    .inactive {
        background-color: var(--nav);
        color: var(--bg);
    }

    @media only screen and (max-width: 640px) {
        a {
            max-width: 100%;
            width: 95vw;
            margin: 1vh 1vw;
            display: none;
        }
    }
</style>