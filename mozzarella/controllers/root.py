"""Main Controller"""

from tg import expose, flash, require, url, lurl, abort
from tg import request, redirect, tmpl_context, response
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates, session
from mozzarella import model
from mozzarella.model import DBSession
from tgext.admin.controller import AdminController
from mozzarella.config.app_cfg import AdminConfig

from mozzarella.model import Meeting, Survey, Banner

from mozzarella.lib.base import BaseController
from mozzarella.controllers.error import ErrorController

from mozzarella.controllers.mailinglist import MailingListController
from mozzarella.controllers.contact import ContactController
from mozzarella.controllers.user import UsersController
from mozzarella.controllers.meeting import MeetingsController
from mozzarella.controllers.schedule import ScheduleController
from mozzarella.controllers.survey import SurveysController
from mozzarella.controllers.project import ProjectsController
from mozzarella.controllers.presentations import PresentationsController
from mozzarella.controllers.research import ResearchController

from sqlalchemy.sql import functions

import datetime

__all__ = ['RootController']

class RootController(BaseController):
    """
    The root controller for Mozzarella.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    admin = AdminController(model, DBSession, config_type=AdminConfig)
    mailinglist = MailingListController()
    u = UsersController()
    m = MeetingsController()
    s = SurveysController()
    schedule = ScheduleController()
    error = ErrorController()
    contact = ContactController()
    projects = ProjectsController()
    presentations = PresentationsController()
    research = ResearchController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "Mozzarella"

    @expose('mozzarella.templates.index')
    def index(self):
        """Handle the front-page."""
        meetings = DBSession.query(Meeting).filter(
            Meeting.date > datetime.datetime.now() - datetime.timedelta(hours=3)
        ).order_by(Meeting.date).limit(2)
        banner = DBSession.query(Banner).order_by(functions.random()).first()
        return dict(page='index', meetings=meetings, banner=banner)

    @expose('mozzarella.templates.login')
    def login(self, came_from=lurl('/'), failure=None, login=''):
        """login(came_from=tg.lurl('/'), failure=None, login='')

        Start the user login."""
        if failure is not None:
            if failure == 'user-not-found':
                flash(_('User not found'), 'error')
            elif failure == 'invalid-password':
                flash(_('Invalid Password'), 'error')

        login_counter = request.environ.get('repoze.who.logins', 0)
        if failure is None and login_counter > 0:
            flash(_('Wrong credentials'), 'warning')

        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from, login=login)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """post_login(came_from=tg.lurl('/'))

        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.
        """
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                     params=dict(came_from=came_from, __logins=login_counter))
        user = request.identity['user']
        flash(_('Welcome back, %s!') % user.display_name)

        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """post_logout(came_from=tg.lurl('/'))

        Redirect the user to the initially requested page on logout and say
        goodbye as well.
        """
        flash(_('We hope to see you soon!'))
        return HTTPFound(location=came_from)

    @expose()
    def toggle_theme(self):
        if session.get('theme', None) == 'dark':
            session['theme'] = 'light'
        else:
            session['theme'] = 'dark'
        session.save()
        return session.get('theme', None)

    @expose()
    def attend(self):
        meeting = DBSession.query(Meeting)\
                           .join(Meeting.survey)\
                           .filter(
                               Survey.opens < datetime.datetime.now()
                           ).order_by(Meeting.date.desc()).first()

        if meeting and meeting.survey.active:
            redirect('s/{}/respond'.format(meeting.survey.id))
        else:
            abort(404, 'No active meeting')
