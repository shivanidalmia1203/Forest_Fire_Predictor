package com.nikki.hack.ui.tools;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;

import com.nikki.hack.CustomAdaptor;
import com.nikki.hack.MainActivity;
import com.nikki.hack.R;

import java.util.ArrayList;

public class ToolsFragment extends Fragment {

//    private ToolsViewModel toolsViewModel;

    public View onCreateView(@NonNull LayoutInflater inflater,
            ViewGroup container, Bundle savedInstanceState) {
            ListView listView;
        ArrayList<String> cars;
        ArrayAdapter<String> adapter;

        View view = inflater.inflate(R.layout.fragment_tools, container, false);
        listView = view.findViewById(R.id.listView);
        cars= new ArrayList<String>();
        cars.add("Paypal");
        cars.add("Paytm");
        cars.add("UPI");
        cars.add("Debit/Credit");

        adapter=new CustomAdaptor(getContext(),cars);

        listView.setAdapter(adapter);

        return view;
    }

}