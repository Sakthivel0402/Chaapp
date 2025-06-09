#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="chatapp")
cur = con.cursor()
form = cgi.FieldStorage()

id = form.getvalue("id")

q = f"""select * from userreg where id='{id}'"""
cur.execute(q)
query = cur.fetchall()



if query:
    profile = query[0][14]
    print("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>user Profile</title>
   <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Open Sans", serif;
            font-weight: 400;
        }

        body {
            background-color: #b4ffdf;
            color: #282B28;
        }

        /* Sidebar */
        .sidebar {
            height: 100vh;
            width: 250px; /* Default for big screens */
            position: fixed;
            left: 0;
            background: #b4ffdf;
            color: #004aad; 
            box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
            overflow-y: auto;
            transition: width 0.3s ease-in-out;
            z-index: 1000;
        }

        .sidebar h4 {
            text-align: center;
            padding: 15px;
            font-weight: bold;
        }

        .sidebar a {
            color: #004aad;
            text-decoration: none;
            padding: 10px 15px;
            display: block;
            border-radius: 5px;
            margin: 5px;
        }

        .sidebar a:hover, .active1 {
            background-color: #dceeff;
            color: #002766;
        }

        /* Content */
        .content {
            margin-left: 250px;
            padding: 20px;
            transition: margin-left 0.3s ease-in-out;
        }

        /* Logout Button */
        .logout {
            position: absolute;
            bottom: 20px;
            width: 100%;
            text-align: center;
        }

        .logout a {
            display: block;
            padding: 8px 15px;
            color: #dd2323;
            text-decoration: none;
            font-weight: bold;
            border: 1px solid #dd2323;
            border-radius: 5px;
        }

        .logout a:hover {
            background-color: #dd2323;
            color: #ffffff;
        }

        .menu-btn {
            position: fixed;
            top: 10px;
            right: 10px;
            background: #004aad;
            color: white;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            border-radius: 5px;
            z-index: 1100;
            transition: all 0.3s ease-in-out;
            display: none; /* Hide by default */
        }

        .menu-btn:hover {
            background: #002766;
        }

        @media screen and (max-width: 767px) {
            .sidebar {
                width: 0;
            }

            .content {
                margin-left: 0;
            }

            .menu-btn {
                display: block; 
            }
        }
        
         

    </style>
</head>""")
    print(f"""
<body>

    <!-- Sidebar -->
    <div class="sidebar" id="sidebar">
        <h4>User Dashboard</h4>

       <a href="./userDashboard.py?id={id}" class="fw-bold  mb-3">Home</a>
        <a href="./userChat.py?id={id}" class="fw-bold  mb-3">Chat</a>
        <a href="./userFriends.py?id={id}" class="fw-bold mb-3">Friends</a>
        <a href="./userProfile.py?id={id}" class="fw-bold mb-3 active1  ">Profile</a>
        <a href="./groupChat.py?id={id}" class="fw-bold mb-3 ">Group</a>
        <a href="./groupReg.py?id={id}" class="fw-bold mb-3 ">Group Requests </a>
        <div class="logout">
 <a href="../forms/userlogin.py">Logout</a>        </div>
    </div>

    <button class="menu-btn" onclick="toggleSidebar()"><i class="fa-solid fa-bars"></i></button>

    <div class="content" id="content">
        <h1>Welcome, User</h1>

        <div><h2 class=" d-flex justify-content-center mt-5">Time to change your profile picture and password</h2></div>
        <div class="mt-4">""")
    if profile =='':
        print("""<h6> Upload your first profile picture</h6>""")
    else:
        print(f"""
                <img src="../assets/{profile}" width="200px"  style="border-radius: 50%; border: #b6d2ff 1px solid;" alt="hiii">""")

    print("""
    </div> <div class="">
 <form action="" method="post" enctype="multipart/form-data">

            <label for="" class="mb-2 mt-4">Change your profile picture</label><input type="file" class="form-control w-25" name="pic" id=""></div>
            <div> <input type="submit" class="btn btn-success mt-3" value="Update" name="profile" id=""></div>
</form>

            <div class="mt-5">
                <h5 class="mb-2" for="">Change password</h5> <br>
                <label class="mb-1" for="">Enter old password:</label>
                <input class="form-control w-25" type="password" name="" id="">

                <label class="mt-3 mb-1" for="">Enter new password:</label>
                <input class="form-control w-25" type="password" name="" id="">

                <div> <input type="submit" class="btn btn-success mt-3" value="Change now" name="" id=""></div>
            </div>


    </div>

""")
    print("""
    <script>
        let sidebarState = 0; 

        function toggleSidebar() {
            let sidebar = document.getElementById("sidebar");
            let content = document.getElementById("content");

            if (sidebarState === 0) {
                sidebar.style.width = "320px";
                content.style.marginLeft = "320px";
                sidebarState = 1;
            }else {
                sidebar.style.width = "0";
                content.style.marginLeft = "0";
                sidebarState = 0;
            }
        }

        function adjustSidebar() {
            let screenWidth = window.innerWidth;
            let sidebar = document.getElementById("sidebar");
            let content = document.getElementById("content");
            let menuBtn = document.querySelector(".menu-btn");

            if (screenWidth > 767) {
                sidebar.style.width = "250px"; 
                content.style.marginLeft = "250px";
                menuBtn.style.display = "none";
            } else {
                sidebar.style.width = "0"; 
                content.style.marginLeft = "0";
                menuBtn.style.display = "block";
            }
        }

        window.addEventListener("resize", adjustSidebar);
        window.addEventListener("load", adjustSidebar);
    </script>

</body>
</html>
""")

else:
    print(f"""<script> alert("Please login to continue");
     href.location="../forms/userLogin.py"</script>""")


profile=form.getvalue("profile")
if profile != None:
    pic=form['pic']
    if pic.filename:
        proof = os.path.basename(pic.filename)
        open("../assets/" + proof, "wb").write(pic.file.read())
        u=f"""update userreg set profile='{proof}'  where id='{id}'"""
        cur.execute(u)
        con.commit()
        print(f"""<script>location.href="userProfile.py?id={id}"
                                       alert("Success !")
                                 </script>""")