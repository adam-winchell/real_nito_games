<a class="contact-icon" href={url}>
    <img src={"/" + icon + ".svg"} alt="google scholar">
</a>


<script>
    export let url = "http://github.com/"
    export let icon = "github"
</script>

<style>
    .contact-icon {
        margin: auto 3vw;
        padding: 1vh 1vw;
    }
    .contact-icon img {
        height: 4vh;
    }

    .contact-icon:hover {
        border-radius: 5%;
        background-color: var(--nav);
    }

</style>