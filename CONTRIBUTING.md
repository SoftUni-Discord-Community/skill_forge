## **Contribution Guidelines**

### **Welcome Contributors!**

Thank you for considering contributing to Skill Forge project! By participating, you're helping to improve the experience for all users and furthering the development of our platform. Before getting started, please take a moment to review the guidelines outlined below.

### **Code of Conduct**
Before contributing, please familiarize yourself with our Code of Conduct. We expect all contributors to adhere to these guidelines to ensure a respectful and inclusive community environment.

### **How to Contribute**

#### :one: Fork the Repository: 
Start by forking the main repository to your GitHub account. 

#### :two: Clone the Repository: 
Clone the forked repository to your local machine.

```bash
git clone https://github.com/your-username/repository.git
```

In order to be able to start development instance of the application you will need few prerequisites:

* Postgres database running on your local machnine. Setup PostgreSQL server or deploy Docker container locally. Check official [DockerHub](https://hub.docker.com/_/postgres) image instructions for more details.

* Create your own environment file with the application properties:

```text
# Server Settings
SERVER_IP_ADDR = 'your-local-ip-address'
DEBUG_PORT = 'flask-debug-port' #You can set 5000 as default Flask settings

# Database Settings (change the values with your own)
DB_NAME_PROD='postgres-db-name'
DB_USER_PROD='postgres-root-user'
DB_PASSWORD_PROD='postgres-root-password'
SQLALCHEMY_DATABASE_URI_DEV='postgresql://<root-username>:<root-password>@<db-host-ip>:<db-host-port>/<db-name>'
```

* Install Python requirements. It is recommended to crate Python virtual env
```bash
pip install -r requirements.txt --no-cache
```

* In order to run succesfully the code runners, micro applications which execute the user code in the backend, you need to install the folloiwng packages on your dev server
```bash
apt install python3 nodejs mono-complete openjdk-17-jdk-headless -y
```

#### :three: Create a Branch:
Before making any changes, create a new branch to work on. Ensure your branch name is descriptive of the feature or fix you're implementing.

```bash
git checkout -b feature-name
```

#### :four: Make Changes:
Make your desired changes to the codebase. Ensure that your changes adhere to our coding standards and naming conventions.

#### :five: Test Your Changes: 
Before submitting a pull request, test your changes thoroughly to ensure they function as intended and don't introduce any regressions.

#### :six: Commit Your Changes: 
Once you're satisfied with your changes, commit them with a clear and descriptive commit message.

```bash
git commit -m "Brief summary of changes"
```

#### :seven: Push Changes: 
Push your changes to your forked repository.
```bash
git push origin feature-name
```

#### :eight: Submit a Pull Request: 
Finally, submit a pull request from your forked repository to the `development` branch in the origin repository. Be sure to provide a detailed description of your changes in the pull request.

### Coding Standards

* Follow the coding standards specific to each programming language and technology used to build the app(Python, JavaScript, C#, Java, Docker, Bash, etc.) 
* Write clean, readable, and well-documented code. 
* Ensure that your code follows consistent indentation and formatting.

### Naming Conventions
* Use descriptive and meaningful names for variables, functions, classes, and other identifiers.
* Follow the naming conventions established for each programming language (e.g., PEP 8 for Python).
* Write descriptive code comments explaining what your code does and how it works

### Pull Requests
* Submit ONE pull request per feature or bug fix. If you're addressing multiple issues, create separate pull requests for each.
* Provide a clear and concise description of the changes included in your pull request.
* Reference any relevant issues or feature requests in your pull request description using GitHub's issue linking syntax (e.g., #issue-number).

### Issues
* Report any bugs, feature requests, or other issues using our issue tracker.
* Clearly describe the problem or feature request, providing as much detail as possible.
* Use descriptive titles and labels to categorize your issues appropriately.

### Review Process
* Reviewers may provide feedback or request changes to be made before the pull request is merged.
* Once approved, a member of the team will merge the pull request into the main branch.

### Communication
* Feel free to reach out to the development team via our communication channels if you have any questions or need assistance.
* Engage with other contributors respectfully and constructively.

### Recognition
* We value and appreciate all contributions to our project. Contributors who demonstrate dedication and excellence will be recognized by mentioned in the Contributors section of the project.

### Thank you for contributing to Skill Forge project and helping to make it even better!