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
