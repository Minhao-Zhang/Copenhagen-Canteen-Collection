import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";

function NavigationBar() {
  return (
    <Navbar bg="primary" expand="lg" variant="dark">
      <Container>
        <Navbar.Brand href="/Copenhagen-Canteen-Collection/">CCC</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#/map">Map</Nav.Link>
            <NavDropdown title="KU Søndre" id="basic-nav-dropdown">
              <NavDropdown.Item href="#/canteens/jur">
                Wicked Rabbit - JUR
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/hum">
                Wicked Rabbit - HUM
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/fol">
                Folke Køkken
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/teo">
                TEO Kantinen
              </NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="KU Nørre" id="basic-nav-dropdown">
              <NavDropdown.Item href="#/canteens/hco">
                HCØ Kantinen
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/bio">
                Biocenteret Kantinen
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/nbi">
                NBI Kantinen
              </NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="KU Others" id="basic-nav-dropdown">
              <NavDropdown.Item href="#/canteens/geo">
                Geo Center Kantinen
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/gam">
                Gamble Taastrup
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/gim">
                Gimle Kantine
              </NavDropdown.Item>
              <NavDropdown.Item href="#/canteens/gum">
                Gumble Kantine
              </NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavigationBar;
