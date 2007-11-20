<%page expression_filter="h"/>
<%inherit file="../base.mako" />

          <!-- content is injected here -->
          <div>
      <div id="oc-content-main">
        <!-- join form -->
        <form target="" id="oc-join-form" name="edit_form" class="oc-boxy" method="post" action="/join">
          <fieldset>

            <h1>Join OpenPlans</h1>

            <p>
Registration is free and your email will not be shared with anyone,
however, you will need to confirm your email address in order to avoid
spam bots abusing this system. </p>

            <!-- on successful registration -->
            

            <table class="oc-form">
              <thead></thead>
              <tbody>
            
                <tr class="oc-form-row">
                  <th class="oc-form-label">
                    <label for=username>Username</label>
                  </th>
                  <td class="oc-form-value">
                    <input name=username id=username class="oc-autoFocus oc-js-liveValidate" type="text">
                  </td>
                  <td class="oc-form-help">
                    <span class="oc-form-context">
                      
                    </span>
                    <span id="oc-username-validator" class="oc-form-validator">
                      
                    </span>
                    <span id="oc-username-error" class="oc-form-error"><form:error name="username"/></span>
                  </td>           
                </tr>

                <tr>
                  <th class="oc-form-label">
                    <label for="fullname">Full Name</label>
                  </th>
                  <td class="oc-form-value">
                    <input name="fullname" id="fullname" class="" type="text">
                  </td>
                  <td class="oc-form-help">
                    <span class="oc-form-context">
                      (optional)
                    </span>
                    <span id="oc-fullname-validator" class="oc-form-validator">
                      
                    </span>
                    <span id="oc-fullname-error" class="oc-form-error"></span>
                  </td>
                </tr>

                <tr>
                  <th class="oc-form-label">
                    <label for="email">Email</label>
                  </th>
                  <td class="oc-form-value">
                    <input name="email" id="email" type="text">
                  </td>
                  <td class="oc-form-help">
                    <span class="oc-form-context">
                      
                    </span>
                    <span id="oc-email-validator" class="oc-form-validator">
                      
                    </span>
                    <span style="visibility: visible;" id="oc-email-error" class="oc-form-error"><form:error name="email"/></span>
                  </td>
                </tr>

                <tr>
                  <th class="oc-form-label">
                    <label for="password">Password</label>
                  </th>
                  <td class="oc-form-value">
                    <input name="password" id="password" class="" type="password">
                  </td>
                  <td class="oc-form-help">
                    <span class="oc-form-context">
                      
                    </span>
                    <span id="oc-password-validator" class="oc-form-validator">
                      
                    </span>
                    <span id="oc-password-error" class="oc-form-error"></span>
                    <span style="visibility: visible;" id="oc-email-error" class="oc-form-error"><form:error name="password"/></span>
                  </td>
                </tr>
                
                <tr>
                  <th class="oc-form-label">
                    <label for="confirm_password">Confirm passsword</label>
                  </th>
                  <td class="oc-form-value">
                    <input name="confirm_password" id="confirm_password" type="password">  
                  </td>
                  <td class="oc-form-help">
                    <span class="oc-form-context">
                      
                    </span>
                    <span id="oc-confirm_password-validator" class="oc-form-validator">
                      
                    </span>
                    <span id="oc-confirm_password-error" class="oc-form-error"><form:error name="confirm_password"/></span>
                  </td>
                </tr>

                <tr class="oc-actions">
                  <th class="oc-form-label">
                  </th>
                  <td class="oc-form-value">
                    <input name="task|join" value="Join" type="submit">
                  </td>
                  <td class="oc-form-help">
                    <span class="oc-form-context">
                      
                    </span>
                    <span class="oc-form-validator">
                      
                    </span>
                  </td>
                </tr>
                
              </tbody>
            </table>            
          </fieldset>
          
        </form>
      </div><!-- end #oc-content-main -->
      
      <div id="oc-content-sidebar">
        <div class="oc-boxy">
          <h2>Already a member?</h2>
          <a href="/user/login">Sign in</a>
        </div>
      </div><!-- end #oc-content-sidebar -->

    </div>