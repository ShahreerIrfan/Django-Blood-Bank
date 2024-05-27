let num1 = document.getElementById('num1').value

const clickeed = () =>{
    console.log("Button Clicked")
    let num1 = document.getElementById('num1').value
    let num2 = document.getElementById('num2').value;
    let sum = parseFloat(num1)+parseFloat(num2);
    document.getElementById('result').innerHTML = sum;
}

function calculateBMI(event) {
    event.preventDefault();
    const heightFeet = parseFloat(document.getElementById('heightFeet').value);
    const weight = parseFloat(document.getElementById('weight').value);

    if (!isNaN(heightFeet) && !isNaN(weight)) {
        const heightMeters = heightFeet * 0.3048;
        const bmi = weight / (heightMeters * heightMeters);
        let resultText = '';
        let resultColor = '';
        let additionalMessage = '';

        if (bmi < 18.5) {
            resultText = `Your BMI is ${bmi.toFixed(2)}`;
            resultColor = 'bg-red-500';
            additionalMessage = 'You are underweight. It is important to eat a balanced diet and consult with a healthcare provider.';
        } else if (bmi >= 18.5 && bmi <= 24.9) {
            resultText = `Your BMI is ${bmi.toFixed(2)}`;
            resultColor = 'bg-green-500';
            additionalMessage = 'You have a normal weight. Keep up the good work with a balanced diet and regular exercise!';
        } else if (bmi >= 25 && bmi <= 29.9) {
            resultText = `Your BMI is ${bmi.toFixed(2)}`;
            resultColor = 'bg-yellow-500';
            additionalMessage = 'You are overweight. Consider a healthy diet and regular physical activity to improve your health.';
        } else {
            resultText = `Your BMI is ${bmi.toFixed(2)}`;
            resultColor = 'bg-red-500';
            additionalMessage = 'You are obese. It is important to seek advice from a healthcare provider to manage your weight.';
        }

        const resultElement = document.getElementById('bmiResult');
        resultElement.innerHTML = `
            <div class="${resultColor} text-white p-4 rounded-lg">
                <p class="text-xl font-bold">${resultText}</p>
                <p class="mt-2">${additionalMessage}</p>
            </div>
        `;
    } else {
        const resultElement = document.getElementById('bmiResult');
        resultElement.innerHTML = `
            <div class="bg-red-500 text-white p-4 rounded-lg">
                <p class="text-xl font-bold">Invalid input</p>
                <p class="mt-2">Please enter valid height and weight.</p>
            </div>
        `;
    }
}