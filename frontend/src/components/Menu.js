import React from 'react';
import { NavLink } from 'react-router-dom'


class Menu extends React.Component {
  capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
  }
  // <nav className="navbar navbar-expand-lg navbar-light bg-light"></nav>
  render () {
    return (
      <nav className="navbar navbar-expand-md navbar-light bg-light">
        <div className="container-fluid">
          <a className="navbar-brand abs" href="/">Task manager</a>
          <button className="navbar-toggler ms-auto" type="button" data-bs-toggle="collapse" data-bs-target="#collapseNavbar">
              <span className="navbar-toggler-icon"></span>
          </button>
          <div className="navbar-collapse collapse" id="collapseNavbar">
            <ul className="navbar-nav ms-auto">
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
            <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  {
                    this.props.isAuth()
                    ? <NavLink to="/" className="nav-link" onClick={this.props.logout}>{`${this.capitalize(this.props.username)} (logout)`}</NavLink>
                    : <NavLink to="/login" className="nav-link">Login</NavLink>
                  }
                </li>
              </ul>
          </div>
        </div>
      </nav>
    )
  }
}

export default Menu;
