package com.nikki.hack;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;

public class CustomAdaptor extends ArrayAdapter<String>{

    public CustomAdaptor(Context context, ArrayList<String> data)
    {
        super(context,0,data);
    }


    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        String value = getItem(position);
        /*
        TextView textView = new TextView(getContext());
        textView.setText(value);
        textView.setPadding(10,10,10,10);
        if(position%2==0)
        {
            textView.setBackgroundColor(getContext().getColor(android.R.color.darker_gray));
        }
        return textView;
        */

        View view = LayoutInflater.from(getContext()).inflate(R.layout.fragment_payment_custom_layout,parent,false);
        TextView textView = view.findViewById(R.id.textView);
        textView.setText(value);
        ImageView imageView = view.findViewById(R.id.imageView);
        switch(value)
        {
            case "Paypal":
                imageView.setImageResource(R.drawable.paypal);
                break;
            case "Paytm":
                imageView.setImageResource(R.drawable.paytm);
                break;
            case "UPI":
                imageView.setImageResource(R.drawable.upi);
                break;
            case "Debit/Credit":
                imageView.setImageResource(R.drawable.visa);
                break;
        }
        return view;
    }
}
