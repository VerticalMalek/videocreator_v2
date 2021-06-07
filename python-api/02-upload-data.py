import boto3

s3 = boto3.resource('s3')
MY_BUCKET = '200543'
bucket = s3.Bucket(MY_BUCKET)

my_elephant = '''

              ._   __...._____.-~"~-
            .'    `    \ ~"~        ``-.
           /` _      /  `\              `\
          /`  a    /     |               `\
         :`        /      |                 \
    <`-._|`  .-.  (      /   .            `;\\
     `-. `--'_.'-.;\___/'   .      .       | \\
  _     /:--`     |        /     /        .'  \\
 ("\   /`/        |       '     '         /    :`;
 `\'\_/`/         .\     /`~`=-.:        /     ``
   `._.'          /`\    |      `\      /(
                 /  /\   |        `Y   /  \
                J  /  Y  |         |  /`\  \
               /  |   |  |         |  |  |  |
              "---"  /___|        /___|  /__|

              '''

bucket.put_object(
Key = "foo/moo/boo/zoo/animal.txt",
Body= bytes(my_elephant, 'utf-8')

)