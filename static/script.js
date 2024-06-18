$(document).ready(function() {
    console.log("Document ready");

    $('#fileInput').on('change', function() {
        console.log("File input changed");
        var file = this.files[0];
        if (file) {
            var reader = new FileReader();
            reader.onload = function(e) {
                console.log("File loaded");
                $('#preview').attr('src', e.target.result);
                displayFileInfo(file);
                displaySelectedFileName(file.name);
            }
            reader.readAsDataURL(file);
        }
    });

    function displayFileInfo(file) {
        console.log("Displaying file info");
        var fileInfo = "File type: " + file.type + ", Size: " + formatBytes(file.size);
        $('#fileInfo').text(fileInfo);
    }

    function displaySelectedFileName(fileName) {
        console.log("Displaying selected file name");
        $('#selectedFileName').text('Selected file: ' + fileName);
    }

    function formatBytes(bytes, decimals = 2) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const dm = decimals < 0 ? 0 : decimals;
        const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    // Progress bar for upload
    $('form').submit(function() {
        console.log("Form submitted");
        var progressBar = $('#progressBar');
        var progressText = $('#progressText');
        var formData = new FormData($(this)[0]);

        $.ajax({
            url: '/',
            type: 'POST',
            data: formData,
            async: true,
            xhr: function() {
                var xhr = new XMLHttpRequest();
                xhr.upload.addEventListener('progress', function(e) {
                    if (e.lengthComputable) {
                        var percent = Math.round((e.loaded / e.total) * 100);
                        progressBar.css('width', percent + '%');
                        progressText.text(percent + '%');
                    }
                }, false);
                return xhr;
            },
            success: function(data) {
                // Reset progress bar after successful upload
                progressBar.css('width', '0%');
                progressText.text('0%');
                // Update the images and download link based on the server response
                if (data.filename && data.result_filename) {
                    $('#originalImage').attr('src', data.upload_url + data.filename);
                    $('#processedImage').attr('src', data.upload_url + data.result_filename);
                    $('#downloadLink').attr('href', data.download_url + data.result_filename).show();
                    $('.result-section').show();
                }
            },
            cache: false,
            contentType: false,
            processData: false
        });
        return false;
    });

    // Prevent form submission on Enter key press
    $(document).on('keypress', function(e) {
        if (e.which == 13) {
            e.preventDefault();
            return false;
        }
    });
});
