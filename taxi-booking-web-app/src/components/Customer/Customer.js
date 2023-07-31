import axios from "axios";

import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Alert, Form, Button } from "react-bootstrap";

import Footer from "../Footer/Footer.js";
import TaxiNavbar from "../Navbar/TaxiNavbar";
import { generateRandomLocation, getCurrentTime } from "../helper";

const Customer = () => {
  const [response, setResponse] = useState("");
  const [alert, setAlert] = useState(false);
  const navigate = useNavigate();
  const [formValue, setformValue] = React.useState({
    id: null,
    name: "",
    location: {},
    timestamp: "",
  });

  const goToPanel = (customer_list) => {
    setAlert(false);
    navigate("/panel");
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
        // server api here
        "...",
        formValue
      )
      .then((res) => {
        console.log(res.data);
        setResponse(JSON.stringify(res.data));
        setAlert(true);
        setTimeout(() => goToPanel(), 2000);
      })
      .catch((err) => {
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

      <h1 className="text-center mt-3">Customer Registration</h1>

      <div className="container d-flex justify-content-center m-5">
        <Form style={{ height: "300px" }} onSubmit={(e) => Register(e)}>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Enter cutomer Id</Form.Label>
            <Form.Control
              type="number"
              name="id"
              placeholder="Enter cutomer id"
              onChange={handleChange}
            />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Enter Customer Name</Form.Label>
            <Form.Control
              type="text"
              name="name"
              placeholder="customer"
              onChange={handleChange}
            />
          </Form.Group>

          <Button variant="primary" type="submit">
            Submit
          </Button>

          <Link className="mx-2" to="/panel">
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

export default Customer;
