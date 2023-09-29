-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema discord_app
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema discord_app
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `discord_app` DEFAULT CHARACTER SET utf8mb3 ;
USE `discord_app` ;

-- -----------------------------------------------------
-- Table `discord_app`.`servers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `discord_app`.`servers` (
  `server_id` INT NOT NULL AUTO_INCREMENT,
  `server_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`server_id`),
  UNIQUE INDEX `server_name` (`server_name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 14
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `discord_app`.`channels`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `discord_app`.`channels` (
  `channel_id` INT NOT NULL AUTO_INCREMENT,
  `channel_name` VARCHAR(100) NOT NULL,
  `server_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`channel_id`),
  UNIQUE INDEX `channel_name` (`channel_name` ASC) VISIBLE,
  INDEX `server_id` (`server_id` ASC) VISIBLE,
  CONSTRAINT `channels_ibfk_1`
    FOREIGN KEY (`server_id`)
    REFERENCES `discord_app`.`servers` (`server_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `discord_app`.`user_roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `discord_app`.`user_roles` (
  `role_id` INT NOT NULL AUTO_INCREMENT,
  `role_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`role_id`),
  UNIQUE INDEX `role_id_UNIQUE` (`role_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `discord_app`.`user_status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `discord_app`.`user_status` (
  `status_id` INT NOT NULL AUTO_INCREMENT,
  `status_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`status_id`),
  UNIQUE INDEX `status_id_UNIQUE` (`status_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `discord_app`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `discord_app`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `first_name` VARCHAR(50) NULL DEFAULT NULL,
  `last_name` VARCHAR(50) NULL DEFAULT NULL,
  `date_of_birth` DATE NULL DEFAULT NULL,
  `phone_number` VARCHAR(15) NULL DEFAULT NULL,
  `creation_date` TIMESTAMP NULL DEFAULT NULL,
  `last_login` TIMESTAMP NULL DEFAULT NULL,
  `user_status_status_id` INT NOT NULL,
  `user_roles_role_id` INT NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  INDEX `fk_users_user_status1_idx` (`user_status_status_id` ASC) VISIBLE,
  INDEX `fk_users_user_roles1_idx` (`user_roles_role_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_user_roles1`
    FOREIGN KEY (`user_roles_role_id`)
    REFERENCES `discord_app`.`user_roles` (`role_id`),
  CONSTRAINT `fk_users_user_status1`
    FOREIGN KEY (`user_status_status_id`)
    REFERENCES `discord_app`.`user_status` (`status_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 14
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `discord_app`.`suscription`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `discord_app`.`suscription` (
  `suscription_user_id` INT NOT NULL,
  `suscription_server_id` INT NOT NULL,
  PRIMARY KEY (`suscription_user_id`, `suscription_server_id`),
  INDEX `fk_users_has_servers_servers1_idx` (`suscription_server_id` ASC) VISIBLE,
  INDEX `fk_users_has_servers_users1_idx` (`suscription_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_servers_users1`
    FOREIGN KEY (`suscription_user_id`)
    REFERENCES `discord_app`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_servers_servers1`
    FOREIGN KEY (`suscription_server_id`)
    REFERENCES `discord_app`.`servers` (`server_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `discord_app`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `discord_app`.`messages` (
  `messages_id` INT NOT NULL AUTO_INCREMENT,
  `content` TEXT(500) NOT NULL,
  `creation_date` DATE NOT NULL,
  `channels_channel_id` INT NOT NULL,
  `users_user_id` INT NOT NULL,
  PRIMARY KEY (`messages_id`, `channels_channel_id`, `users_user_id`),
  UNIQUE INDEX `messages_id_UNIQUE` (`messages_id` ASC) VISIBLE,
  INDEX `fk_messages_channels1_idx` (`channels_channel_id` ASC) VISIBLE,
  INDEX `fk_messages_users1_idx` (`users_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_channels1`
    FOREIGN KEY (`channels_channel_id`)
    REFERENCES `discord_app`.`channels` (`channel_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_users1`
    FOREIGN KEY (`users_user_id`)
    REFERENCES `discord_app`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;