import { useParams } from "react-router-dom";
import Header from "./Header";


const ProjectItem = ({project}) => {
  let users = [];
  project.users.map((user) => (users.push(user.username)));
  return (
    <tr>
      <td>{project.title}</td>
      <td><a href={project.repo}>{project.repo}</a></td>
      <td>{users.join(", ")}</td>
    </tr>
  )
}

const ProjectList = ({projects}) => {
  return (
    <div className="container">
      <Header />
      <table className="table">
        <thead className="table-light">
          <tr>
            <th scope="col">Title</th>
            <th scope="col">Repo link</th>
            <th scope="col">Users</th>
          </tr>
        </thead>
        <tbody>
          {projects.map((project) => <ProjectItem key={project.id} project={project}/>)}
        </tbody>
      </table>
    </div>
  )
}

const ProjectDetails = ({projects}) => {
  let params = useParams();
  let project = projects.find((project) => (project.id === parseInt(params.projectId)));
  if(project){
    let users = [];
    project.users.map((user) => (users.push(user.username)));
    return (
      <ul>
        <li>Id: {`${project.id}`}</li>
        <li>Title: {`${project.title}`}</li>
        <li>Repo: <a href={project.repo}>{project.repo}</a></li>
        <li>Users: {`${users.join(", ")}`}</li>
      </ul>
    )
  } else {
    return (
      <h4>Ooops, such project not found!</h4>
    )
  }
}

export {ProjectList, ProjectDetails};
