const form = document.querySelector("form");

// get all the inputs from the form
const input1 = form.querySelector("#input1");
const input2 = form.querySelector("#input2");
const input3 = form.querySelector("#input3");
const input4 = form.querySelector("#input4");
const input5 = form.querySelector("#input5");
const input6 = form.querySelector("#input6");
const input7 = form.querySelector("#input7");

function onSubmitClick(event) {
  // stop form from submitting data through default method
  event.preventDefault();

  console.log("Submit Button Clicked");

  // get values from all the inputs
  const input1Value = input1.value;
  const input2Value = input2.value;
  const input3Value = input3.value;
  const input4Value = input4.value;
  const input5Value = input5.value;
  const input6Value = input6.value;
  const input7Value = input7.value;

  // call the backend url that would give the prediction values
  fetch({
    url: "/put backend route url here/",
    method: "POST",
    body: {
      input1: input1Value,
      input2: input2Value,
      input3: input3Value,
      input4: input4Value,
      input5: input5Value,
      input6: input6Value,
      input7: input7Value,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      // extract predicted values from data
      const { value } = data;
      window.alert("The value of our car is predicted to be " + value);
    })
    .catch((error) => {
      console.error("Error while fetching data\n" + error);
    });
}
