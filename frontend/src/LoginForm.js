import React from 'react';


class LoginForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'login': '',
      'password': ''
    }
  }

  handleChange(event) { 
    this.setState({
       [event.target.name]: event.target.value
    })
  }

  handleSubmit(event) { 
    event.preventDefault();
    this.props.obtainAuthToken(this.state.login, this.state.password);
  }

  render () {
    return (
      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-xl-5 col-md-8">
            <div className="card px-5 py-5" id="form1">
              <form className="rounded" onSubmit={(event) => (this.handleSubmit(event))}>
                <div className="mb-3">
                  <label for="login" className="form-label">Login</label>
                  <input type="text" className="form-control" name="login" aria-describedby="loginHelp" value={this.state.login} onChange={(event) => this.handleChange(event)} />
                  <div id="loginHelp" className="form-text">Don't share your login with anyone else.</div>
                </div>
                <div className="mb-3">
                  <label for="password" className="form-label">Password</label>
                  <input type="password" className="form-control" name="password" value={this.state.password} onChange={(event) => this.handleChange(event)} />
                </div>
                <button type="submit" className="btn btn-block btn-primary text-center w-100">Submit</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default LoginForm;
