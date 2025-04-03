openEditUserInputs = false;
function editUserInputs(el){
    if(!openEditUserInputs){
        document.querySelector('.form').style.display = 'block';
        el.innerHTML = `الغاء`;
        openEditUserInputs = true;
    }else{
        document.querySelector('.form').style.display = 'none';
        el.innerHTML = `تعديل الرغبات`;
        openEditUserInputs = false;
    }
    
    console.log('clicked')
}

swapState = true;
function swap(el){
    if(swapState){
        document.querySelector('#places').style.display = 'none';
        document.querySelector('#rests').style.display = 'block';
        el.innerHTML = `الاماكن <i class="fa-solid fa-arrow-right"></i>`;
        swapState = false;
    }else{
        document.querySelector('#rests').style.display = 'none';
        document.querySelector('#places').style.display = 'block';
        el.innerHTML = `المطاعم <i class="fa-solid fa-arrow-left"></i>`;
        swapState = true;
    }
    
}

editState = true;
function editPlaces(el){
    els = document.querySelectorAll('.delete');
    if(editState){
        els.forEach(i => {
            i.style.display = 'block';
        });
        el.innerHTML = 'الغاء التحرير';
        editState = false;
    }else{
        els.forEach(i => {
            i.style.display = 'none';
        });
        el.innerHTML = 'التحرير';
        editState = true;
    }
}


document.querySelector("#formSubmit").addEventListener("submit", function(event) {
    let errors = [];
    let numberInput = document.querySelector("input[name='duration']");
    let placesChecked = Array.from(document.getElementsByName("places")).some(input => input.checked);
    let restaurantsChecked = Array.from(document.getElementsByName("restaurants")).some(input => input.checked);
    let kidsChecked = Array.from(document.getElementsByName("kids")).some(input => input.checked);
    let interestsChecked = Array.from(document.getElementsByName("interests")).some(input => input.checked);

    // التحقق من الأماكن
    if (!placesChecked) {
        errors.push(" يرجى اختيار **مكان واحد على الأقل**.");
    }
    
    // التحقق من المطاعم
    if (!restaurantsChecked) {
        errors.push(" يرجى اختيار **نوع مطعم واحد على الأقل**.");
    }
    
    // التحقق من الأطفال
    if (!kidsChecked) {
        errors.push(" يرجى تحديد خيار بخصوص **الأطفال**.");
    }
    
    // التحقق من الاهتمامات الخاصة
    if (!interestsChecked) {
        errors.push(" يرجى اختيار **اهتمام واحد على الأقل**.");
    }
    
    // التحقق من عدد الأيام
    if (!numberInput.value || numberInput.value < 1) {
        errors.push(" يرجى إدخال **عدد الأيام الصحيح**.");
    }

    // إذا كان هناك أخطاء، يتم عرضها باستخدام SweetAlert2
    if (errors.length > 0) {
        event.preventDefault(); // منع الإرسال إذا كانت هناك أخطاء
        Swal.fire({
            icon: 'error',
            title: '🚨 تنبيه!',
            html: errors.join("<br><br>"), // عرض الأخطاء بداخل النافذة
            confirmButtonText: 'بضبطها',
            background: "linear-gradient(135deg, #add8e6, #f2f5f6)", // تدرجات الأزرق
            color: "#01617e",
            customClass: {
                popup: 'swal2-popup-custom',
                title: 'swal2-title-custom',
                confirmButton: 'swal2-button-custom'
            }
        });
    }
});


document.querySelector("#pdfButton").addEventListener("click", function(event) {
    event.preventDefault(); // منع إرسال الفورم الفعلي

    Swal.fire({
        title: " قريبًا جدًا!",
        html: " ",
        icon: "info",
        confirmButtonText: " انتظركم ⏳",
        background: "linear-gradient(135deg, #add8e6, #f2f5f6)", // تدرجات الأزرق
        color: "#01617e",
        confirmButtonColor: "#004d80", // زر التأكيد بلون أزرق داكن
        customClass: {
            popup: "swal2-popup-custom",
            title: "swal2-title-custom",
            confirmButton: "swal2-button-custom"
        }
    });
});