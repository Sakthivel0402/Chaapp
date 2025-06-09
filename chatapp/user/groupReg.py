#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="chatapp")
cur = con.cursor()
form = cgi.FieldStorage()

id = form.getvalue("id")
group_id = form.getvalue("gid")

q = f"""select * from userreg where id='{id}'"""
cur.execute(q)
query = cur.fetchall()



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
        
          body { font-family: Arial, sans-serif; margin: 20px; }
        .container { width: 350px; margin: auto; }
        label, input, textarea { display: block; width: 100%; margin-bottom: 10px; }
        .button { display: block; width: 100%; padding: 10px; background: blue; color: white; border: none; }

    </style>
</head>
""")
    print(f"""
<body>

    <!-- Sidebar -->
    <div class="sidebar" id="sidebar">
        <h4>User Dashboard</h4>

        <a href="./userDashboard.py?id={id}" class="fw-bold  mb-3">Home</a>
        <a href="./userChat.py?id={id}" class="fw-bold  mb-3">Chat</a>
        <a href="./userFriends.py?id={id}" class="fw-bold mb-3">Friends</a>
        <a href="./userProfile.py?id={id}" class="fw-bold mb-3 ">Profile</a>
        <a href="./groupChat.py?id={id}" class="fw-bold mb-3 ">Group</a>
        <a href="./groupReg.py?id={id}" class="fw-bold mb-3 active1">Group Requests </a>

        <div class="logout">
 <a href="../forms/userlogin.py">Logout</a>        </div>
    </div>

    <button class="menu-btn" onclick="toggleSidebar()"><i class="fa-solid fa-bars"></i></button>

    <div class="content" id="content">
        <div class="container">
        <h2>Create new group</h2>
        <form  method="POST" enctype="multipart/form-data">
            <label for="group_name">Group Name:</label>
            <input type="text" class="form-control" id="group_name" name="group_name" required>""")
    print("""<label for="profile_pic">Profile Picture:</label>
                <input type="file" id="profile_pic" class="form-control" name="profile_pic" accept="image/*">

                <input type="submit" name="register" value="Create new group" class="button"> 
           
    <label for="members">Add members:</label>""")
    f = f"""SELECT sender_id, receiver_id FROM friend_requests WHERE (sender_id='{id}' OR receiver_id='{id}') AND status='friends'"""
    cur.execute(f)
    friend_list = cur.fetchall()

    friends = [friend_id for pair in friend_list for friend_id in pair if friend_id != int(id)]
    friends_str = ', '.join(map(str, friends))

    f = f"""SELECT * FROM userreg WHERE id IN ({friends_str})"""
    cur.execute(f)
    friends_details = cur.fetchall()

    for i in friends_details:
        print(f"""
            <div style="display: flex; align-items: center; ">
                <input type="checkbox" name="friends" value="{i[0]}" id="friend_{i[0]}" >
                <label for="friend_{i[0]}">{i[1]} (Friends)</label>
            </div></form>""")

    print("""
    </div>    
    
    <h2 class="mt-5">Group Requests:</h2>""")
    f = f"""select * from chat_groups where user_id='{id}' and (status='pending' or status='created')"""
    cur.execute(f)
    user_details = cur.fetchall()
    if user_details == ():
        print("""<h5 class="mt-4">No requests found..</h5>""")
    else:
        print(f"""
           <table class="table table-success table-striped table-hover ">

                  <tbody>
                    <tr class="table-dark" >
                      <th scope="row">S.No</th>
                      <td>Group name</td>
                      <td>Group members</td>
                      <td>Action </td>
                    </tr>""")
    sno=1
    for i in user_details:
        print(f"""
                          <tr><td>{sno}</td>
                            <td>{ i[2]}</td>""")
        f=f"""select member_name from chat_groups where group_id='{i[1]}'"""
        cur.execute(f)
        mems=cur.fetchall()
        cleaned_string = ", ".join(i[0] for i in mems)
        print(f"""<td>{cleaned_string}</td>""")
        if i[7]==query[0][1]:
            print(f"""<td>You created this group </td>""")
        else:
            print(f"""<td><form method="post"><input type="hidden" name="users_list" value="{i[0]}"> <input type="submit" name="accept" value="Accept" class="btn btn-success"> 
                  <input type="submit" name="reject" value="Reject" class="btn btn-danger"></form></td></tr>""")
        sno+=1

    print("""</tbody></table>""")








    print("""<script>
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
</html>    """)

else:
    print(f"""<script> alert("Please login to continue");
     href.location="../forms/userLogin.py"</script>""")

group_name=form.getvalue("group_name")
friend_count=form.getvalue("friends")

register=form.getvalue("register")
if register is not None:
    # Profile Picture Handling
    pic = form["profile_pic"]
    proof = ""
    if pic.filename:
        proof = os.path.basename(pic.filename)
        open("../assets/" + proof, "wb").write(pic.file.read())

    cur.execute("SELECT MAX(id) FROM chat_groups")
    group = cur.fetchone()

    if group[0] is not None:
        if group[0] < 10:
            num = "GRO00" + str(group[0] + 1)
        elif group[0] < 100:
            num = "GRO0" + str(group[0] + 1)
        elif group[0] < 1000:
            num = "GRO" + str(group[0] + 1)
    else:
        num = "GRO001"

    for friend_id in friend_count:
        cur.execute(f"SELECT id, firstname FROM userreg WHERE id='{friend_id}'")
        user_details = cur.fetchone()

        if user_details:
            insert_query = f"""INSERT INTO `chat_groups` 
                (`group_id`, `group_name`, `member_name`, `profile`, `user_id`, `status`)
                VALUES ('{num}', '{group_name}', '{user_details[1]}', '{proof}', '{user_details[0]}', 'pending')"""
            cur.execute(insert_query)

    con.commit()
    insert_query = f"""INSERT INTO `chat_groups` 
                    (`group_id`, `group_name`, `member_name`, `profile`, `user_id`, `status`,`created_by`)
                    VALUES ('{num}', '{group_name}', '{query[0][1]}', '{proof}', '{id}', 'created','{query[0][1]}')"""
    cur.execute(insert_query)
    con.commit()
    print(f"""<script>alert("Group registered ");
        window.location.href = "./groupReg.py?id={id}"; </script>""")


accept=form.getvalue("accept")
reject=form.getvalue("reject")

if accept != None:
    f=f"""UPDATE `chat_groups` SET `status`='accepted' where user_id='{id}' """
    cur.execute(f)
    con.commit()

    print(f"""<script>alert("You are now in {i[2]} ");
            window.location.href = "./groupReg.py?id={id}"; </script>""")


if reject != None:
    print(f"""<script>alert("Group registered ");
            window.location.href = "./groupReg.py?id={id}"; </script>""")