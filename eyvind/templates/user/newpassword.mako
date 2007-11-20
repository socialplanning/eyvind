<%page expression_filter="h"/>
<%inherit file="../base.mako" />

<div id="oc-content-main">
  
  <form id="oc-join-form" class="oc-boxy"
        name="pwreset_action" method="post"
        action="/reset-password">
    <fieldset>
      <h1>
        Enter a new password
      </h1>

      <input type="hidden" name="key"
             value="${c.key}" />
      <table class="oc-form">
        <tbody>
          <tr class="oc-fieldBlock">
            <th class="oc-form-label" scope="row">
              <label for="userid">Username</label>
            </th>
            <td class="oc-form-value">

              <input name="userid" size="15" />
            </td>
            <td class="oc-form-help">
            </td>
          </tr>
          <tr class="oc-fieldBlock">
            <th class="oc-form-label" scope="row">
              <label for="password">New password</label>

            </th>
            <td class="oc-form-value">
              <input type="password" id="password"
                     name="password" size="15" />
            </td>
            <td class="oc-form-help">
            </td>
          </tr>
          <tr class="oc-fieldBlock">
            <th class="oc-form-label" scope="row">

              <label for="confirm">Confirm password</label>
            </th>
            <td class="oc-form-value">
              <input type="password" id="password2"
                     name="password2" size="15" />
            </td>
            <td class="oc-form-help">
            </td>
          </tr>

          <tr class="oc-actions">
            <th></th>
            <td class="oc-form-value">
            <button class="context" type="submit" name="set:boolean" value="True">Reset password</button>
            </td>
          </tr>
        </tbody>
      </table>

      <input type="hidden" name="form.submitted" value="1" />
    </fieldset>
  </form>
</div>