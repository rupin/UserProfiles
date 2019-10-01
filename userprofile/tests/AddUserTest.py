# from django.shortcuts import reverse

# from rest_framework.test import APITestCase

# from userprofile.models.CustomUserModel import CustomUser


# class AddUserTest(APITestCase):
#     def setUp(self):
#         # create movie
#         self.user = CustomUser(first_name='Rupin', last_name='chheda', username='rupin', password='twinklestar', is_superuser=True, is_staff=True, is_active=True)
#         self.user.save()

#     def test_add_user_creation(self):
#         print(reverse('adduser'))
#         response = self.client.post(reverse('adduser'), {
#             'username': 'bharti',
#             'password':'newpassword',
#             'email':'bharti@gmail.com'
#         })

       

#         # Assert 401 because the user is not logged in
#         self.assertEqual(401, response.status_code)



        
#         #get Authentication token
#         self.client.headers.update({"Content-Type":"application/x-www-form-urlencoded"})
#         response = self.client.post('/api/auth/login/', {
#             'username': 'rupin',
#             'password':'twinklestar',
            
#         })

#         self.assertEqual(200, response.status_code)
#         print(response)



#         #self.client.headers.update({'Authorization': 'Token '+})



#         response = self.client.post(reverse('adduser'), {
#             'username': 'bharti',
#             'password':'newpassword',
#             'email':'bharti@gmail.com'
#         })

#          # assert new movie was added
#         self.assertEqual(CustomUser.objects.count(), 2)

#     # def test_getting_movies(self):
#     #     response = self.client.get(reverse('movies'), format="json")
#     #     self.assertEqual(len(response.data), 1)

#     # def test_updating_movie(self):
#     #     response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
#     #         'name': 'The Space Between Us updated',
#     #         'year_of_release': 2017
#     #     }, format="json")

#     #     # check info returned has the update
#     #     self.assertEqual('The Space Between Us updated', response.data['name'])

#     # def test_deleting_movie(self):
#     #     response = self.client.delete(reverse('detail', kwargs={'pk': 1}))

#     #     self.assertEqual(204, response.status_code)