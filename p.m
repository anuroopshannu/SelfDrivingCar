pkg load image
inpath=('/home/pi/pred/img.jpg');
img=imread(inpath);
img=rgb2gray(img);
b=1;
for j=10:20;
for k=1:20;
m(1,b)=img(j,k);
b=b+1;
endfor
endfor
save p.mat -6 m
disp("From P.M")