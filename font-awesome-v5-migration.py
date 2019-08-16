#!/usr/bin/env python3
"""
This file uses 'grep', so it's only suitable for Linux, Mac, Git Bash, etc.
Running this multiple times may create bad code, so use version control.
TODO: This file needs to be cleaned up.
"""

from datetime import datetime
import subprocess
import sys

# With spaces between dirs, an error occurs: 'FileNotFoundError: [Errno 2] No such file or directory: 'grep: .idea,: No such file or directory''
GREP_EXCLUDE = '--exclude=\\*.{dll,png} --exclude-dir={.git,.idea,.nuget,bin,node_modules}'

findreplace = [
    ('fa fa-500px', 'fab fa-500px'),
    ('fa fa-address-book-o', 'fas fa-address-book'),
    ('fa fa-address-card-o', 'fas fa-address-card'),
    ('fa fa-adn', 'fab fa-adn'),
    ('fa fa-amazon', 'fab fa-amazon'),
    ('fa fa-android', 'fab fa-android'),
    ('fa fa-angellist', 'fab fa-angellist'),
    ('fa fa-apple', 'fab fa-apple'),
    ('fa fa-area-chart', 'fas fa-chart-area'),
    ('fa fa-arrow-circle-o-down', 'fas fa-arrow-alt-circle-down'),
    ('fa fa-arrow-circle-o-left', 'fas fa-arrow-alt-circle-left'),
    ('fa fa-arrow-circle-o-right', 'fas fa-arrow-alt-circle-right'),
    ('fa fa-arrow-circle-o-up', 'fas fa-arrow-alt-circle-up'),
    ('fa fa-arrows-alt', 'fas fa-expand-arrows-alt'),
    ('fa fa-arrows-h', 'fas fa-arrows-alt-h'),
    ('fa fa-arrows-v', 'fas fa-arrows-alt-v'),
    ('fa fa-arrows', 'fas fa-arrows-alt'),
    ('fa fa-asl-interpreting', 'fas fa-american-sign-language-interpreting'),
    ('fa fa-automobile', 'fas fa-car'),
    ('fa fa-bandcamp', 'fab fa-bandcamp'),
    ('fa fa-bank', 'fas fa-university'),
    ('fa fa-bar-chart-o', 'fas fa-chart-bar'),
    ('fa fa-bar-chart', 'fas fa-chart-bar'),
    ('fa fa-bathtub', 'fas fa-bath'),
    ('fa fa-battery-0', 'fas fa-battery-empty'),
    ('fa fa-battery-1', 'fas fa-battery-quarter'),
    ('fa fa-battery-2', 'fas fa-battery-half'),
    ('fa fa-battery-3', 'fas fa-battery-three-quarters'),
    ('fa fa-battery-4', 'fas fa-battery-full'),
    ('fa fa-battery', 'fas fa-battery-full'),
    ('fa fa-behance', 'fab fa-behance'),
    ('fa fa-behance-square', 'fab fa-behance-square'),
    ('fa fa-bell-o', 'fas fa-bell'),
    ('fa fa-bell-slash-o', 'fas fa-bell-slash'),
    ('fa fa-bitbucket-square', 'fab fa-bitbucket'),
    ('fa fa-bitbucket', 'fab fa-bitbucket'),
    ('fa fa-bitcoin', 'fab fa-btc'),
    ('fa fa-black-tie', 'fab fa-black-tie'),
    ('fa fa-bluetooth-b', 'fab fa-bluetooth-b'),
    ('fa fa-bluetooth', 'fab fa-bluetooth'),
    ('fa fa-bookmark-o', 'fas fa-bookmark'),
    ('fa fa-btc', 'fab fa-btc'),
    ('fa fa-building-o', 'fas fa-building'),
    ('fa fa-buysellads', 'fab fa-buysellads'),
    ('fa fa-cab', 'fas fa-taxi'),
    ('fa fa-calendar-check-o', 'fas fa-calendar-check'),
    ('fa fa-calendar-minus-o', 'fas fa-calendar-minus'),
    ('fa fa-calendar-o', 'fas fa-calendar'),
    ('fa fa-calendar-plus-o', 'fas fa-calendar-plus'),
    ('fa fa-calendar-times-o', 'fas fa-calendar-times'),
    ('fa fa-calendar', 'fas fa-calendar-alt'),
    ('fa fa-caret-square-o-down', 'fas fa-caret-square-down'),
    ('fa fa-caret-square-o-left', 'fas fa-caret-square-left'),
    ('fa fa-caret-square-o-right', 'fas fa-caret-square-right'),
    ('fa fa-caret-square-o-up', 'fas fa-caret-square-up'),
    ('fa fa-cc-amex', 'fab fa-cc-amex'),
    ('fa fa-cc-diners-club', 'fab fa-cc-diners-club'),
    ('fa fa-cc-discover', 'fab fa-cc-discover'),
    ('fa fa-cc-jcb', 'fab fa-cc-jcb'),
    ('fa fa-cc-mastercard', 'fab fa-cc-mastercard'),
    ('fa fa-cc-paypal', 'fab fa-cc-paypal'),
    ('fa fa-cc-stripe', 'fab fa-cc-stripe'),
    ('fa fa-cc-visa', 'fab fa-cc-visa'),
    ('fa fa-cc', 'fas fa-closed-captioning'),
    ('fa fa-chain-broken', 'fas fa-unlink'),
    ('fa fa-chain', 'fas fa-link'),
    ('fa fa-check-circle-o', 'fas fa-check-circle'),
    ('fa fa-check-square-o', 'fas fa-check-square'),
    ('fa fa-chrome', 'fab fa-chrome'),
    ('fa fa-circle-o-notch', 'fas fa-circle-notch'),
    ('fa fa-circle-o', 'fas fa-circle'),
    ('fa fa-circle-thin', 'fas fa-circle'),
    ('fa fa-clipboard', 'fas fa-clipboard'),
    ('fa fa-clock-o', 'fas fa-clock'),
    ('fa fa-clone', 'fas fa-clone'),
    ('fa fa-close', 'fas fa-times'),
    ('fa fa-cloud-download', 'fas fa-cloud-download-alt'),
    ('fa fa-cloud-upload', 'fas fa-cloud-upload-alt'),
    ('fa fa-cny', 'fas fa-yen-sign'),
    ('fa fa-code-fork', 'fas fa-code-branch'),
    ('fa fa-codepen', 'fab fa-codepen'),
    ('fa fa-codiepie', 'fab fa-codiepie'),
    ('fa fa-comment-o', 'fas fa-comment'),
    ('fa fa-commenting-o', 'fas fa-comment-dots'),
    ('fa fa-commenting', 'fas fa-comment-dots'),
    ('fa fa-comments-o', 'fas fa-comments'),
    ('fa fa-compass', 'fas fa-compass'),
    ('fa fa-connectdevelop', 'fab fa-connectdevelop'),
    ('fa fa-contao', 'fab fa-contao'),
    ('fa fa-copyright', 'fas fa-copyright'),
    ('fa fa-creative-commons', 'fab fa-creative-commons'),
    ('fa fa-credit-card-alt', 'fas fa-credit-card'),
    ('fa fa-credit-card', 'fas fa-credit-card'),
    ('fa fa-css3', 'fab fa-css3'),
    ('fa fa-cutlery', 'fas fa-utensils'),
    ('fa fa-dashboard', 'fas fa-tachometer-alt'),
    ('fa fa-dashcube', 'fab fa-dashcube'),
    ('fa fa-deafness', 'fas fa-deaf'),
    ('fa fa-dedent', 'fas fa-outdent'),
    ('fa fa-delicious', 'fab fa-delicious'),
    ('fa fa-deviantart', 'fab fa-deviantart'),
    ('fa fa-diamond', 'fas fa-gem'),
    ('fa fa-digg', 'fab fa-digg'),
    ('fa fa-dollar', 'fas fa-dollar-sign'),
    ('fa fa-dot-circle-o', 'fas fa-dot-circle'),
    ('fa fa-dribbble', 'fab fa-dribbble'),
    ('fa fa-drivers-license-o', 'fas fa-id-card'),
    ('fa fa-drivers-license', 'fas fa-id-card'),
    ('fa fa-dropbox', 'fab fa-dropbox'),
    ('fa fa-drupal', 'fab fa-drupal'),
    ('fa fa-edge', 'fab fa-edge'),
    ('fa fa-eercast', 'fab fa-sellcast'),
    ('fa fa-empire', 'fab fa-empire'),
    ('fa fa-envelope-open-o', 'fas fa-envelope-open'),
    ('fa fa-envelope-o', 'fas fa-envelope'),
    ('fa fa-envira', 'fab fa-envira'),
    ('fa fa-etsy', 'fab fa-etsy'),
    ('fa fa-euro', 'fas fa-euro-sign'),
    ('fa fa-eur', 'fas fa-euro-sign'),
    ('fa fa-exchange', 'fas fa-exchange-alt'),
    ('fa fa-expeditedssl', 'fab fa-expeditedssl'),
    ('fa fa-external-link-square', 'fas fa-external-link-square-alt'),
    ('fa fa-external-link', 'fas fa-external-link-alt'),
    ('fa fa-eye-slash', 'fas fa-eye-slash'),
    ('fa fa-eyedropper', 'fas fa-eye-dropper'),
    ('fa fa-eye', 'fas fa-eye'),
    ('fa fa-facebook-f', 'fab fa-facebook-f'),
    ('fa fa-facebook-official', 'fab fa-facebook'),
    ('fa fa-facebook-square', 'fab fa-facebook-square'),
    ('fa fa-facebook', 'fab fa-facebook-f'),
    ('fa fa-feed', 'fas fa-rss'),
    ('fa fa-file-archive-o', 'fas fa-file-archive'),
    ('fa fa-file-audio-o', 'fas fa-file-audio'),
    ('fa fa-file-code-o', 'fas fa-file-code'),
    ('fa fa-file-excel-o', 'fas fa-file-excel'),
    ('fa fa-file-image-o', 'fas fa-file-image'),
    ('fa fa-file-movie-o', 'fas fa-file-video'),
    ('fa fa-file-o', 'fas fa-file'),
    ('fa fa-file-pdf-o', 'fas fa-file-pdf'),
    ('fa fa-file-photo-o', 'fas fa-file-image'),
    ('fa fa-file-picture-o', 'fas fa-file-image'),
    ('fa fa-file-powerpoint-o', 'fas fa-file-powerpoint'),
    ('fa fa-file-sound-o', 'fas fa-file-audio'),
    ('fa fa-file-text-o', 'fas fa-file-alt'),
    ('fa fa-file-text', 'fas fa-file-alt'),
    ('fa fa-file-video-o', 'fas fa-file-video'),
    ('fa fa-file-word-o', 'fas fa-file-word'),
    ('fa fa-file-zip-o', 'fas fa-file-archive'),
    ('fa fa-files-o', 'fas fa-copy'),
    ('fa fa-firefox', 'fab fa-firefox'),
    ('fa fa-first-order', 'fab fa-first-order'),
    ('fa fa-flag-o', 'fas fa-flag'),
    ('fa fa-flash', 'fas fa-bolt'),
    ('fa fa-flickr', 'fab fa-flickr'),
    ('fa fa-floppy-o', 'fas fa-save'),
    ('fa fa-folder-o', 'fas fa-folder'),
    ('fa fa-folder-open-o', 'fas fa-folder-open'),
    ('fa fa-font-awesome', 'fab fa-font-awesome'),
    ('fa fa-fonticons', 'fab fa-fonticons'),
    ('fa fa-fort-awesome', 'fab fa-fort-awesome'),
    ('fa fa-forumbee', 'fab fa-forumbee'),
    ('fa fa-foursquare', 'fab fa-foursquare'),
    ('fa fa-free-code-camp', 'fab fa-free-code-camp'),
    ('fa fa-frown-o', 'fas fa-frown'),
    ('fa fa-futbol-o', 'fas fa-futbol'),
    ('fa fa-gbp', 'fas fa-pound-sign'),
    ('fa fa-gears', 'fas fa-cogs'),
    ('fa fa-gear', 'fas fa-cog'),
    ('fa fa-get-pocket', 'fab fa-get-pocket'),
    ('fa fa-ge', 'fab fa-empire'),
    ('fa fa-gg-circle', 'fab fa-gg-circle'),
    ('fa fa-gg', 'fab fa-gg'),
    ('fa fa-git-square', 'fab fa-git-square'),
    ('fa fa-github-alt', 'fab fa-github-alt'),
    ('fa fa-github-square', 'fab fa-github-square'),
    ('fa fa-github', 'fab fa-github'),
    ('fa fa-gitlab', 'fab fa-gitlab'),
    ('fa fa-gittip', 'fab fa-gratipay'),
    ('fa fa-git', 'fab fa-git'),
    ('fa fa-glass', 'fas fa-glass-martini'),
    ('fa fa-glide-g', 'fab fa-glide-g'),
    ('fa fa-glide', 'fab fa-glide'),
    ('fa fa-google-plus-circle', 'fab fa-google-plus'),
    ('fa fa-google-plus-official', 'fab fa-google-plus'),
    ('fa fa-google-plus-square', 'fab fa-google-plus-square'),
    ('fa fa-google-plus', 'fab fa-google-plus-g'),
    ('fa fa-google-wallet', 'fab fa-google-wallet'),
    ('fa fa-google', 'fab fa-google'),
    ('fa fa-gratipay', 'fab fa-gratipay'),
    ('fa fa-grav', 'fab fa-grav'),
    ('fa fa-group', 'fas fa-users'),
    ('fa fa-hacker-news', 'fab fa-hacker-news'),
    ('fa fa-hand-grab-o', 'fas fa-hand-rock'),
    ('fa fa-hand-lizard-o', 'fas fa-hand-lizard'),
    ('fa fa-hand-o-down', 'fas fa-hand-point-down'),
    ('fa fa-hand-o-left', 'fas fa-hand-point-left'),
    ('fa fa-hand-o-right', 'fas fa-hand-point-right'),
    ('fa fa-hand-o-up', 'fas fa-hand-point-up'),
    ('fa fa-hand-paper-o', 'fas fa-hand-paper'),
    ('fa fa-hand-peace-o', 'fas fa-hand-peace'),
    ('fa fa-hand-pointer-o', 'fas fa-hand-pointer'),
    ('fa fa-hand-rock-o', 'fas fa-hand-rock'),
    ('fa fa-hand-scissors-o', 'fas fa-hand-scissors'),
    ('fa fa-hand-spock-o', 'fas fa-hand-spock'),
    ('fa fa-hand-stop-o', 'fas fa-hand-paper'),
    ('fa fa-handshake-o', 'fas fa-handshake'),
    ('fa fa-hard-of-hearing', 'fas fa-deaf'),
    ('fa fa-hdd-o', 'fas fa-hdd'),
    ('fa fa-header', 'fas fa-heading'),
    ('fa fa-heart-o', 'fas fa-heart'),
    ('fa fa-hospital-o', 'fas fa-hospital'),
    ('fa fa-hotel', 'fas fa-bed'),
    ('fa fa-hourglass-1', 'fas fa-hourglass-start'),
    ('fa fa-hourglass-2', 'fas fa-hourglass-half'),
    ('fa fa-hourglass-3', 'fas fa-hourglass-end'),
    ('fa fa-hourglass-o', 'fas fa-hourglass'),
    ('fa fa-houzz', 'fab fa-houzz'),
    ('fa fa-html5', 'fab fa-html5'),
    ('fa fa-id-badge', 'fas fa-id-badge'),
    ('fa fa-id-card-o', 'fas fa-id-card'),
    ('fa fa-ils', 'fas fa-shekel-sign'),
    ('fa fa-image', 'fas fa-image'),
    ('fa fa-imdb', 'fab fa-imdb'),
    ('fa fa-inr', 'fas fa-rupee-sign'),
    ('fa fa-instagram', 'fab fa-instagram'),
    ('fa fa-institution', 'fas fa-university'),
    ('fa fa-internet-explorer', 'fab fa-internet-explorer'),
    ('fa fa-intersex', 'fas fa-transgender'),
    ('fa fa-ioxhost', 'fab fa-ioxhost'),
    ('fa fa-joomla', 'fab fa-joomla'),
    ('fa fa-jpy', 'fas fa-yen-sign'),
    ('fa fa-jsfiddle', 'fab fa-jsfiddle'),
    ('fa fa-keyboard-o', 'fas fa-keyboard'),
    ('fa fa-krw', 'fas fa-won-sign'),
    ('fa fa-lastfm-square', 'fab fa-lastfm-square'),
    ('fa fa-lastfm', 'fab fa-lastfm'),
    ('fa fa-leanpub', 'fab fa-leanpub'),
    ('fa fa-legal', 'fas fa-gavel'),
    ('fa fa-lemon-o', 'fas fa-lemon'),
    ('fa fa-level-down', 'fas fa-level-down-alt'),
    ('fa fa-level-up', 'fas fa-level-up-alt'),
    ('fa fa-life-bouy', 'fas fa-life-ring'),
    ('fa fa-life-buoy', 'fas fa-life-ring'),
    ('fa fa-life-ring', 'fas fa-life-ring'),
    ('fa fa-life-saver', 'fas fa-life-ring'),
    ('fa fa-lightbulb-o', 'fas fa-lightbulb'),
    ('fa fa-line-chart', 'fas fa-chart-line'),
    ('fa fa-linkedin-square', 'fab fa-linkedin'),
    ('fa fa-linkedin', 'fab fa-linkedin-in'),
    ('fa fa-linode', 'fab fa-linode'),
    ('fa fa-linux', 'fab fa-linux'),
    ('fa fa-list-alt', 'fas fa-list-alt'),
    ('fa fa-long-arrow-down', 'fas fa-long-arrow-alt-down'),
    ('fa fa-long-arrow-left', 'fas fa-long-arrow-alt-left'),
    ('fa fa-long-arrow-right', 'fas fa-long-arrow-alt-right'),
    ('fa fa-long-arrow-up', 'fas fa-long-arrow-alt-up'),
    ('fa fa-mail-forward', 'fas fa-share'),
    ('fa fa-mail-reply-all', 'fas fa-reply-all'),
    ('fa fa-mail-reply', 'fas fa-reply'),
    ('fa fa-map-marker', 'fas fa-map-marker-alt'),
    ('fa fa-map-o', 'fas fa-map'),
    ('fa fa-maxcdn', 'fab fa-maxcdn'),
    ('fa fa-meanpath', 'fab fa-font-awesome'),
    ('fa fa-medium', 'fab fa-medium'),
    ('fa fa-meetup', 'fab fa-meetup'),
    ('fa fa-meh-o', 'fas fa-meh'),
    ('fa fa-minus-square-o', 'fas fa-minus-square'),
    ('fa fa-mixcloud', 'fab fa-mixcloud'),
    ('fa fa-mobile-phone', 'fas fa-mobile-alt'),
    ('fa fa-mobile', 'fas fa-mobile-alt'),
    ('fa fa-modx', 'fab fa-modx'),
    ('fa fa-moon-o', 'fas fa-moon'),
    ('fa fa-money', 'fas fa-money-bill-alt'),
    ('fa fa-mortar-board', 'fas fa-graduation-cap'),
    ('fa fa-navicon', 'fas fa-bars'),
    ('fa fa-newspaper-o', 'fas fa-newspaper'),
    ('fa fa-object-group', 'fas fa-object-group'),
    ('fa fa-object-ungroup', 'fas fa-object-ungroup'),
    ('fa fa-odnoklassniki-square', 'fab fa-odnoklassniki-square'),
    ('fa fa-odnoklassniki', 'fab fa-odnoklassniki'),
    ('fa fa-opencart', 'fab fa-opencart'),
    ('fa fa-openid', 'fab fa-openid'),
    ('fa fa-opera', 'fab fa-opera'),
    ('fa fa-optin-monster', 'fab fa-optin-monster'),
    ('fa fa-pagelines', 'fab fa-pagelines'),
    ('fa fa-paper-plane-o', 'fas fa-paper-plane'),
    ('fa fa-paste', 'fas fa-clipboard'),
    ('fa fa-pause-circle-o', 'fas fa-pause-circle'),
    ('fa fa-paypal', 'fab fa-paypal'),
    ('fa fa-pencil-square', 'fas fa-pen-square'),
    ('fa fa-pencil-square-o', 'fas fa-edit'),
    ('fa fa-pencil', 'fas fa-pencil-alt'),
    ('fa fa-photo', 'fas fa-image'),
    ('fa fa-picture-o', 'fas fa-image'),
    ('fa fa-pie-chart', 'fas fa-chart-pie'),
    ('fa fa-pied-piper-alt', 'fab fa-pied-piper-alt'),
    ('fa fa-pied-piper-pp', 'fab fa-pied-piper-pp'),
    ('fa fa-pied-piper', 'fab fa-pied-piper'),
    ('fa fa-pinterest-p', 'fab fa-pinterest-p'),
    ('fa fa-pinterest-square', 'fab fa-pinterest-square'),
    ('fa fa-pinterest', 'fab fa-pinterest'),
    ('fa fa-play-circle-o', 'fas fa-play-circle'),
    ('fa fa-plus-square-o', 'fas fa-plus-square'),
    ('fa fa-product-hunt', 'fab fa-product-hunt'),
    ('fa fa-qq', 'fab fa-qq'),
    ('fa fa-question-circle-o', 'fas fa-question-circle'),
    ('fa fa-quora', 'fab fa-quora'),
    ('fa fa-ravelry', 'fab fa-ravelry'),
    ('fa fa-ra', 'fab fa-rebel'),
    ('fa fa-rebel', 'fab fa-rebel'),
    ('fa fa-reddit-alien', 'fab fa-reddit-alien'),
    ('fa fa-reddit-square', 'fab fa-reddit-square'),
    ('fa fa-reddit', 'fab fa-reddit'),
    ('fa fa-refresh', 'fas fa-sync'),
    ('fa fa-registered', 'fas fa-registered'),
    ('fa fa-remove', 'fas fa-times'),
    ('fa fa-renren', 'fab fa-renren'),
    ('fa fa-reorder', 'fas fa-bars'),
    ('fa fa-repeat', 'fas fa-redo'),
    ('fa fa-resistance', 'fab fa-rebel'),
    ('fa fa-rmb', 'fas fa-yen-sign'),
    ('fa fa-rotate-left', 'fas fa-undo'),
    ('fa fa-rotate-right', 'fas fa-redo'),
    ('fa fa-rouble', 'fas fa-ruble-sign'),
    ('fa fa-ruble', 'fas fa-ruble-sign'),
    ('fa fa-rub', 'fas fa-ruble-sign'),
    ('fa fa-rupee', 'fas fa-rupee-sign'),
    ('fa fa-s15', 'fas fa-bath'),
    ('fa fa-safasi', 'fab fa-safasi'),
    ('fa fa-scissors', 'fas fa-cut'),
    ('fa fa-scribd', 'fab fa-scribd'),
    ('fa fa-sellsy', 'fab fa-sellsy'),
    ('fa fa-send-o', 'fas fa-paper-plane'),
    ('fa fa-send', 'fas fa-paper-plane'),
    ('fa fa-share-square-o', 'fas fa-share-square'),
    ('fa fa-shekel', 'fas fa-shekel-sign'),
    ('fa fa-sheqel', 'fas fa-shekel-sign'),
    ('fa fa-shield', 'fas fa-shield-alt'),
    ('fa fa-shirtsinbulk', 'fab fa-shirtsinbulk'),
    ('fa fa-sign-in', 'fas fa-sign-in-alt'),
    ('fa fa-sign-out', 'fas fa-sign-out-alt'),
    ('fa fa-signing', 'fas fa-sign-language'),
    ('fa fa-simplybuilt', 'fab fa-simplybuilt'),
    ('fa fa-skyatlas', 'fab fa-skyatlas'),
    ('fa fa-skype', 'fab fa-skype'),
    ('fa fa-slack', 'fab fa-slack'),
    ('fa fa-sliders', 'fas fa-sliders-h'),
    ('fa fa-slideshare', 'fab fa-slideshare'),
    ('fa fa-smile-o', 'fas fa-smile'),
    ('fa fa-snapchat-ghost', 'fab fa-snapchat-ghost'),
    ('fa fa-snapchat-square', 'fab fa-snapchat-square'),
    ('fa fa-snapchat', 'fab fa-snapchat'),
    ('fa fa-snowflake-o', 'fas fa-snowflake'),
    ('fa fa-soccer-ball-o', 'fas fa-futbol'),
    ('fa fa-sort-alpha-asc', 'fas fa-sort-alpha-down'),
    ('fa fa-sort-alpha-desc', 'fas fa-sort-alpha-up'),
    ('fa fa-sort-amount-asc', 'fas fa-sort-amount-down'),
    ('fa fa-sort-amount-desc', 'fas fa-sort-amount-up'),
    ('fa fa-sort-asc', 'fas fa-sort-up'),
    ('fa fa-sort-desc', 'fas fa-sort-down'),
    ('fa fa-sort-numeric-asc', 'fas fa-sort-numeric-down'),
    ('fa fa-sort-numeric-desc', 'fas fa-sort-numeric-up'),
    ('fa fa-soundcloud', 'fab fa-soundcloud'),
    ('fa fa-spoon', 'fas fa-utensil-spoon'),
    ('fa fa-spotify', 'fab fa-spotify'),
    ('fa fa-square-o', 'fas fa-square'),
    ('fa fa-stack-exchange', 'fab fa-stack-exchange'),
    ('fa fa-stack-overflow', 'fab fa-stack-overflow'),
    ('fa fa-star-half-empty', 'fas fa-star-half'),
    ('fa fa-star-half-full', 'fas fa-star-half'),
    ('fa fa-star-half-o', 'fas fa-star-half'),
    ('fa fa-star-o', 'fas fa-star'),
    ('fa fa-steam-square', 'fab fa-steam-square'),
    ('fa fa-steam', 'fab fa-steam'),
    ('fa fa-sticky-note-o', 'fas fa-sticky-note'),
    ('fa fa-stop-circle-o', 'fas fa-stop-circle'),
    ('fa fa-stumbleupon-circle', 'fab fa-stumbleupon-circle'),
    ('fa fa-stumbleupon', 'fab fa-stumbleupon'),
    ('fa fa-sun-o', 'fas fa-sun'),
    ('fa fa-superpowers', 'fab fa-superpowers'),
    ('fa fa-support', 'fas fa-life-ring'),
    ('fa fa-tablet', 'fas fa-tablet-alt'),
    ('fa fa-tachometer', 'fas fa-tachometer-alt'),
    ('fa fa-telegram', 'fab fa-telegram'),
    ('fa fa-television', 'fas fa-tv'),
    ('fa fa-tencent-weibo', 'fab fa-tencent-weibo'),
    ('fa fa-themeisle', 'fab fa-themeisle'),
    ('fa fa-thermometer-0', 'fas fa-thermometer-empty'),
    ('fa fa-thermometer-1', 'fas fa-thermometer-quarter'),
    ('fa fa-thermometer-2', 'fas fa-thermometer-half'),
    ('fa fa-thermometer-3', 'fas fa-thermometer-three-quarters'),
    ('fa fa-thermometer-4', 'fas fa-thermometer-full'),
    ('fa fa-thermometer', 'fas fa-thermometer-full'),
    ('fa fa-thumb-tack', 'fas fa-thumbtack'),
    ('fa fa-thumbs-o-down', 'fas fa-thumbs-down'),
    ('fa fa-thumbs-o-up', 'fas fa-thumbs-up'),
    ('fa fa-ticket', 'fas fa-ticket-alt'),
    ('fa fa-times-circle-o', 'fas fa-times-circle'),
    ('fa fa-times-rectangle-o', 'fas fa-window-close'),
    ('fa fa-times-rectangle', 'fas fa-window-close'),
    ('fa fa-toggle-down', 'fas fa-caret-square-down'),
    ('fa fa-toggle-left', 'fas fa-caret-square-left'),
    ('fa fa-toggle-right', 'fas fa-caret-square-right'),
    ('fa fa-toggle-up', 'fas fa-caret-square-up'),
    ('fa fa-trash-o', 'fas fa-trash-alt'),
    ('fa fa-trash', 'fas fa-trash-alt'),
    ('fa fa-trello', 'fab fa-trello'),
    ('fa fa-tripadvisor', 'fab fa-tripadvisor'),
    ('fa fa-try', 'fas fa-lira-sign'),
    ('fa fa-tumblr-square', 'fab fa-tumblr-square'),
    ('fa fa-tumblr', 'fab fa-tumblr'),
    ('fa fa-turkish-lira', 'fas fa-lira-sign'),
    ('fa fa-twitch', 'fab fa-twitch'),
    ('fa fa-twitter-square', 'fab fa-twitter-square'),
    ('fa fa-twitter', 'fab fa-twitter'),
    ('fa fa-unsorted', 'fas fa-sort'),
    ('fa fa-usb', 'fab fa-usb'),
    ('fa fa-usd', 'fas fa-dollar-sign'),
    ('fa fa-user-circle-o', 'fas fa-user-circle'),
    ('fa fa-user-o', 'fas fa-user'),
    ('fa fa-vcard-o', 'fas fa-address-card'),
    ('fa fa-vcard', 'fas fa-address-card'),
    ('fa fa-viacoin', 'fab fa-viacoin'),
    ('fa fa-viadeo-square', 'fab fa-viadeo-square'),
    ('fa fa-viadeo', 'fab fa-viadeo'),
    ('fa fa-video-camera', 'fas fa-video'),
    ('fa fa-vimeo-square', 'fab fa-vimeo-square'),
    ('fa fa-vimeo', 'fab fa-vimeo-v'),
    ('fa fa-vine', 'fab fa-vine'),
    ('fa fa-vk', 'fab fa-vk'),
    ('fa fa-volume-control-phone', 'fas fa-phone-volume'),
    ('fa fa-warning', 'fas fa-exclamation-triangle'),
    ('fa fa-wechat', 'fab fa-weixin'),
    ('fa fa-weibo', 'fab fa-weibo'),
    ('fa fa-weixin', 'fab fa-weixin'),
    ('fa fa-whatsapp', 'fab fa-whatsapp'),
    ('fa fa-wheelchair-alt', 'fab fa-accessible-icon'),
    ('fa fa-wikipedia-w', 'fab fa-wikipedia-w'),
    ('fa fa-window-close-o', 'fas fa-window-close'),
    ('fa fa-window-maximize', 'fas fa-window-maximize'),
    ('fa fa-window-restore', 'fas fa-window-restore'),
    ('fa fa-windows', 'fab fa-windows'),
    ('fa fa-won', 'fas fa-won-sign'),
    ('fa fa-wordpress', 'fab fa-wordpress'),
    ('fa fa-wpbeginner', 'fab fa-wpbeginner'),
    ('fa fa-wpexplorer', 'fab fa-wpexplorer'),
    ('fa fa-wpforms', 'fab fa-wpforms'),
    ('fa fa-xing-square', 'fab fa-xing-square'),
    ('fa fa-xing', 'fab fa-xing'),
    ('fa fa-y-combinator-square', 'fab fa-hacker-news'),
    ('fa fa-y-combinator', 'fab fa-y-combinator'),
    ('fa fa-yahoo', 'fab fa-yahoo'),
    ('fa fa-yc', 'fab fa-y-combinator'),
    ('fa fa-yc-square', 'fab fa-hacker-news'),
    ('fa fa-yelp', 'fab fa-yelp'),
    ('fa fa-yen', 'fas fa-yen-sign'),
    ('fa fa-yoast', 'fab fa-yoast'),
    ('fa fa-youtube-play', 'fab fa-youtube'),
    ('fa fa-youtube-square', 'fab fa-youtube-square'),
    ('fa fa-youtube', 'fab fa-youtube'),
    ('fa fa-fa', 'fab fa-font-awesome')
]

