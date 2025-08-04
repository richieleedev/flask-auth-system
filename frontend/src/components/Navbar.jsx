import { Link, useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    sessionStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <nav style={{ padding: "10px", borderBottom: "1px solid #ccc", background: "black", color: "white" }}>
      <Link to="/signup" style={{ marginRight: 10, color: "white" }}>Signup</Link>
      <Link to="/login" style={{ marginRight: 10, color: "white" }}>Login</Link>
      <Link to="/private" style={{ marginRight: 10, color: "white" }}>Private</Link>
      <button onClick={handleLogout}>Logout</button>
    </nav>
  );
};

export default Navbar;
