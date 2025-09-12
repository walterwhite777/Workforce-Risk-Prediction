import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
from tabulate import tabulate
import warnings
warnings.filterwarnings('ignore')


def plot_numerical_distributions(data, columns, palette="tab10"):
    plt.style.use("seaborn-v0_8-whitegrid")
    sns.set_context("notebook", font_scale=1.2)
    colors = sns.color_palette(palette, n_colors=len(columns))

    for i, col in enumerate(columns):
        data_to_plot = data[col]

        fig = plt.figure(figsize=(18, 10))
        gs = fig.add_gridspec(2, 2, height_ratios=[3, 1], width_ratios=[2, 1])
        fig.suptitle(
            f"Univariate Analysis of {col}", fontsize=16, weight="bold", y=1.05
        )

        # Histogram with KDE
        ax1 = fig.add_subplot(gs[0, 0])
        sns.histplot(data_to_plot, kde=True, color=colors[i], bins=30, ax=ax1)
        ax1.set_title(f"Histogram", fontsize=14)
        ax1.set_xlabel(f"{col}", fontsize=12)
        ax1.set_ylabel("Frequency", fontsize=12)

        mean_val = data_to_plot.mean()
        median_val = data_to_plot.median()
        ax1.axvline(
            mean_val, color="green", linestyle="--", label=f"Mean: {mean_val:.2f}"
        )
        ax1.axvline(
            median_val, color="purple", linestyle="-", label=f"Median: {median_val:.2f}"
        )
        ax1.legend(fontsize=10)

        # Box plot
        ax2 = fig.add_subplot(gs[0, 1])
        sns.boxplot(
            y=data_to_plot,
            ax=ax2,
            color=colors[i],
            flierprops=dict(marker="o", markerfacecolor="red", markersize=8),
        )
        ax2.set_title(f"Box Plot", fontsize=14)
        ax2.set_ylabel(f"{col}", fontsize=12)

        # Calculate and annotate outliers
        Q1 = data_to_plot.quantile(0.25)
        Q3 = data_to_plot.quantile(0.75)
        IQR = Q3 - Q1
        outliers = data_to_plot[
            (data_to_plot < (Q1 - 1.5 * IQR)) | (data_to_plot > (Q3 + 1.5 * IQR))
        ]
        ax2.text(
            0.95,
            0.95,
            f"Outliers: {len(outliers)}",
            transform=ax2.transAxes,
            fontsize=10,
            verticalalignment="top",
            bbox=dict(facecolor="white", alpha=0.8),
        )

        # Q-Q Plot
        ax3 = fig.add_subplot(gs[1, 0])
        stats.probplot(data_to_plot, dist="norm", plot=ax3, rvalue=True)
        ax3.set_title(f"Q-Q Plot", fontsize=14)
        ax3.set_xlabel("Theoretical Quantiles", fontsize=12)
        ax3.set_ylabel("Sample Quantiles", fontsize=12)

        # Summary statistics table using tabulate
        stats_data = pd.DataFrame(
            {
                "Metric": [
                    "Count",
                    "Mean",
                    "Median",
                    "Std",
                    "Min",
                    "Max",
                    "Skewness",
                    "Kurtosis",
                ],
                "Value": [
                    len(data[col]),
                    data[col].mean(),
                    data[col].median(),
                    data[col].std(),
                    data[col].min(),
                    data[col].max(),
                    stats.skew(data[col]),
                    stats.kurtosis(data[col]),
                ],
            }
        ).round(2)

        print(f"\nSummary Statistics for {col}:")
        print(
            tabulate(
                stats_data,
                headers=["Metric", "Value"],
                tablefmt="psql",
                showindex=False,
            )
        )

        plt.tight_layout()
        plt.show()


def plot_categorical_features(data, columns, palette="tab10", max_categories=15):
    plt.style.use("seaborn-v0_8-whitegrid")
    sns.set_context("notebook", font_scale=1.2)
    colors = sns.color_palette(palette, n_colors=len(columns))

    for i, col in enumerate(columns):
        value_counts = data[col].value_counts()
        if len(value_counts) > max_categories:
            print(
                f"Warning: {col} has {len(value_counts)} categories. Showing top {max_categories} only."
            )
            value_counts = value_counts.head(max_categories)
            truncated = True
        else:
            truncated = False

        plt.figure(figsize=(10, 6))
        ax = sns.barplot(x=value_counts.index, y=value_counts.values, color=colors[i])
        plt.title(f"Distribution of {col}", fontsize=14, weight="bold")
        plt.xlabel(col, fontsize=12)
        plt.ylabel("Count", fontsize=12)
        plt.xticks(rotation=45, ha="right")

        total = len(data[col])
        for p in ax.patches:
            height = p.get_height()
            ax.text(
                p.get_x() + p.get_width() / 2.0,
                height + 0.5,
                f"{height/total*100:.1f}%",
                ha="center",
                fontsize=10,
            )

        if truncated:
            plt.text(
                0.95,
                0.95,
                f"Top {max_categories} categories shown",
                transform=ax.transAxes,
                fontsize=10,
                verticalalignment="top",
                bbox=dict(facecolor="white", alpha=0.8),
            )

        plt.tight_layout()
        plt.show()

        relative_freq = (value_counts / total * 100).round(1)
        table_data = pd.DataFrame(
            {
                "Value": value_counts.index,
                "Count": value_counts.values,
                "Relative Frequency (%)": relative_freq.values,
            }
        )

        print(f"\nSummary for {col}:")
        print(f"Mode: {data[col].mode()[0]}")
        print(tabulate(table_data, headers="keys", tablefmt="psql", showindex=False))
        print("\n")