findreplace_unicode = """
fa-address-book-o f2ba f2b9
fa-address-card-o f2bc f2bb
fa-arrow-circle-o-down f01a f358
fa-arrow-circle-o-left f190 f359
fa-arrow-circle-o-right f18e f35a
fa-arrow-circle-o-up f01b f35b
fa-arrows f047 f0b2
fa-arrows-h f07e f337
fa-arrows-v f07d f338
fa-bell-o f0a2 f0f3
fa-bell-slash-o f1f7 f1f6
fa-bitbucket-square f172 f171
fa-bookmark-o f097 f02e
fa-building-o f0f7 f1ad
fa-check-circle-o f05d f058
fa-check-square-o f046 f14a
fa-circle-o f10c f111
fa-circle-thin f1db f111
fa-cloud-download f0ed f381
fa-cloud-upload f0ee f382
fa-comment-o f0e5 f075
fa-commenting-o f27b f4ad
fa-comments-o f0e6 f086
fa-credit-card-alt f283 f09d
fa-cutlery f0f5 f2e7
fa-dashboard f0e4 f3fd
fa-diamond f219 f3a5
fa-drivers-license-o f2c3 f2c2
fa-envelope-o f003 f0e0
fa-envelope-open-o f2b7 f2b6
fa-exchange f0ec f362
fa-external-link f08e f35d
fa-external-link-square f14c f360
fa-facebook-official f230 f09a
fa-file-o f016 f15b
fa-file-text-o f0f6 f15c
fa-flag-o f11d f024
fa-folder-o f114 f07b
fa-folder-open-o f115 f07c
fa-heart-o f08a f004
fa-hourglass-o f250 f254
fa-id-card-o f2c3 f2c2
fa-level-down f149 f3be
fa-level-up f148 f3bf
fa-long-arrow-down f175 f309
fa-long-arrow-left f177 f30a
fa-long-arrow-right f178 f30b
fa-long-arrow-up f176 f30c
fa-mail-reply f112 f3e5
fa-map-o f278 f279
fa-meanpath f20c f2b4
fa-minus-square-o f147 f146
fa-paper-plane-o f1d9 f1d8
fa-pause-circle-o f28c f28b
fa-pencil f040 f303
fa-play-circle-o f01d f144
fa-plus-square-o f196 f0fe
fa-question-circle-o f29c f059
fa-reply f112 f3e5
fa-send-o f1d9 f1d8
fa-share-square-o f045 f14d
fa-shield f132 f3ed
fa-sign-in f090 f2f6
fa-sign-out f08b f2f5
fa-spoon f1b1 f2e5
fa-square-o f096 f0c8
fa-star-half-empty f123 f089
fa-star-half-full f123 f089
fa-star-half-o f123 f089
fa-star-o f006 f005
fa-sticky-note-o f24a f249
fa-stop-circle-o f28e f28d
fa-tachometer f0e4 f3fd
fa-thumbs-o-down f088 f165
fa-thumbs-o-up f087 f164
fa-ticket f145 f3ff
fa-times-circle-o f05c f057
fa-times-rectangle f2d3 f410
fa-times-rectangle-o f2d4 f410
fa-trash-o f014 f2ed
fa-user-circle-o f2be f2bd
fa-user-o f2c0 f007
fa-vcard-o f2bc f2bb
fa-wheelchair-alt f29b f368
fa-window-close f2d3 f410
fa-window-close-o f2d4 f410
fa-youtube-play f16a f167
"""

