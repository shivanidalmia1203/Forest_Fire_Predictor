package com.nikki.shehack.Fragments;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentTransaction;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.nikki.shehack.MrBeanActivity;
import com.nikki.shehack.R;

public class FragmentAccountActivity extends AppCompatActivity {

    Button btnRegister, btnLogin;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_fragment_account);

        btnLogin = findViewById(R.id.login);
        btnRegister = findViewById(R.id.register);

        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                FragmentLogin fragLogin =new FragmentLogin();
                FragmentTransaction fragmentTransaction = getSupportFragmentManager().beginTransaction();
                fragmentTransaction.replace(R.id.frameLayout, fragLogin);
                fragmentTransaction.commit();

            }
        });

        btnRegister.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                FragmentRegister fragRegister = new FragmentRegister();
                FragmentTransaction fragmentTransaction = getSupportFragmentManager().beginTransaction();
                fragmentTransaction.replace(R.id.frameLayout, fragRegister);
                fragmentTransaction.commit();

            }
        });

    }

    public void MrBeanPage(View v) {
                Intent intent = new Intent(getApplicationContext(), MrBeanActivity.class);
                //intent.setClassName("com.nikki", "com.nikki.shehack");
                startActivity(intent);


    }
}
