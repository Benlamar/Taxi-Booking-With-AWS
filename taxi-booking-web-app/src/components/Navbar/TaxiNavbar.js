import { Navbar, Nav, Container } from "react-bootstrap";
import { Link } from "react-router-dom";
import "./navbar.css";

function TaxiNavbar() {
  return (
    <Navbar bg="dark" variant="dark" expand="lg" className="sticky-top">
      <Container>
        <Navbar.Brand>
          <img src="./image/taxi.png" alt="logo" className="brand-logo" />
          Taxi and Booking
        </Navbar.Brand>
        <Nav className="mx-2 my-0">
          <Link className="links" to="/">
            Home
          </Link>
        </Nav>
        <Nav className="mx-2 my-0">
          <Link className="links"  to="/taxi">Taxi</Link>
        </Nav>
        <Nav className="ms-2 me-auto my-0">
        <Link className="links" to="/customer">Customer</Link>
        </Nav>
      </Container>
    </Navbar>
  );
}

export default TaxiNavbar;
