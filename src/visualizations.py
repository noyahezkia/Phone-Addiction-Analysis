import logging
import matplotlib.pyplot as plt
import seaborn as sns

# Plot bar chart
def bar_plot(data_dict, title, ylabel):
    logging.info(f"Plotting bar chart: {title}")

    plt.figure()
    plt.bar(data_dict.keys(), data_dict.values())
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

# Visualize scatter plot
def scatter_plot(df, x_col, y_col, title):
    logging.info(f"Plotting scatter: {x_col} vs {y_col}")

    sns.scatterplot(data=df, x=x_col, y=y_col)
    plt.title(title)
    plt.show()

# Visualize box plot
def box_plot(df, group_col, target_col, title):
    logging.info(f"Plotting boxplot for {group_col}")

    sns.boxplot(data=df, x=group_col, y=target_col)
    plt.xticks(rotation=30)
    plt.title(title)
    plt.show()

# Plot correlation heatmap between all variables
def plot_correlation_heatmap(data, columns, title="Correlation Matrix"):

    # Filter only numeric columns
    numeric_df = data[columns].select_dtypes(include=["number"])
    
    if numeric_df.empty:
        logging.warning("Warning: No numeric columns found for heatmap.")
        return

    plt.figure(figsize=(12, 10))

    # Correlate all numeric variables with each other
    corr = numeric_df.corr()
    
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    
    plt.title(title, fontsize=16)
    plt.tight_layout()
    plt.show()

# Plot regression plot with two regressions
def plot_split_regression(data, x_col, y_col, hue_col, title):

    # Creates scaater plot with regression
    g = sns.lmplot(x=x_col, y=y_col, hue=hue_col, data=data, 
                   aspect=1.5, height=6, scatter_kws={"alpha":0.5})
    
    plt.title(title, fontsize=14)
    plt.show()
