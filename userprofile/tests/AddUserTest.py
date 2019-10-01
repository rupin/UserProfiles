from django.shortcuts import reverse

from rest_framework.test import APITestCase

from userprofile.models.CustomUserModel import CustomUser
from userprofile.models.UserProfileModel import UserProfile
from rest_framework.test import APIClient


class AddUserTest(APITestCase):
    def setUp(self):
        # create User
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(email="user1@test.com", username='user1@test.com',is_staff=True)
        self.user.set_password("password1")
        self.user.save()

        self.client.login(username='user1@test.com',password='password1')        
        addresponse = self.client.post(reverse('adduser'), {
            'username': 'bharti',
            'password':'newpassword',
            'email':'bharti@gmail.com'
        })
        self.assertEqual(201, addresponse.status_code)

        if (addresponse.status_code==201):
            self.newuserid=addresponse.data['id']
        
        self.client.logout() # Logout from Admin Login 

    def test_user_creation_without_login(self):
    	
        # create a standard User
        
        addresponse = self.client.post(reverse('adduser'), {
            'username': 'nilesh',
            'password':'nileshspwd',
            'email':'nilesh@gmail.com'
        })

        
        # Assert 401 because the user is not logged in
        self.assertEqual(401, addresponse.status_code)  

        response = self.client.patch(reverse('updateUser', kwargs={'pk':self.newuserid}), {
            'first_name': 'Bharti',
            'last_name':'Chheda',
            
        })
        self.assertEqual(401, response.status_code)     

        response = self.client.get(reverse('listProfile', kwargs={'userid':self.newuserid}))
        #print(response.data)
        self.assertEqual(401, response.status_code) 

        # Check if standard Login can list Users
        response = self.client.get(reverse('listusers'))
        self.assertEqual(401, response.status_code)

        response = self.client.get(reverse('generatepdf', kwargs={'pk':self.newuserid}))
        self.assertEqual(401, response.status_code)
        
        #Check if User can delete users
        response = self.client.delete(reverse('deleteuser', kwargs={'pk':self.newuserid}))
        self.assertEqual(401, response.status_code)

    def test_with_admin_login(self):


        self.client.login(username='user1@test.com',password='password1')
        
        addresponse = self.client.post(reverse('adduser'), {
            'username': 'nilesh',
            'password':'nileshspwd',
            'email':'nilesh@gmail.com'
        })
        #print(addresponse.data)
        self.assertEqual(201, addresponse.status_code)
        
         # assert new User was added
        self.assertEqual(CustomUser.objects.count(), 3)
        myuser=CustomUser.objects.get(id=self.newuserid)
        #print(myuser.username)

        #assert if profiles were created
        self.assertEqual(UserProfile.objects.filter(user=myuser).count(), 2)

        updateresponse = self.client.patch(reverse('updateUser', kwargs={'pk':self.newuserid}), {
            'first_name': 'Bharti',
            'last_name':'Chheda',
            
        })
        #print(updateresponse)
        self.assertEqual(CustomUser.objects.filter(id=self.newuserid, first_name='Bharti', last_name='Chheda').count(), 1)


        response = self.client.get(reverse('listProfile', kwargs={'userid':self.newuserid}))
        #print(response.data)
        self.assertEqual(200, response.status_code)

        # Check if standard Login can list Users
        response = self.client.get(reverse('listusers'))
        self.assertEqual(200, response.status_code)

        response = self.client.get(reverse('generatepdf', kwargs={'pk':self.newuserid}))
        self.assertEqual(200, response.status_code)

        #Check if User can delete users
        response = self.client.delete(reverse('deleteuser', kwargs={'pk':self.newuserid}))
        self.assertEqual(204, response.status_code)

    def test_with_standard_login(self):

        self.client.login(username='bharti',password='newpassword')
        
        response = self.client.post(reverse('adduser'), {
            'username': 'nilesh',
            'password':'newpassword',
            'email':'nilesh@gmail.com'
        })
        
        self.assertEqual(403, response.status_code)

        #Check if Standard Profile can update users
        response = self.client.patch(reverse('updateUser', kwargs={'pk':self.newuserid}), {
            'first_name': 'Bharti',
            'last_name':'Chheda',
            
        })
        self.assertEqual(403, response.status_code)


        # Check if standard Login can list profiles
        response = self.client.get(reverse('listProfile', kwargs={'userid':self.newuserid}))
        self.assertEqual(403, response.status_code)


        # Check if standard Login can list Users. They can
        response = self.client.get(reverse('listusers'))        
        self.assertEqual(200, response.status_code)

        #Check if User can generate PDF
        response = self.client.get(reverse('generatepdf', kwargs={'pk':self.newuserid}))
        self.assertEqual(403, response.status_code)

        #Check if User can delete another user
        response = self.client.delete(reverse('deleteuser', kwargs={'pk':self.newuserid}))
        self.assertEqual(403, response.status_code)

        


    