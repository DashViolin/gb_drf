import React from 'react';
import { Link } from "react-router-dom";


const ProjectItem = ({ project, deleteProject }) => {
  let users = [];
  project.users.map((user) => (users.push(user.username)));
  return (
    <tr>
      <td>
        <ul className="list-inline m-0">
          <li className="list-inline-item">
            <Link to={`/projects/${project.id}`}>
              {/* <button onClick={() => (window.location = `projects/${project.id}`)} className="btn btn-primary btn-sm rounded-2" type="button" data-toggle="tooltip" data-placement="top" title="Edit"><i className="fa fa-edit"></i></button> */}
              <button onClick={() => {}} className="btn btn-primary btn-sm rounded-2" type="button" data-toggle="tooltip" data-placement="top" title="Edit"><i className="fa fa-edit"></i></button>
            </Link>
          </li>
          <li className="list-inline-item">
            <button onClick={() => deleteProject(project.id)} className="btn btn-danger btn-sm rounded-2" type="button" data-toggle="tooltip" data-placement="top" title="Delete"><i className="fa fa-trash"></i></button>
          </li>
        </ul>
      </td>
      <td>{project.title}</td>
      <td><a href={project.repo}>{project.repo}</a></td>
      <td>{users.join(", ")}</td>
    </tr>
  )
}

class ProjectList extends React.Component {
  render() {
    const filterText = this.props.filterText;
    const rows = [];

    this.props.projects.forEach((project) => {
      if (project.title.toLowerCase().indexOf(filterText.toLowerCase()) === -1) {
        return;
      }
      rows.push(<ProjectItem
        key={project.id}
        project={project}
        deleteProject={(id) => this.props.deleteProject(id)}
      />);
    });

    return (
      <div className="container">
        <div className="table-responsive">
          <table className="table">
            <thead className="table-light m-0">
              <tr>
                <th scope="col">
                  <Link to='/projects/create'>
                    <button className="btn btn-success btn-sm rounded-2" type="button" data-toggle="tooltip" data-placement="top" title="Create"><i className="fas fa-plus"></i>{' '}New</button>
                  </Link>
                </th>
                <th scope="col">Title</th>
                <th scope="col">Repo link</th>
                <th scope="col">Users</th>
              </tr>
            </thead>
            <tbody>
              {rows}
            </tbody>
          </table>
        </div>
      </div>
    )
  }
}

// const ProjectDetails = ({ projects }) => {
//   let params = useParams();
//   let project = projects.find((project) => (project.id === parseInt(params.projectId)));
//   if (project) {
//     let users = [];
//     project.users.map((user) => (users.push(user.username)));
//     return (
//       <ul style={{ 'fontSize': '16px' }}>
//         <li><u>Id:</u>{' '}<b>{`${project.id}`}</b></li>
//         <li><u>Title:</u>{' '}<b>{`${project.title}`}</b></li>
//         <li><u>Repo:</u>{' '}<b><a href={project.repo}>{project.repo}</a></b></li>
//         <li><u>Users:</u>{' '}<b>{`${users.join(", ")}`}</b></li>
//       </ul>
//     )
//   } else {
//     return (
//       <h5>Ooops, such project not found!</h5>
//     )
//   }
// }

export default ProjectList;
