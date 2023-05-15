const renderChart7 = (data, labels) => {
  var ctx = document.getElementById("myChart7").getContext("2d");
  var myChart7 = new Chart(ctx, {
    type: "pie",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Last month incomes",
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
        text: "Last month incomes",
      },
    },
  });
};

const getChartData7 = () => {
  console.log("fetching");
  fetch("/income/income_category_summary_month")
    .then((res) => res.json())
    .then((results) => {
      console.log("results", results);
      const category_data = results.income_category_data;
      const [labels, data] = [
        Object.keys(category_data),
        Object.values(category_data),
      ];

      renderChart7(data, labels);
    });
};

document.addEventListener("DOMContentLoaded", getChartData7);
