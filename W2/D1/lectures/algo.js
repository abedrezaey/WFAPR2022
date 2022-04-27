



Math.ceil (9.51)


Math.floor(8.45)





// generating a random number. 


var random = Math.random();


random = random * 11

random = Math.floor(random)

for(var i =0; i<10; i++)
{

      var random = Math.floor(Math.random() * 11 +1);

}


//////////////////////////////////////////////////////



function d6() {
      var roll = Math.random();
      roll = Math.floor(roll * 6 +1)
      // your code here
      return roll;
  }
      
  var playerRoll = d6();
  console.log("The player rolled: " + playerRoll);



  //////////////////////////////////////////////////////

  // Consult the Oracle
// Using the following array, write a function that will answer all of our questions by randomly choosing a response

var lifesAnswers = [
      "It is certain.",
      "It is decidedly so.",
      "Without a doubt.",
      "Yes – definitely.",
      "You may rely on it.",
      "As I see it, yes.",
      "Most likely.",
      "Outlook good.",
      "Yes.",
      "Signs point to yes.",
      "Reply hazy, try again.",
      "Ask again later.",
      "Better not tell you now.",
      "Cannot predict now.",
      "Concentrate and ask again.",
      "Don't count on it.",
      "My reply is no.",
      "My sources say no.",
      "Outlook not so good.",
      "Very doubtful."
      ];

var result = lifesAnswers[Math.floor(Math.random() * lifesAnswers.length)];
console.log(result);


  //////////////////////////////////////////////////////////////////////////









