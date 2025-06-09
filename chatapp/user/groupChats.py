#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
from datetime import datetime, timedelta

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="chatapp")
cur = con.cursor()
form = cgi.FieldStorage()

id = form.getvalue("id")
group_id = form.getvalue("group_id")

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
    <title>group chat</title>
    <!-- Bootstrap CSS -->
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
       <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">


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
            padding: 10px;
            transition: margin-left 0.3s ease-in-out;
        }


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

        .chat-container {
            height: 100vh;
            display: flex;
            overflow: hidden;
        }

        /* Sidebar (Fixed) */
        .chat-sidebar {
            width: 20.5%;
            top: 0;
            background: #efefef;
            border-right: 1px solid #ddd;
            display: flex;
            flex-direction: column;
            position: fixed;
            height: 100vh;
        }

        /* Sidebar Header */
        .sidebar-header {
            padding: 15px;
            background: #66937d;
            color: white;
            font-weight: bold;
            text-align: center;

        }

        /* Sidebar Chats List */
        .chat-list {
            flex-grow: 1;
            overflow-y: auto;
            padding: 10px;
        }

        .chat-list div {
            padding: 10px;
            border-bottom: 1px solid #ddd;
            cursor: pointer;
        }

        .chat-list div:hover {
            background: #e9ecef;
        }

        /* Chat Window */
        .chat-window {
            width: 75%;
            margin-left: 25%;
            display: flex;
            flex-direction: column;
            height: 100vh;

        }

        /* Chat Header (Fixed) */
        .chat-header {
            padding: 15px;
            border-left: 1px black solid;
            background: #66937d;
            color: white;
            font-weight: bold;
            position: fixed;
            width: 64%;
            top: 0;
            z-index: 1000;
        }

        .chat-body {
         padding: 10px; 
        overflow-y: auto;
         display: flex;
        flex-direction: column-reverse; /* Puts new messages at the bottom */
        scroll-behavior: smooth;
        margin-top: 4%;
        margin-bottom:5%;


        }

      .chat-message {
    padding: 5px;
    border-radius: 8px;
    margin-bottom: 5px;
    max-width: 60%;
    word-wrap: break-word;
}

.message-sent {
    background-color: #dcf8c6; /* Light green (like WhatsApp) */
    align-self: flex-end;
    text-align: right;
}

.message-received {
    background-color: #f1f1f1;
    align-self: flex-start;
    text-align: left;
}

.message-time {
    font-size: 9px;
    color: gray;
    margin-top: 3px;
}

        .chat-footer {
            position: fixed;
            bottom: 0;
            width: 80%;
            background: #fff;
            padding: 10px;
            border-top: 1px solid #ccc;
            display: flex;
            align-items: center;
        }

        .message-input {
            width: 70% !important;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 20px;
            margin-right: 10px;
        }

        /* Responsive for Mobile */
        /* Responsive for Small Screens */
        @media (max-width: 768px) {
            .chat-body {
                width: 100%;
                position: fixed;
                z-index: 1000;
                height: 100%;
                transform: translateX(0);
            }

            .chat-window {
                width: 100%;
                margin-left: 0;
            }

            .chat-body{
                margin-top: 8%;
                margin-bottom:10%;
            }
            .chat-footer{
                z-index: 10000;
            }
            .chat-header{
                z-index: 10000;
            }
            .chat-footer > input{
                margin-left: 12px;
            }

            .chat-header, .chat-footer {
                width: 100%;
            }
            .chat-sidebar{
                display:none;
            }

            .back-btn {
                display: inline-block;
                background: none;
                border: none;
                color: white;
                font-size: 20px;
            }
        }

        .send{
border-radius: 50%;
height: fit-content;
font-weight: 900;
        }
        .sender {
    background-color: #dcf8c6; /* Light green */
    text-align: right;
    float: right;
    clear: both;
}

