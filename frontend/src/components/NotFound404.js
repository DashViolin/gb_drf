import { useLocation } from "react-router-dom"

const NotFound404 = () => {
  let {pathname} = useLocation()
  return (
    <div>
      <h3>Страница по адресу '{pathname}' не найдена</h3>
    </div>
  )
}

export default NotFound404
