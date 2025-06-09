#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="chatapp")
cur = con.cursor()

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CrypTalk - Index</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Poppins", sans-serif;
            font-weight: 300;
        }
        body {
            background-color: #b4ffdf;
            padding-top: 80px; /* Add space for the fixed navbar */
        }
        .navbar {
            background-color: #b4ffdf;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            z-index: 10;
        }
        .navbar-brand {
            font-family: "Playwrite CU", cursive;
            font-size: 1.7rem;
            font-weight: 900;
            color: black;
            animation: color-change 20s infinite;
        }
        .nav-item {
            margin-left: 160px;
            font-size: 17px;
        }
        .nav-item.nav-margin {
            margin-left: 10px;
        }
        .nav-item a {
            font-weight: 500;
            color: black;
            transition: all 0.6s;
        }
        .nav-item a:hover {
            color: #297373;
            transform: translateY(-5px);
            scale: 1.02;
            transition: all 0.6s;
        }
        .carousel-inner img {
            height: 500px;
            object-fit: cover;
        }
        .carousel{
        margin-top:50px;
        }

.container {
            width: 90%;
            max-width: 1200px;
           transition: all ease 0.6s;

        }
        .row {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            transition: all ease 0.6s;

        }
        .pic-30 {
            width: 30%;
            background-color: #ddd;
            padding: 10px;
            overflow: hidden;
            text-align: center;
            transition: all ease 0.6s;
        }
        .pic-30:hover img {
            transform: scale(1.1);
            transition: all ease 0.6s;

            }

        .para-50 {
            width: 50%;
            padding: 10px;
        }
        .gap-20 {
            width: 20%;
        }
        
         html,body{height:100%}
.bg_heart{position:relative;top:0;left:0;width:100%;height:100%;overflow:hidden}

.heart{position:absolute;top:-50%;-webkit-transform:rotate(-45deg);-moz-transform:rotate(-45deg);-m-transform:rotate(-45deg);transform:rotate(-45deg)}
.heart:before{position:absolute;top:-50%;left:0;display:block;content:"";width:100%;height:100%;background:inherit;border-radius:100%;}
.heart:after{position:absolute;top:0;right:-50%;display:block;content:"";width:100%;height:100%;background:inherit;border-radius:100%;}

@-webkit-keyframes love {
  0%{top:110%}
}
@-moz-keyframes love {
  0%{top:110%}
}
@-ms-keyframes love {
  0%{top:110%}
}
@keyframes love {
  0%{top:110%}
}
    </style>
</head>
<body>

<nav class="navbar navbar-expand-md navbar-light fixed-top">
    <div class="container">
        <a href="./index.py" class="navbar-brand">CrypTalk;)</a>
        <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ">
                <li class="nav-item"></li>
                <li class="nav-item"></li>
                <li class="nav-item dropdown" style="margin-left:650px ;">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        LogIn
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                        <li><a class="dropdown-item" href="./forms/userlogin.py">User</a></li>
                        <li><a class="dropdown-item" href="./forms/AdminLogin.py">Admin</a></li>
                    </ul>
                </li>
                <span class="hi mt-2 fw-bold">|</span>
                <li class="nav-item dropdown" style="margin-left: -1px;">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Register
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                        <li><a class="dropdown-item" href="./forms/userreg.py">User</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>

<div id="carouselExample" class="carousel slide">
  <div class="carousel-inner">
    <!-- First Slide: General WebChat Applications -->
<div class="carousel-item active">
    <img src="./assets/chat index1.jpg" class="d-block w-100" alt="General WebChat" style="cursor:pointer;">
    <div class="carousel-caption d-flex flex-column align-items-start" style="left: 10%; bottom: 20%;">
        <h2 style="font-weight:500; color:#D9FFF5 !important;" class="display-5 text-light">Seamless Web Chat Experience</h2>
        <p style="font-weight:300;" class="text-light">Connect, chat, and share instantly with our modern web chat platform.</p>
        <a href="./userLogin.py" class="btn btn-primary">Get Started</a>
    </div>
</div>

