import React from 'react'


class ToDoForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'text': '',
      'project': props.projects[0].id,
      'author': (props.users.find((user) => (user.username === props.username))).id
    }
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    })
  }

  handleProjectSelect(event) {
    this.setState({
      'project': event.target.selectedIndex
    })
  }

  handleSubmit(event) {
    this.props.createToDo(this.state.text, this.state.project, this.state.author)
    event.preventDefault()
  }

  render() {
    return (
      <form onSubmit={(event) => this.handleSubmit(event)}>
        <div className="mb-3">
          <label name="text">Text</label>
          <input type="text" className="form-control" name="text" placeholder="Task text"
            value={this.state.text} onChange={(event) => this.handleChange(event)} />
        </div>
        <div className="mb-3">
          <label name="projects">Pojects</label>
          <select name="projects" className='form-control' onChange={(event) => this.handleProjectSelect(event)} >
            {this.props.projects.map((item) => <option key={item.id} value={item.id}>{item.title}</option>)}
          </select>
        </div>
        <input type="submit" value="Create" className="btn btn-primary" />
      </form>
    );
  }
}

export default ToDoForm;
