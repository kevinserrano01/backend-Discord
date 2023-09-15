-- Insert Example Data into User Status Table
INSERT INTO user_status (status_name) VALUES ('active');
INSERT INTO user_status (status_name) VALUES ('suspended');
INSERT INTO user_status (status_name) VALUES ('deactivated');

-- Insert Example Data into User Roles Table
INSERT INTO user_roles (role_name) VALUES ('user');
INSERT INTO user_roles (role_name) VALUES ('admin');

-- Insert Example Data into Users Table
-- Insert a user with status 'active' and role 'user'
INSERT INTO users (
  username, password, email, first_name, last_name, date_of_birth, phone_number, status_id, role_id
) VALUES (
  'john_doe', 'john123', 'john.doe@example.com', 'John', 'Doe', '1990-01-01', '123-456-7890', 1, 1
);

-- Insert an admin with status 'active' and role 'admin'
INSERT INTO users (
  username, password, email, first_name, last_name, date_of_birth, phone_number, status_id, role_id
) VALUES (
  'admin_user', 'admin123', 'admin@example.com', 'Admin', 'User', '1985-05-05', '555-555-5555', 1, 2
);

INSERT INTO users (
  username, password, email, first_name, last_name, date_of_birth, phone_number, status_id, role_id
) VALUES (
  'Leo777', 'leo123', 'leo777@gmail.com', 'Leo', 'Gaspar', '2004-05-05', '387-532-123', 1, 1
);