-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 14, 2025 at 05:42 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chatapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `blocked_groups`
--

CREATE TABLE `blocked_groups` (
  `id` int(20) NOT NULL,
  `group_id` varchar(20) NOT NULL,
  `reason` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blocked_users`
--

CREATE TABLE `blocked_users` (
  `id` int(20) NOT NULL,
  `user_id` int(20) NOT NULL,
  `name` varchar(40) NOT NULL,
  `reason` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blocked_users`
--

INSERT INTO `blocked_users` (`id`, `user_id`, `name`, `reason`) VALUES
(1, 4, '', 'Inappropriate behaviour');

-- --------------------------------------------------------

--
-- Table structure for table `chat_groups`
--

CREATE TABLE `chat_groups` (
  `id` int(20) NOT NULL,
  `group_id` varchar(20) NOT NULL,
  `group_name` varchar(50) NOT NULL,
  `member_name` varchar(50) NOT NULL,
  `profile` varchar(100) NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `block_status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chat_groups`
--

INSERT INTO `chat_groups` (`id`, `group_id`, `group_name`, `member_name`, `profile`, `user_id`, `status`, `created_by`, `block_status`) VALUES
(3, 'GRO003', 'the boyss', 'Sakthivel', '33997169-4k-minimalist-broken-car-wallpaper.jpg', '1', 'accepted', '', ''),
(4, 'GRO003', 'the boyss', 'Ravichandran', '33997169-4k-minimalist-broken-car-wallpaper.jpg', '3', 'accepted', '', ''),
(5, 'GRO003', 'the boyss', 'sudhesh', '33997169-4k-minimalist-broken-car-wallpaper.jpg', '2', 'created', 'sudhesh', '');

-- --------------------------------------------------------

--
-- Table structure for table `friend_requests`
--

CREATE TABLE `friend_requests` (
  `request_id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `status` enum('pending','friends','rejected') DEFAULT 'pending',
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `friend_requests`
--

INSERT INTO `friend_requests` (`request_id`, `sender_id`, `receiver_id`, `status`, `created_at`) VALUES
(1, 2, 1, 'friends', '2025-02-08 15:41:25'),
(2, 3, 1, 'friends', '2025-02-08 15:42:20'),
(3, 2, 3, 'friends', '2025-02-08 15:42:55');

-- --------------------------------------------------------

--
-- Table structure for table `group_messages`
--

CREATE TABLE `group_messages` (
  `msg_id` int(11) NOT NULL,
  `group_id` varchar(10) NOT NULL,
  `sender_id` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL,
  `message` varchar(200) NOT NULL,
  `sent_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `group_messages`
--

INSERT INTO `group_messages` (`msg_id`, `group_id`, `sender_id`, `type`, `message`, `sent_at`) VALUES
(1, 'GRO003', '1', 'image', 'img2.wallspic.com-cumulus-cloud-tranquillity-calm-sky-6000x4284.jpg', '2025-02-12 16:33:25'),
(2, 'GRO003', '1', 'text', 'lkmslkccd', '2025-02-12 16:37:32'),
(3, 'GRO003', '2', 'text', 'jknwdjkcdc', '2025-02-12 16:50:28'),
(4, 'GRO003', '3', 'text', 'hiiii', '2025-02-12 16:58:14'),
(5, 'GRO003', '3', 'text', 'lawadeyy', '2025-02-12 16:58:27'),
(6, 'GRO003', '3', 'image', 'dp8.jpg', '2025-02-12 16:58:42'),
(7, 'GRO003', '3', 'text', '', '2025-02-12 16:58:42'),
(8, 'GRO003', '2', 'text', 'helooo', '2025-02-13 04:29:29'),
(9, 'GRO003', '1', 'text', 'hiiii', '2025-02-13 13:24:00');

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `message_id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `message` text NOT NULL,
  `sent_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `is_read` tinyint(1) DEFAULT 0,
  `type` varchar(20) NOT NULL,
  `schedule_time` datetime DEFAULT NULL,
  `disappear_after` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`message_id`, `sender_id`, `receiver_id`, `message`, `sent_at`, `is_read`, `type`, `schedule_time`, `disappear_after`) VALUES
(1, 2, 1, 'hii daa', '2025-02-11 06:04:40', 0, 'text', NULL, NULL),
(2, 2, 1, 'land3.jpg', '2025-02-11 06:05:02', 0, 'image', NULL, NULL),
(3, 1, 2, 'hello ', '2025-02-11 06:05:19', 0, 'text', NULL, NULL),
(4, 1, 2, 'bubble.png', '2025-02-11 06:05:32', 0, 'image', NULL, NULL),
(5, 2, 1, 'saved the pic', '2025-02-11 06:07:45', 0, 'text', NULL, NULL),
(6, 2, 1, 'jnc', '2025-02-11 06:10:14', 0, 'text', NULL, NULL),
(7, 2, 1, 'heyyyy', '2025-02-11 06:11:07', 0, 'text', NULL, NULL),
(8, 2, 1, 'kjjidwncjcd', '2025-02-11 06:11:18', 0, 'text', NULL, NULL),
(9, 2, 1, '5e8de559ab8182431ce9c71fceda38.png', '2025-02-11 06:11:30', 0, 'image', NULL, NULL),
(10, 2, 1, 'nwdcjndcsd', '2025-02-11 06:15:02', 0, 'text', NULL, NULL),
(11, 2, 1, 'TOUR.jpg', '2025-02-11 06:15:15', 0, 'image', NULL, NULL),
(12, 2, 1, '176380-amphibian-frogs-red_eyed_tree_frog-true_frog-tree_frogs-3840x2160.jpg', '2025-02-11 06:49:05', 0, 'image', NULL, NULL),
(13, 2, 1, 'pexels-tom-fisk-2246950.jpg', '2025-02-11 06:49:21', 0, 'image', NULL, NULL),
(14, 1, 2, '177920-bmw-sports_car-cars-bmw_m3-bayerische_motoren_werke_ag-3840x2160.jpg', '2025-02-11 08:54:34', 0, 'image', NULL, NULL),
(15, 2, 1, 'pexels-kateryna-babaieva-1423213-3715583.jpg', '2025-02-11 08:56:07', 0, 'image', NULL, NULL),
(16, 1, 2, 'dp8.jpg', '2025-02-11 08:57:02', 0, 'image', NULL, NULL),
(17, 2, 1, '179637-freestyle_motocross-motorcycle-ktm-dakar_rally-off_road_racing-3840x2160.jpg', '2025-02-11 09:33:41', 0, 'image', NULL, NULL),
(18, 2, 1, '177796-lake_louise-bear_street-water-cloud-plant-3840x2160.jpg', '2025-02-11 09:57:44', 0, 'image', NULL, NULL),
(19, 2, 1, 'kwxwkcewc', '2025-02-11 09:58:37', 0, 'text', NULL, NULL),
(20, 2, 1, 'lkdncdcce', '2025-02-11 10:06:06', 0, 'text', NULL, NULL),
(21, 2, 1, 'hellowdwe', '2025-02-11 10:14:49', 0, 'text', NULL, NULL),
(22, 2, 1, 'heyy', '2025-02-11 11:27:30', 0, 'text', '2025-02-11 20:00:00', NULL),
(23, 2, 1, 'h', '2025-02-11 11:28:13', 0, 'text', NULL, 30),
(24, 2, 1, 'hiiiiii', '2025-02-11 12:05:35', 0, 'text', '2025-02-11 17:36:00', NULL),
(25, 2, 1, 'hjwencjkwdncjdkncd', '2025-02-11 12:08:40', 0, 'text', NULL, 30),
(26, 1, 2, 'kl;wdmcw', '2025-02-11 12:21:13', 0, 'text', NULL, NULL),
(27, 1, 2, '', '2025-02-11 12:21:26', 0, 'text', NULL, NULL),
(28, 1, 2, '177796-lake_louise-bear_street-water-cloud-plant-3840x2160.jpg', '2025-02-11 12:23:03', 0, 'image', NULL, NULL),
(30, 2, 1, '177796-lake_louise-bear_street-water-cloud-plant-3840x2160.jpg', '2025-02-11 12:26:46', 0, 'image', NULL, 5),
(31, 2, 1, '176830-flower-yellow-plant-water-people_in_nature-3840x2160.jpg', '2025-02-11 12:27:40', 0, 'image', '2025-02-11 17:59:00', NULL),
(32, 2, 1, '177796-lake_louise-bear_street-water-cloud-plant-3840x2160.jpg', '2025-02-11 12:30:50', 0, 'image', NULL, NULL),
(33, 2, 1, '177796-lake_louise-bear_street-water-cloud-plant-3840x2160.jpg', '2025-02-11 12:33:49', 0, 'image', NULL, 10),
(34, 2, 3, '176039-narrow_road-road-cloud-plant-natural_landscape-3840x2160.jpg', '2025-02-11 12:39:32', 0, 'image', NULL, NULL),
(35, 2, 1, 'wallpaperflare.com_wallpaper (5).jpg', '2025-02-12 04:11:10', 0, 'image', NULL, 60),
(36, 1, 2, 'img3.wallspic.com-atmosphere-friendship-daytime-cloud-blue-5173x3325.jpg', '2025-02-13 12:05:49', 0, 'image', NULL, NULL),
(37, 1, 3, 'dp5.jpg', '2025-02-13 12:11:34', 0, 'image', NULL, NULL),
(38, 1, 2, 'dp2.jpg', '2025-02-13 13:23:24', 0, 'image', NULL, NULL),
(39, 1, 3, 'dp14.jpg', '2025-02-13 13:23:40', 0, 'image', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `userreg`
--

CREATE TABLE `userreg` (
  `id` int(20) NOT NULL,
  `firstname` varchar(40) NOT NULL,
  `lastname` varchar(40) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `address1` varchar(200) NOT NULL,
  `address2` varchar(200) NOT NULL,
  `zipcode` varchar(10) NOT NULL,
  `district` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `aadharnumber` varchar(20) NOT NULL,
  `profile` varchar(50) NOT NULL,
  `otp_status` varchar(20) NOT NULL,
  `block_status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userreg`
--

INSERT INTO `userreg` (`id`, `firstname`, `lastname`, `dob`, `gender`, `phone`, `mail`, `address1`, `address2`, `zipcode`, `district`, `state`, `country`, `aadharnumber`, `profile`, `otp_status`, `block_status`) VALUES
(1, 'Sakthivel', 'murugan', '2002-02-04', 'male', '+919894183896', 'sakthivelsubash0402@gmail.com', '57, abc street', 'xyz nagar', '638004', 'Erode', 'Tamil Nadu', 'India', '381240651150', 'bubble.png', 'verified', ''),
(2, 'sudhesh', 'k', '2002-02-04', 'male', '8838379412', 'sudhesh418@gmail.com', '119b, alangariyur', 'singampettai', '638311', 'Erode', 'Tamil Nadu', 'India', '521478632541', 'profile4.png', 'verified', ''),
(3, 'Ravichandran', 'k', '2002-04-15', 'male', '6379486280', 'ravichandraak@gmail.com', '123, kavery street', 'nattham', '631202', 'Dindigul', 'Tamil Nadu', 'India', '351245967215', 'profile2.png', 'verified', ''),
(4, 'Badrinath', 'CV', '2002-08-12', 'male', '9360148336', 'techvolt.badri@gmail.com', '123, kavery street', 'dindigul', '621011', 'Dindigul', 'Tamil Nadu', 'India', '3343553732', 'profile2.png', 'verified', 'blocked'),
(18, 'Badrinath', 'CV', '', 'None', '9894183896', 'te.badri@gmail.com', '123, kavery street', 'dindigul', '621011', '', 'Tamil Nadu', 'India', '3343553732', '', 'pending', ''),
(19, 'ggdfgd ', 'gfghfhgfh', '2222-11-11', 'male', '9360148336', 'hgtdtfdth@gmail.com', 'yfyjfj', 'ghgddd', '537537', 'Madurai', 'Maharashtra', 'trfghf', '2898765487676', '', 'pending', ''),
(20, 'ggdfgd ', 'gfghfhgfh', '2222-11-11', 'male', '9360148336', 'hdtfdth@gmail.com', 'yfyjfj', 'ghgddd', '537537', 'Madurai', 'Maharashtra', 'trfghf', '2898765487676', '', 'pending', ''),
(21, 'ggdfgd ', 'gfghfhgfh', '2222-11-11', 'male', '+919360148336', 'hdfdth@gmail.com', 'yfyjfj', 'ghgddd', '537537', 'Madurai', 'Maharashtra', 'trfghf', '2898765487676', '', 'pending', ''),
(22, 'pjmwciwcd', 'kmqwdkcdcmedc', '2002-01-02', 'male', '+919894183896', 'kwknnkc@gmail.com', 'oiwncwcc', 'kwmekcxlwcmkle', '458121', 'Kanyakumari', 'Tamil Nadu', 'india', '89415894518', '', 'pending', '');

-- --------------------------------------------------------

--
-- Table structure for table `user_otp`
--

CREATE TABLE `user_otp` (
  `otp_id` int(20) NOT NULL,
  `user_id` int(10) NOT NULL,
  `user_phone` varchar(15) NOT NULL,
  `otp` varchar(10) NOT NULL,
  `status` varchar(20) NOT NULL,
  `time` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_otp`
--

INSERT INTO `user_otp` (`otp_id`, `user_id`, `user_phone`, `otp`, `status`, `time`) VALUES
(2, 0, '9894183896', '686658', 'verified', '2025-02-09 17:27:48.081874'),
(3, 0, '9360148336', '321859', 'pending', '2025-02-11 18:25:58.156938'),
(4, 0, '9360148336', '566055', 'pending', '2025-02-11 18:30:19.610307'),
(5, 0, '+919360148336', '567278', 'pending', '2025-02-11 18:30:54.357028'),
(6, 0, '+919894183896', '873441', 'verified', '2025-02-12 09:54:02.466392');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blocked_groups`
--
ALTER TABLE `blocked_groups`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `blocked_users`
--
ALTER TABLE `blocked_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chat_groups`
--
ALTER TABLE `chat_groups`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `friend_requests`
--
ALTER TABLE `friend_requests`
  ADD PRIMARY KEY (`request_id`),
  ADD KEY `sender_id` (`sender_id`),
  ADD KEY `receiver_id` (`receiver_id`);

--
-- Indexes for table `group_messages`
--
ALTER TABLE `group_messages`
  ADD PRIMARY KEY (`msg_id`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`message_id`),
  ADD KEY `sender_id` (`sender_id`),
  ADD KEY `receiver_id` (`receiver_id`);

--
-- Indexes for table `userreg`
--
ALTER TABLE `userreg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_otp`
--
ALTER TABLE `user_otp`
  ADD PRIMARY KEY (`otp_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blocked_groups`
--
ALTER TABLE `blocked_groups`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `blocked_users`
--
ALTER TABLE `blocked_users`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `chat_groups`
--
ALTER TABLE `chat_groups`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `friend_requests`
--
ALTER TABLE `friend_requests`
  MODIFY `request_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `group_messages`
--
ALTER TABLE `group_messages`
  MODIFY `msg_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `message_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `userreg`
--
ALTER TABLE `userreg`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `user_otp`
--
ALTER TABLE `user_otp`
  MODIFY `otp_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `friend_requests`
--
ALTER TABLE `friend_requests`
  ADD CONSTRAINT `friend_requests_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `userreg` (`id`),
  ADD CONSTRAINT `friend_requests_ibfk_2` FOREIGN KEY (`receiver_id`) REFERENCES `userreg` (`id`);

--
-- Constraints for table `messages`
--
ALTER TABLE `messages`
  ADD CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `userreg` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`receiver_id`) REFERENCES `userreg` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
