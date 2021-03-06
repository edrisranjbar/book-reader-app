# Islamic Book-Reader
book reader application

## Goals
1. Allah's satisfaction
2. Cultralize digital book reading
3. Learn team working
4. CV

## Requirements
- [ ] communication with publishers
- [ ] application designing and implementation
- [ ] publish to app stores
- [ ] get users
- [ ] provide server and it's needies
- [ ] licenses

## Project definition
## UX design
## UI design
## Front-end development
### Initialize Project Structure
### Design system
### Widget Design
### State management
## Back-end development
back-end will be written with dart, and we will call our Rest-ful API to 
interact with Model, and the model will take care of Database.
### Provide database documentation
Data model structure designed in ```wwww.draw.io```, and your access via [this 
link](https://drive.google.com/file/d/1vgvq7cNwpcDk_zDo7BsD71i2DSW-TX6h/view?usp=sharing)
### Create API Models
Here's a list of all different classes which works as model.
<br>
**_note that the Model is neither responsible for Data validation nor 
Authorization; these kinds of processes will be in the Controller side of 
the API._**
1. Admin
<br>
| No | Name          | Parameters                                                                | Description                                                                                                                | return Value |
|----|---------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------|
| 1  | create_table  |                                                                           | if the table does not exists, this method will create it. this is cool for migration and running in different environments | Void         |
| 2  | add           | name:str,<br>email:str,<br>mobile: str                                    | adds a new admin                                                                                                           | Boolean      |
| 3  | update        | admin_id:int,<br>admin_name:str,<br>admin_email:str, <br>admin_mobile:str | updates admin details based on given id                                                                                    | Boolean      |
| 4  | delete        | admin_id:int                                                              | deletes specefic admin based on given id                                                                                   | Boolean      |
| 5  | get_all       |                                                                           | get all admins with their details (id, name, email, mobile)                                                                | List         |
| 6  | exist         | mobile:str                                                                | check if a specific admin with a given mobile exists                                                                       | Boolean      |
| 7  | request_login | mobile:str                                                                | sends a random token to admin mobile and saves that token in redis Key-Value DataBase                                      | Boolean      |
| 8  | verify_login  | mobile:str,<br>user_token:str                                             | check if the given token and mobile are pair                                                                               | Boolean      |
2. User
3. Book
4. Category
5. Publisher
6. Author
7. Translator
8. SMS
9. SMS Token
### Provide API routes
### Write Test API collection
## Test

## App features
- [ ] Authentication & Authentication
- [ ] My library
- [ ] purchase
- [ ] Search
- [ ] Category
- [ ] Book information
- [ ] Discovery Page
- [ ] Open a Book
- [ ] Book Download Management