# These icons must have `font-weight: bold` or prefix of fas (which sets `font-weight: 900`, aka bold)
ICON_V5_ONLY_SOLID = """
ad f641
adjust f042
air-freshener f5d0
align-center f037
align-justify f039
align-left f036
align-right f038
allergies f461
ambulance f0f9
american-sign-language-interpreting f2a3
anchor f13d
angle-double-down f103
angle-double-left f100
angle-double-right f101
angle-double-up f102
angle-down f107
angle-left f104
angle-right f105
angle-up f106
ankh f644
apple-alt f5d1
archive f187
archway f557
arrow-circle-down f0ab
arrow-circle-left f0a8
arrow-circle-right f0a9
arrow-circle-up f0aa
arrow-down f063
arrow-left f060
arrow-right f061
arrow-up f062
arrows-alt f0b2
arrows-alt-h f337
arrows-alt-v f338
assistive-listening-systems f2a2
asterisk f069
at f1fa
atlas f558
atom f5d2
audio-description f29e
award f559
baby f77c
baby-carriage f77d
backspace f55a
backward f04a
bacon f7e5
balance-scale f24e
balance-scale-left f515
balance-scale-right f516
ban f05e
band-aid f462
barcode f02a
bars f0c9
baseball-ball f433
basketball-ball f434
bath f2cd
battery-empty f244
battery-full f240
battery-half f242
battery-quarter f243
battery-three-quarters f241
bed f236
beer f0fc
bezier-curve f55b
bible f647
bicycle f206
biking f84a
binoculars f1e5
biohazard f780
birthday-cake f1fd
blender f517
blender-phone f6b6
blind f29d
blog f781
bold f032
bolt f0e7
bomb f1e2
bone f5d7
bong f55c
book f02d
book-dead f6b7
book-medical f7e6
book-open f518
book-reader f5da
border-all f84c
border-none f850
border-style f853
bowling-ball f436
box f466
box-open f49e
boxes f468
braille f2a1
brain f5dc
bread-slice f7ec
briefcase f0b1
briefcase-medical f469
broadcast-tower f519
broom f51a
brush f55d
bug f188
bullhorn f0a1
bullseye f140
burn f46a
bus f207
bus-alt f55e
business-time f64a
calculator f1ec
calendar-day f783
calendar-week f784
camera f030
camera-retro f083
campground f6bb
candy-cane f786
cannabis f55f
capsules f46b
car f1b9
car-alt f5de
car-battery f5df
car-crash f5e1
car-side f5e4
caret-down f0d7
caret-left f0d9
caret-right f0da
caret-up f0d8
carrot f787
cart-arrow-down f218
cart-plus f217
cash-register f788
cat f6be
certificate f0a3
chair f6c0
chalkboard f51b
chalkboard-teacher f51c
charging-station f5e7
chart-area f1fe
chart-line f201
chart-pie f200
check f00c
check-double f560
cheese f7ef
chess f439
chess-bishop f43a
chess-board f43c
chess-king f43f
chess-knight f441
chess-pawn f443
chess-queen f445
chess-rook f447
chevron-circle-down f13a
chevron-circle-left f137
chevron-circle-right f138
chevron-circle-up f139
chevron-down f078
chevron-left f053
chevron-right f054
chevron-up f077
child f1ae
church f51d
circle-notch f1ce
city f64f
clinic-medical f7f2
clipboard-check f46c
clipboard-list f46d
cloud f0c2
cloud-download-alt f381
cloud-meatball f73b
cloud-moon f6c3
cloud-moon-rain f73c
cloud-rain f73d
cloud-showers-heavy f740
cloud-sun f6c4
cloud-sun-rain f743
cloud-upload-alt f382
cocktail f561
code f121
code-branch f126
coffee f0f4
cog f013
cogs f085
coins f51e
columns f0db
comment-dollar f651
comment-medical f7f5
comment-slash f4b3
comments-dollar f653
compact-disc f51f
compress f066
compress-arrows-alt f78c
concierge-bell f562
cookie f563
cookie-bite f564
couch f4b8
crop f125
crop-alt f565
cross f654
crosshairs f05b
crow f520
crown f521
crutch f7f7
cube f1b2
cubes f1b3
cut f0c4
database f1c0
deaf f2a4
democrat f747
desktop f108
dharmachakra f655
diagnoses f470
dice f522
dice-d20 f6cf
dice-d6 f6d1
dice-five f523
dice-four f524
dice-one f525
dice-six f526
dice-three f527
dice-two f528
digital-tachograph f566
directions f5eb
divide f529
dna f471
dog f6d3
dollar-sign f155
dolly f472
dolly-flatbed f474
donate f4b9
door-closed f52a
door-open f52b
dove f4ba
download f019
drafting-compass f568
dragon f6d5
draw-polygon f5ee
drum f569
drum-steelpan f56a
drumstick-bite f6d7
dumbbell f44b
dumpster f793
dumpster-fire f794
dungeon f6d9
egg f7fb
eject f052
ellipsis-h f141
ellipsis-v f142
envelope-open-text f658
envelope-square f199
equals f52c
eraser f12d
ethernet f796
euro-sign f153
exchange-alt f362
exclamation f12a
exclamation-circle f06a
exclamation-triangle f071
expand f065
expand-arrows-alt f31e
external-link-alt f35d
external-link-square-alt f360
eye-dropper f1fb
fan f863
fast-backward f049
fast-forward f050
fax f1ac
feather f52d
feather-alt f56b
female f182
fighter-jet f0fb
file-contract f56c
file-csv f6dd
file-download f56d
file-export f56e
file-import f56f
file-invoice f570
file-invoice-dollar f571
file-medical f477
file-medical-alt f478
file-prescription f572
file-signature f573
file-upload f574
fill f575
fill-drip f576
film f008
filter f0b0
fingerprint f577
fire f06d
fire-alt f7e4
fire-extinguisher f134
first-aid f479
fish f578
fist-raised f6de
flag-checkered f11e
flag-usa f74d
flask f0c3
folder-minus f65d
folder-plus f65e
font f031
football-ball f44e
forward f04e
frog f52e
funnel-dollar f662
gamepad f11b
gas-pump f52f
gavel f0e3
genderless f22d
ghost f6e2
gift f06b
gifts f79c
glass-cheers f79f
glass-martini f000
glass-martini-alt f57b
glass-whiskey f7a0
glasses f530
globe f0ac
globe-africa f57c
globe-americas f57d
globe-asia f57e
globe-europe f7a2
golf-ball f450
gopuram f664
graduation-cap f19d
greater-than f531
greater-than-equal f532
grip-horizontal f58d
grip-lines f7a4
grip-lines-vertical f7a5
grip-vertical f58e
guitar f7a6
h-square f0fd
hamburger f805
hammer f6e3
hamsa f665
hand-holding f4bd
hand-holding-heart f4be
hand-holding-usd f4c0
hand-middle-finger f806
hands f4c2
hands-helping f4c4
hanukiah f6e6
hard-hat f807
hashtag f292
hat-wizard f6e8
haykal f666
heading f1dc
headphones f025
headphones-alt f58f
headset f590
heart-broken f7a9
heartbeat f21e
helicopter f533
highlighter f591
hiking f6ec
hippo f6ed
history f1da
hockey-puck f453
holly-berry f7aa
home f015
horse f6f0
horse-head f7ab
hospital-alt f47d
hospital-symbol f47e
hot-tub f593
hotdog f80f
hotel f594
hourglass-end f253
hourglass-half f252
hourglass-start f251
house-damage f6f1
hryvnia f6f2
i-cursor f246
ice-cream f810
icicles f7ad
icons f86d
id-card-alt f47f
igloo f7ae
inbox f01c
indent f03c
industry f275
infinity f534
info f129
info-circle f05a
italic f033
jedi f669
joint f595
journal-whills f66a
kaaba f66b
key f084
khanda f66d
kiwi-bird f535
landmark f66f
language f1ab
laptop f109
laptop-code f5fc
laptop-medical f812
layer-group f5fd
leaf f06c
less-than f536
less-than-equal f537
level-down-alt f3be
level-up-alt f3bf
link f0c1
lira-sign f195
list f03a
list-ol f0cb
list-ul f0ca
location-arrow f124
lock f023
lock-open f3c1
long-arrow-alt-down f309
long-arrow-alt-left f30a
long-arrow-alt-right f30b
long-arrow-alt-up f30c
low-vision f2a8
luggage-cart f59d
magic f0d0
magnet f076
mail-bulk f674
male f183
map-marked f59f
map-marked-alt f5a0
map-marker f041
map-marker-alt f3c5
map-pin f276
map-signs f277
marker f5a1
mars f222
mars-double f227
mars-stroke f229
mars-stroke-h f22b
mars-stroke-v f22a
mask f6fa
medal f5a2
medkit f0fa
memory f538
menorah f676
mercury f223
meteor f753
microchip f2db
microphone f130
microphone-alt f3c9
microphone-alt-slash f539
microphone-slash f131
microscope f610
minus f068
minus-circle f056
mitten f7b5
mobile f10b
mobile-alt f3cd
money-bill f0d6
money-bill-wave f53a
money-bill-wave-alt f53b
money-check f53c
money-check-alt f53d
monument f5a6
mortar-pestle f5a7
mosque f678
motorcycle f21c
mountain f6fc
mouse-pointer f245
mug-hot f7b6
music f001
network-wired f6ff
neuter f22c
not-equal f53e
notes-medical f481
oil-can f613
om f679
otter f700
outdent f03b
pager f815
paint-brush f1fc
paint-roller f5aa
palette f53f
pallet f482
paperclip f0c6
parachute-box f4cd
paragraph f1dd
parking f540
passport f5ab
pastafarianism f67b
paste f0ea
pause f04c
paw f1b0
peace f67c
pen f304
pen-alt f305
pen-fancy f5ac
pen-nib f5ad
pen-square f14b
pencil-alt f303
pencil-ruler f5ae
people-carry f4ce
pepper-hot f816
percent f295
percentage f541
person-booth f756
phone f095
phone-alt f879
phone-slash f3dd
phone-square f098
phone-square-alt f87b
phone-volume f2a0
photo-video f87c
piggy-bank f4d3
pills f484
pizza-slice f818
place-of-worship f67f
plane f072
plane-arrival f5af
plane-departure f5b0
play f04b
plug f1e6
plus f067
plus-circle f055
podcast f2ce
poll f681
poll-h f682
poo f2fe
poo-storm f75a
poop f619
portrait f3e0
pound-sign f154
power-off f011
pray f683
praying-hands f684
prescription f5b1
prescription-bottle f485
prescription-bottle-alt f486
print f02f
procedures f487
project-diagram f542
puzzle-piece f12e
qrcode f029
question f128
quidditch f458
quote-left f10d
quote-right f10e
quran f687
radiation f7b9
radiation-alt f7ba
rainbow f75b
random f074
receipt f543
recycle f1b8
redo f01e
redo-alt f2f9
remove-format f87d
reply f3e5
reply-all f122
republican f75e
restroom f7bd
retweet f079
ribbon f4d6
ring f70b
road f018
robot f544
rocket f135
route f4d7
rss f09e
rss-square f143
ruble-sign f158
ruler f545
ruler-combined f546
ruler-horizontal f547
ruler-vertical f548
running f70c
rupee-sign f156
satellite f7bf
satellite-dish f7c0
school f549
screwdriver f54a
scroll f70e
sd-card f7c2
search f002
search-dollar f688
search-location f689
search-minus f010
search-plus f00e
seedling f4d8
server f233
shapes f61f
share f064
share-alt f1e0
share-alt-square f1e1
shekel-sign f20b
shield-alt f3ed
ship f21a
shipping-fast f48b
shoe-prints f54b
shopping-bag f290
shopping-basket f291
shopping-cart f07a
shower f2cc
shuttle-van f5b6
sign f4d9
sign-in-alt f2f6
sign-language f2a7
sign-out-alt f2f5
signal f012
signature f5b7
sim-card f7c4
sitemap f0e8
skating f7c5
skiing f7c9
skiing-nordic f7ca
skull f54c
skull-crossbones f714
slash f715
sleigh f7cc
sliders-h f1de
smog f75f
smoking f48d
smoking-ban f54d
sms f7cd
snowboarding f7ce
snowman f7d0
snowplow f7d2
socks f696
solar-panel f5ba
sort f0dc
sort-alpha-down f15d
sort-alpha-down-alt f881
sort-alpha-up f15e
sort-alpha-up-alt f882
sort-amount-down f160
sort-amount-down-alt f884
sort-amount-up f161
sort-amount-up-alt f885
sort-down f0dd
sort-numeric-down f162
sort-numeric-down-alt f886
sort-numeric-up f163
sort-numeric-up-alt f887
sort-up f0de
spa f5bb
space-shuttle f197
spell-check f891
spider f717
spinner f110
splotch f5bc
spray-can f5bd
square-full f45c
square-root-alt f698
stamp f5bf
star-and-crescent f699
star-half-alt f5c0
star-of-david f69a
star-of-life f621
step-backward f048
step-forward f051
stethoscope f0f1
stop f04d
stopwatch f2f2
store f54e
store-alt f54f
stream f550
street-view f21d
strikethrough f0cc
stroopwafel f551
subscript f12c
subway f239
suitcase f0f2
suitcase-rolling f5c1
superscript f12b
swatchbook f5c3
swimmer f5c4
swimming-pool f5c5
synagogue f69b
sync f021
sync-alt f2f1
syringe f48e
table f0ce
table-tennis f45d
tablet f10a
tablet-alt f3fa
tablets f490
tachometer-alt f3fd
tag f02b
tags f02c
tape f4db
tasks f0ae
taxi f1ba
teeth f62e
teeth-open f62f
temperature-high f769
temperature-low f76b
tenge f7d7
terminal f120
text-height f034
text-width f035
th f00a
th-large f009
th-list f00b
theater-masks f630
thermometer f491
thermometer-empty f2cb
thermometer-full f2c7
thermometer-half f2c9
thermometer-quarter f2ca
thermometer-three-quarters f2c8
thumbtack f08d
ticket-alt f3ff
times f00d
tint f043
tint-slash f5c7
toggle-off f204
toggle-on f205
toilet f7d8
toilet-paper f71e
toolbox f552
tools f7d9
tooth f5c9
torah f6a0
torii-gate f6a1
tractor f722
trademark f25c
traffic-light f637
train f238
tram f7da
transgender f224
transgender-alt f225
trash f1f8
trash-restore f829
trash-restore-alt f82a
tree f1bb
trophy f091
truck f0d1
truck-loading f4de
truck-monster f63b
truck-moving f4df
truck-pickup f63c
tshirt f553
tty f1e4
tv f26c
umbrella f0e9
umbrella-beach f5ca
underline f0cd
undo f0e2
undo-alt f2ea
universal-access f29a
university f19c
unlink f127
unlock f09c
unlock-alt f13e
upload f093
user-alt f406
user-alt-slash f4fa
user-astronaut f4fb
user-check f4fc
user-clock f4fd
user-cog f4fe
user-edit f4ff
user-friends f500
user-graduate f501
user-injured f728
user-lock f502
user-md f0f0
user-minus f503
user-ninja f504
user-nurse f82f
user-plus f234
user-secret f21b
user-shield f505
user-slash f506
user-tag f507
user-tie f508
user-times f235
users f0c0
users-cog f509
utensil-spoon f2e5
utensils f2e7
vector-square f5cb
venus f221
venus-double f226
venus-mars f228
vial f492
vials f493
video f03d
video-slash f4e2
vihara f6a7
voicemail f897
volleyball-ball f45f
volume-down f027
volume-mute f6a9
volume-off f026
volume-up f028
vote-yea f772
vr-cardboard f729
walking f554
wallet f555
warehouse f494
water f773
wave-square f83e
weight f496
weight-hanging f5cd
wheelchair f193
wifi f1eb
wind f72e
wine-bottle f72f
wine-glass f4e3
wine-glass-alt f5ce
won-sign f159
wrench f0ad
x-ray f497
yen-sign f157
yin-yang f6ad
"""


