document.addEventListener('DOMContentLoaded', function () {
    // Sidebar toggle
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.querySelector('.sidebar');
    const dashboardMain = document.querySelector('.dashboard-main');

    sidebarToggle.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');
        dashboardMain.classList.toggle('expanded');
    });

    // Navigation
    const navItems = document.querySelectorAll('.sidebar-nav a');
    const contentSections = document.querySelectorAll('.dashboard-content');

    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = item.getAttribute('data-section');

            navItems.forEach(navItem => navItem.parentElement.classList.remove('active'));
            item.parentElement.classList.add('active');

            contentSections.forEach(section => section.classList.remove('active'));
            document.getElementById(`${targetId}-section`).classList.add('active');
        });
    });

    // Charts
    // const revenueCtx = document.getElementById('revenueChart').getContext('2d');
    // new Chart(revenueCtx, {
    //     type: 'line',
    //     data: {
    //         labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    //         datasets: [{
    //             label: 'Monthly Revenue',
    //             data: [12000, 19000, 15000, 22000, 18000, 24000],
    //             borderColor: '#0a2463',
    //             tension: 0.1
    //         }]
    //     },
    //     options: {
    //         responsive: true,
    //         maintainAspectRatio: false
    //     }
    // });

    // const orderCtx = document.getElementById('orderChart').getContext('2d');
    // new Chart(orderCtx, {
    //     type: 'bar',
    //     data: {
    //         labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    //         datasets: [{
    //             label: 'Orders',
    //             data: [65, 59, 80, 81, 56, 55],
    //             backgroundColor: '#3e92cc'
    //         }]
    //     },
    //     options: {
    //         responsive: true,
    //         maintainAspectRatio: false
    //     }
    // });


    // const timeFilter = document.getElementById("timeFilter");

    // const revenueCtx = document.getElementById('revenueChart').getContext('2d');
    // const orderCtx = document.getElementById('orderChart').getContext('2d');

    // let revenueChart = null;
    // let orderChart = null;

    // const dataSets = {
    //     day: {
    //         labels: ['12 AM', '6 AM', '12 PM', '6 PM'],
    //         revenue: [1000, 4000, 7000, 9000],
    //         orders: [5, 20, 35, 40]
    //     },
    //     week: {
    //         labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    //         revenue: [10000, 15000, 12000, 18000, 22000, 19000, 25000],
    //         orders: [50, 70, 60, 90, 100, 80, 120]
    //     },
    //     month: {
    //         labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
    //         revenue: [40000, 50000, 45000, 60000],
    //         orders: [200, 250, 230, 300]
    //     },
    //     year: {
    //         labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    //         revenue: [120000, 190000, 150000, 220000, 180000, 240000, 200000, 210000, 230000, 250000, 270000, 300000],
    //         orders: [650, 590, 800, 810, 560, 550, 700, 750, 900, 950, 1000, 1100]
    //     },
    //     allTime: {
    //         labels: ['2019', '2020', '2021', '2022', '2023', '2024'],
    //         revenue: [500000, 600000, 700000, 800000, 900000, 1000000],
    //         orders: [5000, 6000, 7000, 8000, 9000, 10000]
    //     }
    // };

    // function createCharts(timeRange) {
    //     const revenueData = dataSets[timeRange].revenue;
    //     const orderData = dataSets[timeRange].orders;
    //     const labels = dataSets[timeRange].labels;

    //     if (!revenueChart) {
    //         revenueChart = new Chart(revenueCtx, {
    //             type: 'line',
    //             data: {
    //                 labels: labels,
    //                 datasets: [{
    //                     label: 'Revenue',
    //                     data: revenueData,
    //                     borderColor: '#0a2463',
    //                     tension: 0.1
    //                 }]
    //             },
    //             options: {
    //                 responsive: true,
    //                 maintainAspectRatio: false
    //             }
    //         });
    //     } else {
    //         revenueChart.data.labels = labels;
    //         revenueChart.data.datasets[0].data = revenueData;
    //         revenueChart.update();
    //     }

    //     if (!orderChart) {
    //         orderChart = new Chart(orderCtx, {
    //             type: 'bar',
    //             data: {
    //                 labels: labels,
    //                 datasets: [{
    //                     label: 'Orders',
    //                     data: orderData,
    //                     backgroundColor: '#3e92cc'
    //                 }]
    //             },
    //             options: {
    //                 responsive: true,
    //                 maintainAspectRatio: false
    //             }
    //         });
    //     } else {
    //         orderChart.data.labels = labels;
    //         orderChart.data.datasets[0].data = orderData;
    //         orderChart.update();
    //     }
    // }

    // createCharts("month"); // Default view

    // timeFilter.addEventListener("change", function () {
    //     createCharts(this.value);
    // });

    // Settings
    const sidebarLinks = document.querySelectorAll(".settings-sidebar ul li a");
    const sections = document.querySelectorAll(".settings-section");
    const forms = document.querySelectorAll(".settings-form");
    const sidebarItems = document.querySelectorAll(".settings-sidebar ul li");

    sidebarLinks.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();

            // Remove active class from all sidebar items
            document.querySelector(".settings-sidebar ul li.active")?.classList.remove("active");

            // Add active class to the clicked sidebar item
            this.parentElement.classList.add("active");

            // Hide all sections
            sections.forEach(section => {
                section.classList.remove("active");
            });

            // Show the clicked section
            const targetSection = document.querySelector(this.getAttribute("href"));
            if (targetSection) {
                targetSection.classList.add("active");
            }
        });
    });

    forms.forEach((form, index) => {
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            // Find the next sidebar item
            const nextItem = sidebarItems[index + 1];
            if (nextItem) {
                nextItem.querySelector("a").click();
            } else {
                // alert("Settings saved successfully!");
                console.log("Settings saved successfully!");
            }
        });
    });

    const forms1 = document.querySelectorAll(".settings-form");
    const sections1 = document.querySelectorAll(".settings-section");

    forms1.forEach(form => {
        form.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent full page reload

            // Submit the form using AJAX
            fetch(form.action, {
                method: "POST",
                body: new FormData(form),
            })
                .then(response => {
                    if (response.ok) {
                        // Find the current section and move to the next
                        const currentSection = form.closest(".settings-section");
                        const nextSection = currentSection.nextElementSibling;

                        if (nextSection) {
                            sections1.forEach(sec => sec.classList.remove("active")); // Hide all sections
                            nextSection.classList.add("active"); // Show next section
                        } else {
                            alert("All settings saved successfully!");
                            window.location.reload(); // Reload the page to prevent blank screen
                        }
                    }
                })
                .catch(error => console.error("Error:", error));
        });
    });
});