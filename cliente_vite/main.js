import './style.css'
import javascriptLogo from './javascript.svg'
import viteLogo from '/vite.svg'
import { setupCounter } from './counter.js'

// src/main.js
import { fetchPokemons, filterByType, searchPokemons } from './counter.js';

document.getElementById('load-pokemon-btn').addEventListener('click', fetchPokemons);
document.getElementById('type-filter').addEventListener('change', (event) => {
    filterByType(event.target.value);
});
document.getElementById('search-input').addEventListener('input', (event) => {
    searchPokemons(event.target.value);
});

