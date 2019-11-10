package com.nikki.shehack;

import androidx.appcompat.app.AppCompatActivity;
//import android.support.v7.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

import com.nikki.shehack.mrBeanDesign.MrBeanDesignActivity;
import com.nikki.shehack.uploadImage.Upload;

import androidx.appcompat.app.AppCompatActivity;

public class MrBeanActivity extends AppCompatActivity {

    ImageView img;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mr_bean);

        img = findViewById(R.id.img1);

        img.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), MrBeanDesignActivity.class);
                startActivity(intent);
            }
        });
    }

    public void OpenUploadPage(View v){
        Intent intent = new Intent(getApplicationContext(), Upload.class);
        startActivity(intent);
    }
}