.sender-name {
        font-weight: bold;      
        font-size: 12px;       
        color: blue;            
        margin-bottom: 3px;   
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
        <a href="./userProfile.py?id={id}" class="fw-bold mb-3 ">Profile</a>
        <a href="./groupChat.py?id={id}" class="fw-bold active1 mb-3 ">Group</a>
        <a href="./groupReg.py?id={id}" class="fw-bold mb-3 ">Group Requests </a>

        <div class="logout">
 <a href="../forms/userlogin.py">Logout</a>        </div>
    </div>

    <button class="menu-btn" onclick="toggleSidebar()"><i class="fa-solid fa-bars"></i></button>

    <div class="content" id="content">
        <div class="chat-container">""")
    f = f"""SELECT * FROM chat_groups WHERE user_id='{id}' AND (status='accepted' or status='created')"""
    cur.execute(f)
    group_details = cur.fetchall()


    print(f"""
            <div class="chat-sidebar">
                <div class="hello">
                <div class="sidebar-header">Chats</div>
                <div class="chat-list">""")
    for i in group_details:
        print(f"""
        <div>
            <a href="#" class="chat-link text-decoration-none text-dark" data-id="{i[1]}">
                <img src="../assets/{i[4]}" width="25px"> {i[2]}
            </a>
        </div>
        """)
    print("""
                </div>
            </div>
            </div>""")

    f = f"""select group_name from chat_groups where group_id='{group_id}'"""
    cur.execute(f)
    group_name = cur.fetchone()


    print(f"""
            <div class="chat-window">
            <div class="chat-header"><a href="" class="d-inline"> <i class="fa-solid fa-arrow-left-long me-3" title="Back"></i></a> <div class="  d-inline text-decoration-none" style="color: #282B28;  ">{group_name[0]}</div>
           </div>

                <div class="chat-body d-flex flex-column" id="chat-body">""")
    f = f"""SELECT sender_id, message, sent_at,type FROM group_messages WHERE (sender_id='{id}' or group_id='{group_id}') ORDER BY sent_at ASC"""
    cur.execute(f)
    chat = cur.fetchall()


    if not chat:
        print(f"""<div class="mt-5"> <h4 class="d-flex justify-content-center"> Start your convo now :)</h4></div>""")
    else:
        for msg in chat:
            sender_id, message, sent_at, msg_type = msg

            time_format = sent_at.strftime("%I:%M %p") if sent_at else ""

            # Fetch sender's name if it's not the logged-in user
            sender_name = ""
            if int(sender_id) != int(id):
                cur.execute(f"SELECT firstname FROM userreg WHERE id='{sender_id}'")
                sender_name = cur.fetchone()[0] if cur.rowcount > 0 else "Unknown"

            if int(sender_id) == int(id):
                print(f"""<div class="chat-message message-sent">""")
            else:
                print(f"""<div class="chat-message message-received">""")


                print(f"""<div class="sender-name">{sender_name}</div>""")

            if msg_type == "text":
                print(f"""{message}""")
            elif msg_type == "image":
                print(f"""<img src="../assets/{message}" width="150px" class="chat-image">""")

            # Show time
            print(f"""<div class="message-time">{time_format}</div></div>""")

    print("""</div>
        <form method="post" enctype="multipart/form-data" id="chatForm">
                <div class="chat-footer">
                    <input type="file" name="pic" id="fileInput" style="display: none;" accept="image/*" onchange="uploadFile()">

                    <button type="button" class="btn fw-bold" onclick="document.getElementById('fileInput').click()">+</button>


                    <input type="text" name="msg" class="message-input"  placeholder="Type a message..."><div></div>

                   
                        <input type="submit" title="Send" class="btn send btn-success" name="send" value=">"></form> 
                </div>""")



    print("""</div>""")



    print(f"""
    <script>



    document.addEventListener("DOMContentLoaded", function() {{
    const chatLinks = document.querySelectorAll(".chat-link");

    chatLinks.forEach(link => {{
        link.addEventListener("click", function(event) {{
            event.preventDefault();
            let groupId = this.getAttribute("data-id"); 
            window.location.href = `groupChats.py?group_id=${{groupId}}&id={id}`;
        }});
    }});
}});
    """)
    print("""  

    setInterval(() => {
    location.reload();  
}, 100000);

    window.onload = function() {
    let chatbox = document.getElementById("chat-body");
    chatbox.scrollTop = chatbox.scrollHeight;  
};


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
</html>""")

else:
    print(f"""<script> alert("Please login to continue");
     href.location="../forms/userLogin.py"</script>""")

send = form.getvalue("send")
msg = form.getvalue("msg")
file = form.getvalue("pic")


msg_type = form.getvalue("msg_type")
if send != None:
    if file != None:
        pic = form["pic"]
        if pic.filename:
            proof = os.path.basename(pic.filename)
            open("../assets/" + proof, "wb").write(pic.file.read())
            f = f"""INSERT INTO `group_messages`( `sender_id`, `group_id`, `message`, `sent_at`,`type`) VALUES ('{id}','{group_id}','{proof}',CURRENT_TIMESTAMP,'image')"""
            cur.execute(f)
            con.commit()
            print(f"""<script>alert("File Sent: {proof}");
                    window.location.href = "./groupChats.py?group_id={group_id}&id={id}";</script>""")
    if msg!=None:
        f = f"""INSERT INTO `group_messages`( `sender_id`, `group_id`, `message`, `sent_at`,`type`) VALUES ('{id}','{group_id}','{msg}',CURRENT_TIMESTAMP,'text')"""
        cur.execute(f)
        con.commit()
        print(f"""<script>alert("msg sent");
                 window.location.href = "./groupChats.py?group_id={group_id}&id={id}";</script>""")