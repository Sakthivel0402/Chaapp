#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="chatapp")
cur = con.cursor()
form = cgi.FieldStorage()

id = form.getvalue("id")

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
    <title>user Friends</title>
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
        .content-section{
            display: flex;
            margin-top: 2%;
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
        <a href="./userFriends.py?id={id}" class="fw-bold active1 mb-3">Friends</a>
        <a href="./userProfile.py?id={id}" class="fw-bold mb-3 ">Profile</a>
        <a href="./groupChat.py?id={id}" class="fw-bold mb-3 ">Group</a>
        <a href="./groupReg.py?id={id}" class="fw-bold mb-3 ">Group Requests </a>

        <div class="logout">
 <a href="../forms/userlogin.py">Logout</a>        </div>
    </div>

    <button class="menu-btn" onclick="toggleSidebar()"><i class="fa-solid fa-bars"></i></button>

    <div class="content" id="content">
        <div class="d-flex justify-content-center gap-2">
            <input type="checkbox" class="btn-check" name="friendOptions" id="btn-check-all" autocomplete="off">
            <label class="btn btn-outline-primary" for="btn-check-all">All Friends</label>  
            
            <input type="checkbox" class="btn-check" name="friendOptions" id="btn-check-add" autocomplete="off">
            <label class="btn btn-outline-primary" for="btn-check-add">Given Requests</label> 
            
            <input type="checkbox" class="btn-check" name="friendOptions" id="btn-check-requests" autocomplete="off">
            <label class="btn btn-outline-primary" for="btn-check-requests">Requests</label>   <br> 
        </div>
        
        <!-- Content Sections -->
        <div id="content-all" class="content-section" ">
            <h2 class="mt-5"> Add Friends :</h2>
            <div class="row d-flex justify-content-center mb-5">
            <form method="post">
                <input class="form-control me-2 w-50 d-inline" type="search" name="num" placeholder="Search by number" aria-label="Search">
            <input class="btn btn-warning"  type="submit" value="Search">
              </form>""")

    search = form.getvalue("num")

    if search:
        search_term = f"%{search}%"
        query = "SELECT * FROM userreg WHERE LOWER(phone) LIKE LOWER(%s)"

        try:
            cur.execute(query, (search_term,))
            details = cur.fetchall()
            if details:
                print(f"""<div><h5 class="mt-4">Details for '{search}'</h5></div>
                            <table class='table table-success table-striped table-hover'>""")
                print("""<thead class="table-dark"><tr><th>Name</th><th>Phone</th><th>Action</th></tr></thead>""")
                print("""<tbody>""")
                for row in details:
                    print(f"""<form method="post"><input type="hidden" name="r_id" value={row[0]}>
                              <input type="hidden" name="r_name" value={row[1] + row[2]}">""")
                    r_id = row[0]
                    name = row[1] + " " + row[2]
                    phone = row[5]
                    print(f"""<tr><td>{name}</td><td>{phone}</td>""")
                    f = f"""select status from friend_requests where receiver_id='{r_id}'"""
                    cur.execute(f)
                    sts = cur.fetchone()

                    if sts is not None:
                        if sts[0] == 'pending':
                            print("""<td><div class="badge text-bg-warning">Request sent already</div></td>""")
                        elif sts[0] == 'friends':
                            print("""<td><div class="badge text-bg-success">Friends</div></td>""")
                        elif sts[0] == 'rejected':
                            print("""<td><div class="badge text-bg-danger">Rejected</div></td>""")
                    else:
                        print(
                            """<td><input type="submit" class="btn btn-primary" name="request" value="Send Friend Request"></form></td></tr>""")

                print("</tbody></table>")
            else:
                print("""<h2>No users found</h2>""")
        except Exception as e:
            print(f"Error executing query: {e}")

    f = f"""SELECT sender_id, receiver_id FROM friend_requests WHERE (sender_id='{id}' OR receiver_id='{id}') AND status='friends'"""
    cur.execute(f)
    friend_list = cur.fetchall()

    friends = [friend_id for pair in friend_list for friend_id in pair if friend_id != int(id)]
    friends_str = ', '.join(map(str, friends))

    f = f"""SELECT * FROM userreg WHERE id IN ({friends_str})"""
    cur.execute(f)
    friends_details = cur.fetchall()
    if friends_details:
        print(f"""<div class="mb-2 mt-5 "><h2>Friend list:</h2></div>
                    <table class=" table table-success table-striped table-hover ">
                        <tbody>
                          <tr class="table-dark" >
                            <th scope="row">S.No</th>
                            <td>Name</td>
                            <td>Phone</td>
                            <td>Action</td>
                          </tr>""")
        sno = 1
        for i in friends_details:
            print(f"""
                      <tr><td>{sno}</td>
                            <td>{i[1] + " " + i[2]}</td>
                        <td>{i[5]}</td>
                        <td><a class="btn btn-primary" href="./chats.py?friend_id={i[0]}&id={id}">Chat</a></td>
                        </tr>""")
            sno += 1
        print("""</tbody></table></div>""")
        print("""</div>""")
    else:
        print("""<h4> You have no friends currently</h4>""")


    f = f"""select * from friend_requests where sender_id='{id}' and status='pending'"""
    cur.execute(f)
    given_requests = cur.fetchall()


    print(f"""<div id="content-add" class="content-section" style="display: none;">
            <h2 class="mb-3"> Given Requests:</h2>""")


    if given_requests == ():
        print("""<h5>No requests found..</h5>""")
        print("""</div>""")

    else:
        print(f"""
            <table class="table table-success table-striped table-hover ">
                <tbody>
                  <tr class="table-dark" >
                    <th scope="row">S.No</th>
                    <td>Name</td>
                    <td>Phone</td>
                    <td>Request status</td>
                  </tr>""")
        sno = 1
        for i in given_requests:
            f = f"""select * from userreg where id='{i[2]}'"""
            cur.execute(f)
            user_details = cur.fetchall()
            for i in user_details:
                print(f"""
                  <tr><td>{sno}</td>
                        <td>{i[1] + " " + i[2]}</td>
                    <td>{i[5]}</td>
                    <td><div class="badge text-bg-warning">Pending</div></td>
                    </tr>""")
                sno += 1
            print("""</tbody></table></div>""")




    f = f"""select * from friend_requests where receiver_id='{id}' and status='pending'"""
    cur.execute(f)
    received_requests = cur.fetchall()

    print("""  
            <div id="content-requests" class="content-section" style="display: none;">
                <h2 class="mt-3">  Friend Requests:</h2>""")
    if received_requests == ():
        print("""<h5>No requests founfcefcd..</h5>""")
    else:

        print(f"""
           <table class="table table-success table-striped table-hover ">
                
                  <tbody>
                    <tr class="table-dark" >
                      <th scope="row">S.No</th>
                      <td>Name</td>
                      <td>Phone</td>
                      <td>Action</td>
                    </tr>""")


    sno = 1
    for i in received_requests:
        f = f"""select * from userreg where id='{i[1]}'"""
        cur.execute(f)
        user_details = cur.fetchall()
        for i in user_details:
            print(f"""
                      <tr><td>{sno}</td>
                        <td>{i[1]+" "+ i[2]}</td>
                        <td>{i[5]}</td>
                        <td><form method="post"><input type="hidden" name="users_list" value="{i[0]}"> <input type="submit" name="accept" value="Accept" class="btn btn-success"> 
                                                 <input type="submit" name="reject" value="Reject" class="btn btn-danger">
                            </form></td>
                        </tr>""")
            sno += 1
    print("""</tbody></table></div></div>""")

    print("""
    
    <script>
        function showContentSection(checkboxId) {
            const contentId = `content-${checkboxId.split('-')[2]}`;
            const contentSection = document.getElementById(contentId);
            if (contentSection) {
                contentSection.style.display = 'block';
            }
        }
    
        function uncheckOtherButtons(checkbox) {
            document.querySelectorAll('.btn-check').forEach(otherBtn => {
                if (otherBtn !== checkbox) {
                    otherBtn.checked = false;
                }
            });
        }
    
        document.querySelectorAll('.btn-check').forEach(btn => {
            btn.addEventListener('change', function () {
                document.querySelectorAll('.content-section').forEach(content => {
                    content.style.display = 'none';
                });
    
                uncheckOtherButtons(this);
    
                if (this.checked) {
                    showContentSection(this.id);
                }
            });
        });
    
        window.onload = function () {
            const allFriendsCheckbox = document.getElementById('btn-check-all');
            if (allFriendsCheckbox) {
                allFriendsCheckbox.checked = true;
                showContentSection(allFriendsCheckbox.id);
            }
        };
  

        let sidebarState = 0; 

        function toggleSidebar() {
            let sidebar = document.getElementById("sidebar");
            let content = document.getElementById("content");

            if (sidebarState === 0) {
                sidebar.style.width = "400px";
                content.style.marginLeft = "400px";
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
</html>""")

