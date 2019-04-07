var gpio = require('rpi-gpio');
var gpiop = gpio.promise;

gpio.setup(11, gpio.DIR_OUT)
    .then(() => {
        return gpiop.write(7, true)
    })
    .catch((err)=> {
        console.log('error: '+err.toString())
    })
