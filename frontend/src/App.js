import React from 'react';
import './App.css';

import axios from 'axios'
import {BrowserRouter, Route, Routes, Navigate} from 'react-router-dom'

import LoginForm from './LoginForm';
import Menu from './components/Menu'
import Footer from './components/Footer'
import UserList from './components/User'
import {ProjectList, ProjectDetails} from './components/Project'
import ToDoList from './components/ToDo'
import NotFound404 from './components/NotFound404.js'


class App extends React.Component {
  constructor(props) {
    super(props)
    this.api_url = 'http://127.0.0.1:8000'
    this.obtain_token_api_url = `${this.api_url}/api-token-auth/`
    this.projects_api_url = `${this.api_url}/api/projects`
    this.todos_api_url = `${this.api_url}/api/todos`
    this.users_api_url = `${this.api_url}/api/users`
    this.state = {
      'projects': [],
      'todos': [],
      'users': [],
      'token': '',
      'username': ''
    }
  }

  componentDidMount() {
    const token = localStorage.getItem('token')
    const username = localStorage.getItem('username')
    this.setState({
      'token': token,
      'username': username
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
          'username': login
        }, this.getData)
      }).catch(error => console.log(error))
  }

  getData() {
    let headers = this.getHeaders();
    axios.get(this.projects_api_url, {headers})
      .then(response => {
        const projects = response.data;
        this.setState(
          {'projects': projects.results}
        )
      }).catch(error => {
        console.log(error);
        this.setState(
          {'projects': []}
        )
      })
    axios.get(this.todos_api_url, {headers})
      .then(response => {
        const todos = response.data;
        this.setState(
          {'todos': todos.results}
        )
      }).catch(error => {
        console.log(error);
        this.setState(
          {'todos': []}
        )
      })
    axios.get(this.users_api_url, {headers})
      .then(response => {
        const users = response.data;
        this.setState(
          {'users': users.results}
        )
      }).catch(error => {
        console.log(error);
        this.setState(
          {'users': []}
        )
      })
  }

  getHeaders(){
    if (this.isAuth()){
      let headers = {'Authorization': `Token ${this.state.token}`};
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
      'username': ''
    }, this.getData)
  }

  render () {
    return (
      <main role="main">
        <BrowserRouter>
          <Menu username={this.state.username} isAuth={() => this.isAuth()} logout={() => this.logout()}/>
          <div className="container">
            <Routes>
              <Route exact path='/' element={<Navigate to='/projects' />} />
              <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)} />} />
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