# This always ensures a newline at the end of file
def update_via_sed(file_path, find_replace):
    for icon in find_replace:
        subprocess.run(['sed', '-ie', 's/{}/{}/g'.format(icon[0], icon[1]), file_path])


def update_via_replace(file_path, find_replace):
    """ Sidenote: Neither using binary mode nor `open(..., newline='')` helped to keep newlines stay the same."""
    with open(file_path, 'r', newline='') as read_file:
        content = read_file.read()

    for icon in find_replace:
        content = content.replace(icon[0], icon[1])

    with open(file_path, 'w', newline='') as write_file:
        write_file.write(content)


def update_icons_with_prefix():
    print('update_icons_with_prefix()')
    file_paths = subprocess.getoutput('grep -rl "fa fa-" . {}'.format(GREP_EXCLUDE)).splitlines()
    for file_path in file_paths:
        # noinspection PyBroadException
        try:
            print(file_path)
            # update_via_sed(fpath)
            update_via_replace(file_path, findreplace)
            # After all icons with name changes have finished updating, update the remaining prefixes
            update_via_replace(file_path, [('fa fa-', 'fas fa-')])
        except Exception:
            pass


def update_icons_without_prefix():
    print('update_icons_without_prefix()')

    findreplace_without_prefix = []
    for fr in findreplace:
        # Remove 'fa-fa' because we don't want to accidentally convert `userTypeID = new Guid("5e2cd4fa-fa11-423d-bb62-865d3d9c3151");`
        if (fr[0] is not 'fa-fa'):
            # Adding `[^-]` (aka, 'not dash') so that we don't get the case of something like `fa-trash-alt-alt` or `fa-pencil-alt-alt`
            findreplace_without_prefix.append((fr[0].split(' ')[1] + '[^-]', fr[1].split(' ')[1]))

    file_paths = subprocess.getoutput('grep -rl "fa-" . {}'.format(GREP_EXCLUDE)).splitlines()

    for file_path in file_paths:
        # noinspection PyBroadException
        try:
            print(file_path)
            # update_via_sed(fpath)
            update_via_replace(file_path, findreplace_without_prefix)
        except Exception:
            pass


