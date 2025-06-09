#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="chatapp")
cur = con.cursor()
form = cgi.FieldStorage()



print("""

    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>admin Dashboard</title>
   <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Bootstrap Bundle JS (with Popper.js) -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

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
</head>

<body>

    <!-- Sidebar -->
    <div class="sidebar" id="sidebar">
        <h4>Admin Dashboard</h4>

        <a href="./adminDashboard.py" class="fw-bold  ">Home</a>
       <a href="adminUsers.py" class="fw-bold active1"> Manage Users</a>
        <a href="adminGroups.py" class="fw-bold"> Manage Groups</a>
        <a href="adminUserchats.py" class="fw-bold ">  User Chats </a>
        <a href="adminGroupchats.py" class="fw-bold ">  Group Chats </a>


        <div class="logout">
 <a href="../forms/adminLogin.py">Logout</a>        </div>
    </div>

    <button class="menu-btn" onclick="toggleSidebar()"><i class="fa-solid fa-bars"></i></button>

    <div class="content" id="content">
        <h1>Welcome, Admin</h1>
        
        <div> <h3 class="mt-5"> User list:</h3>
    """)

f="""select * from userreg where otp_status='verified' and block_status=''"""
cur.execute(f)
users=cur.fetchall()

print("""
<table class="table table-bordered table-hover">
    <thead>
        <tr class="table-dark">
            <th>S.No</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
""")

sno = 1
for i in users:
    print(f"""
        <tr>
            <td>{sno}</td>
            <td>{i[1]}</td>
            <td>{i[2]}</td>
            <td>{i[6]}</td>
            <td>{i[5]}</td>
            <td>
                <button type="button" class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#viewUserModal{i[0]}">View More</button>
            </td></tr>""")

    sno += 1

    print(f"""
    <div class="modal fade" id="viewUserModal{i[0]}" tabindex="-1" aria-labelledby="userModalLabel{i[0]}" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="userModalLabel{i[0]}">User Details</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p><strong>ID:</strong> {i[0]}</p>
                    <p><strong>Name:</strong> {i[1]} {i[2]}</p>
                    <p><strong>DOB:</strong> {i[3]}</p>
                    <p><strong>Gender:</strong> {i[4]}</p>
                    <p><strong>Phone:</strong> {i[5]}</p>
                    <p><strong>Email:</strong> {i[6]}</p>
                    <p><strong>Address:</strong> {i[7]}, {i[8]}, {i[10]}, {i[11]}, {i[12]}</p>
                    <p><strong>ZIP Code:</strong> {i[9]}</p>
                    <p><strong>Aadhar No:</strong> {i[13]}</p>
                    <p><strong>Status:</strong> {i[15]}</p>
                    <p><strong>Profile Picture:</strong></p>
                    <img src="../assets/{i[14]}" alt="Profile" class="img-fluid" width="100">
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#blockUserModal{i[0]}">Block User</button>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Block User Modal -->
    <div class="modal fade" id="blockUserModal{i[0]}" tabindex="-1" aria-labelledby="blockUserLabel{i[0]}" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="blockUserLabel{i[0]}">Block User</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form method="post">
                    <div class="modal-body">
                        <label for="blockReason{i[0]}" class="form-label">Reason for blocking:</label>
                        <textarea class="form-control" name="block_reason" id="blockReason{i[0]}" rows="3" placeholder="Enter reason..."></textarea>
                        <input type="hidden" name="block_user_id" value="{i[0]}">
                    </div>
                    <div class="modal-footer">
                        <input type="submit" class="btn btn-danger" name="block_user" value="Confirm Block">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    """)

block_user = form.getvalue("block_user")
block_user_id = form.getvalue("block_user_id")
block_reason = form.getvalue("block_reason")

if block_user:
    u=f"""UPDATE `userreg` SET `block_status`='blocked' where id='{block_user_id}'"""
    cur.execute(u)
    con.commit()
    f = f"""INSERT INTO `blocked_users`( `user_id`, `reason`) VALUES ('{block_user_id}','{block_reason}')"""
    cur.execute(f)
    con.commit()
    print(f"""<script> 
        alert("User {block_user_id} blocked for reason: {block_reason}"); 
        window.location.href="./adminUsers.py";
    </script>""")


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
</html> """)



