FROM grafana/grafana:latest

ADD --chown=grafana:root https://raw.githubusercontent.com/domainaware/parsedmarc/refs/heads/master/dashboards/grafana/Grafana-DMARC_Reports.json /var/lib/grafana/dashboards/

COPY grafana-provisioning/ /etc/grafana/provisioning/
