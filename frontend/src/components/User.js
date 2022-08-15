const UserItem = ({user, index}) => {
  return (
    <tr>
      <td>{index + 1}</td>
      <td>{user.username}</td>
      <td>{user.first_name}</td>
      <td>{user.last_name}</td>
      <td>{user.email}</td>
    </tr>
  )
}

const UserList = ({users}) => {
  return (
    <table className="table">
      <thead className="table-light">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Username</th>
          <th scope="col">First Name</th>
          <th scope="col">Last Name</th>
          <th scope="col">Email</th>
        </tr>
      </thead>
      <tbody>
        {users.map((user, index) => <UserItem key={user.email} user={user} index={index}/>)}
      </tbody>
    </table>
  )
}

export default UserList
