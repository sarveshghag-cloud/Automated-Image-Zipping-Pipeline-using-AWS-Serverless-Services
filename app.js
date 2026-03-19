AWS.config.update({
  accessKeyId: "YOUR_ACCESS_KEY",
  secretAccessKey: "YOUR_SECRET_KEY",
  region: "ap-southeast-1"
});

function uploadImage() {
    const fileInput = document.getElementById('imageInput');
    const status = document.getElementById('status');
    const file = fileInput.files[0];

    if (!file) {
        status.innerText = "Please select a file";
        return;
    }

    const s3 = new AWS.S3();

    const params = {
        Bucket: "raw-images-uploads-bucket",
        Key: file.name,
        Body: file,
        ContentType: file.type
    };

    s3.upload(params, function(err, data) {
        if (err) {
            console.error(err);
            status.innerText = "Upload failed ❌";
        } else {
            console.log(data);
            status.innerText = "Upload successful ✅";
        }
    });
}