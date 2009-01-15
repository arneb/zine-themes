from zine.widgets import Widget
from zine.models import Post

class ListPages(Widget):
    """Show a list of static pages."""

    name = 'list_pages'
    template = 'widgets/list_pages.html'

    def __init__(self, show_title=False, ignore_blocked=False):
        self.pages = Post.query.type('page').all()
        self.show_title = show_title
        
        
class MetaInfo(Widget):
    """Show Meta Information."""
    
    name = 'meta_info'
    template = 'widgets/meta.html'
    
    def __init__(self, show_title=False):
        self.show_title = show_title