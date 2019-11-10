package com.nikki.shehack.sliding;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.nikki.shehack.MainActivity;
import com.nikki.shehack.R;

public class ReplayActivity extends AppCompatActivity {

    Button b1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_replay);
        b1 = (Button) findViewById(R.id.b1);
    }

    public void replay(View view) {
        PreferenceManager preferenceManager = new PreferenceManager(getApplicationContext());
        preferenceManager.setFirstTimeLaunch(true);
        startActivity(new Intent(getApplicationContext(), MainScreen.class));
        finish();
    }
}
