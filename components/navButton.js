import Link from "next/link";
import { withRouter } from "next/router";
import { Button } from "@chakra-ui/react";

const NavButton = (props) => {
  let backgroundColor =
    props.category === props.path.substring(1) ? "#ffd9cc" : null;

  return (
    <Link href={props.path}>
      <Button
        width="15%"
        className={`NavButton ${
          props.router.pathname === props.path ? "active" : ""
        }`}
        style={{
          background: backgroundColor,
          color: "black",
        }}
      >
        {props.label}
      </Button>
    </Link>
  );
};

export default withRouter(NavButton);
