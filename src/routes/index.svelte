<section>
    <div class="image-container">
        <img src="/adam_pierre.jpg" alt="profile">
    </div>
    
    <div class="info">
        <p>
            We are Adam Winchell and Pierre Delcourt from Real Nito Games. 
            We are an independent tabletop game design
            team based in Illinois and Washington, USA. 
            We hope you enjoy reading about our games!
        </p>
    </div>

    <div class="image-container">
        <img class="icon" src="/icon.png" alt="icon">
    </div>


</section>


<script>
    import {menu_open} from "../stores/store"
</script>


<style>
    section {
        flex-grow: 3;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .image-container {
        display: flex;
        flex-direction: column;
        justify-content: left;
        align-items: center;
    }

    img {
        border-radius: 15%;
        max-height: 45vh;
    }

    .info {
        max-width: 50%;
        margin: 25px;
        padding: 10px;
    }

    p {
        font-size: 1.5em;
    }

    .icon {
            max-height: 15vh;
            max-width: 90vw;
            border-radius: 50%;
        }
     


    @media only screen and (max-width: 640px) {
        section {
            flex-direction: column;
        }

        img {
            max-height: 25vh;
            max-width: 90vw;
            border-radius: 50%;
            margin-top: 10vh;
        }
        .info {
            max-width: 90%;
        } 

        .icon {
            max-height: 25vh;
            max-width: 20vw;
        }
    }
</style>