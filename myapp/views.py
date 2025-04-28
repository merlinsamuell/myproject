from .forms import ThyroidForm
from django.shortcuts import render
import joblib
import os

# Load the trained model once during module import
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'myapp', 'thyroid_classifier1.pkl')
model = joblib.load(model_path)

def thyroid_view(request):
    submitted_data = None
    prediction = None
    message = ""
    
    if request.method == 'POST':
        form = ThyroidForm(request.POST)
        if form.is_valid():
            submitted_data = form.cleaned_data

            try:
                # Prepare feature vector for prediction
                features = [
                    submitted_data['age'],
                    submitted_data['tsh'],
                    submitted_data['t3'],
                    submitted_data['t4'],
                    1 if submitted_data['thyroid_meds'].lower() == 'yes' else 0
                ]

                # Predict thyroid condition
                prediction = model.predict([features])[0]

                # Interpret prediction result
                if prediction == 1:
                    message = "⚠️ The patient may have **hypothyroidism**."
                elif prediction == 2:
                    message = "⚠️ The patient may have **hyperthyroidism**."
                else:
                    message = "✅ The patient likely does **not** have a thyroid condition."

            except Exception as e:
                message = f"❌ Error during prediction: {str(e)}"

        else:
            message = "❌ Please correct the errors in the form."
    else:
        form = ThyroidForm()

    return render(request, 'myapp/form.html', {
        'form': form,
        'message': message,
        'submitted_data': submitted_data,
        'prediction': prediction
    })
