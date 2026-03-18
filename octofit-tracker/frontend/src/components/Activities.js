import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Fetching Activities from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched Activities:', results);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching activities:', err);
        setLoading(false);
      });
  }, [endpoint]);

  if (loading) return <div className="text-center my-4">Loading Activities...</div>;

  if (!activities.length) return <div className="alert alert-info">No activities found.</div>;

  // Get table headers from first activity
  const headers = activities[0] ? Object.keys(activities[0]) : [];

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Activities</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="thead-dark">
              <tr>
                {headers.map((header) => (
                  <th key={header}>{header}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {activities.map((activity, idx) => (
                <tr key={activity.id || idx}>
                  {headers.map((header) => (
                    <td key={header}>{String(activity[header])}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Activities;
