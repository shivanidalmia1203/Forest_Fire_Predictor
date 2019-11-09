package com.nikki.hack;

import android.content.Intent;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

class SplashTimer extends Thread{

    Welcome welcome;
    SplashTimer(Welcome wel){
        welcome = wel;
    }

    public void run(){

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }finally {

            Intent launchlogin = new Intent(welcome, MainActivity.class);
            welcome.startActivity(launchlogin);

        }
    }
}

public class Welcome extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_welcome);
        SplashTimer splashTimer = new SplashTimer(this);
        splashTimer.start();
    }
}