else:
    print(f"""<script> alert("Please login to continue");
     href.location="../forms/userLogin.py"</script>""")

#FOR GIVE REQUESTS:)
request = form.getvalue("request")
r_id=form.getvalue("r_id")
name=form.getvalue("r_name")
if request != None:
        f = f"""INSERT INTO `friend_requests`( `sender_id`, `receiver_id`, `status`, `created_at`) VALUES ('{id}','{r_id}','pending',CURRENT_TIMESTAMP) """
        cur.execute(f)
        con.commit()
        print(f"""<script> alert("Request given to {name}, please wait for sometime..");
             href.location="../forms/userFriends.py?id={id}"</script>""")


#FOR RECEIVED REQUESTS:)
accept=form.getvalue("accept")
users_list=form.getvalue("users_list")
f=f"""select firstname,lastname from userreg where id='{users_list}'"""
cur.execute(f)
friend_name=cur.fetchone()

if accept!=None:
    f=f"""update friend_requests set status="friends" where receiver_id='{id}' and sender_id='{users_list}'"""
    cur.execute(f)
    con.commit()
    f = f"""update friend_requests set status="friends" where receiver_id='{users_list}' and sender_id='{id}'"""
    cur.execute(f)
    con.commit()
    print(f"""<script> alert("You and {friend_name[0]+" "+friend_name[1]} were friends now");
                 href.location="../forms/userFriends.py?id={id}"</script>""")


reject=form.getvalue("reject")
if reject!=None:
    print(f"""<script> alert("Please ooooo to continue");
         href.location="../forms/userLogin.py"</script>""")