
DROP TABLE UserTable;
DROP TABLE SecurityQuestion;
DROP TABLE securityAnswer;

--Creating table
CREATE TABLE UserTable (
    userID NUMBER(3,0) Not NULL,
    userFirstName VARCHAR2(50) Not NULL,
    userLastName VARCHAR2(50) Not NULL,
    streetAddress VARCHAR2(100) Not NULL,
    city VARCHAR2(50) Not NULL,
    state VARCHAR2(2) Not NULL,
    zipCode VARCHAR2(9) Not NULL,
    phoneNumber VARCHAR2(15)
);


-- Creating securityQuestion table
CREATE TABLE SecurityQuestion (
    questionID NUMBER (3,0) Not NULL,
    securityQuestion VARCHAR2(255) Not NULL
);

-- Creating securityAnswer table
CREATE TABLE securityAnswer (
    userID NUMBER(3,0) Not NULL,
    questionID NUMBER(3,0) Not NULL,
    answer VARCHAR2(255) Not NULL
);

-- create primary key
-- create usertable pk
ALTER TABLE UserTable
and constraint pk_UserTable
PRIMARY KEY (userID);
-- create securityQuestion pk
ALTER TABLE SecurityQuestion
and constraint pk_SecurityQuestion
PRIMARY KEY (questionID);
-- create securityAnswer pk
ALTER TABLE securityAnswer
and constraint pk_securityAnswer
PRIMARY KEY (userID, questionID);

ALTER TABLE UserTable
ADD CONSTRAINT fk_UserTable_userID
FOREIGN KEY (userID) REFERENCES UserTable(userID);

ALTER TABLE securityAnswer_questionID
ADD CONSTRAINT fk_securityAnswer
FOREIGN KEY (questionID) REFERENCES SecurityQuestion(questionID);

INSERT INTO UserTable (userID, userFirstName, userLastName, streetAddress, city, state, zipCode, phoneNumber)
VALUES (100, 'Waldo', 'Wildcat', '2400 Stadium Way', 'Ogden', 'UT', '84408', '8016266000');

INSERT INTO SecurityQuestion (questionID, securityQuestion)
VALUES (1, 'What is your best band?');

INSERT INTO securityAnswer (userID, questionID, answer)
VALUES (100, 1, 'The Beatles');