def update_font_family():
    print('update_font_family()')
    file_paths = subprocess.getoutput(
        'grep -rl "font-family:" . {}'.format(GREP_EXCLUDE)).splitlines()
        # 'grep -rl "font-family: FontAwesome;" . {}'.format(GREP_EXCLUDE)).splitlines()
    for file_path in file_paths:
        try:
            update_via_replace(file_path, [('font-family: FontAwesome;', 'font-family: "Font Awesome 5 Free";')])
            update_via_replace(file_path, [("font-family: 'Fontawesome'", 'font-family: "Font Awesome 5 Free"')])
            update_via_replace(file_path, [("font-family: 'FontAwesome';", 'font-family: "Font Awesome 5 Free";')])
            update_via_replace(file_path, [('font-family: "FontAwesome";', 'font-family: "Font Awesome 5 Free";')])
            update_via_replace(file_path, [("font-family: Font Awesome 5 Free;", 'font-family: "Font Awesome 5 Free";')])
            update_via_replace(file_path, [("font-family: 'Font Awesome 5 Free';", 'font-family: "Font Awesome 5 Free";')])
            update_via_replace(file_path, [("font-family: 'Font Awesome 5 Brands';", 'font-family: "Font Awesome 5 Brands";')])
        except Exception:
            pass


