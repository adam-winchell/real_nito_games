import { redirect } from '@sveltejs/kit';

//   /**
//    * @type {import("@svelte/kit").Load}
//    */

export function load() {
    throw redirect(302, 'https://studio--studio-6551973043-b0204.us-central1.hosted.app/');
  }