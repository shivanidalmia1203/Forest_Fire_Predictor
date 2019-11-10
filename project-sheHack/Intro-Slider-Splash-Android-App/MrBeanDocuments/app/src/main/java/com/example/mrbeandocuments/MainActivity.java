package com.example.mrbeandocuments;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

//    ImageView electricity, waterbill, landown;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
//
//        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.HONEYCOMB) {
//            getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE);
//        }
//
//        electricity = findViewById(R.id.electricity);
//        waterbill = findViewById(R.id.waterbill);
//        landown = findViewById(R.id.landown);

//        electricity.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent intent = new Intent(getApplicationContext(), electricitybill.class);
//                startActivity(intent);
//            }
//        });
//
//        waterbill.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent intent = new Intent(getApplicationContext(), waterUsage.class);
//                startActivity(intent);
//            }
//        });
//
//        landown.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent intent = new Intent(getApplicationContext(), housedeed.class);
//                startActivity(intent);
//            }
//        });
    }
}
