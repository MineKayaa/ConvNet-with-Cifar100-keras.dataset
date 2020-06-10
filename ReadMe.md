//Dataset

There are 600 images in the Cifar100 database. 500 of them are devoted to training and the remaining 100 are reserved for testing. dataset.py is creating folders for 6 different classes and all images belonging to the classes are in these folders.Seperated as train and test.

These are the labels I wanted to separate 22,23,48,65,90 ve 97.For this reason, I opened subfolders according to these labels under the train and test folders.

(DATASET.PY is already making this part but I put the image file in the directory)

//Data Augmentation

Enriching data for the data on the network we developed increases the ability of the model to generalize and overfitting decreases. If we have a small number of data, this method allows us to generate more training data than the existing examples.
Here I enriched my existing images by making use of ImageDataGenerator ()

//Neural Network

Then I started creating my convolutional neural network, first I added the 2DConv layers, which helped me filter the R, G, B components in color images separately.

After the second Conv2D layer, I combined the Pooling process with the convolution process and the ‘channels. This helped me reduce the size. And I added one Dropout, which is to lower the 'overfitting', meaning that it doesn't memorize it.
After these processes, I added 2 more Conv2D layers and one pooling and a bigger Dropout than the previous one. So that I will be more likely to prevent memorization.
Before starting Dense layers, I made Flatten, that is, flattening process, to make the output values coming to us from the convolution layers so that we can see and understand them.
Then I added Dense layers.

Then I compiled the network.

//Traning the Network

Since I enriched it with ImageDataGenarator, it was actually more efficient than the files. I used model.fit_genarator instead of model.fit as I wanted to use them in education.

I specified the training data, number of epoch, test data, etc.
I put them in a variable like history, so that I can draw the graphics I want and learn about the training of the network.And I made this data visualized.
