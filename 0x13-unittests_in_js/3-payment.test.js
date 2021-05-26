const chai = require("chai");
const should = chai.should();
const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment.js");

describe("#sendPaymentRequestToApi()", function () {
  it("should check functionality of Utils.calculateNumber()", function () {
    const sendSpy = sinon.spy(Utils, "calculateNumber");
    sendPaymentRequestToApi(100, 20);

    sendSpy.calledWith("SUM", 100, 20).should.equal(true);
    sendSpy.restore();
  });
});
