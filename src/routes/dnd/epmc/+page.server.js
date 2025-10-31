import { redirect } from '@sveltejs/kit';

//   /**
//    * @type {import("@svelte/kit").Load}
//    */

export function load() {
    throw redirect(302, 'https://colab.research.google.com/drive/14hnAx9MXJIv2_BGRJpXUWyICOnc9tdJ3#scrollTo=vpLvhsQLkTrA');
  }