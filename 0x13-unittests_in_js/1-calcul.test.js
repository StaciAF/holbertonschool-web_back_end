const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('#calculateNumber()', function () {
    it('should return 6 when calculateNumber is passed SUM, 1.4, and 4.5', function () {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('should return -4 when calculateNumber is passed SUBTRACT, 1.4 and 4.5', function () {
	assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('should return 0.2 when calculateNumber is passed DIVIDE, 1.4, and 4.5', function () {
	assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('should return Error when calculateNumber is passed DIVIDE, 1.4, and 0', function () {
	assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });
  
