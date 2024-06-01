function loadCustomNavbar() {
    var customNavBar = `
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <!-- icono o nombre -->

      <a class="navbar-brand" href="#">
        <img src="./assets/IMG/carniceria2.png" alt="" width="70" height="70">
        <span class="text-warning"></span>
      </a>

      <!-- boton del menu -->

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- elementos del menu colapsable -->

      <div class="collapse navbar-collapse" id="menu">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Inicio</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown"
              aria-expanded="false">
              Productos
            </a>

            <ul class="dropdown-menu bg-secondary" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="Ave.html">Ave</a></li>
              <li><a class="dropdown-item" href="Cerdo.html">Cerdo</a>
              <li>
              <li><a class="dropdown-item" href="Vacuno.html">Vacuno</a></li>
            </ul>
          </li>
        </ul>
        <hr class="d-md-none text-white-50">
        <form class="d-flex" role="search">
          <input class="form-control me-1" type="search" placeholder="Necesitas algo?" aria-label="Search">
          <button class="btn btn-outline-success" type="submit" style="margin-right: 20px;">Buscar</button>
        </form>
        <i class="fa-solid fa-cart-plus fa-xl" style="color: #ffffff; margin-right: 20px;"></i>
        <i class="fa-regular fa-user fa-xl" style="color: #ffffff; margin-right: 20px;"></i>
      
      <!-- Button trigger modal -->
      <button type="button" class="btn btn-primary" 
      data-bs-toggle="modal" data-bs-target="#logindemo">
          Ingresar
      </button>
      <!-- Modal -->
      <div id="logindemo" class="modal fade">        
        <div class="modal-dialog modal-dialog-centered">        
          <div class="modal-content">
            <div class="modal_body">
              <button 
                type="button" 
                class="btn-close btn-close-white"
                data-bs-dismiss="modal"
              ></button>
              <div class="myform bg-dark">
                <h2 class="text-center">Acceso Cliente</h2>
                <form action="#">
                  <div class="mb-3 mt-3"> 
                    <label for="email">Correo Electrónico </label>
                    <input type="email" class="form-control"/>
                  </div>
                  <div class="mb-3 mt-3">
                    <label for="email">Contraseña</label>
                    <input type="contraseña" class="form-control"/>
                  </div>
                  <button type="button" class="btn btn-light mt-3 ">Ingresar</button>
                  <p>No eres Miembro<a href="#"> Regístrate</a></p>
                </form>
              </div>  
          </div>
        </div>
      </div>
      </div>
    </div>
  
  </nav>
    `;
    var customNabBarHTML = document.getElementById("custom-navbar");
    customNabBarHTML.innerHTML = customNavBar;
}

loadCustomNavbar();