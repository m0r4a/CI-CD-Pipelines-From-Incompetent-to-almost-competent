FROM golang:1.21-alpine AS builder

WORKDIR /app

COPY ./server.go ./

RUN CGO_ENABLED=0 go build -ldflags="-s -w" -o ./server ./server.go

FROM scratch

COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /app/server /server

USER nobody:nogroup

CMD ["/server"]
