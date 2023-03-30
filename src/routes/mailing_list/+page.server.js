import { redirect } from '@sveltejs/kit';

//   /**
//    * @type {import("@svelte/kit").Load}
//    */

export function load() {
    throw redirect(302, 'https://mailchi.mp/352c8f713e56/mailing-list');
  }