var express = require('express');
var router = express.Router();
var PythonShell = require('python-shell');


/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('predict',{status: 'Enter participant information and click predict'});
});


router.post('/', function(req,res,next){
    var options = {
        pythonPath: '/usr/local/bin/python3',
        scriptPath: '/Users/tysovsky/Desktop/HackRU/',
        args: [req.body.marital_status,
            req.body.sex,
            req.body.longitude,
            req.body.latitude,
            req.body.date_added,
            req.body.birth_date,
            req.body.coverage,
            req.body.premium,
            req.body.plan,
            req.body.policy_start_date,
            req.body.state]
    };

    console.log(options)
    //
    PythonShell.run('evaluate_model.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        res.render('predict',{status: results[0]});
        console.log(results);
    });
});


module.exports = router;
