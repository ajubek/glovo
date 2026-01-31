"""
Django data population script - main.py
Run this file directly: python main.py
"""

import os
import sys
import django

# Add the mysite directory to Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'mysite'))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysit.settings')

# Initialize Django BEFORE importing models
django.setup()

# NOW we can safely import models
from glovo_app.models import (
    UserProfile, Category, Contact,
    CourierProduct, Store, Address,
    StoreMenu, Product, Order, Review
)
import random


def create_users():
    """Create clients, owners, and couriers"""
    print('Creating users...')
    users = {
        'clients': [],
        'owners': [],
        'couriers': []
    }

    # Clients
    clients_data = [
        ('Aibek', 'Sultanov', '+996700123456', 'aibek.sultanov'),
        ('Maria', 'Ivanova', '+996700234567', 'maria.ivanova'),
        ('Nurlan', 'Asanov', '+996700345678', 'nurlan.asanov'),
        ('Elena', 'Petrova', '+996700456789', 'elena.petrova'),
        ('Bektur', 'Toktomushev', '+996700567890', 'bektur.tokto'),
        ('Olga', 'Sidorova', '+996700678901', 'olga.sidorova'),
        ('Azamat', 'Karimov', '+996700789012', 'azamat.karimov'),
    ]

    for first, last, phone, username in clients_data:
        user, created = UserProfile.objects.get_or_create(
            username=username,
            defaults={
                'first_name': first,
                'last_name': last,
                'phone_number': phone,
                'role': 'client',
                'email': f'{username}@example.com',
            }
        )
        if created:
            user.set_password('password123')
            user.save()
        users['clients'].append(user)

    # Owners
    owners_data = [
        ('Murat', 'Bekov', '+996555123456', 'murat.bekov'),
        ('Svetlana', 'Kim', '+996555234567', 'svetlana.kim'),
        ('Timur', 'Abdullaev', '+996555345678', 'timur.abdullaev'),
        ('Natasha', 'Romanova', '+996555456789', 'natasha.romanova'),
        ('Daniyar', 'Kasymov', '+996555567890', 'daniyar.kasymov'),
        ('Irina', 'Volkova', '+996555678901', 'irina.volkova'),
        ('Erlan', 'Jumabayev', '+996555789012', 'erlan.jumabayev'),
    ]

    for first, last, phone, username in owners_data:
        user, created = UserProfile.objects.get_or_create(
            username=username,
            defaults={
                'first_name': first,
                'last_name': last,
                'phone_number': phone,
                'role': 'owner',
                'email': f'{username}@example.com',
            }
        )
        if created:
            user.set_password('password123')
            user.save()
        users['owners'].append(user)

    # Couriers
    couriers_data = [
        ('Alibek', 'Mamytov', '+996770123456', 'alibek.courier'),
        ('Dmitry', 'Sokolov', '+996770234567', 'dmitry.courier'),
        ('Akyl', 'Bakirov', '+996770345678', 'akyl.courier'),
        ('Ivan', 'Morozov', '+996770456789', 'ivan.courier'),
        ('Altynbek', 'Osmonov', '+996770567890', 'altynbek.courier'),
        ('Sergey', 'Lebedev', '+996770678901', 'sergey.courier'),
    ]

    for first, last, phone, username in couriers_data:
        user, created = UserProfile.objects.get_or_create(
            username=username,
            defaults={
                'first_name': first,
                'last_name': last,
                'phone_number': phone,
                'role': 'courier',
                'email': f'{username}@example.com',
            }
        )
        if created:
            user.set_password('password123')
            user.save()
        users['couriers'].append(user)

    return users


def create_categories():
    """Create food categories with multilingual names"""
    print('Creating categories...')
    categories_data = [
        {
            'category_name_en': 'Restaurants',
            'category_name_ru': 'Рестораны',
            'category_name_ky': 'Ресторандар'
        },
        {
            'category_name_en': 'Fast Food',
            'category_name_ru': 'Фастфуд',
            'category_name_ky': 'Тез тамак'
        },
        {
            'category_name_en': 'Cafes',
            'category_name_ru': 'Кафе',
            'category_name_ky': 'Кафелер'
        },
        {
            'category_name_en': 'Bakery',
            'category_name_ru': 'Пекарня',
            'category_name_ky': 'Нан пышыруу жайы'
        },
        {
            'category_name_en': 'Grocery',
            'category_name_ru': 'Продукты',
            'category_name_ky': 'Азык-түлүк'
        },
        {
            'category_name_en': 'Desserts',
            'category_name_ru': 'Десерты',
            'category_name_ky': 'Таттуулар'
        },
        {
            'category_name_en': 'Asian Cuisine',
            'category_name_ru': 'Азиатская кухня',
            'category_name_ky': 'Азия тамагы'
        },
    ]

    categories = []
    for data in categories_data:
        category, created = Category.objects.get_or_create(
            category_name=data['category_name_en'],
            defaults=data
        )
        categories.append(category)

    return categories


