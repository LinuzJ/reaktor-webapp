import NavButton from "./navButton";

const NavBar = (props) => (
  <div
    className="NavBar"
    style={{
      display: "flex",
      justifyContent: "space-around",
      alignItems: "center",

      height: "70px",
      width: "100%",
      padding: "5px 0",

      background: "gray",

      fontSize: "30px",
      color: "white",

      boxShadow: "0px -2px 15px rgba(50, 50, 50, 0.45)",
    }}
  >
    {props.navButtons.map((button) => (
      <NavButton
        key={button.path}
        path={button.path}
        label={button.label}
        icon={button.icon}
      />
    ))}
  </div>
);

export default NavBar;
