
<main>
    <NavBar />
    <slot />
    <footer>
        <FooterItem icon="youtube" url="https://www.youtube.com/channel/UCXdbmCHPcSW_UF_h7EeXrTA"/>
        <FooterItem icon="email" url="mailto:realnitogames@gmail.com" />
    </footer>
</main>

<script>
    import FooterItem from "../components/FooterItem.svelte"
    import NavBar from "../components/NavBar.svelte"
</script>

<style>

    :root {
        --bg: #dffce7;
        --nav: #0d7d1a;
    }

    main {
        width: 100vw;
        min-height: 100vh;
        height: 100%;

        display: flex;
        flex-direction: column;
        background-color: var(--bg);
    }

    footer {
        width: 100%;
        flex-grow: 1;
        max-height: 7vh;
        display: flex;
        justify-content: center;
        align-items: center;
        bottom: 0; 
        padding-bottom: 10px;
    }

    @media only screen and (max-width: 640px) {
        main {
            max-height: 100%;
            height: 100%;
        }
    }
</style>