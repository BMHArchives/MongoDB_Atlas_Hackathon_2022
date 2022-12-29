# Stock Twitter Feeder
Stock Twitter Feeder is an application allows users to select their favorite stocks and lookup tweets relating to their favorite stocks.

I originally created this app so that I can submit it to the [MongoDB Atlas Hackathon 2022 on DEV Challenge](https://dev.to/devteam/announcing-the-mongodb-atlas-hackathon-2022-on-dev-2107). Regrettably I ran out of time and I could not submit my final project.
Maybe next year I might if they start up the challenge again. 



Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)

Challenge Rules:
https://dev.to/devteam/announcing-the-mongodb-atlas-hackathon-2022-on-dev-2107

A brief description of what this project does and who it's for


## Application Makeup

The application is made up of 3 parts:

### Stock Twitter Feeder
Stock Twitter Feeder is a python console application that will retrieve tweets that includes content relating to 
stocks that the user selects. The tweets that are pulled from twitter will include either the stock's company name,
ticker sybmol and any additional content that the user wants the app to lookup. For example: 

Lets say the user adds Microsoft to their list, and they want the application to lookup tweets that 
includes text such as 'XBox', 'SharePoint', 'Azure' and 'VR'. The application will search for tweets that contains
'Microsoft', 'MSFT' and 'XBox', 'SharePoint', 'Azure' and 'VR'.

The application uses a MongoDB database to store user's data and tweets pulled from twitter and the application 
is hosted in Azure as a web job which runs every 25 minutes.

### Stock Twitter Reader
Stock Twitter Reader is a python console application that will monitor any new tweets added to the MongoDB and
adds them to a queue for subscribers to retrieve from and perform searches from the any client.

The application uses a MongoDB database to retrieve new tweets and adds them to a queue collection for
consumption by clients.

### Stocker Twitter web
Stocker Twitter web is a web application client that provides an interface for users to select their favorite
stocks, checkout the latest tweets relating to their stock lists and perform searches on them as well.

The application written as a Django application which is hosted in Azure as an web application.

## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Appendix

Any additional information goes here


## Authors

- [@brandonmichaelhunter](https://github.com/brandonmichaelhunter)


## Documentation

[Documentation](https://linktodocumentation)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Demo

Insert gif or link to demo


## Deployment

To deploy this project run

```bash
  npm run deploy
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2


## Feedback

If you have any feedback, please reach out to us at fake@fake.com


## 🚀 About Me
I'm a full stack developer...


# Hi, I'm Katherine! 👋


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherineoelsner.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)

Stock API aggreator
https://www.alphavantage.co/

Atlast Search, pick up from here
https://www.mongodb.com/docs/atlas/atlas-search/tutorial/run-query/#std-label-fts-tutorial-run-query


https://towardsdatascience.com/how-to-use-twitter-premium-search-apis-for-mining-tweets-2705bbaddca


## Other Common Github Profile Sections
👩‍💻 I'm currently working on...

🧠 I'm currently learning...

👯‍♀️ I'm looking to collaborate on...

🤔 I'm looking for help with...

💬 Ask me about...

📫 How to reach me...

😄 Pronouns...

⚡️ Fun fact...


## 🛠 Skills
Javascript, HTML, CSS...


## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?


## License

[MIT](https://choosealicense.com/licenses/mit/)


![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

