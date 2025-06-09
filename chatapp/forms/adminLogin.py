#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="chatapp")
cur = con.cursor()

print("""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> admin Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>
<script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>


    <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    *{
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
        font-weight: 300;
    }
        body {
            background-color: #b4ffdf;
            color: #020202;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 17px;
            height: 100vh;
        }

        form {
            width: 500px;
            padding: 20px;
        }

        .side-nav1 {
            font-size: 20px;
            font-weight: 500;
        }
        .form-control{


        }
        .form-control:focus {
        outline: none; 
        border-color: #28a745; 
        box-shadow: 0 0 5px rgba(40, 167, 69, 0.5);
         background-color: #FFF8F0;
    }

        .custom-shadow {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .blur-effect {
            backdrop-filter: blur(1px); 
            background-color: rgba(255, 255, 255, 0.2); 
            padding: 20px;
            border-radius: 10px;
        }

        #sidebar {
            background: rgba(255, 255, 255, 0.1); 
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }

        .main-content {
            flex-grow: 1;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); 
            background: rgba(255, 255, 255, 0.01); 
        }

        .nav-link {
            padding: 10px 20px;
            color: #000;
            text-decoration: none;
            border-radius:10px !important;
            display: block;
            font-size: 17px; /* Make all text the same size */
            transition: all ease 0.6s;
            font-weight: 500;
        }

        .nav-link:hover {
            background-color: #083D77 !important;
            color: #ffffff !important;
            border-radius: 4px;
        }

        .nav-link:active {
            background-color: #083D77 !important;
            color: #ffffff !important;
        }

        .active {
            background-color: #083D77 !important;
            color: #ffffff;
            border-radius: 4px;
        }

        .text {
            font-size: 17px;
            color: #000000;
            padding: 5px 10px;
            transition: all ease 0.6s;
        }
        .text:hover{
            color: #083D77;
            transition: all ease 0.6s;

        }

        .accordion-item {
            margin-bottom: 20px; 
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(128, 125, 125, 0.527); 
        }

        .accordion-button {
            font-size: 17px;
            font-weight: 500;
            padding: 10px 20px;
            border-radius: 10px;
            transition: all ease 0.6s;
            background-color: #FFF8F0;

        }
        .accordion-button:hover{
            background-color: #083D77;
            color: #FFF8F0;
            transition: all ease 0.6s;

        }

        .accordion-body{
            background-color: #FFF8F0;
                    }

        .accordion-body a{
            color: #ff8800;
                    }
        .accordion-item a {
            display: block;
            padding: 10px 20px;
            font-size: 17px;
            font-weight: 500;
        }

        .main-header {
            position: relative;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            height: 100px;
        }

         span{
    color: rgb(49, 124, 209);
    font-weight: 400;
    margin-left: 6px;
  }

        .main-header h1 {
            margin-left: -150px;
            text-align: center;
            flex-grow: 1;
        }

        .logout-btn {
            background-color: rgb(244, 67, 54);
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 17px;
            box-shadow: 0 4px 6px rgba(244, 67, 54, 0.71); 
            transition: all ease 0.6s;
        }

        .logout-btn:hover {
            background-color: #d32f2f;
            box-shadow: 0 6px 8px rgba(255, 112, 101, 0.71);
        }

        .main-header img {
            max-width: 350px;
        }
        .lol{
            color: #ffffff !important;
        }
        .accordion-button{
            box-shadow: none !important;
        }

    </style>
</head>

<body>
 <div class="main-header">
        <a class="mt-5 text-decoration-none text-dark " href="../index.py"><h3 class="fw-bold">CrypTalk ;)</h3></a>

    </div>
    <form action="" method="post" enctype="multipart/form-data">

        <div class="container border mt-5 rounded-4  custom-shadow mb-5 blur-effect">
            <h2 class="text-center mb-4 fw-bold">Admin Login</h2>
            <div class="row">
                <div class="ms-5 col-md-10">
                    <img src="assets/user (1).png" class="mb-1" width="15px" alt=""> <label for="" class="form-label mt-5"> Admin ID</label> <br>
                    <input type="text" name="username" id="" class="form-control">
                </div>
            </div>
            <div class="row">
                <div class="col-md-10 mt-4 ms-5">
                    <img src="assets/padlock.png" class="mb-1" width="15px" alt=""> <label for="" class="form-label">Password</label> <br>
                    <input type="password" name="password" id="" class="form-control">

                </div>
            </div>
            <div class="row">
                <div class="col-md-3"></div>
                <div class="col-md-3 mt-4 d-flex justify-content-center">
                    <input type="submit" class="btn btn-primary" value="Login" name="login">
                </div>
                <div class="col-md-3 mt-4 d-flex justify-content-center">
                    <a type="submit" href="./index.py" class="btn btn-danger">Back</a>
                    </form>
                </div>
                <div class="col-md-3"></div>
            </div>

     </div>   

</body>""")

login = store.getvalue("login")
if login != None:
    adminID = store.getvalue("username")
    password = store.getvalue("password")
    if adminID == "admin" and password == "1234":
        print("""
        <script>alert("Login Successful!")
        location.href="../admin/adminDashboard.py"
        </script>""")
    else:
        print("""
                <script>alert("Enter valid username or password!")
                location.href="adminLogin.py"
                </script>""")
