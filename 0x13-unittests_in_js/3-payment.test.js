const chai = require('chai');
const expect = chai.expect;
const assert = require('assert');

const sinon = require('sinon');
const spy = sinon.spy;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi', function () {
    it('should check functionality of Utils.calculateNumber()', function() {
	const sendSpy = spy(Utils, "calculateNumber");
	sendPaymentRequestToApi(100, 20);
	expect(sendSpy.calledWith('SUM', 100, 20)).to.equal(true);
	sendSpy.restore();
    })
});
