# Cost Optimization Report

Estimated pilot cost for the Skynet Ops Audit Service.

## Architecture
- Docker container for application
- Small compute instance (t3.micro)
- CloudWatch logs for monitoring

## Estimated Monthly Cost

Compute: ~$10–15  
Logs & Monitoring: ~$5–10  
Storage: ~$2–5  

Total Estimated Cost: $20–30/month

## Cost Controls
- Use small instance size
- Log retention limited to 7 days
- Non-production environments can be shut down when not needed
