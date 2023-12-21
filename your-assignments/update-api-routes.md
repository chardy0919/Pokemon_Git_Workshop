# Update API Routes

For reasons above our pay grade, we need to change all our API routing from `api/v1` to `api/v2`. We can keep the v1 routes for legacy / support reasons, but our Django API server should provide routes starting with `api/v2` and our frontend app should use the `api/v2` routes.