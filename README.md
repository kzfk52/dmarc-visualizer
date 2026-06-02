# dmarc-visualizer

Analyse and visualize DMARC results using open-source tools.

* [parsedmarc](https://github.com/domainaware/parsedmarc) for parsing DMARC reports,
* [Elasticsearch](https://www.elastic.co/) to store aggregated data.
* [Grafana](https://grafana.com/) to visualize the aggregated reports.

See the full blog post with instructions at https://debricked.com/blog/2020/05/14/analyse-and-visualize-dmarc-results-using-open-source-tools/.

## Gmail API setup

When fetching DMARC reports through the Gmail API, parsedmarc needs an
OAuth token. The OAuth consent flow cannot complete inside the headless
container, so the token must be generated in advance on a machine with a
browser and then mounted into the container.

1. Place your OAuth client (Desktop app) credentials as `credentials.json`
   in the project root.
2. Generate the token (run where a browser is available):

   ```bash
   pip install google-auth-oauthlib
   python3 generate_token.py
   ```

   Sign in and approve access; `token.json` is written to the project root.
3. Start the stack:

   ```bash
   docker compose up -d --build
   ```

`credentials.json` and `token.json` are bind-mounted into the parsedmarc
container (see `docker-compose.yml`) and are git-ignored. parsedmarc
refreshes the access token automatically using the stored refresh token,
so no further browser interaction is required.

## Screenshot

![Screenshot of Grafana dashboard](/big_screenshot.png?raw=true)
