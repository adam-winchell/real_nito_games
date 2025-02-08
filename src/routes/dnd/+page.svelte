<section>
  <div class="dnd">
    <h2>Dungeons and Dragons Content</h2>
    <p>We are currently working on a Dungeons & Dragons module called Xem's Guide To the Underdark.
      Check back soon for more details. In the meantime, please check out our currently released content below.

      If you subscribe to our mailing list, we will send out discount codes on the release of new content. As a token
      of our appreciation check out this    
      <span class="reset-style"> 
        <a href="https://www.dmsguild.com/browse.php?discount=92aba439fd&src=mywebsite&affiliate_id=3603198"> 20% discount for <i>Xem's Guide to Exploration </i></a>
      </span>

    </p>
    <ul>
        <li>
            <a  href="https://www.dmsguild.com/product/448158/Xems-Guide-to-Exploration?affiliate_id=3603198&src=mywebsite">
                <strong>Xem's Guide to Exploration </strong>  written by Adam Winchell and Josh Ladd.
            </a>
        </li>
        <li>
            <a  href="https://www.dmsguild.com/product/422142/Extraordinary-Actions?affiliate_id=3603198&src=mywebsite">
                <strong>Extraordinary Actions </strong>  written by Adam Winchell and Josh Ladd.
            </a>
        </li>
        <li>
            <a href="https://mod.io/g/baldursgate3/m/xp-for-the-restless">
                <strong>XP for the Restless for Baldur's Gate 3</strong>  made by Adam Winchell
            </a>
        </li>
        <li>
            <a href="https://mod.io/g/baldursgate3/m/extraordinaryactions">
                <strong>Extraordinary Actions for Baldur's Gate 3</strong>  made by Adam Winchell
            </a>
        </li>
        <li>
            <a href="https://mod.io/g/baldursgate3/m/sanctuary-debuff">
                <strong>Sanctuary Debuff for Baldur's Gate 3</strong>  made by Adam Winchell
            </a>
        </li>
        <li>
            <a href="https://mod.io/g/baldursgate3/m/cure-wounds-bonus-action">
                <strong>Cure Wounds as a Bonus Action for Baldur's Gate 3</strong>  made by Adam Winchell
            </a>
        </li>
    </ul>
</div>

</section>

<script>
    import { onMount } from 'svelte';
    import {generate_encounter} from "./generate_encounters"

    // let myInput;

    // onMount(() => {
    //     // myInput.value = 'Hello world!';
    //     myInput.value = generate_encounter("twilight");
    // });

    
    // generate_encounter("twilight","randomEncounter")
    let zones = [
  {
    zone:"Twilight",
    text:generate_encounter("twilight"),
		visibility: -1
  },
  {
    zone:"Dusk",
    text:generate_encounter("dusk"),
		visibility: -1
  },

    {
    zone:"Gloom",
    text:generate_encounter("gloom"),
		visibility: -1
  }
]
</script>

<style>

    .reset-style, .reset-style * {
        all: revert;
        color: black;
    }

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