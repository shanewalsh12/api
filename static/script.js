document.addEventListener('DOMContentLoaded', function() {
    const headlineContainer = document.getElementById('headline-container');

    function fetchAndDisplayHeadlines(category) {
        fetch(`/top-${category}-headlines`)
            .then(response => response.json())
            .then(data => {
                headlineContainer.innerHTML = '';

                data.forEach(headline => {
                    const headlineElement = document.createElement('div');
                    headlineElement.innerHTML = `
                        <h3><a href="${headline.url}" target="_blank">${headline.title}</a></h3>
                        ${headline.author ? `<p>Author: ${headline.author}</p>` : ''}
                        <hr>
                    `;
                    headlineContainer.appendChild(headlineElement);
                });
            })
            .catch(error => {
                console.error('Error fetching headlines:', error);
                headlineContainer.innerHTML = '<p>Error fetching headlines. Please try again later.</p>';
            });
    }

    document.getElementById('sports-link').addEventListener('click', function(event) {
        event.preventDefault();
        fetchAndDisplayHeadlines('sports');
    });

    document.getElementById('business-link').addEventListener('click', function(event) {
        event.preventDefault();
        fetchAndDisplayHeadlines('business');
    });

    document.getElementById('entertainment-link').addEventListener('click', function(event) {
        event.preventDefault();
        fetchAndDisplayHeadlines('entertainment');
    });

    document.getElementById('health-link').addEventListener('click', function(event) {
        event.preventDefault();
        fetchAndDisplayHeadlines('health');
    });

    document.getElementById('general-link').addEventListener('click', function(event) {
        event.preventDefault();
        fetchAndDisplayHeadlines('general');
    });

    document.getElementById('science-link').addEventListener('click', function(event) {
        event.preventDefault();
        fetchAndDisplayHeadlines('science');
    });

    document.getElementById('technology-link').addEventListener('click', function(event) {
        event.preventDefault();
        fetchAndDisplayHeadlines('technology');
    });
});
