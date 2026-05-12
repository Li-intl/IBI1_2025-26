# 1. Define variables for age, weight, gender, and creatine concentration
age = 45           # Age in years
weight = 65        # Weight in kg
gender = "female"  # Gender: "male" or "female"
cr = 80            # Creatine concentration in umol/l

# 2. Check if the input values are within the correct ranges
# Check age: must be less than 100 years
if age >= 100:
    print("Error: Age input needs to be corrected (must be < 100 years).")

# Check weight: must be greater than 20 kg and less than 80 kg
elif weight <= 20 or weight >= 80:
    print("Error: Weight input needs to be corrected (must be > 20 kg and < 80 kg).")

# Check creatine concentration: must be greater than 0 and less than 100 umol/l
elif cr <= 0 or cr >= 100:
    print("Error: Creatine concentration needs to be corrected (must be > 0 and < 100 umol/l).")

# Check gender: must be either 'male' or 'female'
elif gender != "male" and gender != "female":
    print("Error: Gender input needs to be corrected (must be 'male' or 'female').")

# 3. If all conditions are met, calculate the creatine clearance rate (CrCl)
else:
    # Calculate the base formula without gender modifier: (140 - age) * weight / (72 * Cr)
    numerator = (140 - age) * weight
    denominator = 72 * cr
    crcl = numerator / denominator
    
    # 4. Apply the gender modifier (multiply by 0.85 if female)
    if gender == "female":
        crcl = crcl * 0.85
        
    # 5. Output the result using the str() command to convert the number to a string
    print("The patient's calculated Creatine Clearance (CrCl) is: " + str(crcl))
