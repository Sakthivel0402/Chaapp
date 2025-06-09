#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="chatapp")
cur = con.cursor()
form = cgi.FieldStorage()

id=form.getvalue("id")

q=f"""select * from userreg where id='{id}' and block_status=''"""
cur.execute(q)
query=cur.fetchall()

if query:
    print("""
    
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>user Dashboard</title>
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
        
        .btn {
            background-color: #28AFB0;
            color: white;
            padding: 10px 15px;
            border: none;
            height:45px;
            width:180px;
            font-size:15px;
            border-radius: 5px;
            cursor: pointer;
            text-align: center;
            display: inline-block;
            margin-top: 10px;
        }
        .btn:hover {
            background-color: #217980;
            color:#ffffff;
        }
        .btn:focus {
            background-color: #000000;
            color:#ffffff;
        }
         .card {
            background: #caffe8;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
            width:35%;
        }
        .card h3 {
            margin: 0 0 10px;
        }
        .card p {
            margin: 5px 0;
        }

.loader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #c7ffe7;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease-in-out;
        }
        .loader.active {
            opacity: 1;
            visibility: visible;
        }
        .bubble {
            width: 15px;
            height: 15px;
            margin: 5px;
            background-color: #474554;
            border-radius: 50%;
            animation: bounce 1.5s infinite ease-in-out;
        }
        .bubble:nth-child(2) {
            animation-delay: 0.2s;
        }
        .bubble:nth-child(3) {
            animation-delay: 0.4s;
        }
        @keyframes bounce {
            0%, 80%, 100% {
                transform: scale(0);
            }
            40% {
                transform: scale(1);
            }
        }
        
           @media (max-width: 768px) {
        .content {
            width: 95%;
        }

        .card {
        width:100%;
            margin: 10px 0;
            padding: 15px;
        }

        .btn {
            width: 100%;
            padding: 12px;
        }
    }
        
         @media (max-width: 468px) {
        .content {
            width: 95%;
        }

        .card {
        width:100%;
            margin: 10px 0;
            padding: 15px;
        }

        .btn {
            width: 100%;
            padding: 12px;
        }
    }
    </style>
</head>
""")
    print(f"""
<body>

<div class="loader" id="loader">
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
    </div>
    <!-- Sidebar -->
    <div class="sidebar" id="sidebar">
        <h4>User Dashboard</h4>

       <a id="loadTrigger" href="./userDashboard.py?id={id}" class="fw-bold active1 mb-3">Home</a>
        <a id="loadTrigger" href="./userChat.py?id={id}" class="fw-bold  mb-3">Chat</a>
        <a id="loadTrigger" href="./userFriends.py?id={id}" class="fw-bold mb-3">Friends</a>
        <a id="loadTrigger" href="./userProfile.py?id={id}" class="fw-bold mb-3 ">Profile</a>
        <a id="loadTrigger" href="./groupChat.py?id={id}" class="fw-bold mb-3 ">Group</a>
        <a id="loadTrigger" href="./groupReg.py?id={id}" class="fw-bold mb-3 ">Group Requests </a>

        <div class="logout">
 <a href="../forms/userlogin.py">Logout</a>        </div>
    </div>

    <button class="menu-btn" onclick="toggleSidebar()"><i class="fa-solid fa-bars"></i></button>

    <div class="content" id="content">
        <h1>Welcome, {query[0][1]}</h1>
        
         <div>
        
        <div class="card mt-4">
        <div class="loader" id="loader">
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
    </div>
                <h3>Add Friends</h3>
                <p>Add the people into your network.</p>
                <a id="loadTrigger" href="./userFriends.py?id={id}" class="btn">Add Friends </a>
            </div>
            <div class="card">
                <h3> Chats</h3>
                <p>Let's have fun with your friends.</p>
                <a id="loadTrigger" href="./userChat.py?id={id}" class="btn">View Chats</a>
            </div>
            <div class="card">
                <h3>Profile</h3>
                <p>View and edit your profile details.</p>
                <a id="loadTrigger" href="./userProfile.py?id={id}" class="btn">View Profile</a>
            </div>
        </div>
    </div>
""")
    print("""

    <script>
    
      document.getElementById("loadTrigger").addEventListener("click", function (e) {
            e.preventDefault(); // Prevent actual navigation
            
            const loader = document.getElementById("loader");
            loader.classList.add("active");

            setTimeout(() => {
                loader.classList.remove("active");
            }, 2000); // Simulate loading duration
        });
    
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
