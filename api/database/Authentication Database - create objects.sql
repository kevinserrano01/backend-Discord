CREATE DATABASE discord_app;
USE discord_app;

CREATE TABLE user_status (
  status_id INT AUTO_INCREMENT PRIMARY KEY,
  status_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE user_roles (
  role_id INT AUTO_INCREMENT PRIMARY KEY,
  role_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  date_of_birth DATE,
  phone_number VARCHAR(15),
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_login TIMESTAMP,
  status_id INT,
  role_id INT,
  CONSTRAINT fk_users_status_id FOREIGN KEY (status_id) REFERENCES user_status(status_id),
  CONSTRAINT fk_users_role_id FOREIGN KEY (role_id) REFERENCES user_roles(role_id)
);