from extensions import login_manager

from models.tenant import Tenant


@login_manager.user_loader
def load_user(user_id):

    return Tenant.query.get(int(user_id))