def update_hard_coded_unicode_values():
    print('update_hard_coded_unicode_values(): TODO')
    # TODO: Double-check CSS files that hard-code font-awesome unicode values (ex: `content: "\f005"` in reportFinderStyle.css)
    # Perhaps just in files where `font-family: FontAwesome` has changed, but maybe more, because CWS.
    pass


def update_css_variables():
    print('update_css_variables()')
    # Hard-coded file for speed (since there are few usages).
    variable_less_file = subprocess.getoutput('find . -type f -name variables.less')
    update_via_replace(variable_less_file, [('@fa-css-prefix:       fa;', '@fa-css-prefix:       fa;\n@fa-solid-css-prefix: fas;\n@fa-brand-css-prefix: fab;')])
    update_via_replace(variable_less_file, [('@fa-version:          "4.7.0";', '@fa-version:          "5.10.1";')])

    variable_less_file = subprocess.getoutput('find . -type f -name _variables.scss')
    update_via_replace(variable_less_file, [('$fa-css-prefix:       fa !default;', '$fa-css-prefix:       fa !default;\n$fa-solid-css-prefix: fas !default;\n$fa-brand-css-prefix: fab !default;')])
    update_via_replace(variable_less_file, [('$fa-version:          "4.7.0" !default;', '$fa-version:          "5.10.1" !default;')])


