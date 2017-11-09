module.exports = function (grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        sass: {
            dev: {
                options: {
                    sourceMap: false,
                    debugInfo: true,
                    trace: true,
                    outputStyle: "compressed"
                },
                files: [{
                    expand: true,
                    cwd: "assets/scss",
                    src: ["**/*.scss"],
                    dest: "assets/css/themes",
                    rename: function (dest, src) {
                        return dest + "/" + src.replace('.scss', '.min.css')
                    }
                }]
            },
            prod: {
                options: {
                    sourceMap: false,
                    debugInfo: true,
                    trace: true,
                    outputStyle: "expanded"
                },
                files: [{
                    expand: true,
                    cwd: "assets/scss",
                    src: ["**/*.scss"],
                    dest: "assets/css/themes",
                    rename: function (dest, src) {
                        return dest + "/" + src.replace('.scss', '.css')
                    }
                }]
            }
        },
        watch: {
            scripts: {
                files: ['**/*.scss'],
                tasks: ['sass:dev'],
                options: {
                    spawn: false,
                },
            },
        },
        validation: {
            options: {
                doctype: 'HTML5'
            },
            files: {
                src: ['*.html']
            }
        },
        copy: {
            main: {
                files: [
                    {
                        expand: true, 
                        cwd: 'assets/plugins/node_modules', 
                        src: ['**'], 
                        dest: 'assets/plugins/'
                    }
                ]
            }
        },
        remove: {
            options: {
                trace: false
            },
            main: {
                dirList: ['assets/plugins/node_modules']
            }
        },
        cssmin: {
            target: {
                files: {
                    'assets/css/plugins-bundle.css': 
                    [
                        'assets/plugins/bootstrap/dist/css/bootstrap.min.css',
                        'assets/plugins/slick-carousel/slick/slick.css',
                        'assets/plugins/animate.css/animate.min.css'
                    ],
                    'assets/css/icons-bundle.css': 
                    [
                        'assets/css/fpslineicons.css',
                        'assets/css/themify-icons.css'
                    ]
                }
            }
        },
        uglify: {
            options: {
                mangle: {
                    except: ['jQuery']
                }
            },
            my_target: {
                files: {
                    'assets/js/plugins-bundle.js':
                    [
                        'assets/plugins/jquery/dist/jquery.min.js',
                        'assets/plugins/tether/dist/js/tether.min.js',
                        'assets/plugins/bootstrap/dist/js/bootstrap.min.js',
                        'assets/plugins/slick-carousel/slick/slick.min.js',
                        'assets/plugins/jquery.appear/jquery.appear.js',
                        'assets/plugins/jquery.scrollto/jquery.scrollTo.min.js',
                        'assets/plugins/jquery.localscroll/jquery.localScroll.min.js',
                        'assets/plugins/waypoints/lib/jquery.waypoints.min.js',
                        'assets/plugins/waypoints/lib/shortcuts/sticky.min.js',
                        'assets/plugins/jquery-validation/dist/jquery.validate.min.js',
                        'assets/plugins/jquery.mb.ytplayer/dist/jquery.mb.YTPlayer.min.js',
                        'assets/plugins/masonry-layout/dist/masonry.pkgd.min.js',
                        'assets/plugins/imagesloaded/imagesloaded.pkgd.min.js',
                        'assets/plugins/twitter-fetcher/js/twitterFetcher_min.js',
                        'assets/plugins/skrollr/dist/skrollr.min.js'
                    ]
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-w3c-html-validation');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-remove');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.registerTask('default', ['watch']);
}