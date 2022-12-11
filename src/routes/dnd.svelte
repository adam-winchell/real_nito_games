<section>
  <div class="dnd">
    <h2>Dungeons and Dragons Content</h2>
    <p>We are currently working on a Dungeons & Dragons module called Xem's Guide To the Underdark.
      Check back soon for more details. In the meantime, please check out our currently released content below.
    </p>
    <ul>
        <li>
            <a target="_self" href="games/Extrodinary_Actions.pdf">
                <strong>Extraordinary Actions </strong>  written by Adam Winchell and Josh Ladd.
            </a>
        </li>
        <li>
            <a target="_self" href="https://github.com/adam-winchell/Xem-s-Guide-To-the-Underdark-PDFs/blob/main/output/XGU_Players_Supplement.pdf">
                <strong>Xem's Guide To the Underdark Players Supplement </strong>  written by Adam Winchell and Josh Ladd.
            </a>
        </li>
    </ul>
</div>
<div id="example-visualization" style='width: 100%'></div>
    </section>

<svelte:head>
    <link rel="stylesheet" href="/src/webweb/style.css">
    <script type="text/javascript" src="src/webweb/Blob.js"></script>
    <script type="text/javascript" src="src/webweb/colors.js"></script>
    <script type="text/javascript" src="src/webweb/d3.v5.min.js"></script>
    <script type="text/javascript" src="src/webweb/FileSaver.min.js"></script>
    <script type="text/javascript">
        // var wwdata;
        // fetch('src/stores/viz.json')
        // .then(response => response.json())
        // .then(data => {wwdata = data})
        // console.log(wwdata);
        //TODO the above is not JSON its a string  
    
        var wwdata = {"display":{"attachWebwebToElementWithId":"example-visualization"},"networks":{"webweb":{"layers":[{"edgeList":[[0,1],[1,2],[2,3],[3,4],[4,5]],"metadata":null,"nodes":{}}]}},"title":"webweb"};
        // wwdata.display.attachWebwebToElementWithId = "example-visualization";
        wwdata.display.w = 250;
        wwdata.display.h = 250;

        //window.onload is not being called below unless developer tools open
        </script>
        <!-- <script type="text/javascript" src="src/webweb/webweb.v5.js?1565662230803397000"></script> -->
        <script type="text/javascript" src="src/webweb/webweb.v5.js?1565662230803397000"></script>
</svelte:head>


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

    .bizarre_bazaar {
        flex-grow: 0;
        max-width: 80%;
        margin: 0 auto;
        padding: 10px;
    }

    .dnd {
        flex-grow: 1;
        width: 80%;
        /* max-width: 80%; */
        margin: 0 auto;
        padding: 10px;
        /* margin-left: 15px; */
        /*display: flex;
        flex-direction: column; */
        /* justify-content: left; */
    }


    a {
        text-decoration: underline;
        color: black;       
        font-size: 1.5em; 
    }

    li {
        margin-left: 3%;
        margin-bottom: 5px;
    }

    a:hover {
        text-decoration: underline;
    }

    .dnd p {
        margin-left: 1%;
        font-size: 1.5em;
    }

    
</style>