def update_misc_precheck_normalization():
    print('update_misc_precheck_normalization()')
    # Note the double-space in the following grep
    file_paths = subprocess.getoutput('grep -rl "fa  fa-" . {}'.format(GREP_EXCLUDE)).splitlines()
    for file_path in file_paths:
        update_via_replace(file_path, [('fa  fa-', 'fa fa-')])

    # Note the extra 'fa'
    file_paths = subprocess.getoutput('grep -rl "fa fa fa-" . {}'.format(GREP_EXCLUDE)).splitlines()
    for file_path in file_paths:
        update_via_replace(file_path, [('fa fa fa-', 'fa fa-')])


def update_unicode():
    print('update_unicode()')
    v4_name_unicode_v5_unicode = []
    lines = findreplace_unicode.split('\n')
    for line in lines:
        tokens = line.split(' ')
        if len(tokens) > 2:
            v4_name = tokens[0]
            v4_unicode = tokens[1]
            v5_unicode = tokens[2]

            file_paths = subprocess.getoutput('grep -rl "{}" . {}'.format('\\' + v4_unicode, GREP_EXCLUDE)).splitlines()
            for file_path in file_paths:
                try:
                    update_via_replace(file_path, [('\\' + v4_unicode, '\\' + v5_unicode)])
                except Exception:
                    pass

