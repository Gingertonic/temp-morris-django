Thursday

**Database/Models**
  - [x] Setup database
  - [x] Access admin console
  - [x] Create Category & Item DB models
    + *category has:*
      + code:CharField & pk - exact length 3
      + name:CharField
    + *item has:*
      + auto pk
      + name:CharField
      + quantity:PositiveIntegerField
      + category:ForeignKey _(belongs to Category)_
  - [x] Update views to call models
    + Include basic error handling - 404 if item not found

**Custom Error Handlers**
  - [x] Check user experience of errors out of debug mode
  - [x] Add custom error handlers for 404 & 500


**Testing**
  - [x] Create case for basic views
  - [x] `inventory-how-to`
    + renders inventory/about.html template
  - [x] `inventory-index`
    + response has a context with key of 'items'
    + context 'items' contains 2 elements
  - [x] `show-item` with arg of `2`
    + response has a context with key of `item`
    + context `item` has a key `name` of value `ketchup`
    + context `item` has a key `category` of value `CDT


**Auth**
  Registration
  - [x] Create new app for user management
  - [x] Create registration form extending Django's `UserCreationForm`
  - [x] Add path & view method for `register` 
    + on `GET` request => generate new form, render placeholder html
    + on `POST` request => validates form, adds User to DB, redirects to index
  - [x] Create registration form template, render on `GET register`
  - [x] Try the form! Check for the new user in admin portal

  Login/Logout
  - [x] Add login & logout paths pointing to Django views
  - [x] Create login & logout templates
  - [x] Define redirect path on successful login
  - [x] Show conditional content based on login status

  Protect
  "Only logged-in users can access individual item pages"
  - [x] Define redirect path for non-logged in users
  - [x] Decorate route(s) to be protected

**Custom Forms**
  "All logged-in users can add a food item"
  "Category managers can increase (+1) the quantity of an item"
  - [ ] Create basic NewFoodForm
  - [ ] Add view method for `create`
    + on `GET` request => generate a NewFoodForm, render `new.html`
    + on `POST` request => validates form, adds item to DB, redirects to show page
  - [ ] Complete `new.html`: render form
  - [ ] Update `index.html`: show link to create new item if user logged in
  - [ ] Create basic UpdateQuantityForm
  - [ ] Add manager:CharField to Category model 
  - [ ] Update view method for `show` 
    + on `GET` request => generate a UpdateQuantityForm, pass form in context
    + on `POST` request => validates form, updates item in DB, redirects to show page
  - [ ] Update `show.html`: show button to +1 if user is category manager

**Bonus**
  Many to Many relationship
  "Logged-in users can 'like' an item once"
  - [ ] Add field to Item model of `likes` using ManyToManyField with User
  - [ ] Rerun migrations
  - [ ] Implement a 'like' button on an item show page
  - [ ] Show list of users who have 'liked' the item on the show page
  - [ ] Show a star symbol next to the item in the index if more than 3 people have 'liked' the item
