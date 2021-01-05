instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS post;',
    'DROP TABLE IF EXISTS user;',
    'DROP TABLE IF EXISTS comment;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
        CREATE TABLE user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            rol INT NOT NULL DEFAULT 0
        )
    """,
    """
        CREATE TABLE post (
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            img VARCHAR(250) NOT NULL,
            FOREIGN KEY (created_by) REFERENCES user (id)
        )
    """,
    """
        CREATE TABLE comment (
            id INT PRIMARY KEY AUTO_INCREMENT,
            description TEXT NOT NULL,
            user_id INT NOT NULL,
            post_id INT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user (id),
            FOREIGN KEY (post_id) REFERENCES post (id)
        )
    """    
]