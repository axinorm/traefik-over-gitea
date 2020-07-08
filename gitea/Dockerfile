FROM golang:1.13-alpine3.10 AS build-env

ARG GITEA_VERSION=1.10.3
ARG GOARM=6

RUN apk update && apk upgrade && \
	apk add --no-cache git \
		bash \
		curl ;

WORKDIR /

RUN git clone https://github.com/go-gitea/gitea.git gitea \
	&& cd gitea \
	&& git checkout tags/v${GITEA_VERSION}

FROM alpine:3.10

EXPOSE 22 3000

RUN apk --no-cache add \
	su-exec \
	ca-certificates \
	sqlite \
	bash \
	git \
	linux-pam \
	gettext \
	s6 \
	curl \
	openssh \
	tzdata  && \
	addgroup \
	-S -g 1000 \
	git && \
	adduser \
	-S -H -D \
	-h /data/git \
	-s /bin/bash \
	-u 1000 \
	-G git \
	git && \
	echo "git:$(date +%s | sha256sum | base64 | head -c 32)" | chpasswd

ENV USER=git
ENV GITEA_CUSTOM=/data/gitea GITEA_WORK_DIR=/data/gitea
ARG GITEA_VERSION=1.10.3
ARG GOARM=6
ENV GODEBUG=netdns=go

VOLUME ["/data"]

ENTRYPOINT ["/usr/bin/entrypoint"]
CMD ["/bin/s6-svscan", "/etc/s6"]

RUN mkdir -p /app/gitea && \ 
    curl -o /app/gitea/gitea https://dl.gitea.io/gitea/${GITEA_VERSION}/gitea-${GITEA_VERSION}-linux-arm-${GOARM} && \
    chmod +x /app/gitea/gitea && \
    chown git /app/gitea/gitea

COPY --from=build-env /gitea/docker/root /
RUN ln -s /app/gitea/gitea /usr/local/bin/gitea