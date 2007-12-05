<html>
<head>

<title>
OpenPlans Login
</title>
</head>

<body>

<!-- This is oc-tasktracker-wrapper so that we only have to edit the 
rules once when we simplify markup -->
<div id="oc-tasktracker-wrapper">
  <div id="oc-statusMessage-container">
%for message in c.status_message:
      <div class="oc-statusMessage oc-js-closeable">${message|n}</div>
%endfor
  </div>

    ${ next.body() }
</div>

</body>
</html>