<!-- Second Slide: User Using Web Chat App -->
<div class="carousel-item">
    <img src="./assets/chat inedx2.jpg" class="d-block w-100" alt="User Chatting" style="cursor:pointer;">
    <div class="carousel-caption d-flex flex-column align-items-start" style="left: 10%; bottom: 20%;">
        <h2 style="font-weight:500; color:#D9FFF5 !important;" class="display-5 text-light">Chat Anytime, Anywhere</h2>
        <p style="font-weight:300;" class="text-light">Enjoy real-time messaging with friends and colleagues on any device.</p>
        <a href="./userLogin.py" class="btn btn-primary">Start Chatting</a>
    </div>
</div>

<!-- Third Slide: Group Chat -->
<div class="carousel-item">
    <img src="./assets/chat index.jpg" class="d-block w-100" alt="Group Chat" style="cursor:pointer;">
    <div class="carousel-caption d-flex flex-column align-items-start" style="left: 10%; bottom: 20%;">
        <h2 style="font-weight:500; color:#D9FFF5 !important;" class="display-5 text-light">Stay Connected with Groups</h2>
        <p style="font-weight:300;" class="text-light">Create and manage group chats effortlessly for work, friends, or family.</p>
        <a href="./userLogin.py" class="btn btn-primary">Join a Group</a>
    </div>
</div>

  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>


<div>
    <h1 class="mt-5 mx-5"> What We Provide:</h1>
    <div class="container mt-5">
        
        <!-- First Section: General WebChat Features -->
        <div class="row mt-5">
            <div class="pic-30">
                <img src="./assets/1.png" alt="Image" style="width: 100%; height: auto; cursor:pointer;">
            </div>

            <div class="gap-20"></div>
            <div class="para-50">
                <h1>Welcome to WebChat!</h1> 
                <h3>Seamless and Secure Messaging</h3>
                <p id="features" class="mt-3">
                    WebChat offers a fast, secure, and user-friendly messaging experience. Whether you're connecting with friends, family, or colleagues, our platform ensures smooth communication with real-time updates, multimedia sharing, and privacy-focused encryption.
                </p>
            </div>
        </div>

        <!-- Second Section: Individual User Chat -->
        <div class="row mt-5">
            <div class="para-50">
                <h1>One-on-One Conversations</h1> 
                <h5 class="mt-2">Stay connected with direct messaging.</h5>
                <p class="mt-3">
                    Enjoy private, uninterrupted chats with your contacts. Our platform allows you to send text messages, images, videos, and even voice recordings, ensuring a seamless conversation experience.
                </p>
            </div>
            <div class="gap-20"></div>
            <div class="pic-30">
                <img src="./assets/2.png" alt="Image" style="width: 100%; height: auto; cursor:pointer;">
            </div>
        </div>

        <!-- Third Section: Group Chat -->
        <div class="row mt-5">
            <div class="pic-30">
                <img src="./assets/3.png" alt="Image" style="width: 100%; height: auto; cursor:pointer;">
            </div>

            <div class="gap-20"></div>
            <div class="para-50">
                <h1>Group Chats & Communities</h1> 
                <h5 class="mt-2">Chat with multiple people in a single space.</h5>
                <p class="mt-3">
                    Create and join group chats to stay in touch with your teams, family, or social circles. Share messages, files, and updates effortlessly, making communication easier than ever.
                </p>
            </div>
        </div>

        <!-- Fourth Section: Secure & Feature-Packed -->
        <div class="row mt-5">
            <div class="para-50">
                <h1 id="security">Privacy & Advanced Features</h1> 
                <h5 class="mt-2">Your security is our priority.</h5>
                <p class="mt-3">
                    With end-to-end encryption, disappearing messages, and scheduled messages, WebChat ensures your privacy while giving you full control over your conversations. Stay secure while enjoying a rich chat experience.
                </p>
            </div>
            <div class="gap-20"></div>
            <div class="pic-30">
                <img src="./assets/4.png" alt="Image" style="width: 100%; height: auto; cursor:pointer;">
            </div>
        </div>

    </div>
</div>

<p class="d-flex justify-content-center">&copy; 2025 CrypTalk</p> 


</body>
</html>
""")
