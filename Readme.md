# 📄 A4 Sheet Prediction

With roughly 4,000 students at NIT Jamshedpur wrapping up the semester, the campus is currently flooded with last minute assignments and vivas. While A4 sheet sales remain fairly flat during the rest of the year, this peak season creates a massive, sudden spike in demand. To help local shopkeepers prepare for the rush, I interviewed the two biggest vendors and collected real, on-the-ground sales data. Using those observations, I built this platform to give them a clear summary of their daily traffic and predict exactly how much A4 stock they need to keep on hand for tomorrow so they don't run out.

## The Real Output
Based on my 2 hours of physical observation at the shop, the tool processed the following real data:
- **Valid records:** 32 (recorded in 5-minute intervals)
- **Total requested:** 575 sheets
- **Missed sales:** 25 sheets
- **Students turned away:** 7

When configured for a standard **8-hour** operating day with a **20%** safety buffer, the tool predicts a base daily demand of 1,725 sheets and outputs a final recommendation to stock **2,070 A4 sheets** for tomorrow.

## What the Tool Gets Wrong
This tool relies on linear extrapolation, dividing total demand by observed hours to calculate an average "Hourly demand" (215.62 sheets/hour). In reality, university stationary demand is highly non-linear. It ignores massive spikes in foot traffic that occur 30 minutes before major assignment submission deadlines or morning exams, meaning the shopkeeper could still run out of stock during a rush even if the total daily stock is theoretically sufficient.

## Demonstration Video
The 3 minute screen recording of the tool live here: 
**[https://drive.google.com/file/d/1eXQHqwHKiJ7QhDW9kSSRJYanhQyFS5b8/view?usp=drivesdk]**

---

## How to Run Locally

1. Install Python and open a terminal in this project folder.
2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
3. Install the required dependencies: 
      pip install streamlit pandas
4.   Start the dashboard:  
      streamlit run app.py
