from django.urls import path
from . import views

urlpatterns = [
    # for registration to driver
    path('', views.root),
    path('reg', views.reg ,name="reg"),
    path('driver', views.driver),

    # for registration to police
    path('regp', views.police),
    path('police', views.regpolice),

    # for login to User
    path('login', views.login),
    path('signin', views.signin),
    path('policeinfo', views.policeinfo),

    path('addviolation', views.addviolation, name="addviolation"),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('update_violation/<int:id>', views.update_violation, name="update_violation"),

    path('add', views.add_vio, name="add"),
    path('showviolation', views.showviolation, name="showviolation"),

    path('home', views.home),
    path('logout2', views.logout2),
    path('logout', views.logout),
    path('driveredit', views.driveredit),
    path('getviolation', views.getviolation, name="getviolation"),
    path('policeviolation', views.policeviolation),
    path('rule', views.rule),
    path('email',views.email),
    path('send_message',views.send_email),
    path('license',views.licenses),
    path('upload',views.upload)

]
