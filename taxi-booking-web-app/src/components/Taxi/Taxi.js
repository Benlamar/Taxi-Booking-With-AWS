import React from "react";
import { useState } from "react";
import TaxiNavbar from "../Navbar/TaxiNavbar";
import axios from "axios";
import { getCurrentTime, generateRandomLocation } from "../helper";
import { Alert, Form, Button } from "react-bootstrap";
import { useNavigate, Link } from "react-router-dom";
import Footer from "../Footer/Footer.js";

const Taxi = () => {
  const [response, setResponse] = useState("");
  const [alert, setAlert] = useState(false);
  const [formValue, setformValue] = React.useState({
    id: null,
    name: "",
    location: {},
    timestamp: "",
    type: "",
  });
  const navigate = useNavigate();

  const goToPanel = () => {
    setAlert(false);
    navigate("/taxipanel");
  };

  const handleChange = (event) => {
    setformValue({
      ...formValue,
      [event.target.name]: event.target.value,
    });
  };

  const Register = (e) => {
    e.preventDefault();
    formValue.id = parseInt(formValue.id);
    formValue.location = {
      type: "Point",
      coordinates: generateRandomLocation(),
    };
    formValue.timestamp = getCurrentTime();
    console.log(formValue);

    axios
      .post(
        // register api endpoint
        "...",
        formValue
      )
      .then((res) => {
        console.log(res);
        setResponse(JSON.stringify(res.data));
        setAlert(true);
        setTimeout(() => goToPanel(), 2000);
      })
      .catch((err) => {
        console.log(err.response);
        setResponse(JSON.stringify(err.response.data));
        setAlert(true);
        setTimeout(() => setAlert(false), 2000);
      });
  };

  return (
    <div>
      <TaxiNavbar />
      {alert ? (
        <Alert
          className="fixed-top"
          style={{ top: "65px" }}
          key="secondary"
          variant="secondary"
        >
          {response}
        </Alert>
      ) : null}
      <h1 className="text-center mt-3">Taxi Registration</h1>
      <div className="container d-flex justify-content-center m-5">
        <Form onSubmit={(e) => Register(e)}>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Enter Taxi Id</Form.Label>
            <Form.Control
              type="number"
              name="id"
              placeholder="Enter cutomer id"
              onChange={handleChange}
            />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Enter Taxi Name</Form.Label>
            <Form.Control
              type="text"
              name="name"
              placeholder="customer"
              onChange={handleChange}
            />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Select Type</Form.Label>
            <Form.Select name="type" onChange={handleChange}>
              <option value=""></option>
              <option value="Basic">Basic</option>
              <option value="Deluxe">Deluxe</option>
              <option value="Luxury">Luxury</option>
            </Form.Select>
          </Form.Group>

          <Button variant="primary" type="submit">
            Submit
          </Button>

          <Link className="mx-2" to="/taxipanel">
            <Button
              variant="primary"
              style={{ backgroundColor: "crimson" }}
              type="submit"
            >
              Cancel
            </Button>
          </Link>
        </Form>
      </div>

      <Footer />
    </div>
  );
};

export default Taxi;
