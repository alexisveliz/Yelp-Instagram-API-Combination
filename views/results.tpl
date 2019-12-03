<!doctype html>
<html>
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Restaurant Vibes</title>
<head>
</head>
<body>
    <div class="container">
        %if True:
            <h3>Showing the top result for {{term}} in {{location}}</h3>
            <a href='search'>Back to search</a>
            <h1>{{name}}<h2>
            <img src={{picture}}>
        %end
    </div>
</body>
</html>
