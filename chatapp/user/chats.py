#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os
from datetime import datetime, timedelta

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="chatapp")
cur = con.cursor()
form = cgi.FieldStorage()

id = form.getvalue("id")
friend_id = form.getvalue("friend_id")

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
    <title>userChat</title>
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
            width: 75%;
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



    </style>
</head>""")
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

        <a id="loadTrigger"  href="./userDashboard.py?id={id}" class="fw-bold  mb-3">Home</a>
        <a id="loadTrigger" href="./userChat.py?id={id}" class="fw-bold active1 mb-3">Chat</a>
        <a id="loadTrigger" href="./userFriends.py?id={id}" class="fw-bold mb-3">Friends</a>
        <a id="loadTrigger" href="./userProfile.py?id={id}" class="fw-bold mb-3 ">Profile</a>
        <a id="loadTrigger" href="./groupChat.py?id={id}" class="fw-bold mb-3 ">Group</a>
        <a id="loadTrigger" href="./groupReg.py?id={id}" class="fw-bold mb-3 ">Group Requests </a>

        <div class="logout">
            <a href="../forms/userlogin.py">Logout</a>
        </div>
    </div>

    <button class="menu-btn" onclick="toggleSidebar()"><i class="fa-solid fa-bars"></i></button>

    <div class="content" id="content">
        <div class="chat-container">""")
    f = f"""SELECT sender_id, receiver_id FROM friend_requests WHERE (sender_id='{id}' OR receiver_id='{id}') AND status='friends'"""
    cur.execute(f)
    friend_list = cur.fetchall()

    friends = [friend_id for pair in friend_list for friend_id in pair if friend_id != int(id)]
    friends_str = ', '.join(map(str, friends))

    f = f"""SELECT * FROM userreg WHERE id IN ({friends_str})"""
    cur.execute(f)
    friends_details = cur.fetchall()
    print(f"""
            <div class="chat-sidebar">
                <div class="hello">
                <div class="sidebar-header">Chats</div>
                <div class="chat-list">""")
    for i in friends_details:
        print(f"""
        <div>
            <a href="#" class="chat-link text-decoration-none text-dark" data-id="{i[0]}">
                <img src="../assets/{i[14]}" width="25px"> {i[1]}
            </a>
        </div>
        """)
    print("""
                </div>
            </div>
            </div>""")

    f=f"""select firstname from userreg where id='{friend_id}'"""
    cur.execute(f)
    friend_name=cur.fetchone()
    print(f"""
            <div class="chat-window">
            <div class="chat-header"><a href="" class="d-inline"> <i class="fa-solid fa-arrow-left-long me-3" title="Back"></i></a> <div class="  d-inline text-decoration-none" style="color: #282B28;  ">{friend_name[0]}</div>
           </div>

                <div class="chat-body d-flex flex-column" id="chat-body">""")
    f = f"""SELECT sender_id, message, sent_at,type,schedule_time,disappear_after FROM messages WHERE (sender_id='{id}' AND receiver_id='{friend_id}') OR (sender_id='{friend_id}' AND receiver_id='{id}') ORDER BY sent_at ASC"""
    cur.execute(f)
    chat = cur.fetchall()
    current_time = datetime.now()

    if not chat:
        print("""<div class="mt-5"> <h4 class="d-flex justify-content-center"> Start your convo now :)</h4></div>""")
    else:
        for msg in chat:
            sender_id, message, sent_at, msg_type, schedule_time, disappear_after = msg

            if schedule_time:
                schedule_time = datetime.strptime(str(schedule_time), "%Y-%m-%d %H:%M:%S")
            if sent_at:
                sent_at = datetime.strptime(str(sent_at), "%Y-%m-%d %H:%M:%S")

            if schedule_time and current_time < schedule_time:
                continue

            if disappear_after and sent_at and (current_time - sent_at).total_seconds() > disappear_after:
                continue

            time_format = sent_at.strftime("%I:%M %p") if sent_at else ""

            if sender_id == int(id):  # Example user ID
                print(f"""<div class="chat-message message-sent">""")
            else:
                print(f"""<div class="chat-message message-received">""")

            # Display message based on type
            if msg_type == "text":
                print(f"""{message}""")
            elif msg_type == "image":
                print(f"""<img src="../assets/{message}" width="150px" class="chat-image">""")
            elif msg_type == "pdf":
                pdf_modal_id = f"pdfModal_{message.replace('.', '_')}"

                print(f"""<div style="background-color: #ffffffdf; color: black; height:30px;border-radius:5px;margin:5px;padding:5px;"><div href="../assets/{message}" style="cursor:pointer; font-weight:bold;" title="view" data-bs-toggle="modal" data-bs-target="#{pdf_modal_id}">
                           <i class="fa-solid fa-file"></i>      {message}</div></div> """)

                print(f"""
                            <div class="modal fade" id="{pdf_modal_id}" tabindex="-1" aria-labelledby="{pdf_modal_id}Label" aria-hidden="true">
                                <div class="modal-dialog modal-lg">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h5 class="modal-title" id="{pdf_modal_id}Label">PDF Preview</h5>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                        </div>
                                        <div class="modal-body">
                                            <iframe src="../assets/{message}" style="width: 100%; height: 500px;"></iframe>
                                            
                                        </div>
                                    </div>
                                </div>
                            </div>
                        """)

            # Show time
            print(f"""<div class="message-time">{time_format}</div></div>""")


    print("""</div>


    <form method="post" enctype="multipart/form-data" id="chatForm">
    <div class="chat-footer">
        <input type="file" name="pic" id="fileInput" style="display: none;" accept="image/*" onchange="uploadFile()">
        
        <button type="button" class="btn fw-bold" onclick="document.getElementById('fileInput').click()">+</button>


        <input type="text" name="msg" class="message-input"  placeholder="Type a message..."><div></div>
        
        <div class="btn-group dropup">
            <button type="button" class="btn btn-outline-secondary dropdown-toggle" data-bs-toggle="dropdown">
                <i class="fa-solid fa-ellipsis-vertical"></i>
            </button>
            <ul class="dropdown-menu">
                <li><button class="dropdown-item" type="button" data-bs-toggle="modal" data-bs-target="#scheduleModal" > Schedule Message</button></li>
                <li><button class="dropdown-item" type="button" data-bs-toggle="modal" data-bs-target="#disappearModal"> Disappear Message</button></li>
            </ul>
        </div>   
            <input type="submit" title="Send" class="btn send btn-success" name="send" value=">">
    </div>
        
            <div class="modal fade" id="scheduleModal" tabindex="-1" aria-labelledby="scheduleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="scheduleModalLabel">Schedule Message</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <label for="scheduleTime" class="form-label">Choose Date & Time:</label>
                <input type="datetime-local" name="schedule" id="scheduleTime" class="form-control">
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Schedule</button>
            </div>
        </div>
    </div>
</div>


<div class="modal fade" id="disappearModal" tabindex="-1" aria-labelledby="disappearModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="disappearModalLabel">Set Disappearance Timer</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <label for="disappearTime" class="form-label">Choose Duration:</label>
                <select id="disappearTime" name="disappear" class="form-control">
                    <option > select here</option>
                    <option value="5">5 seconds</option>
                    <option value="10">10 seconds</option>
                    <option value="30">30 seconds</option>
                    <option value="60">1 minute</option>
                    <option value="300">5 minutes</option>
                </select>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Set Timer</button>
            </div>
        </div>
    </div>
</div>
        
        
                
   

</form>
""")


    print(f"""
    <script>
    document.addEventListener("DOMContentLoaded", function() {{
    const chatLinks = document.querySelectorAll(".chat-link");

    chatLinks.forEach(link => {{
        link.addEventListener("click", function(event) {{
            event.preventDefault();
            let friendId = this.getAttribute("data-id"); // Get ID from data-id
            window.location.href = `chats.py?friend_id=${{friendId}}&id={id}`;
        }});
    }});
}});
    """)
    print("""  
    
    document.getElementById("loadTrigger").addEventListener("click", function (e) {
            e.preventDefault(); // Prevent actual navigation
            
            const loader = document.getElementById("loader");
            loader.classList.add("active");

            setTimeout(() => {
                loader.classList.remove("active");
            }, 2000); // Simulate loading duration
        });
    
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


import os

send = form.getvalue("send")
msg = form.getvalue("msg")
file = form.getvalue("pic")
schedule = form.getvalue("schedule")
disappear = form.getvalue("disappear")

if send:
    if msg and schedule:
        query = """INSERT INTO `messages` (`sender_id`, `receiver_id`, `message`, `sent_at`, `type`, `schedule_time`) 
                   VALUES (%s, %s, %s, CURRENT_TIMESTAMP, 'text', %s)"""
        cur.execute(query, (id, friend_id, msg, schedule))
        con.commit()
        print(f"""<script>
                 alert("msg scheduled at {schedule}");
                 window.location.href = "./chats.py?friend_id={friend_id}&id={id}";
              </script>""")

    elif msg and disappear != "select here":
        query = """INSERT INTO `messages` (`sender_id`, `receiver_id`, `message`, `sent_at`, `type`, `disappear_after`) 
                   VALUES (%s, %s, %s, CURRENT_TIMESTAMP, 'text', %s)"""
        cur.execute(query, (id, friend_id, msg, disappear))
        con.commit()
        print(f"""<script>
                 alert("this msg will disappear after {disappear} seconds");
                 window.location.href = "./chats.py?friend_id={friend_id}&id={id}";
              </script>""")

    elif file and schedule:
        pic = form["pic"]
        if pic.filename:
            proof = os.path.basename(pic.filename)
            open("../assets/" + proof, "wb").write(pic.file.read())
            query = """INSERT INTO `messages` (`sender_id`, `receiver_id`, `message`, `sent_at`, `type`, `schedule_time`) 
                       VALUES (%s, %s, %s, CURRENT_TIMESTAMP, 'image', %s)"""
            cur.execute(query, (id, friend_id, proof, schedule))
            con.commit()
            print(f"""<script>
                     alert("File {proof} uploaded and it will appear at {schedule}");
                     window.location.href = "./chats.py?friend_id={friend_id}&id={id}";
                  </script>""")

    elif file and disappear != "select here":
        pic = form["pic"]
        if pic.filename:
            proof = os.path.basename(pic.filename)
            open("../assets/" + proof, "wb").write(pic.file.read())
            query = """INSERT INTO `messages` (`sender_id`, `receiver_id`, `message`, `sent_at`, `type`, `disappear_after`) 
                       VALUES (%s, %s, %s, CURRENT_TIMESTAMP, 'image', %s)"""
            cur.execute(query, (id, friend_id, proof, disappear))
            con.commit()
            print(f"""<script>
                     alert("File Sent: {proof} and it will disappear in {disappear} seconds");
                     window.location.href = "./chats.py?friend_id={friend_id}&id={id}";
                  </script>""")

    elif file:
        pic = form["pic"]
        if pic.filename:
            proof = os.path.basename(pic.filename)
            file_extension = proof.split('.')[-1].lower()

            if file_extension in ["jpg", "jpeg", "png", "gif", "bmp", "webp"]:
                file_type = "image"
            elif file_extension in ["pdf"]:
                file_type = "pdf"
            elif file_extension in ["mp4", "avi", "mov", "wmv", "mkv"]:
                file_type = "video"
            elif file_extension in ["mp3", "wav", "aac", "ogg"]:
                file_type = "audio"
            else:
                file_type = "file"

            open("../assets/" + proof, "wb").write(pic.file.read())
            query = """INSERT INTO `messages` (`sender_id`, `receiver_id`, `message`, `sent_at`, `type`) 
                       VALUES (%s, %s, %s, CURRENT_TIMESTAMP, %s)"""
            cur.execute(query, (id, friend_id, proof, file_type))
            con.commit()
            print(f"""<script>alert("File Sent: {proof}");
                    window.location.href = "./chats.py?friend_id={friend_id}&id={id}";</script>""")

    elif msg != '':
        query = """INSERT INTO `messages` (`sender_id`, `receiver_id`, `message`, `sent_at`, `type`) 
                   VALUES (%s, %s, %s, CURRENT_TIMESTAMP, 'text')"""
        cur.execute(query, (id, friend_id, msg))
        con.commit()
        print(f"""<script>alert("msg sent");
             window.location.href = "./chats.py?friend_id={friend_id}&id={id}";</script>""")