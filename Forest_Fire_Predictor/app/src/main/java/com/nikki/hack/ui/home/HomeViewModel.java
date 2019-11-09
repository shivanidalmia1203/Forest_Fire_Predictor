package com.nikki.hack.ui.home;

import android.widget.ImageView;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.nikki.hack.R;

public class HomeViewModel extends ViewModel {

    //private MutableLiveData<String> mText;
    private ImageView mImage;

    public HomeViewModel() {
        //mText.setValue("This is home fragment");
        mImage.setImageResource(R.drawable.ic_menu_gallery);
    }

    public ImageView getmImage() {
        return mImage;
    }
}