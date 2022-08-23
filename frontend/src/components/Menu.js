import { NavLink } from 'react-router-dom'


const Menu = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        <a className="navbar-brand" href="/">Task manager</a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink to="/projects" className="nav-link" >Projects</NavLink>
            </li>
            <li className="nav-item">
              <NavLink to="/todos" className="nav-link" >ToDos</NavLink>
            </li>            
            <li className="nav-item">
              <NavLink to="/users" className="nav-link" >Users</NavLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Menu