def create_stores(categories, owners):
    """Create stores with multilingual data"""
    print('Creating stores...')
    stores_data = [
        {
            'category': categories[0],
            'owner': owners[0],
            'store_name_en': 'Silk Road Restaurant',
            'store_name_ru': 'Ресторан Шелковый Путь',
            'store_name_ky': 'Жибек Жолу ресторану',
            'description_en': 'Traditional Kyrgyz and Central Asian cuisine with modern twist',
            'description_ru': 'Традиционная кыргызская и центральноазиатская кухня с современным подходом',
            'description_ky': 'Традициялык кыргыз жана Борбор Азия тамагы заманбап стилде',
        },
        {
            'category': categories[1],
            'owner': owners[1],
            'store_name_en': 'Burger King Bishkek',
            'store_name_ru': 'Бургер Кинг Бишкек',
            'store_name_ky': 'Бургер Кинг Бишкек',
            'description_en': 'Best burgers and fries in town. Fast delivery guaranteed!',
            'description_ru': 'Лучшие бургеры и картофель фри в городе. Быстрая доставка гарантирована!',
            'description_ky': 'Шаардагы эң мыкты бургерлер жана картошка. Тез жеткирүү кепилденет!',
        },
        {
            'category': categories[2],
            'owner': owners[2],
            'store_name_en': 'Coffee Time',
            'store_name_ru': 'Время Кофе',
            'store_name_ky': 'Кофе убактысы',
            'description_en': 'Cozy cafe with specialty coffee and fresh pastries',
            'description_ru': 'Уютное кафе с авторским кофе и свежей выпечкой',
            'description_ky': 'Атайын кофе жана жаңы печенье менен ыңгайлуу кафе',
        },
        {
            'category': categories[3],
            'owner': owners[3],
            'store_name_en': 'Golden Crust Bakery',
            'store_name_ru': 'Пекарня Золотая Корочка',
            'store_name_ky': 'Алтын кабык нан пышыруу жайы',
            'description_en': 'Fresh bread and pastries baked daily',
            'description_ru': 'Свежий хлеб и выпечка каждый день',
            'description_ky': 'Күн сайын жаңы нан жана печенье',
        },
        {
            'category': categories[4],
            'owner': owners[4],
            'store_name_en': 'Fresh Market',
            'store_name_ru': 'Свежий Рынок',
            'store_name_ky': 'Жаңы базар',
            'description_en': 'Quality groceries delivered to your door',
            'description_ru': 'Качественные продукты с доставкой до двери',
            'description_ky': 'Сапаттуу азык-түлүк эшигиңизге жеткирилет',
        },
        {
            'category': categories[5],
            'owner': owners[5],
            'store_name_en': 'Sweet Dreams',
            'store_name_ru': 'Сладкие Мечты',
            'store_name_ky': 'Таттуу түштөр',
            'description_en': 'Handmade cakes, ice cream and desserts',
            'description_ru': 'Торты ручной работы, мороженое и десерты',
            'description_ky': 'Колдон жасалган торттор, балмуздак жана таттуулар',
        },
        {
            'category': categories[6],
            'owner': owners[6],
            'store_name_en': 'Tokyo Sushi Bar',
            'store_name_ru': 'Токио Суши Бар',
            'store_name_ky': 'Токио Суши Бар',
            'description_en': 'Authentic Japanese cuisine and sushi',
            'description_ru': 'Аутентичная японская кухня и суши',
            'description_ky': 'Түп япон тамагы жана суши',
        },
    ]

    stores = []
    for data in stores_data:
        store, created = Store.objects.get_or_create(
            store_name=data['store_name_en'],
            defaults=data
        )
        stores.append(store)

    return stores


