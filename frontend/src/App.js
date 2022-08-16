import React from 'react';
import './App.css';

import axios from 'axios'

import Menu from './components/Menu.js'
import Header from './components/Header.js'
import Footer from './components/Footer.js'
import UserList from './components/User.js'


class App extends React.Component {
  constructor(props) {
    super(props)
    this.backend_url = 'http://127.0.0.1:8000/api/users'
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
    axios.get(this.backend_url)
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
        <Menu />
        <Header />
        <div className="container">
          <UserList users={this.state.users} />
        </div>
        <Footer />
      </main>
    )
  }
}

export default App;
