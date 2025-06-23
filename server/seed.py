from datetime import date
from app import create_app, db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

def seed_database():
    app = create_app()
    
    with app.app_context():
        
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        
        print("Creating users...")
        admin_user = User(username='admin', password='password123')
        test_user = User(username='testuser', password='test123')
        
        db.session.add(admin_user)
        db.session.add(test_user)
        db.session.commit()
        
        
        print("Creating guests...")
        guests = [
            Guest(name='Jennifer Lawrence', occupation='Actress'),
            Guest(name='Ryan Reynolds', occupation='Actor'),
            Guest(name='Taylor Swift', occupation='Musician'),
            Guest(name='Elon Musk', occupation='Entrepreneur'),
            Guest(name='Stephen King', occupation='Author'),
            Guest(name='Serena Williams', occupation='Tennis Player'),
            Guest(name='Gordon Ramsay', occupation='Chef'),
            Guest(name='Neil deGrasse Tyson', occupation='Astrophysicist')
        ]
        
        for guest in guests:
            db.session.add(guest)
        db.session.commit()
        
        
        print("Creating episodes...")
        episodes = [
            Episode(date=date(2024, 1, 15), number=101),
            Episode(date=date(2024, 1, 22), number=102),
            Episode(date=date(2024, 1, 29), number=103),
            Episode(date=date(2024, 2, 5), number=104),
            Episode(date=date(2024, 2, 12), number=105),
            Episode(date=date(2024, 2, 19), number=106)
        ]
        
        for episode in episodes:
            db.session.add(episode)
        db.session.commit()
        
        
        print("Creating appearances...")
        appearances = [
            Appearance(rating=5, guest_id=1, episode_id=1),  # Jennifer Lawrence
            Appearance(rating=4, guest_id=2, episode_id=1),  # Ryan Reynolds
            Appearance(rating=5, guest_id=3, episode_id=2),  # Taylor Swift
            Appearance(rating=3, guest_id=4, episode_id=2),  # Elon Musk
            Appearance(rating=4, guest_id=5, episode_id=3),  # Stephen King
            Appearance(rating=5, guest_id=6, episode_id=4),  # Serena Williams
            Appearance(rating=4, guest_id=7, episode_id=5),  # Gordon Ramsay
            Appearance(rating=5, guest_id=8, episode_id=6),  # Neil deGrasse Tyson
        ]
        
        for appearance in appearances:
            db.session.add(appearance)
        db.session.commit()
        
        print("Database seeded successfully!")
        print(f"Created {len(guests)} guests")
        print(f"Created {len(episodes)} episodes")
        print(f"Created {len(appearances)} appearances")
        print(f"Created 2 users (admin/password123, testuser/test123)")

if __name__ == '__main__':
    seed_database()