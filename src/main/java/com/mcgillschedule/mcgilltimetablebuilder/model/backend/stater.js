const http = require('http');
const fs = require('fs');
const app = express();
const PORT = 3000;

app.use(express.json());

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

//create
app.post('/search', (req, res) =>{
    const searchTerm = req.body.searchTerm;

    fs.readFile('data.json','utf8', (err, data) =>{
    if (err) {
        console.error(err);
        return res.status(500).json({ error: 'please contact administrator'});
    }

    const courseData = JSON.parse(data);

    const results = jsonData.filter(course => course.title.includes(searchTerm));

    res.json(results)
    });
});

//check if server is running
server.listen(PORT, () =>{
    console.log(`Server running at http://localhost:${PORT}`);
})

