const chai = require('chai');
const should = chai.should();
const sinon = require('sinon');

const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('#getPaymentTokenfromAPI()', function () {
    it('confirms return message when passed true', function (done) {
	getPaymentTokenFromAPI(true)
	    .then(function (val) {
		val.data.should.equal("Successful response from the API");
		done();
	    });
    });
});
