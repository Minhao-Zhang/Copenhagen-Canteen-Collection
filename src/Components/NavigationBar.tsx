import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";

function NavigationBar() {
  return (
    <Navbar bg="primary" expand="lg" variant="dark">
      <Container>
        <Navbar.Brand href="/">CCC</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#/map">Map</Nav.Link>
            <NavDropdown title="KU Søndre Campus" id="basic-nav-dropdown">
              <NavDropdown.Item href="#/canteens/wicked-rabbit-jur">
                Wicked Rabbit - JUR
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/wicked-rabbit-hum">
                Wicked Rabbit - HUM
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/folkekokken">
                Folke Køkken
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/teo">TEO</NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavigationBar;
