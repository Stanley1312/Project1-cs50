a = imread('unnamed1.jpg');
the 
a1 = rgb2gray(a);
a1(a1>0)=255;
figure,imshow(a);
figure,imshow(a1);