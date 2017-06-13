clc;
inpath=('C:\\Users\\sarma\\Desktop\\pics\\pic (');
for i=1:66;
img=imread(strcat(inpath,num2str(i),").jpg"));
img=rgb2gray(img);
b=1;
for j=1:240;
for k=1:320;
m(i,b)=img(j,k);
b=b+1;
endfor
endfor
endfor
y=[(ones(66,1))];
save('data.mat','-v7','m','y')
