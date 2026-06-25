# دریافت تعداد دروس از کاربر
num_courses = int(input("Tedad dars ra vared konid:\n"))

# متغیرها برای ذخیره مجموع نمرات ضرب در واحدها و مجموع واحدها
total_weighted_scores = 0
total_units = 0

# گرفتن نمره و تعداد واحد هر درس و محاسبه مجموع‌ها
for i in range(num_courses):
    score = float(input(f"Nomreh dars {i + 1} ra vard konid : \n"))
    units = int(input(f"Tedad vahed dars{i + 1} ra vard konid: \n"))
    total_weighted_scores += score * units
    total_units += units

# محاسبه معدل
if total_units > 0:
    average = total_weighted_scores / total_units
    print(f"Moadele Shoma:{average:.2f}")
else:
    print("Tedad vahed nemitavaned 0 Bashad.")