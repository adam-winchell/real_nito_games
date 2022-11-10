import {writable} from 'svelte/store'

export const page = writable('Home');

export const menu_open = writable(false);