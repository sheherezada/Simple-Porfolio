from django.urls import path

from PROJECT.web.views import tutorials, price, IndexView, DashboardView, CreateQuoteView, about_me, success, careers, \
    PortfolioView, \
    portfolio_item, download, contact

urlpatterns = [
    path('', IndexView.as_view(), name='show index'),
    path('quotes/', CreateQuoteView.as_view(), name='quotes'),
    path('tutorials/', tutorials, name='tutorials'),
    path('contact/', contact, name='contact'),
    path('price/', price, name='price'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('about-me/', about_me, name='about me'),
    path('sent/', success, name='success'),
    path('careers/', careers, name='careers'),
    path('portfolio/', PortfolioView.as_view(), name="portfolio"),
    path('portfolio-item/', portfolio_item, name='portfolio item'),
    path('download/', download, name='download'),

]
