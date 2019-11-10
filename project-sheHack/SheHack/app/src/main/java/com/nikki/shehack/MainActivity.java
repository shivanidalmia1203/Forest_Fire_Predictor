package com.nikki.shehack;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import com.nikki.shehack.Fragments.FragmentAccountActivity;
import com.nikki.shehack.sliding.Splash_screen;

public class MainActivity extends AppCompatActivity {

    Button ffp;
    ImageView imageViewAccount;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        imageViewAccount = findViewById(R.id.button_account);
        ffp = findViewById(R.id.ffp);

        imageViewAccount.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), FragmentAccountActivity.class);
                startActivity(intent);
            }
        });

        ffp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), Splash_screen.class);
                startActivity(intent);
            }
        });
    }
}
