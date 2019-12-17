import React from "react";
import { Container, Button } from "reactstrap";
import useLogin from "../hooks/useLogin";
import useViewer from "../hooks/useViewer";

const LandingPage = () => {
  const { redirectToDopeAuth } = useLogin();
  const { settings } = useViewer();
  return (
    <Container>
      <h1>{settings ? settings.app_name : null} Help LIFO</h1>
      <p> brought to you by: {settings ? settings.app_creator : null}</p>

      <p>The help queue system!</p>
      <Button onClick={redirectToDopeAuth} color="primary">
        Login with DopeAuth
      </Button>
    </Container>
  );
};

export default LandingPage;
