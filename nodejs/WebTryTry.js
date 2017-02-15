const fs = require('fs');
const readline = require('readline');
const request = require('request');

console.log('');
console.log('===Node.js Web Directories and Files Scanner By NoobTW===');

const rl = readline.createInterface(process.stdin,process.stdout);

rl.setPrompt('Input target URL : ');
rl.prompt();

rl.on('line', (target) => {
	console.log('');
	console.log(target.replace('https://', '').replace('http://', ''));
	console.log('');
	const dictStream = fs.createReadStream('dictionary.txt');
	const dictReader = readline.createInterface({input: dictStream});

	let processes = 0;
	dictReader.on('line', (line) => {
		processes++;
		request.get(`${target}${line}`, (err, res, b) => {
			if(!err && b){
				if(res.statusCode != 404){
					console.log(`${target}${line} ---> ${res.statusCode}, ${res.statusMessage}`);
				}
			}else{
				console.log(err);
			}
			processes--;
		});
	});
	dictReader.on('close', () => {
		setInterval(() => {
			if(!processes){
				console.log('');
				process.exit();
			}
		}, 100);
	});
});