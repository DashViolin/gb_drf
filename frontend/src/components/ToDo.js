import Header from "./Header";
import { Link } from "react-router-dom";


const handleDeleteClick = ({deleteItem, id, event}) => {
  event.stopPropagation();
  console.log('Bang!')
  deleteItem(id)
}

const ToDoItem = ({ todo, deleteToDo }) => {
  let ltzDate = (new Date(todo.created)).toLocaleString();
  return (
    // <tr className={todo.isCompleted ? 'clickable-row table-success' : 'clickable-row'} style={{ cursor: 'pointer' }} onClick={() => (window.location = `projects/${todo.project}`)} >
    <tr className={todo.isCompleted ? 'clickable-row table-success' : 'clickable-row'} style={{ cursor: 'pointer' }} onClick={() => {}}>
      {todo.isCompleted
        ? <td><i className='far fa-check-square' style={{ 'fontSize': '24px' }}></i></td>
        : <td></td>
      }
      <td>{todo.text}</td>
      <td>{todo.author.username}</td>
      <td>{ltzDate}</td>
      <td>
        <ul className="list-inline m-0">
          {/* <li className="list-inline-item">
            <button className="btn btn-primary btn-sm rounded-2" type="button" data-toggle="tooltip" data-placement="top" title="Edit">
              <i className="fa fa-edit"></i>
            </button>
          </li> */}
          <li className="list-inline-item">
            <button onClick={() => deleteToDo(todo.id)} className="btn btn-danger btn-sm rounded-2" type="button" data-toggle="tooltip" data-placement="top" title="Delete">
              <i className="fa fa-trash"></i>
            </button>
          </li>
        </ul>
      </td>
    </tr>
  )
}

const ToDoList = ({ todos, deleteToDo }) => {
  return (
    <div className="container">
      <Header />
      <table className="table table-sm table-hover">
        <thead className="table-light">
          <tr>
            <th scope="col">Status</th>
            <th scope="col">Text</th>
            <th scope="col">Author</th>
            <th scope="col">Created at</th>
            <th scope="col">
              <Link to='/todos/create'>
                <button className="btn btn-success btn-sm rounded-2" type="button" data-toggle="tooltip" data-placement="top" title="Create">
                  <i className="fas fa-plus"></i><span>{' '}New</span>
                </button>
              </Link>
            </th>
          </tr>
        </thead>
        <tbody>
          {todos.map((todo) => <ToDoItem key={todo.id} todo={todo} deleteToDo={deleteToDo} />)}
        </tbody>
      </table>
    </div>
  )
}

export default ToDoList
