<%page expression_filter="h"/>
<%inherit file="../base.mako" />
<%def name="title()">
    ${c.username} on Openplans
</%def>
<%
active_memberships = []
invitations = []
requested_memberships = []
for membership in c.user.memberships:
	if membership.rejected:
		continue
	if membership.is_pending:
		if membership.is_invite:
			invitations.append(membership)
		else:
			requested_memberships.append(membership)
	else:
		active_memberships.append(membership)
%>
          <div>

<div class="oc-headingBlock">
  <h1>Your account</h1>
  <p class="oc-headingContext">View and manage your project memberships and account settings.</p>
</div>
  
<div id="oc-content-main">
  
  <div id="updates_widget"
       class="oc-widget oc-widget-invite">
        <form name="invitation-form" action="account">
% for invitation in invitations:
<% project_name = invitation.project.uri %>
            <li class="oc-invite oc-boxy oc-clearAfter"
                id="${project_name}_invitation">
              <div class="oc-avatar">
                <!-- XXX is this the project avatar? proj admin avatar? -->
                <img src="" />
              </div>
              <p class="oc-invite-content">
                
                ${invitation.inviter.username} has invited you to become a member of <a href="/projects/${project_name}">${invitation.project.title}</a>
              </p>

              <ul class="oc-actions oc-invite-actions oc-actionClose">
                <li>
                  <a href="/people/${c.username}/account?task|${project_name}|AcceptInvitation=Accept"
                     class="oc-actionLink oc-js-actionLink oc-chooseAccept">Accept</a>
                </li>
                <li>
                  <a href="/people/${c.username}/account?task|${project_name}|DenyInvitation=Deny"
                     class="oc-actionLink oc-js-actionLink oc-chooseDeny">Deny</a>
                </li>
              </ul>

            </li>
%endfor          
        </form>    
    
    
  </div><!-- end .widget-invitations -->
  
  
<%include file="projects.mako" />
    <!-- XXX -->
    

  


</div><!-- end #oc-content-main -->

<div id="oc-content-sidebar">
  <div class="oc-boxy">
    <h2>Account settings</h2>

    <a href="profile-edit">Edit profile</a>
    <form class="oc-js-expander" action="account">
      <fieldset>
        <legend class="oc-legend-label">
          <a href="#" class="oc-js-expander_open oc-expanderLink">Change email</a>
        </legend>
        <ul class="oc-js-expander-content oc-expander-content oc-plainList">
          <li>

            <label for="email">Email</label><br />
            <input type="text" id="email" name="email"
                   value="${c.user.email}" />
          </li>
          
          <li>
            <input type="submit" value="Change" name="task|change-email" class="oc-button oc-chooseThis" />  or <a href="#" class="oc-js-expander_close">Cancel</a>
          </li>
        </ul>

      </fieldset>
    </form>
    <form class="oc-js-expander oc-expander" action="account" method="post">
      <fieldset>
        <legend class="oc-legend-label">
          <a href="#" class="oc-js-expander_open oc-expanderLink">Change password</a>
        </legend>
        <ul class="oc-js-expander-content oc-expander-content oc-plainList">

          <li>
            <label for="passwd_curr">Current password</label><br />
            <input type="password" id="passwd_curr" name="passwd_curr" />
          </li>
          <li>
            <label for="passwd_new">New password</label><br />
            <input type="password" id="password" name="password" />
          </li>

          <li>
            <label for="passwd_new_confirm">Confirm new password</label><br />
            <input type="password" id="password2" name="password2" />
          </li>
          <li>
            <input type="submit" value="Change" name="task|change-password" class="oc-button oc-chooseThis" /> or <a href="#" class="oc-js-expander_close">Cancel</a>
          </li>

        </ul>
      </fieldset>
    </form>
  </div>
  
  <div class="oc-plainList oc-boxy">
    <p><strong>What does it mean to be &ldquo;listed&rdquo; on a project?</strong></p>
    <p>For your privacy, you can choose whether or not to be publicly listed as a member of a project.</p>

    <p>If you choose not to be listed then only fellow team members can see your affiliation. Those who are not members of the project will not see you listed in the team roster, nor will they see the project listed anywhere on your profile.</p>
    <p>However, any updates you make on a publicly viewable project could still display your username and a link to your profile.</p>
  </div>
  
</div><!-- end #oc-content-sidebar -->


  </div>