def create_contacts_and_addresses(stores):
    """Create contacts and addresses for stores"""
    print('Creating contacts and addresses...')

    addresses_data = [
        ('Chuy Avenue 123', 'пр. Чуй 123', 'Чүй проспекти 123'),
        ('Manas Street 45', 'ул. Манас 45', 'Манас көчөсү 45'),
        ('Moskovskaya Street 78', 'ул. Московская 78', 'Москва көчөсү 78'),
        ('Erkindik Boulevard 90', 'бул. Эркиндик 90', 'Эркиндик бульвары 90'),
        ('Ibraimov Street 12', 'ул. Ибраимова 12', 'Ибраимов көчөсү 12'),
        ('Toktogul Street 156', 'ул. Токтогул 156', 'Токтогул көчөсү 156'),
        ('Kievskaya Street 201', 'ул. Киевская 201', 'Киев көчөсү 201'),
    ]

    contact_names = [
        ('Manager', 'Менеджер', 'Башкаруучу'),
        ('Reception', 'Ресепшн', 'Кабыл алуу'),
        ('Orders', 'Заказы', 'Буйрутмалар'),
        ('Support', 'Поддержка', 'Колдоо'),
        ('Administrator', 'Администратор', 'Администратор'),
        ('Service', 'Сервис', 'Кызмат'),
        ('Info Line', 'Инфолиния', 'Маалымат линиясы'),
    ]

    phones = [
        '+996312123456',
        '+996312234567',
        '+996312345678',
        '+996312456789',
        '+996312567890',
        '+996312678901',
        '+996312789012',
    ]

    for i, store in enumerate(stores):
        Contact.objects.get_or_create(
            store=store,
            defaults={
                'contact_name_en': contact_names[i][0],
                'contact_name_ru': contact_names[i][1],
                'contact_name_ky': contact_names[i][2],
                'contact_number': phones[i]
            }
        )

        Address.objects.get_or_create(
            store=store,
            defaults={
                'address_name_en': addresses_data[i][0],
                'address_name_ru': addresses_data[i][1],
                'address_name_ky': addresses_data[i][2]
            }
        )


def create_menus_and_products(stores):
    """Create menus and products for stores"""
    print('Creating menus and products...')
    all_products = []

    # Silk Road Restaurant
    menu1, _ = StoreMenu.objects.get_or_create(
        store=stores[0],
        menu_name='Main Menu',
        defaults={
            'menu_name_en': 'Main Menu',
            'menu_name_ru': 'Основное меню',
            'menu_name_ky': 'Негизги меню'
        }
    )

    products_data = [
        {
            'menu': menu1,
            'name': 'Beshbarmak',
            'desc_en': 'Traditional Kyrgyz dish with boiled meat and noodles',
            'desc_ru': 'Традиционное кыргызское блюдо с вареным мясом и лапшой',
            'desc_ky': 'Бышырылган эт жана кеспе менен традициялык кыргыз тамагы',
            'price': 450,
        },
        {
            'menu': menu1,
            'name': 'Lagman',
            'desc_en': 'Hand-pulled noodles with vegetables and meat',
            'desc_ru': 'Лапша ручной работы с овощами и мясом',
            'desc_ky': 'Колдон жасалган кеспе жашылча жана эт менен',
            'price': 350,
        },
        {
            'menu': menu1,
            'name': 'Plov',
            'desc_en': 'Central Asian rice pilaf with lamb and vegetables',
            'desc_ru': 'Среднеазиатский плов с бараниной и овощами',
            'desc_ky': 'Борбор Азия палобу кой эти жана жашылча менен',
            'price': 400,
        },
    ]

    for prod_data in products_data:
        product, _ = Product.objects.get_or_create(
            store_menu=prod_data['menu'],
            product_name=prod_data['name'],
            defaults={
                'product_descriptions_en': prod_data['desc_en'],
                'product_descriptions_ru': prod_data['desc_ru'],
                'product_descriptions_ky': prod_data['desc_ky'],
                'price': prod_data['price'],
                'quantity': random.randint(10, 50)
            }
        )
        all_products.append(product)

    # Burger King
    menu2, _ = StoreMenu.objects.get_or_create(
        store=stores[1],
        menu_name='Burgers & Sides',
        defaults={
            'menu_name_en': 'Burgers & Sides',
            'menu_name_ru': 'Бургеры и гарниры',
            'menu_name_ky': 'Бургерлер жана гарнирлер'
        }
    )

    products_data2 = [
        {
            'menu': menu2,
            'name': 'Whopper',
            'desc_en': 'Flame-grilled beef burger with fresh vegetables',
            'desc_ru': 'Говяжий бургер на гриле со свежими овощами',
            'desc_ky': 'Гриль менен жаңы жашылча менен уй эт бургер',
            'price': 280,
        },
        {
            'menu': menu2,
            'name': 'Chicken Royale',
            'desc_en': 'Crispy chicken burger with special sauce',
            'desc_ru': 'Хрустящий куриный бургер со специальным соусом',
            'desc_ky': 'Атайын соус менен кытырлап тоок бургер',
            'price': 250,
        },
    ]

    for prod_data in products_data2:
        product, _ = Product.objects.get_or_create(
            store_menu=prod_data['menu'],
            product_name=prod_data['name'],
            defaults={
                'product_descriptions_en': prod_data['desc_en'],
                'product_descriptions_ru': prod_data['desc_ru'],
                'product_descriptions_ky': prod_data['desc_ky'],
                'price': prod_data['price'],
                'quantity': random.randint(20, 100)
            }
        )
        all_products.append(product)

    return all_products


