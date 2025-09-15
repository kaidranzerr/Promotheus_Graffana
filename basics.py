# is the service on?? || is it functioning as expected?? || is it performing well?
# monitoring vs observability 
# data collected for monitoring is called telemetry data
 
# prometheus --> monitor applications || monitor systems  || collects data even query
# graffana --> data visualization 
# usually graphs are present on prometheus but we do dashboarding on graffana

# most of the prometheus exporters are linux based but for windows --> wmi

# push method vs scrapping 
# Scraping (default in Prometheus) 🧹

# Prometheus goes to your app and pulls metrics regularly (like: “Hey, give me your data now”).

# Push method (using Pushgateway) 📤

# Your app itself sends (pushes) metrics to Prometheus (through Pushgateway) instead of waiting to be asked.

# namespace is there to give isolation between main production app monitoring and visualization