import React from "react";
import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";
import "./home.css";

const Home = () => {


  return (
    <div className="home">
        <div
          className="home-panel d-flex flex-column justify-content-start align-items-center"
        >
          <h2>Welcome to Taxi Booking</h2>

          <div>
          <Link className="mx-2" to="/taxipanel">
            <Button style={{backgroundColor:'#0dcaf0'}} className="btn-size border-0">Taxi</Button>
          </Link>

          <Link className="mx-2" to="/panel">
            <Button style={{backgroundColor:'#0dcaf0'}} className="btn-size border-0">Customer</Button>
          </Link>
          </div>
        </div>
        <span className="home-foot">
          &copy; Group-5 - S21
          <span className="fst-italic"> [ACSE,Sept-21 GreatLearning]</span>
        </span>
    </div>
  );
};

export default Home;
