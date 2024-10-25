import './style.css'
import javascriptLogo from './javascript.svg'
import viteLogo from '/vite.svg'
import { setupCounter } from './counter.js'

document.querySelector('#app').innerHTML = `
  <div>
    <a href="https://vite.dev" target="_blank">
      <img src="${viteLogo}" class="logo" alt="Vite logo" />
    </a>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
      <img src="${javascriptLogo}" class="logo vanilla" alt="JavaScript logo" />
    </a>
    <h1>Hello Vite!</h1>
    
    <div class="container mt-5">
        <h1 class="text-center mb-4">Lista de Pokémon</h1>
        
        <div class="d-flex justify-content-between mb-4">
            <input type="text" id="search-input" class="form-control" placeholder="Buscar Pokémon" />
            <select id="type-filter" class="form-select w-auto ms-2">
                <option value="">Todos os Tipos</option>
                <option value="grass">Grama</option>
                <option value="fire">Fogo</option>
                <option value="water">Água</option>
                <option value="bug">Inseto</option>
                <option value="normal">Normal</option>
                <option value="electric">Elétrico</option>
                <option value="ground">Terra</option>
                <option value="fairy">Fada</option>
                <option value="fighting">Lutador</option>
                <option value="psychic">Psíquico</option>
                <option value="rock">Pedra</option>
                <option value="ghost">Fantasma</option>
                <option value="dragon">Dragão</option>
                <option value="ice">Gelo</option>
                <option value="steel">Aço</option>
                <option value="dark">Sombrio</option>
            </select>
        </div>

        <div class="d-grid gap-2 col-6 mx-auto">
            <button id="load-pokemon-btn" class="btn btn-primary btn-lg">Carregar Pokémon</button>
        </div>

        <div id="pokemon-container" class="row mt-4"></div>

        <nav id="pagination" aria-label="Page navigation" class="mt-4">
            <ul class="pagination justify-content-center"></ul>
        </nav>
    </div>
`

setupCounter(document.querySelector('#counter'))
