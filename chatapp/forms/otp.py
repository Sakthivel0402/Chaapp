#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="chatapp")
cur = con.cursor()
form = cgi.FieldStorage()

email=form.getvalue("email")
time=form.getvalue("time")

print("""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OTP Verification </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
        <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

    <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    *{
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
        font-weight: 300;
    }
      
    body{
            background-color: #b4ffdf;
        color: #005c80;
        
        
    }
       
    .otp-container {
            background-color: rgb(241, 255, 254);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            text-align: center;
        }
        .otp-container h2 {
            margin-bottom: 20px;
            color: #333;
        }
        .otp-inputs {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .otp-inputs input {
            width: 50px;
            height: 50px;
            text-align: center;
            font-size: 20px;
            border: 2px solid #ddd;
            border-radius: 8px;
            outline: none;
        }
        .otp-inputs input:focus {
            border-color: #4CAF50;
        }
        .otp-button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
        }
        .otp-button:hover {
            background-color: #45a049;
        }
        .resend-link {
            margin-top: 15px;
            font-size: 14px;
        }
        .resend-link a {
            text-decoration: none;
            color: #007BFF;
        }
        .resend-link a:hover {
            text-decoration: underline;
        }
        .o{margin-top: 10%;}
  


       
    </style>
</head>


<body><div class=" o d-flex justify-content-center">
    <div class="otp-container">
        <h2>Enter OTP</h2>
        <p>Please enter the 6-digit OTP sent to your phone/email.</p>

        <!-- OTP Input Fields -->
        <form  method="POST">
            <div class="otp-inputs">
                <input type="text" name="otp1" maxlength="1" required autocomplete="off" />
                <input type="text" name="otp2" maxlength="1" required autocomplete="off"/>
                <input type="text" name="otp3" maxlength="1" required autocomplete="off"/>
                <input type="text" name="otp4" maxlength="1" required autocomplete="off"/>
                <input type="text" name="otp5" maxlength="1" required autocomplete="off"/>
                <input type="text" name="otp6" maxlength="1" required autocomplete="off"/>
            </div>

            <!-- Submit Button -->
            <input type="submit" name="submit" class="otp-button" value="Verify OTP">
                    </form>

        <!-- Resend OTP Link -->
        <div class="resend-link">
            <p>Didn't receive OTP? <a href="#">Resend OTP</a></p>
        </div>
    </div>
</div>
<script>
    document.querySelectorAll('input').forEach((input, index, inputs) => {
            input.addEventListener('input', function() {
                if (input.value.length === 1 && index < inputs.length - 1) {
                    inputs[index + 1].focus();
                }
            });
        });
</script>
</body>
</html>""")

submit=form.getvalue("submit")
otp1=form.getvalue("otp1")
otp2=form.getvalue("otp2")
otp3=form.getvalue("otp3")
otp4=form.getvalue("otp4")
otp5=form.getvalue("otp5")
otp6=form.getvalue("otp6")

if submit!=None:
    f=f"""select * from user_otp where user_mail='{email}' and time='{time}'"""
    cur.execute(f)
    query=cur.fetchall()
    db_otp=query[0][2]
    db_phone=query[0][1]
    db_time=query[0][4]
    mob_otp = otp1 + otp2 + otp3 + otp4 + otp5 + otp6
    if email== db_phone and time==db_time:
        if mob_otp==db_otp:
            f=f"""UPDATE `user_otp` SET `status`='verified' WHERE `user_mail`='{email}' and `otp`='{mob_otp}' """
            cur.execute(f)
            con.commit()
            f=f"""UPDATE `userreg` SET `otp_status`='verified' where mail='{email}'"""
            cur.execute(f)
            con.commit()
            print(f"""<script>alert("OTP verification success and user registered.");
            alert("Login again :)")
            window.location.href="userlogin.py"</script>""")
        else:
            print(f"""<script>alert("Please enter correct OTP.");
                                        window.location.href="./otp.py"</script>""")
    else:
        print(f"""<script>alert("You entered expired otp or mobile num was not correct.");
                                    window.location.href="../user/userreg.py"</script>""")


