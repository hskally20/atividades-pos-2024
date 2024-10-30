export function setupCounter(element) {
let counter = 0
const setCounter = (count) => {
  counter = count
  element.innerHTML = `count is ${counter}`
}
element.addEventListener('click', () => setCounter(counter + 1))
setCounter(0)
}



// src/dom.js
let currentPage = 1;
const pokemonsPerPage = 10;
let allPokemons = [];
let filteredPokemons = [];


const API_URL = 'https://pokeapi.co/api/v2/pokemon?limit=150';

export async function fetchPokemons() {
    try {
        const response = await fetch(API_URL);
        const { results: pokemons } = await response.json();
        
        allPokemons = await Promise.all(pokemons.map(async (pokemon) => {
            const detailsResponse = await fetch(pokemon.url);
            return detailsResponse.json();
        }));

        filteredPokemons = allPokemons;
        renderPokemons();
        renderPagination();
    } catch (error) {
        console.error('Erro ao buscar os Pokémon:', error);
        alert('Não foi possível carregar os Pokémon.');
    }
}

function renderPokemons() {
    const pokemonContainer = document.getElementById('pokemon-container');
    pokemonContainer.innerHTML = '';

    const start = (currentPage - 1) * pokemonsPerPage;
    const end = start + pokemonsPerPage;
    const pokemonsToDisplay = filteredPokemons.slice(start, end);

    pokemonsToDisplay.forEach(pokemon => {
        const card = document.createElement('div');
        card.className = 'col-md-4 mb-4';
        card.innerHTML = `
            <div class="card pokemon-card">
                <img src="${pokemon.sprites.front_default}" class="card-img-top pokemon-img" alt="${pokemon.name}">
                <div class="card-body">
                    <h5 class="card-title">${pokemon.name}</h5>
                    <p><strong>ID:</strong> ${pokemon.id}</p>
                    <p><strong>Altura:</strong> ${pokemon.height / 10} m</p>
                    <p><strong>Peso:</strong> ${pokemon.weight / 10} kg</p>
                    <p><strong>Tipos:</strong> ${pokemon.types.map(type => type.type.name).join(', ')}</p>
                    <p><strong>Habilidades:</strong> ${pokemon.abilities.map(ability => ability.ability.name).join(', ')}</p>
                </div>
            </div>
        `;
        pokemonContainer.appendChild(card);
    });

    if (pokemonsToDisplay.length === 0) {
        pokemonContainer.innerHTML = '<p class="text-center">Nenhum Pokémon encontrado.</p>';
    }
}

function renderPagination() {
    const paginationElement = document.getElementById('pagination').querySelector('.pagination');
    paginationElement.innerHTML = '';

    const pageCount = Math.ceil(filteredPokemons.length / pokemonsPerPage);
    for (let i = 1; i <= pageCount; i++) {
        const pageItem = document.createElement('li');
        pageItem.className = 'page-item' + (i === currentPage ? ' active' : '');
        pageItem.innerHTML = `<a class="page-link" href="#">${i}</a>`;
        pageItem.querySelector('a').addEventListener('click', (event) => {
            event.preventDefault();
            currentPage = i;
            renderPokemons();
            renderPagination();
        });
        paginationElement.appendChild(pageItem);
    }
}

export function filterByType(type) {
    if (type) {
        filteredPokemons = allPokemons.filter(pokemon => {
            return pokemon.types.some(pokemonType => pokemonType.type.name === type);
        });
    } else {
        filteredPokemons = allPokemons;
    }
    currentPage = 1;
    renderPokemons();
    renderPagination();
}

export function searchPokemons(searchInput) {
    filteredPokemons = allPokemons.filter(pokemon => pokemon.name.toLowerCase().includes(searchInput.toLowerCase()));
    currentPage = 1;
    renderPokemons();
    renderPagination();
}
