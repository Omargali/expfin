const renderChart8 = (data, labels) => {
  var ctx = document.getElementById("myChart8").getContext("2d");
  var myChart8 = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Today's incomes",
          data: data,
          backgroundColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      title: {
        display: true,
        text: "Today's incomes",
      },
    },
  });
};

const getChartData8 = () => {
  console.log("fetching");
  fetch("/income/income_category_summary_day")
    .then((res) => res.json())
    .then((results) => {
      console.log("results", results);
      const category_data = results.income_category_data;
      const [labels, data] = [
        Object.keys(category_data),
        Object.values(category_data),
      ];

      renderChart8(data, labels);
    });
};

document.addEventListener("DOMContentLoaded", getChartData8);
