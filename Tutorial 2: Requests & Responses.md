## Requests & Responses

[http://www.django-rest-framework.org/tutorial/2-requests-and-responses](http://www.django-rest-framework.org/tutorial/2-requests-and-responses)

```
$ http http://127.0.0.1:8000/snippets/
HTTP/1.0 200 OK
Allow: POST, OPTIONS, GET
Content-Length: 199
Content-Type: application/json
Date: Wed, 18 Oct 2017 11:54:34 GMT
Server: WSGIServer/0.1 Python/2.7.12
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "code": "foo = \"bar\"\n",
        "id": 1,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    },
    {
        "code": "foo = \"bar\"",
        "id": 2,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    }
]

$ http http://127.0.0.1:8000/snippets/ Accept:application/json
HTTP/1.0 200 OK
Allow: POST, OPTIONS, GET
Content-Length: 199
Content-Type: application/json
Date: Wed, 18 Oct 2017 11:55:26 GMT
Server: WSGIServer/0.1 Python/2.7.12
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "code": "foo = \"bar\"\n",
        "id": 1,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    },
    {
        "code": "foo = \"bar\"",
        "id": 2,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    }
]

$ http http://127.0.0.1:8000/snippets/ Accept:text/html
HTTP/1.0 200 OK
Allow: POST, OPTIONS, GET
Content-Length: 7376
Content-Type: text/html; charset=utf-8
Date: Wed, 18 Oct 2017 11:55:52 GMT
Server: WSGIServer/0.1 Python/2.7.12
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

<!DOCTYPE html>
<html>
  <head>



        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="robots" content="NONE,NOARCHIVE" />


      <title>Snippet List – Django REST framework</title>



          <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/bootstrap.min.css"/>
          <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/bootstrap-tweaks.css"/>


        <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/prettify.css"/>
        <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/default.css"/>



  </head>


  <body class="">

    <div class="wrapper">

        <div class="navbar navbar-static-top navbar-inverse"
             role="navigation" aria-label="navbar">
          <div class="container">
            <span>

                <a class='navbar-brand' rel="nofollow" href='http://www.django-rest-framework.org'>
                    Django REST framework
                </a>

            </span>
            <ul class="nav navbar-nav pull-right">


                  <li><a href='/api-auth/login/?next=/snippets/'>Log in</a></li>


            </ul>
          </div>
        </div>


      <div class="container">

          <ul class="breadcrumb">


                <li class="active"><a href="/snippets/">Snippet List</a></li>


          </ul>


        <!-- Content -->
        <div id="content" role="main" aria-label="content">


          <div class="region"  aria-label="request form">

            <form id="get-form" class="pull-right">
              <fieldset>

                  <div class="btn-group format-selection">
                    <a class="btn btn-primary js-tooltip" href="/snippets/" rel="nofollow" title="Make a GET request on the Snippet List resource">GET</a>

                    <button class="btn btn-primary dropdown-toggle js-tooltip" data-toggle="dropdown" title="Specify a format for the GET request">
                      <span class="caret"></span>
                    </button>
                    <ul class="dropdown-menu">

                        <li>
                          <a class="js-tooltip format-option" href="/snippets/?format=json" rel="nofollow" title="Make a GET request on the Snippet List resource with the format set to `json`">json</a>
                        </li>

                        <li>
                          <a class="js-tooltip format-option" href="/snippets/?format=api" rel="nofollow" title="Make a GET request on the Snippet List resource with the format set to `api`">api</a>
                        </li>

                    </ul>
                  </div>

              </fieldset>
            </form>



            <form class="button-form" action="/snippets/" data-method="OPTIONS">
              <button class="btn btn-primary js-tooltip" title="Make an OPTIONS request on the Snippet List resource">OPTIONS</button>
            </form>





          </div>

            <div class="content-main" role="main"  aria-label="main content">
              <div class="page-header">
                <h1>Snippet List</h1>
              </div>
              <div style="float:left">

                  <p>List all code snippets, or create a new snippet.</p>

              </div>



              <div class="request-info" style="clear: both" aria-label="request info">
                <pre class="prettyprint"><b>GET</b> /snippets/</pre>
              </div>

              <div class="response-info" aria-label="response info">
                <pre class="prettyprint"><span class="meta nocode"><b>HTTP 200 OK</b>
<b>Allow:</b> <span class="lit">POST, OPTIONS, GET</span>
<b>Content-Type:</b> <span class="lit">application/json</span>
<b>Vary:</b> <span class="lit">Accept</span>

</span>[
    {
        &quot;id&quot;: 1,
        &quot;title&quot;: &quot;&quot;,
        &quot;code&quot;: &quot;foo = \&quot;bar\&quot;\n&quot;,
        &quot;linenos&quot;: false,
        &quot;language&quot;: &quot;python&quot;,
        &quot;style&quot;: &quot;friendly&quot;
    },
    {
        &quot;id&quot;: 2,
        &quot;title&quot;: &quot;&quot;,
        &quot;code&quot;: &quot;foo = \&quot;bar\&quot;&quot;,
        &quot;linenos&quot;: false,
        &quot;language&quot;: &quot;python&quot;,
        &quot;style&quot;: &quot;friendly&quot;
    }
]</pre>
              </div>
            </div>



                <div >


                  <div class="well tab-content">


                    <div  id="post-generic-content-form">

                        <form action="/snippets/" method="POST" class="form-horizontal">
                          <fieldset>



  <div class="form-group">
    <label for="id__content_type" class="col-sm-2 control-label">Media type:</label>
    <div class="col-sm-10">
      <select name="_content_type" data-override="content-type" id="id__content_type" class="form-control">
  <option value="application/json" selected>application/json</option>

  <option value="application/x-www-form-urlencoded">application/x-www-form-urlencoded</option>

  <option value="multipart/form-data">multipart/form-data</option>

</select>
      <span class="help-block"></span>
    </div>
  </div>

  <div class="form-group">
    <label for="id__content" class="col-sm-2 control-label">Content:</label>
    <div class="col-sm-10">
      <textarea name="_content" data-override="content" rows="10" cols="40" id="id__content" class="form-control">
</textarea>
      <span class="help-block"></span>
    </div>
  </div>


                            <div class="form-actions">
                              <button class="btn btn-primary" title="Make a POST request on the Snippet List resource">POST</button>
                            </div>
                          </fieldset>
                        </form>

                    </div>
                  </div>
                </div>





        </div><!-- /.content -->
      </div><!-- /.container -->
    </div><!-- ./wrapper -->




      <script>
        window.drf = {
          csrfHeaderName: "X-CSRFTOKEN",
          csrfCookieName: "csrftoken"
        };
      </script>
      <script src="/static/rest_framework/js/jquery-1.12.4.min.js"></script>
      <script src="/static/rest_framework/js/ajax-form.js"></script>
      <script src="/static/rest_framework/js/csrf.js"></script>
      <script src="/static/rest_framework/js/bootstrap.min.js"></script>
      <script src="/static/rest_framework/js/prettify-min.js"></script>
      <script src="/static/rest_framework/js/default.js"></script>
      <script>
        $(document).ready(function() {
          $('form').ajaxForm();
        });
      </script>


  </body>

</html>
```

```
$ http http://127.0.0.1:8000/snippets.json
HTTP/1.0 200 OK
Allow: POST, OPTIONS, GET
Content-Length: 199
Content-Type: application/json
Date: Wed, 18 Oct 2017 12:01:06 GMT
Server: WSGIServer/0.1 Python/2.7.12
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "code": "foo = \"bar\"\n",
        "id": 1,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    },
    {
        "code": "foo = \"bar\"",
        "id": 2,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    }
]

$ http http://127.0.0.1:8000/snippets.api
HTTP/1.0 200 OK
Allow: POST, OPTIONS, GET
Content-Length: 7400
Content-Type: text/html; charset=utf-8
Date: Wed, 18 Oct 2017 12:01:21 GMT
Server: WSGIServer/0.1 Python/2.7.12
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

<!DOCTYPE html>
<html>
  <head>



        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="robots" content="NONE,NOARCHIVE" />


      <title>Snippet List – Django REST framework</title>



          <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/bootstrap.min.css"/>
          <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/bootstrap-tweaks.css"/>


        <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/prettify.css"/>
        <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/default.css"/>



  </head>


  <body class="">

    <div class="wrapper">

        <div class="navbar navbar-static-top navbar-inverse"
             role="navigation" aria-label="navbar">
          <div class="container">
            <span>

                <a class='navbar-brand' rel="nofollow" href='http://www.django-rest-framework.org'>
                    Django REST framework
                </a>

            </span>
            <ul class="nav navbar-nav pull-right">


                  <li><a href='/api-auth/login/?next=/snippets.api'>Log in</a></li>


            </ul>
          </div>
        </div>


      <div class="container">

          <ul class="breadcrumb">


                <li class="active"><a href="/snippets.api">Snippet List</a></li>


          </ul>


        <!-- Content -->
        <div id="content" role="main" aria-label="content">


          <div class="region"  aria-label="request form">

            <form id="get-form" class="pull-right">
              <fieldset>

                  <div class="btn-group format-selection">
                    <a class="btn btn-primary js-tooltip" href="/snippets.api" rel="nofollow" title="Make a GET request on the Snippet List resource">GET</a>

                    <button class="btn btn-primary dropdown-toggle js-tooltip" data-toggle="dropdown" title="Specify a format for the GET request">
                      <span class="caret"></span>
                    </button>
                    <ul class="dropdown-menu">

                        <li>
                          <a class="js-tooltip format-option" href="/snippets.api?format=json" rel="nofollow" title="Make a GET request on the Snippet List resource with the format set to `json`">json</a>
                        </li>

                        <li>
                          <a class="js-tooltip format-option" href="/snippets.api?format=api" rel="nofollow" title="Make a GET request on the Snippet List resource with the format set to `api`">api</a>
                        </li>

                    </ul>
                  </div>

              </fieldset>
            </form>



            <form class="button-form" action="/snippets.api" data-method="OPTIONS">
              <button class="btn btn-primary js-tooltip" title="Make an OPTIONS request on the Snippet List resource">OPTIONS</button>
            </form>





          </div>

            <div class="content-main" role="main"  aria-label="main content">
              <div class="page-header">
                <h1>Snippet List</h1>
              </div>
              <div style="float:left">

                  <p>List all code snippets, or create a new snippet.</p>

              </div>



              <div class="request-info" style="clear: both" aria-label="request info">
                <pre class="prettyprint"><b>GET</b> /snippets.api</pre>
              </div>

              <div class="response-info" aria-label="response info">
                <pre class="prettyprint"><span class="meta nocode"><b>HTTP 200 OK</b>
<b>Allow:</b> <span class="lit">POST, OPTIONS, GET</span>
<b>Content-Type:</b> <span class="lit">application/json</span>
<b>Vary:</b> <span class="lit">Accept</span>

</span>[
    {
        &quot;id&quot;: 1,
        &quot;title&quot;: &quot;&quot;,
        &quot;code&quot;: &quot;foo = \&quot;bar\&quot;\n&quot;,
        &quot;linenos&quot;: false,
        &quot;language&quot;: &quot;python&quot;,
        &quot;style&quot;: &quot;friendly&quot;
    },
    {
        &quot;id&quot;: 2,
        &quot;title&quot;: &quot;&quot;,
        &quot;code&quot;: &quot;foo = \&quot;bar\&quot;&quot;,
        &quot;linenos&quot;: false,
        &quot;language&quot;: &quot;python&quot;,
        &quot;style&quot;: &quot;friendly&quot;
    }
]</pre>
              </div>
            </div>



                <div >


                  <div class="well tab-content">


                    <div  id="post-generic-content-form">

                        <form action="/snippets.api" method="POST" class="form-horizontal">
                          <fieldset>



  <div class="form-group">
    <label for="id__content_type" class="col-sm-2 control-label">Media type:</label>
    <div class="col-sm-10">
      <select name="_content_type" data-override="content-type" id="id__content_type" class="form-control">
  <option value="application/json" selected>application/json</option>

  <option value="application/x-www-form-urlencoded">application/x-www-form-urlencoded</option>

  <option value="multipart/form-data">multipart/form-data</option>

</select>
      <span class="help-block"></span>
    </div>
  </div>

  <div class="form-group">
    <label for="id__content" class="col-sm-2 control-label">Content:</label>
    <div class="col-sm-10">
      <textarea name="_content" data-override="content" rows="10" cols="40" id="id__content" class="form-control">
</textarea>
      <span class="help-block"></span>
    </div>
  </div>


                            <div class="form-actions">
                              <button class="btn btn-primary" title="Make a POST request on the Snippet List resource">POST</button>
                            </div>
                          </fieldset>
                        </form>

                    </div>
                  </div>
                </div>





        </div><!-- /.content -->
      </div><!-- /.container -->
    </div><!-- ./wrapper -->




      <script>
        window.drf = {
          csrfHeaderName: "X-CSRFTOKEN",
          csrfCookieName: "csrftoken"
        };
      </script>
      <script src="/static/rest_framework/js/jquery-1.12.4.min.js"></script>
      <script src="/static/rest_framework/js/ajax-form.js"></script>
      <script src="/static/rest_framework/js/csrf.js"></script>
      <script src="/static/rest_framework/js/bootstrap.min.js"></script>
      <script src="/static/rest_framework/js/prettify-min.js"></script>
      <script src="/static/rest_framework/js/default.js"></script>
      <script>
        $(document).ready(function() {
          $('form').ajaxForm();
        });
      </script>


  </body>

</html>
```

```
$ http --form POST http://127.0.0.1:8000/snippets/ code="print 123"
HTTP/1.0 201 Created
Allow: POST, OPTIONS, GET
Content-Length: 93
Content-Type: application/json
Date: Wed, 18 Oct 2017 12:02:41 GMT
Server: WSGIServer/0.1 Python/2.7.12
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "code": "print 123",
    "id": 3,
    "language": "python",
    "linenos": false,
    "style": "friendly",
    "title": ""
}

$ http --json POST http://127.0.0.1:8000/snippets/ code="print 456"
HTTP/1.0 201 Created
Allow: POST, OPTIONS, GET
Content-Length: 93
Content-Type: application/json
Date: Wed, 18 Oct 2017 12:03:01 GMT
Server: WSGIServer/0.1 Python/2.7.12
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "code": "print 456",
    "id": 4,
    "language": "python",
    "linenos": false,
    "style": "friendly",
    "title": ""
}
```

