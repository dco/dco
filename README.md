### Hi there 👋
<!DOCTYPE html>
<html lang="zh">
  <head>
    <meta charset="UTF-8" />
    <title>amis demo</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge"/>
    <link href="https://cdn.bootcdn.net/ajax/libs/amis/2.6.0/sdk.min.css" rel="stylesheet">
    <link href="https://cdn.bootcdn.net/ajax/libs/amis/2.6.0/helper.min.css" rel="stylesheet">
    <link href="https://cdn.bootcdn.net/ajax/libs/amis/2.6.0/iconfont.min.css" rel="stylesheet">
    <script src="https://cdn.bootcdn.net/ajax/libs/amis/2.6.0/sdk.min.js"></script>
    <style>
      html,
      body,
      .app-wrapper {
        position: relative;
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <div id="root" class="app-wrapper"></div>
    <script type="text/javascript">
      (function () {
        let amis = amisRequire('amis/embed');
        // 通过替换下面这个配置来生成不同页面
        let amisJSON = {
          "type": "app",
          "brandName": "应用名称",
          
          "pages": [
          ]
        };
        let amisScoped = amis.embed('#root', amisJSON);
      })();
    </script>
  </body>
</html>
