(function(Navigo, window) {
  // Event class to publish/subscribe to events
  const Events = (function() {
    // The event class itself
    class Events {
      // Event class constructor
      constructor() {
        // Contains the events being subscribed to
        this.events = {};
      }
      
      // Subscribes to 'eventName' and uses 'callback' function when the event occurs
      on(eventName, callback) {
        this.events[eventName] = this.events[eventName] || [];
        this.events[eventName].push(callback);
      }
      
      // Unsubscribes to 'eventName'
      off(eventName, callback) {
        if(this.events[eventName]) {
          let eventsLength = this.events[eventName].length;
          
          for(let i=0; i < eventsLength; i++) {
            if(this.events[eventName][i] === callback) {
              this.events[eventName].splice(i, 1);
              break;
            }
          }
        }
      }
      
      // Emits 'eventName' with 'data' so any subscribers to the event can call their callbacks
      emit(eventName, data) {
        if(this.events[eventName]) {
          this.events[eventName].forEach(callback => callback(data));
        }
      }
    }
    
    // Return a new instance of the event class (singleton)
    return new Events();
  })();
  
  // Router class extends Navigo for client-side routing
  const Router = (function(Navigo, root, useHash, hash) {
    // Extending the Navigo class with our own router class
    class Router extends Navigo {
      constructor(root, useHash, hash) {
        super(root, useHash, hash);
      }
      
      // Enable setting routes with assignment
      set routes(routes) {
        routes = routes || {};
        this.on(routes);
        this.resolve();
      }
    }
    
    // Return a new instance of the Router class (singleton)
    return new Router(root, useHash, hash);
  })(Navigo, null, true, '#!');
  
  // The model serves as our gatekeeper for all shop data
  const Model = (function() {
    // Our product data (ideally, you would get this information from a database)
    const products = [{"id":1,"name":"Web Dev 101","short_desc":"Get started learning web development with the most comprehensive course ever written! 40+ hours of HTML, CSS, and JavaScript.","long_desc":"<p>Get started learning web development with the most comprehensive course ever written! 40+ hours of HTML, CSS, and JavaScript.</p><p>Spicy jalapeno bacon ipsum dolor amet frankfurter strip steak venison, jowl shank turkey burgdoggen turducken. Jerky tongue porchetta landjaeger beef ribs. Pancetta salami chicken venison flank andouille, ham hock turducken bresaola hamburger brisket. Filet mignon shank bresaola leberkas flank burgdoggen boudin sirloin pork. T-bone brisket chicken, flank hamburger pork chop venison tenderloin porchetta tail bresaola picanha ham hock.</p><p>Bresaola andouille landjaeger leberkas biltong turkey meatball tail frankfurter salami ham hock. Pork turkey frankfurter meatball. Pig short ribs sirloin shank. T-bone sirloin shoulder cupim burgdoggen. Ham hock short loin tri-tip filet mignon tenderloin t-bone shoulder hamburger chuck shank.</p><p>Picanha ball tip tail pork pork loin, spare ribs cow pancetta cupim. Capicola ground round ham hock t-bone, picanha spare ribs beef rump landjaeger bacon chicken brisket. Tail porchetta t-bone biltong beef ribs bacon doner pork belly. Ribeye tail flank brisket fatback tenderloin beef ribs bacon tongue.</p>","price":99,"image":"https://images.pexels.com/photos/326424/pexels-photo-326424.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb"},{"id":2,"name":"Coffee 'n Code","short_desc":"I'll bring you coffee and then we can code together!","long_desc":"<p>I'll bring you coffee and then we can code together!</p><p>Spicy jalapeno bacon ipsum dolor amet frankfurter strip steak venison, jowl shank turkey burgdoggen turducken. Jerky tongue porchetta landjaeger beef ribs. Pancetta salami chicken venison flank andouille, ham hock turducken bresaola hamburger brisket. Filet mignon shank bresaola leberkas flank burgdoggen boudin sirloin pork. T-bone brisket chicken, flank hamburger pork chop venison tenderloin porchetta tail bresaola picanha ham hock.</p><p>Bresaola andouille landjaeger leberkas biltong turkey meatball tail frankfurter salami ham hock. Pork turkey frankfurter meatball. Pig short ribs sirloin shank. T-bone sirloin shoulder cupim burgdoggen. Ham hock short loin tri-tip filet mignon tenderloin t-bone shoulder hamburger chuck shank.</p><p>Picanha ball tip tail pork pork loin, spare ribs cow pancetta cupim. Capicola ground round ham hock t-bone, picanha spare ribs beef rump landjaeger bacon chicken brisket. Tail porchetta t-bone biltong beef ribs bacon doner pork belly. Ribeye tail flank brisket fatback tenderloin beef ribs bacon tongue.</p>","price":349,"image":"https://images.pexels.com/photos/414584/pexels-photo-414584.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb"},{"id":3,"name":"Learn JavaScript","short_desc":"Take your web development to the next level! Go beyond the fundamentals with 40+ hours of lessons and 30 projects.","long_desc":"<p>Take your web development to the next level! Go beyond the fundamentals with 40+ hours of lessons and 30 projects.</p><p>Spicy jalapeno bacon ipsum dolor amet frankfurter strip steak venison, jowl shank turkey burgdoggen turducken. Jerky tongue porchetta landjaeger beef ribs. Pancetta salami chicken venison flank andouille, ham hock turducken bresaola hamburger brisket. Filet mignon shank bresaola leberkas flank burgdoggen boudin sirloin pork. T-bone brisket chicken, flank hamburger pork chop venison tenderloin porchetta tail bresaola picanha ham hock.</p><p>Bresaola andouille landjaeger leberkas biltong turkey meatball tail frankfurter salami ham hock. Pork turkey frankfurter meatball. Pig short ribs sirloin shank. T-bone sirloin shoulder cupim burgdoggen. Ham hock short loin tri-tip filet mignon tenderloin t-bone shoulder hamburger chuck shank.</p><p>Picanha ball tip tail pork pork loin, spare ribs cow pancetta cupim. Capicola ground round ham hock t-bone, picanha spare ribs beef rump landjaeger bacon chicken brisket. Tail porchetta t-bone biltong beef ribs bacon doner pork belly. Ribeye tail flank brisket fatback tenderloin beef ribs bacon tongue.</p>","price":149,"image":"https://images.pexels.com/photos/360591/pexels-photo-360591.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb"},{"id":4,"name":"NodeJS + React","short_desc":"Continue on your journey to become a fullstack web developer by learning NodeJS and React. 25+ hours of lessons and 5 projects.","long_desc":"<p>Continue on your journey to become a fullstack web developer by learning NodeJS and React. 25+ hours of lessons and 5 projects.</p><p>Spicy jalapeno bacon ipsum dolor amet frankfurter strip steak venison, jowl shank turkey burgdoggen turducken. Jerky tongue porchetta landjaeger beef ribs. Pancetta salami chicken venison flank andouille, ham hock turducken bresaola hamburger brisket. Filet mignon shank bresaola leberkas flank burgdoggen boudin sirloin pork. T-bone brisket chicken, flank hamburger pork chop venison tenderloin porchetta tail bresaola picanha ham hock.</p><p>Bresaola andouille landjaeger leberkas biltong turkey meatball tail frankfurter salami ham hock. Pork turkey frankfurter meatball. Pig short ribs sirloin shank. T-bone sirloin shoulder cupim burgdoggen. Ham hock short loin tri-tip filet mignon tenderloin t-bone shoulder hamburger chuck shank.</p><p>Picanha ball tip tail pork pork loin, spare ribs cow pancetta cupim. Capicola ground round ham hock t-bone, picanha spare ribs beef rump landjaeger bacon chicken brisket. Tail porchetta t-bone biltong beef ribs bacon doner pork belly. Ribeye tail flank brisket fatback tenderloin beef ribs bacon tongue.</p>","price":199,"image":"https://images.pexels.com/photos/34676/pexels-photo.jpg?w=1260&h=750&auto=compress&cs=tinysrgb"}];
    
    // The shopping cart
    let cart = [];
    
    // Returns an array of products
    const getProducts = () => {
      return [...products];
    };
    
    // Checks for a product with 'id' and returns it
    const getProductById = id => {
      id = +id || null;
      return (id) ? products.filter(item => item.id === id)[0] : null;
    };
    
    // Returns the shopping cart (array of product id's)
    const getCart = () => {
      return [...cart];
    };
    
    // Used to add or remove an item from the shopping cart
    const modifyCart = (method, id) => {
      // Adding an item
      if(method === 'add') {
        // Check the the item they want to add is actually a shop item
        if(cart.indexOf(id) === -1) {
          // Push the item into the shopping cart
          cart.push(id);
          
          // Update the localStorage with the new cart
          localStorage.setItem('cart', JSON.stringify({items: getCart()}));
          
          // Emit an event to let everyone know the cart was updated
          Events.emit('cartupdated', getCart());
          
          return true;
        }
        
      // Removing an item
      } else if(method === 'remove') {
        // Check if the item they want to add is actually a shop item
        if(cart.indexOf(id) !== -1) {
          // Remove the item from the cart
          cart.splice(cart.indexOf(id), 1);
          
          // Update the localStorage with the new cart
          localStorage.setItem('cart', JSON.stringify({items: getCart()}));
          
          // Emit an event to let everyone know the cart was updated
          Events.emit('cartupdated', getCart());
          
          return true;
        }
      }
      
      return false;
    };
    
    // Initializes the shopping cart
    const initCart = () => {
      // Check if localStorage is available
      if('localStorage' in window) {
        // Get the cart stored in localStorage
        let storedCart = JSON.parse(localStorage.getItem('cart'));
        
        // Did we find an existing cart?
        if(storedCart) {
          // Cool, set the stored cart equal to our app cart
          cart = storedCart.items;
        } else {
          // Otherwise, create a new localStorage item for our cart
          localStorage.setItem('cart', JSON.stringify({items: getCart()}));
        }
      }
      
      // Tell everyone we've updated the cart
      Events.emit('cartupdated', getCart());
    };
    
    return {
      getCart,
      modifyCart,
      initCart,
      getProducts,
      getProductById
    }
  })();
  
  // Various helpers and utility functions
  const utils = (function(window) {
    // Hides content
    const hideContent = contentEl => {
      return new Promise((resolve, reject) => {
        contentEl.classList.add('hide');
        
        window.setTimeout(() => {
          resolve();
        }, 350);
      })
    };
    
    // Shows content
    const showContent = contentEl => {
      return new Promise((resolve, reject) => {
        contentEl.classList.remove('hide');
        
        window.setTimeout(() => {
          resolve();
        }, 350);
      });
    };
    
    // Sets the active navigation item
    const setActiveNavItem = (nav, params) => {
      nav.forEach(li => li.classList.remove('active'));

      if(params === null) {
        nav[1].classList.add('active');
      } else if(params === '' || params === undefined) {
        nav[0].classList.add('active');
      }
    };
    
    // Removes all children from a parent node
    const removeAllChildren = parent => {
      return new Promise((resolve, reject) => {
        while(parent.firstChild) {
          parent.removeChild(parent.firstChild);
        }
        resolve();
      });
    };
    
    // Paul Irish's solution to cross-browser requestAnimationFrame
    // This is used to scroll the page to the top after navigating
    const requestAnimFrame = (function(){
      return  window.requestAnimationFrame       ||
              window.webkitRequestAnimationFrame ||
              window.mozRequestAnimationFrame    ||
              function( callback ){
                window.setTimeout(callback, 1000 / 60);
              };
    })();
    
    // Scrolls the page to the top after navigating
    const scrollToY = (scrollTargetY, speed, easing) => {
      scrollTargetY = scrollTargetY || 0;
      speed = speed || 2000;
      easing = easing || 'easeOutSine';
      
      const scrollY = window.scrollY || document.documentElement.scrollTop;
      
      let currentTime = 0;
      let time = Math.max(.1, Math.min(Math.abs(scrollY - scrollTargetY) / speed, .8));
      
      const easingEquations = {
        easeOutSine: pos => {
          return Math.sin(pos * (Math.PI / 2));
        },
        easeInOutSine: pos => {
          return (-0.5 * (Math.cos(Math.PI * pos) - 1));
        },
        easeInOutQuint: pos => {
          if ((pos /= 0.5) < 1) {
            return 0.5 * Math.pow(pos, 5);
          }
          return 0.5 * (Math.pow((pos - 2), 5) + 2);
        }
      };

      const tick = () => {
        currentTime += 1 / 60;
        
        const p = currentTime / time;
        const t = easingEquations[easing](p);
        
        if (p < 1) {
          requestAnimFrame(tick);
          window.scrollTo(0, scrollY + ((scrollTargetY - scrollY) * t));
        } else {
          window.scrollTo(0, scrollTargetY);
        }
      }

      tick();
    };
    
    return {
      hideContent,
      setActiveNavItem,
      showContent,
      scrollToY,
      removeAllChildren
    };
  })(window);
  
  // Handles the rendering and interactions with the shop and shopping cart
  const Shop = (function() {
    // Shopping Cart class
    class ShoppingCart {
      // Class constructor binds events and initializes the shopping cart
      constructor() {
        this._bindEvents();
        Model.initCart();
      }
      
      // Updates the shopping cart instance when the cart changes
      _bindEvents() {
        Events.on('cartupdated', cart => {
          this.cartItems = cart;
          this._updateCartNav(cart.length);
        });
      }
      
      // Updates the shopping cart navigation when the cart changes
      _updateCartNav(numItems) {
        const itemCount = document.getElementById('itemCount');
        itemCount.textContent = numItems;
      }
      
      // Returns the cart items
      get items() {
        return this.cartItems;
      }
      
      // Removes an item from the cart
      removeItem(id) {
        Model.modifyCart('remove', id);
      }
      
      // Adds an item to the cart
      addItem(id) {
        Model.modifyCart('add', parseInt(id));
      }
    }
    
    // Shop class
    class Shop {
      // Shop constructor gets shop products and shopping cart
      constructor() {
        this.products = Model.getProducts();
        this.cart = new ShoppingCart();
        
        this.handleProductItemClick = this.handleProductItemClick.bind(this);
        this.handleAddToCartClick = this.handleAddToCartClick.bind(this);
      }
      
      // Public method to loads a single product
      loadProduct(id) {
        return this._loadSingleProduct(id);
      }
      
      // Loads a product list item
      _loadProductListItem(item, index) {
        const fragment = document.createDocumentFragment();
        const div = document.createElement('div');

        // Shop item container
        const li = document.createElement('li');
        li.setAttribute('id', `item-${item.id}`);
        li.classList.add('item');
        li.setAttribute('tabindex', index);

        // Shop item image
        const img = document.createElement('img');
        img.setAttribute('src', item.image);
        img.onload = function() {
          li.appendChild(this);
        };

        // Create the item details container
        const itemDetails = div.cloneNode(true);
        itemDetails.classList.add('item-details');

        // Create the item title container
        const itemTitle = div.cloneNode(true);
        itemTitle.classList.add('item-title');

        // Create the title
        const h3 = document.createElement('h3');
        h3.appendChild(document.createTextNode(item.name));
        itemTitle.appendChild(h3);

        // Create the button
        const button = document.createElement('button');
        button.classList.add('add-to-cart');
        if(this.cart.items.indexOf(item.id) !== -1) {
          button.innerHTML = '&check;';
        } else {
          button.appendChild(document.createTextNode(`$${item.price}`));
        }
        
        itemTitle.appendChild(button);

        // Create the item description container
        const itemDescription = div.cloneNode(true);
        itemDescription.classList.add('item-description');

        // Create the description
        const p = document.createElement('p');
        p.appendChild(document.createTextNode(item.short_desc));
        itemDescription.appendChild(p);

        // Append the children to the item
        itemDetails.appendChild(itemTitle);
        itemDetails.appendChild(itemDescription);
        li.appendChild(itemDetails);
        fragment.appendChild(li);

        return fragment;
      }
      
      // Loads a single product
      _loadSingleProduct(id) {
        const product = Model.getProductById(id);
        const productFragment = document.createDocumentFragment();
        const div = document.createElement('div');
        
        const productWrapper = div.cloneNode(true);
        productWrapper.classList.add('product');
        
        const productBody = div.cloneNode(true);
        productBody.classList.add('product-body');
        
        const imgWrapper = div.cloneNode(true);
        imgWrapper.classList.add('product-image');
        
        const productDescription = div.cloneNode(true);
        productDescription.classList.add('product-desc');
        
        const title = document.createElement('h2');
        title.appendChild(document.createTextNode(product.name));
        productWrapper.appendChild(title);
        
        const img = document.createElement('img');
        img.setAttribute('src', product.image);
        
        const btn = document.createElement('button');
        btn.classList.add('add-to-cart');
        
        if(this.cart.items.indexOf(product.id) !== -1) {
          btn.innerHTML = '&check;';
        } else {
          btn.appendChild(document.createTextNode(`$${product.price}`));
        }
        
        imgWrapper.appendChild(img);
        imgWrapper.appendChild(btn);
        productBody.appendChild(imgWrapper);
        
        // This is just me being lazy... meh
        productDescription.innerHTML = `${product.long_desc}`;
        
        productBody.appendChild(productDescription);
        productWrapper.appendChild(productBody);
        productFragment.appendChild(productWrapper);
        
        return productFragment;
      }
      
      // Handles Product item click events
      handleProductItemClick(e) {
        const productsList = e.currentTarget;
        const target = e.target;

        if(target !== productsList) {
          let product = target;
          while(product.nodeName !== 'LI') {
            product = product.parentNode;
          }
          const productID = parseInt(product.id.split('-')[1], 10);

          if(target.nodeName === 'BUTTON') {
            this.cart.addItem(productID);
            target.innerHTML = '&check;';
          } else {
            Router.navigate(`/products/${productID}`);
          }
        }

        e.stopPropagation();
      }
      
      // Handles add to cart click events
      handleAddToCartClick(target, itemID) {
        this.cart.addItem(itemID);
        target.innerHTML = '&check;';
      }
      
      // Renders the shopping cart
      renderCart() {
        const cartFragment = document.createDocumentFragment();
        const button = document.createElement('button');
        const li = document.createElement('li');
        const span = document.createElement('span');
        const p = document.createElement('p');
        
        const cartTitle = document.createElement('h2');
        cartTitle.textContent = 'My Cart';
        cartFragment.appendChild(cartTitle);
        
        if(this.cart.items.length <= 0) {
          const para = p.cloneNode(true);
          para.textContent = 'It\'s sad and lonely here...';
          cartFragment.appendChild(para);
        } else {
          const cartItems = document.createElement('ul');
          cartItems.classList.add('cart-items');
          let total = 0;
          
          this.cart.items.forEach(itemID => {
            const item = Model.getProductById(itemID);
            total += item.price;
            
            const itemRow = li.cloneNode(true);
            itemRow.setAttribute('id', `item-${item.id}`);
            itemRow.classList.add('cart-item');
            
            const itemTitle = span.cloneNode(true);
            itemTitle.classList.add('cart-item-name');
            itemTitle.textContent = `${item.name}`;
            
            const itemPrice = span.cloneNode(true);
            itemPrice.classList.add('cart-item-price');
            itemPrice.textContent = `$${item.price}`;
            
            const removeBtn = button.cloneNode(true);
            removeBtn.classList.add('remove-item');
            
            itemRow.appendChild(removeBtn);
            itemRow.appendChild(itemTitle);
            itemRow.appendChild(itemPrice);
            cartItems.appendChild(itemRow);
          });
          
          cartFragment.appendChild(cartItems);
          
          const totalPrice = p.cloneNode(true);
          totalPrice.classList.add('cart-total');
          totalPrice.textContent = `TOTAL: $${total}`;
          cartFragment.appendChild(totalPrice);
        }
        
        return cartFragment;
      }
      
      // Renders the default product list
      render() {
        const elementsFragment = document.createDocumentFragment();
        const productsFragment = document.createDocumentFragment();

        const title = document.createElement('h2');
        title.appendChild( document.createTextNode('Web Development Courses') );
        elementsFragment.appendChild(title);

        const ul = document.createElement('ul');
        ul.setAttribute('id', 'shopItems');
        ul.classList.add('item-list');

        this.products.forEach((item, index) => {
          productsFragment.appendChild(this._loadProductListItem(item, index));
        });

        ul.appendChild(productsFragment);
        elementsFragment.appendChild(ul);

        return elementsFragment;
      }
    }
    
    return new Shop();
  })();
  
  // Components for rendering each separate page
  const Pages = (MOUNT_NODE) => {
    const HomePage = () => {
      class HomePage {
        render() {
          MOUNT_NODE.appendChild(Shop.render());
          
          const shopItems = MOUNT_NODE.querySelector('#shopItems');
          if(shopItems.onclick !== undefined) {
            shopItems.addEventListener('click', Shop.handleProductItemClick, false);
          }
        }
      }
      
      return new HomePage().render();
    };

    const ProductPage = (params, query) => {
      class ProductPage {
        render(params, query) {
          MOUNT_NODE.appendChild(Shop.loadProduct(params.id));
          
          const button = document.querySelectorAll('.add-to-cart')[0];
          button.addEventListener('click', e => Shop.handleAddToCartClick(e.target, params.id), false);
        }
      }
      
      new ProductPage().render(params, query);
    };

    const CartPage = () => {
      class CartPage {
        render() {
          MOUNT_NODE.appendChild(Shop.renderCart());
          
          const cartItems = document.querySelectorAll('.cart-items')[0];
          if(cartItems) {
            cartItems.addEventListener('click', e => {
              const productsList = e.currentTarget;
              const target = e.target;

              if(target !== productsList) {
                let product = target;
                while(product.nodeName !== 'LI') {
                  product = product.parentNode;
                }
                const productID = parseInt(product.id.split('-')[1], 10);

                if(target.nodeName === 'BUTTON') {
                  Shop.cart.removeItem(productID);
                  if(Shop.cart.items.length > 0) {
                    const cartTotal = document.querySelectorAll('.cart-total')[0];

                    productsList.removeChild(product);

                    let total = 0;
                    Shop.cart.items.forEach(id => {
                      const item = Model.getProductById(id);
                      total += item.price;
                    });
                    cartTotal.textContent = `TOTAL: $${total}`;
                  } else {
                    Router.navigate('/');
                  }
                } else if(target.className === 'cart-item-name') {
                  Router.navigate(`/products/${productID}`);
                }
              }

              e.stopPropagation();
            }, false);
          }
        }
      }
      
      new CartPage().render();
    };
    
    return {
      HomePage,
      ProductPage,
      CartPage
    };
  };
  
  // Initializes the application
  const init = () => {
    const MOUNT_NODE = document.getElementById('content');
    const NAV = document.querySelectorAll('.nav ul > li');
    
    // Defines the application routes
    Router.routes = {
      '/products/:id': Pages(MOUNT_NODE).ProductPage,
      '/': Pages(MOUNT_NODE).HomePage,
      '/cart': Pages(MOUNT_NODE).CartPage
    };
    
    // Defines the application hooks
    Router.hooks({
      'before': (done, params) => {
        utils.setActiveNavItem(NAV, params);
        
        utils.hideContent(MOUNT_NODE).then(() => {
          return utils.removeAllChildren(MOUNT_NODE);
        }).then(done);
      },
      'after': (done) => {
        utils.scrollToY(0, 1500, 'easeInOutQuint');
        utils.showContent(MOUNT_NODE).then(done);
      }
    });
  };
  
  // Fire away
  window.addEventListener('load', init, false);
})(Navigo, window);