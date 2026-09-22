#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}

exports.addMeMaybe = addMeMaybe;
