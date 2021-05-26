const chai = require("chai");
const should = chai.should();
const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./4-payment.js");

describe("with Stub: #sendPaymentRequestToApi()", function () {
  it("should check functionality of Utils.calculateNumber()", function () {
      const sendStub = sinon.stub(Utils, "calculateNumber").returns(10);
      const conSpy = sinon.spy(console, 'log');
      sendPaymentRequestToApi(100, 20);

      sendStub.calledWith("SUM", 100, 20).should.equal(true);
      conSpy.calledWith('The total is: 10').should.equal(true);
      sendStub.alwaysReturned(10).should.equal(true);

      sendStub.restore();
      conSpy.restore();
  });
});
