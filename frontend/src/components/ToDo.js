import Header from "./Header";


const ToDoItem = ({todo}) => {
  const link = () => (window.location=`projects/${todo.project}`)
  let ltzDate = (new Date(todo.created)).toLocaleString();
  return (
    <tr className='clickable-row' style={{cursor:'pointer'}} onClick={link} >
      {todo.isCompleted
        ? <td>&#x2713;</td>
        : <td></td>
      }
      <td>{todo.text}</td>
      <td>{todo.author.username}</td>
      <td>{ltzDate}</td>
    </tr>
  )
}

const ToDoList = ({todos}) => {
  return (
    <div className="container">
      <Header />
      <table className="table table-hover">
        <thead className="table-light">
          <tr>
            <th scope="col">Status</th>
            <th scope="col">Text</th>
            <th scope="col">Author</th>
            <th scope="col">Created at</th>
          </tr>
        </thead>
        <tbody>
          {todos.map((todo) => <ToDoItem key={todo.id} todo={todo}/>)}
        </tbody>
      </table>
    </div>
  )
}

export default ToDoList
