const http = require('http');

//create an HTTP,server send response by response.write() and get request HTTP Version
const server = http.createServer((request, response)=>{
    console.log("response", 'http version', request.httpVersion,
    'response status code', response.statusCode)
    response.writeHead(200, {'Content-Type':'text/html'});
    response.write('Hello, this will be the backend of timetable project!<br>');
    response.write('I\'m still working on this site and trying to prepare the <b>data set</b>.');
    response.end();
})
//
const PORT = 3000;
//check if server is running
server.listen(PORT, () =>{
    console.log(`Server running at http://localhost:${PORT}`);
})