<section>
    <div  class="wedding_whiz">


        <h1>Coming Soon</h1>

        <p>More details on Wedding Whiz coming soon!</p>
    </div>
</section>

<style>

    section {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        padding: 20px;
        margin-top: 8vh;

    }

    h2 {
        margin-bottom: 10px;
    }

    .wedding_whiz {
        flex-grow: 0;
        max-width: 80%;
        margin: 0 auto;
        padding: 10px;
    }

    a {
        text-decoration: underline;
        color: black;        
    }

    li {
        margin-left: 3%;
        margin-bottom: 5px;
    }

    a:hover {
        text-decoration: underline;
    }

    .wedding_whiz p {
        margin-left: 1%;
        font-size: 1.5em;
    }

    .wedding_whiz iframe {
        margin-left: 1%;
    }

    .title {
        max-height: 25vh;
        max-width: 90vw;
        margin-top: 2vh;
    }

    .title_container{
        position: relative;
        text-align: center;
    }


    button{
        /* color:aqua; */
        background-color: #0d7d1a;
        border: #0d7d1a;
        color: white;
        font-weight: bold;
        /* width: 30%; */
        font-size: x-large;
        padding: 2%;
        border-radius: 5px;
    }

    button:hover{
        background-color: white;
        color: #0d7d1a;
    }

    h3{
        text-align: center;
        left: 100%;
    }

        iframe {
            width: 100vh; 
            height: 50vh;
            /* max-height: 25vh;
            max-width: 90vw; */
        }


        @media only screen and (max-width: 640px) {

        .title {
        max-height: 15vh;
        max-width: 90vw;

    }

        iframe {
            max-width: 75vw;
            max-height: 25vh;
        }

    }

</style>