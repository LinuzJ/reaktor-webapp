import NavBar from "./navBar";
import navButtons from "../config/buttons";

const Layout = (props) => {
  return (
    <div className="Layout">
      <NavBar navButtons={navButtons} category={props.category} />
      <div className="Content">{props.children}</div>

      <div>
        <title>Products</title>
      </div>
    </div>
  );
};

export default Layout;
