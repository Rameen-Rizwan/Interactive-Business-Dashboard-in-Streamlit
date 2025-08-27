#  Task: Interactive Business Dashboard (Global Superstore Dataset)

##  Objective
The goal of this task is to **develop an interactive dashboard** for analyzing sales, profit, and segment-wise performance using the **Global Superstore dataset**.  

The project is divided into two parts:
1. **Data Cleaning & Analysis in Jupyter Notebook**  
2. **Interactive Dashboard in Streamlit (Visual Studio Code)**  

---

##  Dataset Information
The dataset used is the **Global Superstore Dataset**.  
It contains sales-related information with the following columns (not exhaustive list):

- **Category**  
- **City**  
- **Country**  
- **Customer.ID**  
- **Customer.Name**  
- **Discount**  
- **Market**  
- **Order.Date**  
- **Order.ID**  
- **Sales**  
- **Profit**  
- **Segment**  
- **Ship.Date**  
- **Ship.Mode**  
- **Shipping.Cost**  
- **State**  
- **Sub.Category**  
- **Year**  
- **weeknum**

---

##  Part 1: Data Cleaning & Analysis in Jupyter Notebook

### Steps Performed
1. **Import Libraries**
   - Pandas, NumPy, Matplotlib, Seaborn used for data cleaning and visualization.

2. **Load Dataset**
   - Loaded the dataset into a Pandas DataFrame.

3. **Explore Dataset**
   - Checked shape, column names, datatypes, and summary statistics.

4. **Handle Missing Data**
   - Detected null values and handled them appropriately.

5. **Data Cleaning**
   - Removed duplicates.  
   - Converted `Order.Date` and `Ship.Date` into datetime format.  
   - Extracted new features (like `Year` and `weeknum` if not already present).

6. **Exploratory Data Analysis (EDA)**
   - Sales distribution per region.  
   - Profit analysis by category and sub-category.  
   - Identified **Top 5 Customers by Sales**.  
   - Created summary tables for KPIs.

7. **Outputs Generated**
   - Clean dataset ready for dashboard.  
   - Basic KPI calculations (Total Sales, Total Profit, etc.).  
   - Visualization plots for sales/profit distributions.

---

##  Part 2: Interactive Dashboard in Streamlit (Visual Studio Code)

### Features of Dashboard
✅ **Filters**: Users can filter by  
- Region  
- Category  
- Sub-Category  

✅ **KPIs Displayed**:  
- **Total Sales**  
- **Total Profit**  
- **Top 5 Customers by Sales**  

✅ **Visualizations**:  
- Sales by region (bar chart)  
- Profit by category (bar chart)  
- Sales trend (line chart using `Order.Date`)  

---

## 🚀 How to Run the Project

### 🔹 Running Jupyter Notebook (Data Cleaning & Analysis)
1. Open **Jupyter Notebook / JupyterLab**.  
2. Run the notebook file `Global_Superstore_Analysis.ipynb`.  
3. The notebook is structured into cells:  
   - Each step (data loading, cleaning, EDA, etc.) is in **separate cells**.  
   - Each line of code has corresponding output (e.g., `print()` statements or plots).  

---

### 🔹 Running Streamlit Dashboard (Visual Studio Code)
1. Open **Visual Studio Code**.  
2. Install the required dependencies (see below).  
3. Run the following command in terminal:  
   ```bash
   streamlit run app.py

---

## Outputs

**From Jupyter Notebook:**

1. Cleaned dataset
2. KPI summary
3. Sales & profit plots
4. Top customers by sales

**From Streamlit Dashboard:**

1. Interactive filters
2. KPI cards (Total Sales, Total Profit)
3. Visual charts (Sales by Region, Profit by Category)
4. Top 5 Customers ranking
