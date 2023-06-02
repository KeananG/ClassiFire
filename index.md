<html>
  <head>
    <title>ClassiFire</title>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;700&display=swap');

      body {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
        background-color: #F5F5F5; /* Light grey */
        font-family: 'Lite Abril Fatface', sans-serif;
        font-weight: 200;
        color: black;
      }

      header {
        background-color: #8B0000; /* Dark red */
        color: black;
        padding: 10px;
        font-family: Montserrat, sans-serif;
        font-weight: 500;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Wildfires from 2014 through 2023</h1>
    </header>
    <div>
      <p>This heat map shows Wildfires from 2014 through 2023 in the contiguous USA. 
        
        The colors are weighted by fire complexity levels type 1 incidents through type 5 incidents. Type 1 will have a higher weight however majority of the red spots indicate large clusters of type 4 and type 5 incidents and not type 2 or 1 incidents.
        This only shows roughly 18k fires out of the total 250k fires</p>
      <iframe src="https://keanang.github.io/WildFires_capstone/images/Heat_map.html" width="1000" height="1000"></iframe>
    </div>
  </body>
</html>
