const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
const concatCSS = require('gulp-concat-css');
const ftp = require('gulp-ftp');

const workDir = "src/";
const htmlFiles = workDir + "*.html";
const sassFiles = workDir + "sass/*.sass";
const cssDir = workDir + "css/";
const outputCSS = "main.css";

const hostname = "";
const username = "";
const password = "";

gulp.task('sass', function(done) {
    gulp.src(sassFiles)
        .pipe(sass())
        .pipe(autoprefixer({cascade: false}))
        .pipe(concatCSS(outputCSS))
        .pipe(gulp.dest(cssDir))
        .pipe(browserSync.stream());
    done();
});

gulp.task('server', function(done) {
    browserSync.init({
        server: workDir
    });
    gulp.watch(sassFiles, gulp.series('sass'));
    gulp.watch(htmlFiles).on('change', () => {
      browserSync.reload();
      done();
    });
    done();
});

gulp.task('ftp', function(done) {
    return gulp.src(workDir + "**")
        .pipe(ftp({
            host: hostname,
            user: username,
            pass: password
        }))
        .pipe(gutil.noop());
    done();
});

gulp.task('default', gulp.series('sass', 'server'));