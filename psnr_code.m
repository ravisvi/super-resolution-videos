for i=1:5
    fprintf('\n\n Image number %i', i);
    
    h = 'evaluate/h';
    h = strcat(h,num2str(i),'.png');
    g = 'evaluate/g';
    g = strcat(g,num2str(i),'.png');
    ng = 'evaluate/ng';
    ng = strcat(ng,num2str(i),'.png');
    bi = 'evaluate/bi';
    bi = strcat(bi,num2str(i),'.png');
    
    himg = imread(h);
    gimg = imread(g);
    ngimg = imread(ng);
    
    biimg = imread(bi);
    if(i==2)
        biimg = biimg(:, 1:1356, :);
    end
    
    n=size(himg);
    M=n(1);
    N=n(2);
    
    MSE = sum(sum((himg-biimg).^2))/(M*N);
    PSNR = 10*log10(256*256/MSE);
    avMSE = sum(MSE)/3;
    avPSNR = sum(PSNR)/3;
    fprintf('\nBicubic:');
    fprintf('\nMSE: %7.2f ', avMSE);
    fprintf('\nPSNR: %9.7f dB', avPSNR);
    
    MSE = sum(sum((himg-gimg).^2))/(M*N);
    PSNR = 10*log10(256*256/MSE);
    avMSE = sum(MSE)/3;
    avPSNR = sum(PSNR)/3;
    fprintf('\nGANs:');
    fprintf('\nMSE: %7.2f ', avMSE);
    fprintf('\nPSNR: %9.7f dB', avPSNR);
    
    MSE = sum(sum((himg-ngimg).^2))/(M*N);
    PSNR = 10*log10(256*256/MSE);
    avMSE = sum(MSE)/3;
    avPSNR = sum(PSNR)/3;
    fprintf('\nGans with L1:');
    fprintf('\nMSE: %7.2f ', avMSE);
    fprintf('\nPSNR: %9.7f dB', avPSNR);
       
end
