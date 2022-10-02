import React from 'react'
import { useParams } from 'react-router-dom';
 

class ProjectEditForm extends React.Component {
  constructor(props) {
    super(props)
    const project = this.props.projects.find((project) => (project.id === parseInt(this.props.params.projectId)));
    let users_ids = []
    project.users.forEach((user) => {
      users_ids.push(user.id);
    })

    this.state = {
      'id': project.id,
      'title': project.title,
      'repo': project.repo,
      'users': users_ids
    }
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleUsersSelect(event) {
    if (!event.target.selectedOptions) {
      this.setState({
        'users': []
      })
      return;
    }

    let users = []
    for (let option of event.target.selectedOptions) {
      users.push(parseInt(option.value))
    }
    this.setState({
      'users': users
    })
  }

  handleSubmit(event) {
    this.props.editProject(this.state.id, this.state.title, this.state.repo, this.state.users)
    event.preventDefault()
  }

  render() {
    return (
      <form onSubmit={(event) => this.handleSubmit(event)}>
        <div className="mb-3">
          <label name="title">Title</label>
          <input name="title" type="text" className="form-control" placeholder="Project title"
            value={this.state.title} onChange={(event) => this.handleChange(event)} />
        </div>
        <div className="mb-3">
          <label name="repo">Repo link</label>
          <input name="repo" type="text" className="form-control" placeholder="http://"
            value={this.state.repo} onChange={(event) => this.handleChange(event)} />
        </div>
        <div className="mb-3">
          <label name="users">Pojects</label>
          <select multiple name="users" className='form-control'
            value={this.state.users}
            onChange={(event) => this.handleUsersSelect(event)} >
            {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)}
          </select>
        </div>
        <input type="submit" value="Create" className="btn btn-primary" />
      </form>
    );
  }
}


const withRouter = WrappedComponent => props => {
  const params = useParams();
 
  return (
    <WrappedComponent
      {...props}
      params={params}
    />
  );
};

const ProjectEditFormWrapped = withRouter(ProjectEditForm);

export default ProjectEditFormWrapped;
