<%page expression_filter="h"/>
<%inherit file="../base.mako" />
      <div id="oc-content-main">

        
  <form class="oc-boxy" name="login_form" method="post" id="oc-login-form" action="/login">
    

    

    <fieldset>
      <h1>Sign in</h1> 
      <table class="oc-form">
        <tbody>
          <tr>
            <th class="oc-form-label" scope="row"><label for="username">Username </label></th>
            <td class="oc-form-value"><input size="15" tabindex="0" name="username" value="" id="username" class="oc-autoFocus" type="text"></td>
            <td class="oc-form-help">
              <span class="oc-form-context"></span>
              <span id="oc-validator-username" class="oc-form-validator"></span>
            </td>
          </tr>
          <tr>
            <th class="oc-form-label" scope="row"><label for="password">Password </label>
            </th>
            <td class="oc-form-value"><input size="15" name="password" id="password" type="password"></td>
            <td class="oc-form-help"> </td>
          </tr>
          <tr class="oc-options">
            <th></th>
            <td class="oc-form-value oc-form-fieldBlock oc-smallText">
              <input class="oc-input-typeCheck" name="no_expire_cookie" id="no_expire_cookie" type="checkbox"> 
              <label for="no_expire_cookie">Keep me logged in</label>
            </td>
            <td class="oc-form-help">
            </td>
          </tr>
          <tr class="oc-actions">
            <th></th>
            <td class="oc-form-value">
              <button class="context" type="submit" name="login:boolean" value="True">Log in</button>
              <!-- onclick="javascript:return setLoginVars('username','login_name','password','pwd_empty','js_enabled','cookies_enabled')" --></td>
            <td class="oc-form-help"></td>
          </tr>
          <!-- 
          <tr class="oc-options">
            <th></th>
            <td>

            </td>
            <td class="oc-form-helpBlock"></td>
          </tr>
          -->
        </tbody>
      </table>
    </fieldset>
  </form>

        
  <div id="ext-gen20" class="oc-js-expander oc-expander">
  <h2 class="oc-bigText"><a id="ext-gen21" class="oc-js-expander_open oc-expanderLink" href="/forgot">Forgot your username or password?</a></h2>
        <form style="position: static; visibility: visible; display: none; left: auto; top: auto; z-index: auto;" class="oc-js-expander-content oc-expander-content" method="post" id="oc-login-form" action="forgot">
          <p class="oc-headingContext">Enter your username or email address to retrieve your login information.</p>
          <table class="oc-form" cellpadding="0" cellspacing="0">
            <thead></thead>
            <tbody>
              <tr>
                <th class="oc-form-label" scope="row">
                  <label for="username">Username or email address</label>
                </th>
                <td class="oc-form-value"><input size="15" tabindex="0" name="username" value="" id="username" class="oc-firstFocus" type="text"></td>
                <td class="oc-form-help">
                  <span class="oc-form-context"></span>
                  <span id="oc-validator-username" class="oc-form-validator"></span>
                </td>
              </tr>
              <tr class="oc-actions">
               <th></th>
                <td>
                  <button type="submit" name="send:boolean" value="True">Send</button></td>
                <td class="oc-form-help"></td>
              </tr>                    
            </tbody>
          </table>
        </form>
  </div>


      </div><!-- end #content-main -->

      <div id="oc-content-sidebar">
        <div class="oc-getstarted">
          <h2>New users</h2>
          <p>Whether your group is mobilizing voters, planning a protest, or growing a garden, OpenPlans can help you become more effective.</p>
          <a href="/join" class="oc-banana">Join OpenPlans</a>
        </div>
      </div><!-- end #content-sidebar -->
