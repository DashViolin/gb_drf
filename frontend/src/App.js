import React from 'react';
import './App.css';

import axios from 'axios'
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'

import LoginForm from './LoginForm';
import Header from './components/Header';
import Menu from './components/Menu';
import Footer from './components/Footer';
import UserList from './components/User';
import ProjectList from './components/Project'
import ProjectForm from './components/ProjectForm';
import ProjectEditFormWrapped from './components/ProjectEditForm';
import ToDoList from './components/ToDo';
import ToDoForm from './components/ToDoForm';
import SearchBar from './components/SearchBar';
import NotFound404 from './components/NotFound404'


class App extends React.Component {
  constructor(props) {
    super(props)
    this.handleFilterTextChange = this.handleFilterTextChange.bind(this);
    this.srv_api_url = 'http://127.0.0.1:8000'
    this.obtain_token_api_url = `${this.srv_api_url}/api-token-auth/`
    this.projects_api_url = `${this.srv_api_url}/api/projects`
    this.todos_api_url = `${this.srv_api_url}/api/todos`
    this.users_api_url = `${this.srv_api_url}/api/users`
    this.state = {
      'projects': [],
      'todos': [],
      'users': [],
      'token': '',
      'username': '',
      'filterText': '',
      'redirect': false
    }
  }

  componentDidMount() {
    const token = localStorage.getItem('token')
    const username = localStorage.getItem('username')
    const redirect = !!token ? false : '/login'
    this.setState({
      'token': token,
      'username': username,
      'redirect': redirect
    }, this.getData)
  }

  obtainAuthToken(login, password) {
    axios
      .post(this.obtain_token_api_url, {
        'username': login,
        'password': password
      })
      .then(response => {
        const token = response.data.token;
        localStorage.setItem('token', token);
        localStorage.setItem('username', login);
        this.setState({
          'token': token,
          'username': login,
          'redirect': '/'
        }, this.getData)
      }).catch(error => console.log(error))
  }

  getData() {
    this.setState({
      'redirect': false
    })
    let headers = this.getHeaders();
    axios
      .get(this.projects_api_url, { headers })
      .then(response => {
        this.setState({
          'projects': response.data.results
        })
      })
      .catch(error => {
        console.log(error);
        this.setState({
          'projects': []
        })
      })
    axios
      .get(this.todos_api_url, { headers })
      .then(response => {
        this.setState({
          'todos': response.data.results
        })
      })
      .catch(error => {
        console.log(error);
        this.setState({
          'todos': []
        })
      })
    axios
      .get(this.users_api_url, { headers })
      .then(response => {
        this.setState({
          'users': response.data.results
        })
      })
      .catch(error => {
        console.log(error);
        this.setState({
          'users': []
        })
      })
  }

  getHeaders() {
    if (this.isAuth()) {
      let headers = {
        'Authorization': `Token ${this.state.token}`,
        'Accept': 'application/json; version=0.2'
      };
      return headers;
    }
    return {};
  }

  isAuth() {
    return !!this.state.token
  }

  logout() {
    localStorage.setItem('token', '')
    localStorage.setItem('username', '')
    this.setState({
      'token': '',
      'username': '',
      'redirect': '/'
    }, this.getData)
  }

  handleFilterTextChange(filterText) {
    this.setState({
      'filterText': filterText
    });
  }

  createToDo(text, project, author) {
    let headers = this.getHeaders()
    axios
      .post(`${this.todos_api_url}/`, { 'text': text, 'project': project, 'author': author }, { headers })
      .then(response => {
        this.setState({
          'redirect': '/todos'
        }, this.getData)
      })
      .catch(error => console.log(error))
  }

  deleteToDo(id) {
    const headers = this.getHeaders()
    axios
      .delete(`${this.todos_api_url}/${id}/`, { headers })
      .then(response => {
        this.setState({
          'todos': this.state.todos.filter((item) => item.id !== id)
        })
      })
      .catch(error => console.log(error))
  }

  createProject(title, repo, users) {
    const headers = this.getHeaders()
    axios
      .post(`${this.projects_api_url}/`, { 'title': title, 'repo': repo, 'users': users }, { headers })
      .then(response => {
        this.setState({
          'redirect': '/projects'
        }, this.getData)
      })
      .catch(error => console.log(error))
  }

  editProject(id, title, repo, users) {
    const headers = this.getHeaders()
    axios
      .put(`${this.projects_api_url}/${id}/`, {'title': title, 'repo': repo, 'users': users }, { headers })
      .then(response => {
        this.setState({
          'redirect': '/projects'
        }, this.getData)
      })
      .catch(error => console.log(error))
  }

  deleteProject(id) {
    const headers = this.getHeaders()
    axios
      .delete(`${this.projects_api_url}/${id}/`, { headers })
      .then(response => {
        this.setState({
          'projects': this.state.projects.filter((item) => item.id !== id)
        })
      })
      .catch(error => console.log(error))
  }

  render() {
    return (
      <main role="main">
        <BrowserRouter>
          {this.state.redirect ? <Navigate to={this.state.redirect} /> : <div />}
          <Menu
            username={this.state.username}
            isAuth={() => this.isAuth()}
            logout={() => this.logout()}
          />
          <div className="container">
            <Routes>
              <Route exact path='/'
                element={<Navigate to='/projects' />}
              />
              <Route exact path='/login'
                element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)} />}
              />
              <Route exact path='/projects/create'
                element={<ProjectForm
                  users={this.state.users}
                  createProject={(title, repo, users) => this.createProject(title, repo, users)}
                />}
              />
              <Route path='/projects'>
                <Route index
                  element={<>
                    <Header />
                    <SearchBar
                      filterText={this.state.filterText}
                      onFilterTextChange={this.handleFilterTextChange}
                    />
                    <ProjectList
                      projects={this.state.projects}
                      filterText={this.state.filterText}
                      deleteProject={(id) => this.deleteProject(id)}
                    />
                  </>}
                />
                <Route path=':projectId'
                  element={<ProjectEditFormWrapped
                    users={this.state.users}
                    projects={this.state.projects}
                    editProject={(id, text, project, author) => this.editProject(id, text, project, author)}
                  />}
                />
              </Route>
              <Route exact path='/todos/create'
                element={<ToDoForm
                  projects={this.state.projects}
                  users={this.state.users}
                  username={this.state.username}
                  createToDo={(text, project, author) => this.createToDo(text, project, author)}
                />}
              />
              <Route path='/todos'
                element={<ToDoList
                  todos={this.state.todos}
                  deleteToDo={(id) => this.deleteToDo(id)}
                />}
              />
              <Route exact path='/users'
                element={<UserList users={this.state.users} />}
              />
              <Route path='*'
                element={<NotFound404 />}
              />
            </Routes>
          </div>
        </BrowserRouter>
        <Footer />
      </main>
    )
  }
}

export default App;
