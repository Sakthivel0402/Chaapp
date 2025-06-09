#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="chatapp")
cur = con.cursor()
form = cgi.FieldStorage()

sender_id = form.getvalue("sender_id")  # Admin or any user
group_id = form.getvalue("group_id")  # Selected Group ID

# Fetch all groups instead of users
cur.execute("SELECT DISTINCT group_id, group_name FROM chat_groups")
groups = cur.fetchall()

cur.execute("SELECT id, firstname FROM userreg WHERE block_status='' AND otp_status='verified'")
users = cur.fetchall()

# Fetch messages for the selected group
messages = []
if sender_id and group_id:
    query = f"""
    SELECT sender_id, message, sent_at 
    FROM group_messages 
    WHERE group_id = '{group_id}'
    ORDER BY sent_at ASC
    """
    cur.execute(query)
    messages = cur.fetchall()

con.close()

print("""

    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>admin Dashboard</title>
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
        .container {
    margin-left: 20%; /* Ensures content isn't hidden under sidebar */
    padding: 20px;
    transition: margin-left 0.3s ease-in-out;
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



      .chat-container {
    display: flex;
    justify-content: start; /* Pushes elements apart */
    align-items: flex-start;
    gap: 20px; /* Adds spacing between form and chat box */
    width: 100%;
    padding: 20px;
}

.chat-box {
    flex: 1; /* Makes form take some space */
    max-width: 30%; /* Restricts width of form */
}

.chat-messages {
    flex: 3; /* Allows chat to take more space */
    max-width: 80% !important;
    
    border-radius: 8px;

    
    height: 20px;
}

/* Message styling */
.message-sent {
    background-color: #007bff;
    color: white;
    padding: 10px;
    border-radius: 8px;
    margin: 5px 0;
    align-self: flex-end;
    text-align: right;
    max-width: 75%;
    height:auto;
}

.message-received {
    background-color: #e4e6eb;
    color: black;
    padding: 10px;
    border-radius: 8px;
    margin: 5px 0;
    align-self: flex-start;
    max-width: 75%;
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
          @media (max-width: 768px) {
        .chat-container {
            width: 100%;
        } 
    </style>
</head>

<body>

    <!-- Sidebar -->
    <div class="sidebar" id="sidebar">
        <h4>Admin Dashboard</h4>

        <a href="./adminDashboard.py" class="fw-bold  ">Home</a>
       <a href="adminUsers.py" class="fw-bold"> Manage Users</a>
        <a href="adminGroups.py" class="fw-bold"> Manage Groups</a>
        <a href="adminUserchats.py" class="fw-bold ">  User Chats </a>
        <a href="adminGroupchats.py" class="fw-bold active1">  Group Chats </a>



        <div class="logout">
          <a href="../forms/adminLogin.py">Logout</a>
        </div>
    </div>

   <button class="menu-btn" onclick="toggleSidebar()"><i class="fa-solid fa-bars"></i></button>

<div class="container">
    <h2 class="text-center">Admin Group Chat Logs</h2>
    <div class="chat-container">
        <div class="chat-box">
            <h5>Select sender and group to view chat:</h5>
            <form method="POST">
                <div class="mb-3">
                    <label for="senderSelect" class="form-label">Sender:</label>
                    <select name="sender_id" id="senderSelect" class="form-control" required>
                        <option value="">Select Sender</option>
""")

for user in users:
    selected = "selected" if str(user[0]) == str(sender_id) else ""
    print(f'<option value="{user[0]}" {selected}>{user[1]}</option>')
print("""
                    </select>
                </div>

                <div class="mb-3">
                    <label for="groupSelect" class="form-label">Group:</label>
                    <select name="group_id" id="groupSelect" class="form-control" required>
                        <option value="">Select Group</option>
""")

# Fix duplicate group names
group_names = set()  # Store unique group names
for group in groups:
    if group[1] not in group_names:
        group_names.add(group[1])
        selected = "selected" if str(group[0]) == str(group_id) else ""
        print(f'<option value="{group[0]}" {selected}>{group[1]}</option>')

print("""
                    </select>
                </div>

                <button type="submit" class="btn btn-primary">View Chat</button>
            </form>
        </div>

        <!-- Chat Messages Container -->
        <div class="chat-messages">
            <h4>Conversation:</h4>
            <div class="chat-body">
""")

if not messages:
    print("<p class='text-muted'>Select a sender and group to view messages.</p>")
else:
    sender_index = 1  # Initialize sender numbering
    sender_map = {}  # Store sender names dynamically

    for message in messages:
        if message[0] not in sender_map:
            sender_map[message[0]] = f"Sender{sender_index}"
            sender_index += 1

        sender_class = "message-sent" if str(message[0]) == sender_id else "message-received"
        sender_name = sender_map[message[0]]

        print(f"""
        <div class='{sender_class} chat-message'>
            <p><strong>{sender_name}:</strong> {message[1]}</p>
            <small class="text-muted">{message[2]}</small>
        </div>
        """)

print("""
            </div>
        </div>
    </div>
</div>
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
}});       """)

print("""

  function updateReceiverOptions() {
    let senderSelect = document.getElementById("senderSelect");
    let receiverSelect = document.getElementById("receiverSelect");
    let selectedSender = senderSelect.value;

    for (let i = 0; i < receiverSelect.options.length; i++) {
        let option = receiverSelect.options[i];
        if (option.value === selectedSender) {
            option.style.display = "none";
        } else {
            option.style.display = "block";
        }
    }
}
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

