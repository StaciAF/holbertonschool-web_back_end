const chai = require("chai");
const should = chai.should();
const sinon = require("sinon");

const sendPaymentRequestToApi = require("./5-payment.js");

describe("#sendPaymentRequestToApi()", function () {
  let conSpy;
  beforeEach(function() {
    conSpy = sinon.spy(console, "log");
  });

  afterEach(function() {
    conSpy.calledOnce.should.equal(true);
    conSpy.restore();
  });

  it("confirms sendPaymentRequestToApi return when passed 100 and 20", function() {
    sendPaymentRequestToApi(100, 20);
    conSpy.calledWith("The total is: 120").should.equal(true);
  });
  it("confirms sendPaymentRequestToApi return when passed 10 and 10", function() {
    sendPaymentRequestToApi(10, 10);
    conSpy.calledWith("The total is: 20").should.equal(true);
  });
});
