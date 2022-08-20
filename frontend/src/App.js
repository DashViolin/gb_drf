import React from 'react';
import './App.css';

import axios from 'axios'
import {BrowserRouter, Route, Routes, Navigate} from 'react-router-dom'

import Header from './components/Header'
import Menu from './components/Menu'
import Footer from './components/Footer'
import UserList from './components/User'
import {ProjectList, ProjectDetails} from './components/Project'
import ToDoList from './components/ToDo'
import NotFound404 from './components/NotFound404.js'


class App extends React.Component {
  constructor(props) {
    super(props)
    this.projects_backend_url = 'http://127.0.0.1:8000/api/projects'
    this.todos_backend_url = 'http://127.0.0.1:8000/api/todos'
    this.users_backend_url = 'http://127.0.0.1:8000/api/users'
    this.state = {
      'projects': [],
      'todos': [],
      'users': []
    }
  }

  componentDidMount() {
      axios.get(this.projects_backend_url)
        .then(response => {
          const projects = response.data
            this.setState(
              {
                'projects': projects.results
              }
          )
        }).catch(error => console.log(error))
      axios.get(this.todos_backend_url)
        .then(response => {
          const todos = response.data
            this.setState(
              {
                'todos': todos.results
              }
          )
        }).catch(error => console.log(error))
      axios.get(this.users_backend_url)
        .then(response => {
          const users = response.data
            this.setState(
              {
                'users': users.results
              }
          )
        }).catch(error => console.log(error))
    }

  render () {
    return (
      <main role="main">
        <BrowserRouter>
          <Menu />
          <Header />
          <div className="container">
            <Routes>
              <Route exact path='/' element={<Navigate to='/projects' />} />
              <Route path='/projects'>
                <Route index element={<ProjectList projects={this.state.projects} />} />
                <Route path=':projectId' element={<ProjectDetails projects={this.state.projects} />} />
              </Route>
              <Route exact path='/todos' element={<ToDoList todos={this.state.todos} />} />
              <Route exact path='/users' element={<UserList users={this.state.users} />} />
              <Route path='*' element={<NotFound404 />} />
            </Routes>
          </div>
        </BrowserRouter>
        <Footer />
      </main>
    )
  }
}

export default App;