ALL_UNICODE_GREP_REGEX = '\\f\s\s\s'
# ALL_UNICODE_GREP_REGEX = '\\f\w\w\w'
V5_UNICODE_GREP_REGEX = '\\f[0[0[457]2[4e]5[789]7[5bc]8[69]9[ad]b[2]c[8]e[0]f[3e]]1[1[1]4[46ad]5[bc]6[457]7[1]a[d]d[8]f[6]]2[4[9]5[4]7[9]8[bd]b[469bd]c[2]e[57d]f[56]]3[0[39abc]3[78]5[89abd]6[028]8[12]a[5]b[ef]e[5d]f[df]]4[1[0]a[d]]]'


def find_icons_only_solid():
    print('find_icons_only_solid()')
    icon_unicodes = []
    for line in ICON_V5_ONLY_SOLID.split('\n'):
        tokens = line.split(' ')
        if len(tokens) > 1:
            icon_unicodes.append(line.split(' ')[1])
    grep_regex = '\\' + '\\({}\\)'.format('\\|'.join(icon_unicodes))
    # grep_regex = V5_UNICODE_GREP_REGEX

    file_paths = subprocess.getoutput('grep -rl {} "{}" .'.format(GREP_EXCLUDE, 'content: ')).splitlines()
    for file_path in file_paths:
        # fps = subprocess.getoutput('grep -rl {} "{}" {}'.format(GREP_EXCLUDE, grep_regex, file_path)).splitlines()
        # fps = subprocess.getoutput('grep --no-filename {} "{}" {}'.format(GREP_EXCLUDE, grep_regex, file_path)).splitlines()
        # print(fps)
        pass


start_overall = datetime.now()
print(sys.version)
print()

# update_misc_precheck_normalization()

start = datetime.now()
# update_icons_with_prefix()
print('Part 1 of 4 completed in', datetime.now() - start)
print()

start = datetime.now()
# update_icons_without_prefix()
print('Part 2 of 4 completed in', datetime.now() - start)

start = datetime.now()
#update_font_family()
print('Part 3 of 4 completed in', datetime.now() - start)

start = datetime.now()
find_icons_only_solid()
#update_unicode()
# TODO: Maybe don't need this and can completely remove the LESS and SCSS related stuff
#update_css_variables()
# update_hard_coded_unicode_values()
print('Part 4 of 4 completed in', datetime.now() - start)

print('Completed in', datetime.now() - start_overall)
