FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1 \
    APP_ROOT=/var/app

# Install waitfor
ENV WAITFOR_VERSION="v2.1.1"
RUN set -x \
    && BUILD_PACKAGES=' \
        curl \
    ' \
    && RUNTIME_PACKAGES=' \
        gosu \
        netcat \
    ' \
    && apt-get update \
    && apt-get install -y ${BUILD_PACKAGES} ${RUNTIME_PACKAGES} \
    && curl -o /usr/local/bin/wait-for -sSL https://raw.githubusercontent.com/eficode/wait-for/${WAITFOR_VERSION}/wait-for \
    && chmod +x /usr/local/bin/wait-for \
    && apt-get purge -y --auto-remove ${BUILD_PACKAGES} \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ${APP_ROOT}/requirements.txt

RUN set -ex \
    && BUILD_PACKAGES='\
        build-essential \
        git-core \
        liblzma-dev \
        graphviz-dev\
    ' \
    && RUNTIME_PACKAGES=' \
        postgresql-client \
        postgresql-contrib \
        graphviz \
        lzma \
    ' \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        ${BUILD_PACKAGES} ${RUNTIME_PACKAGES} \
    && pip install --no-cache-dir -r ${APP_ROOT}/requirements.txt \
    && apt-get remove -y ${BUILD_PACKAGES} \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* \
    \
    && find /usr/local -depth \
        \( \
            \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
        \) -exec rm -rf '{}' +

# COPY docker-dev-entrypoint.sh /usr/local/bin/default-entrypoint.sh
# ENTRYPOINT ["/usr/local/bin/default-entrypoint.sh"]

COPY ./ ${APP_ROOT}

WORKDIR ${APP_ROOT}
