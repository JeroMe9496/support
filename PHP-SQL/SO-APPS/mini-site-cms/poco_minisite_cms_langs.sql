SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


DROP TABLE IF EXISTS `pages`;
CREATE TABLE `pages` (
  `id` smallint(5) UNSIGNED NOT NULL,
  `is_home` tinyint(1) UNSIGNED DEFAULT '0',
  `is_visible` tinyint(1) UNSIGNED DEFAULT '0',
  `position` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

INSERT INTO `pages` (`id`, `is_home`, `is_visible`, `position`, `last_update`, `created_on`) VALUES
(1, 1, 1, 10, '2019-11-28 08:47:26', '2019-05-25 14:45:17'),
(2, 0, 1, 2, '2019-11-28 08:47:26', '2019-05-25 14:59:00'),
(3, 0, 1, 3, '2019-11-26 10:13:46', '2019-05-25 15:02:22'),
(4, 0, 1, 4, '2019-11-26 10:13:42', '2019-06-08 21:06:23');

DROP TABLE IF EXISTS `pages_langs`;
CREATE TABLE `pages_langs` (
  `id` smallint(5) UNSIGNED NOT NULL,
  `pageid` smallint(5) UNSIGNED NOT NULL,
  `lang` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
  `menu` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` text COLLATE utf8mb4_unicode_ci
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `pages_langs` (`id`, `pageid`, `lang`, `menu`, `title`, `slug`, `content`) VALUES
(1, 1, 'en', 'ABOUT', 'Where hardest stuff is possible !', 'where-hardest-stuff-is-possible', '<div class=\"cols two-cols\">\r\n<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum!</p>\r\n<p>Sed ut dignissim ex, viverra sollicitudin nunc. Vivamus magna elit, sagittis eget condimentum ac, ullamcorper at odio. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi pretium non odio a pretium. Vivamus in dictum arcu. Integer vel ligula sed orci mollis semper. Cras lobortis lacus laoreet malesuada aliquam. Suspendisse et aliquet eros, nec sodales mi. Cras et sapien euismod, congue dolor vitae, posuere enim. Pellentesque at augue quis est convallis pharetra sed vitae purus. Praesent sed sapien eu ex aliquam tempus nec vel lectus. Donec aliquet enim justo, nec tincidunt libero elementum sed. Nulla vehicula neque et justo pellentesque, non blandit nisl lacinia. Nulla consequat, ex a sagittis mattis, urna eros gravida libero, sed ultrices dolor orci quis ipsum.</p>\r\n<p>BOB!!!</p>\r\n</div>'),
(2, 2, 'en', 'WORK', 'A selection of our latest projects', 'a-selection-of-our-latest-projects', '<section class=\"works flex\">\r\n<article>WORK 1</article>\r\n<article>WORK 2</article>\r\n<article>WORK 3</article>\r\n<article>WORK 4</article>\r\n<article>WORK 5</article>\r\n<article>WORK 6</article>\r\n</section>'),
(3, 3, 'en', 'CONTACT', 'Say hello', 'say-hello', '<h2 class=\"align-center MB30\">Contact info</h2>\r\n<p class=\"align-center\">Heavy Metal Company</p>\r\n<p class=\"align-center\">---</p>\r\n<h2 class=\"align-center\">Say Hello with form</h2>\r\n<p class=\"align-center\">Please fill the form bellow to say hello</p>\r\n<div><input class=\"uk-input\" name=\"name\" type=\"text\" value=\"\" placeholder=\"Name\"></div>\r\n<div><input class=\"uk-input\" name=\"email\" type=\"email\" value=\"\" placeholder=\"email\"></div>\r\n<div><input class=\"uk-input\" name=\"subject\" type=\"text\" value=\"\" placeholder=\"subject\"></div>\r\n<div><textarea class=\"uk-textarea\" name=\"message\" rows=\"8\" placeholder=\"message\"></textarea></div>'),
(4, 4, 'en', 'BLOG', 'The Dark Side of the Moon', 'the-dark-side-of-the-moon', '<h2>Pink Floyd</h2>\r\n<p>The Dark Side of the Moon content...</p>');

DROP TABLE IF EXISTS `settings`;
CREATE TABLE `settings` (
  `id` smallint(5) UNSIGNED NOT NULL,
  `settings_key` varchar(50) NOT NULL,
  `settings_value` text,
  `position` tinyint(3) UNSIGNED DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

INSERT INTO `settings` (`id`, `settings_key`, `settings_value`, `position`) VALUES
(1, 'global_title', 'The Heavy Metal Company.', 1),
(2, 'description', 'How to use PHP/SQL to create a dynamic website', 2),
(3, 'keywords', 'php,dynamic site,cool,raoul', 3),
(7, 'author', 'Sorin Paun', 4);

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` tinyint(3) UNSIGNED NOT NULL,
  `fullname` varchar(50) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `pass` varchar(60) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

INSERT INTO `users` (`id`, `fullname`, `email`, `pass`) VALUES
(1, 'Sorin Paun', 'sorin.paun@powercoders.org', '$2y$10$ZEDYjYsgaM5wuaGbgQZKR.4z5aLp7X0zVbgGhJhxEKtG3MyKZrbti');


ALTER TABLE `pages`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `pages_langs`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `pages`
  MODIFY `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

ALTER TABLE `pages_langs`
  MODIFY `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

ALTER TABLE `settings`
  MODIFY `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

ALTER TABLE `users`
  MODIFY `id` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
