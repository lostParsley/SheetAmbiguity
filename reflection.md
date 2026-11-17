# Project Reflection

### What I assumed wrong at the start
I thought the leftover sheets can be resold back to retailers, but Ashish mentioned that they can't be resold as an opened, sealed sheet's quality degrades over time.

### What I would cut
I initially considered building a complex time series forecasting model to predict foot traffic. However, I realized that a simple mathematical safety buffer is far more practical and transparent for a local shopkeeper to actually trust and use on a daily basis. 

### Where AI helped
AI was incredibly useful for quickly translating my raw Pandas data manipulation logic into a clean Streamlit web interface. It also saved me time by writing the exception handling blocks to ensure the dashboard wouldn't crash if a bad row was accidentally entered into the CSV.

### Where AI wasted time
I lost some time during the deployment phase when the AI gave me standard Git push commands that resulted in a merge conflict with my GitHub repository's remote history. It also initially generated broken Markdown formatting for my README file, which I had to go back and fix.