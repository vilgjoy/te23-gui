-- Lambda --

Lambda är syntax som används för att skapa engångs- funktioner. Används ofta när man behöver en liten funktion som ska bara användas vid ett specifikt tillfälle. Och i tkinter används det för att skicka argument till funktioner och fördröja händelser

exempel i def simon_says(): först går den igenom en loop. Denna loop går igenom varje färg i listan colors (t.ex. "red", "green", "blue", "yellow").

sen skapar den en knapp (btn) med bakgrundsfärgen color (t.ex "red)

sen kommer lambda in. lambda c=color: player_click(c) skapar en funktion utan namn som tar emot ett argument (c) och anropar player_click(c) med denna färg.

man använder lambda i detta exempel eftersom knapparna är skapade inom en loop där vi behöver få det aktuella värdet av color varje gång loopen körs. utan lambda skulle alla knappar ha samma värde för color (den sista färgen i listan). lambda c=color: ser till att varje knapp får sitt eget specifika värde för color, och den ger player_click() med rätt färg när knappen klickas.