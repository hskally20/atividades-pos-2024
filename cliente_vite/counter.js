export function setupCounter(element) {
let counter = 0
const setCounter = (count) => {
  counter = count
  element.innerHTML = `count is ${counter}`
}
element.addEventListener('click', () => setCounter(counter + 1))
setCounter(0)
}



let currentPage = 1;
const pokemonsPerPage = 10;
let allPokemons = [];
let filteredPokemons = [];

// Função para carregar os Pokémon
async function loadPokemon() {
    try {
        const url = 'https://pokeapi.co/api/v2/pokemon?limit=150'; // Carregar um número maior para facilitar a busca e o filtro
        const response = await fetch(url);
        const { results: pokemons } = await response.json();

        // Carregar os detalhes de cada Pokémon para incluir tipos
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

// Função para renderizar os Pokémon na tela
function renderPokemons() {
    const pokemonContainer = document.getElementById('pokemon-container');
    pokemonContainer.innerHTML = ''; // Limpa o container anterior

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

// Função para renderizar a paginação
function renderPagination() {
    const paginationElement = document.getElementById('pagination').querySelector('.pagination');
    paginationElement.innerHTML = ''; // Limpa a paginação anterior

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

// Função para filtrar Pokémon por tipo
function filterByType(type) {
    if (type) {
        filteredPokemons = allPokemons.filter(pokemon => {
            return pokemon.types.some(pokemonType => pokemonType.type.name === type);
        });
    } else {
        filteredPokemons = allPokemons;
    }
    currentPage = 1; // Reseta para a primeira página ao filtrar
    renderPokemons();
    renderPagination();
}

// Função para buscar Pokémon
function searchPokemons() {
    const searchInput = document.getElementById('search-input').value.toLowerCase();
    filteredPokemons = allPokemons.filter(pokemon => pokemon.name.toLowerCase().includes(searchInput));
    currentPage = 1; // Reseta para a primeira página ao buscar
    renderPokemons();
    renderPagination();
}

// Adiciona eventos aos filtros e busca
document.getElementById('load-pokemon-btn').addEventListener('click', loadPokemon);
document.getElementById('type-filter').addEventListener('change', (event) => {
    filterByType(event.target.value);
});
document.getElementById('search-input').addEventListener('input', searchPokemons);
