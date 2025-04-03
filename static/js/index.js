
function changeShape(){
    els = document.querySelectorAll('.c')
    els.forEach(el => {
        el.style = 'transform: scale(1.2);';
    });
}

function returnShape(){
    els = document.querySelectorAll('.c')
    els.forEach(el => {
        el.style = 'transform: scale(1);';
    });
}

function allRight(){
    document.querySelector('.circle-right').style = `
    right: 70%;
    `;
    document.querySelector('.circle-right-small').style = `
    right: 60%;
    `;
    document.querySelector('.circle-left').style = `
    left: 80%;
    `;
    document.querySelector('.circle-left-small').style = `
    left: 50%;
    `;
}

function allLeft(){
    document.querySelector('.circle-right').style = `
    right: -20%;
    `;
    document.querySelector('.circle-right-small').style = `
    right: 12%;
    `;
    document.querySelector('.circle-left').style = `
    left: -20%;
    `;
    document.querySelector('.circle-left-small').style = `
    left: -5%;
    `;
}


contents = document.querySelectorAll('.content');
counter = 0;
stateMov = true;

function updateButtons() {
    let btnUp = document.querySelector('#btnUp');
    let btnDown = document.querySelector('#btnDown');
    
    if (counter >= 3) {
        btnUp.classList.remove('fade-out');
        btnUp.classList.add('fade-in');
    } else {
        btnUp.classList.remove('fade-in');
        btnUp.classList.add('fade-out');
    }
    
    if (counter > 7) {
        btnDown.classList.remove('fade-in');
        btnDown.classList.add('fade-out');
    } else {
        btnDown.classList.remove('fade-out');
        btnDown.classList.add('fade-in');
    }
}

 // دالة للتبديل بين الصفحتين
function pageDown() {
        counter++;
        if(counter >= 3){
           // document.querySelector('#btnUp').style.display = 'block';
            document.querySelector('#btnUp').style.top = '50px';
        }else{
           // document.querySelector('#btnUp').style.display = 'none';
            document.querySelector('#btnUp').style.top = '-100px';

        }

        if(counter > 5) {
            document.querySelector('#btnDown').style.bottom = '-100px';
        }else{
            document.querySelector('#btnDown').style.bottom = '50px';
        }
        // التبديل بين الصفحتين مع تأثير تلاشي
        contents[counter-1].style = 'opacity: 0;';  // إخفاء الصفحة الحالية تدريجيًا
        setTimeout(() => {
            contents[counter-1].style.display = 'none';  // إخفاء الصفحة بعد التلاشي
            contents[counter].style.display = 'block';
            if(counter== contents.length-1){
                returnShape()
            }else{
                if(stateMov){
                    allRight();
                    stateMov = false;
                }else{
                    allLeft();
                    stateMov = true;
                }
            }
              // إظهار الصفحة الثانية
            setTimeout(() => {
                contents[counter].style.opacity = 1;  // إظهار الصفحة الثانية بتأثير تدريجي
            }, 50);  // تأخير صغير لتطبيق التغيير
        }, 1000); 
         // تأخير نفس مدة التلاشي
}

 // دالة للتبديل بين الصفحتين
 function pageUp() {
    counter--;
    if(counter >= 3){
       // document.querySelector('#btnUp').style.display = 'block';
        document.querySelector('#btnUp').style.top = '50px';
    }else{
       // document.querySelector('#btnUp').style.display = 'none';
        document.querySelector('#btnUp').style.top = '-100px';
    }

    if(counter > 5) {
        document.querySelector('#btnDown').style.bottom = '-100px';
    }else{
        document.querySelector('#btnDown').style.bottom = '50px';
    }
    // التبديل بين الصفحتين مع تأثير تلاشي
    contents[counter+1].style = 'opacity: 0;';  // إخفاء الصفحة الحالية تدريجيًا
    setTimeout(() => {
        contents[counter+1].style.display = 'none';  // إخفاء الصفحة بعد التلاشي
        contents[counter].style.display = 'block';
        if(counter== contents.length-1){
            returnShape()
            submit()
        }else{
            if(stateMov){
                allRight();
                stateMov = false;
            }else{
                allLeft();
                stateMov = true;
            }
        }
          // إظهار الصفحة الثانية
        setTimeout(() => {
            contents[counter].style.opacity = 1;  // إظهار الصفحة الثانية بتأثير تدريجي
        }, 50);  // تأخير صغير لتطبيق التغيير
    }, 1000); 
     // تأخير نفس مدة التلاشي
}

document.querySelector("form").addEventListener("submit", function(event) {
    let errors = [];
    let numberInput = document.getElementById("numberInput");

    function isChecked(name) {
        return Array.from(document.getElementsByName(name)).some(input => input.checked);
    }

    if (!isChecked("places")) {
        errors.push(" يرجى اختيار **مكان واحد على الأقل**.");
    }
    if (!isChecked("restaurants")) {
        errors.push(" يرجى اختيار **نوع مطعم واحد على الأقل**.");
    }
    if (!isChecked("kids")) {
        errors.push(" يرجى تحديد خيار بخصوص **الأطفال**.");
    }
    if (!isChecked("interests")) {
        errors.push(" يرجى اختيار **اهتمام واحد على الأقل**.");
    }
    if (!numberInput.value || numberInput.value < 1) {
        errors.push(" يرجى إدخال **عدد الأيام الصحيح**.");
    }

    if (errors.length > 0) {
        event.preventDefault(); // منع الإرسال إذا كان هناك أخطاء
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