def create_orders(clients, couriers, products):
    """Create orders"""
    print('Creating orders...')
    orders = []

    addresses = [
        'Микрорайон 7, дом 12, кв. 45',
        'ул. Манаса 78, офис 301',
        'пр. Чуй 156, квартира 89',
        'Джал, ул. Ленина 34',
        'Ак-Орго, 5 мкр, дом 7',
        'ул. Киевская 90, кв. 12',
        'бул. Эркиндик 234',
    ]

    statuses = ['pending', 'pending', 'pending', 'delivered', 'delivered', 'canceled', 'pending']

    for i in range(min(7, len(clients))):
        order, _ = Order.objects.get_or_create(
            client=clients[i],
            products=random.choice(products),
            defaults={
                'status': statuses[i],
                'delivery_address': addresses[i],
                'courier': random.choice(couriers)
            }
        )
        orders.append(order)

    return orders


def create_reviews(clients, stores):
    """Create reviews for stores"""
    print('Creating reviews...')

    reviews_data = [
        {'client': 0, 'store': 0, 'rating': 5, 'text': 'Excellent food and fast delivery!'},
        {'client': 1, 'store': 1, 'rating': 4, 'text': 'Good burgers, but delivery was slow.'},
        {'client': 2, 'store': 2, 'rating': 5, 'text': 'Best coffee in Bishkek!'},
        {'client': 3, 'store': 5, 'rating': 5, 'text': 'Amazing cakes!'},
        {'client': 4, 'store': 6, 'rating': 4, 'text': 'Fresh sushi, good quality.'},
    ]

    for data in reviews_data:
        if data['client'] < len(clients) and data['store'] < len(stores):
            Review.objects.get_or_create(
                client=clients[data['client']],
                store=stores[data['store']].owner,  # Bug workaround
                defaults={
                    'rating': data['rating'],
                    'text': data['text']
                }
            )


def main():
    """Main function to populate database"""
    print('=' * 50)
    print('🚀 Starting data population...')
    print('=' * 50)

    # Create data
    users = create_users()
    categories = create_categories()
    stores = create_stores(categories, users['owners'])
    create_contacts_and_addresses(stores)
    products = create_menus_and_products(stores)
    orders = create_orders(users['clients'], users['couriers'], products)
    create_reviews(users['clients'], stores)

    # Print summary
    print('\n' + '=' * 50)
    print('✅ DATA POPULATION COMPLETED!')
    print('=' * 50)
    print(f'👥 Users: {UserProfile.objects.count()}')
    print(f'   - Clients: {UserProfile.objects.filter(role="client").count()}')
    print(f'   - Owners: {UserProfile.objects.filter(role="owner").count()}')
    print(f'   - Couriers: {UserProfile.objects.filter(role="courier").count()}')
    print(f'📁 Categories: {Category.objects.count()}')
    print(f'🏪 Stores: {Store.objects.count()}')
    print(f'📞 Contacts: {Contact.objects.count()}')
    print(f'📍 Addresses: {Address.objects.count()}')
    print(f'📋 Menus: {StoreMenu.objects.count()}')
    print(f'🍽️  Products: {Product.objects.count()}')
    print(f'📦 Orders: {Order.objects.count()}')
    print(f'⭐ Reviews: {Review.objects.count()}')
    print('=' * 50)
    print('\n✨ All data created successfully!')
    print('Login credentials: username/password123')
    print('=' * 50)


if __name__ == '__main__':
    main()