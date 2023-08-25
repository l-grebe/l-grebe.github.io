```go
// github.com/bigwhite/experiments/tree/master/uber-zap-advanced-usage/benchmark/log_lib_test.go
package main

import (
	"io"
	"testing"
	"time"

	"github.com/sirupsen/logrus"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

func BenchmarkLogrus(b *testing.B) {
	b.ReportAllocs()
	b.StopTimer()
	logger := logrus.New()
	logger.SetOutput(io.Discard)
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		logger.WithFields(logrus.Fields{
			"url":     "http://foo.com",
			"attempt": 3,
			"backoff": time.Second,
		}).Info("failed to fetch URL")
	}
}

func BenchmarkZap(b *testing.B) {
	b.ReportAllocs()
	b.StopTimer()
	cfg := zap.NewProductionConfig()
	core := zapcore.NewCore(
		zapcore.NewJSONEncoder(cfg.EncoderConfig),
		zapcore.AddSync(io.Discard),
		zapcore.InfoLevel,
	)
	logger := zap.New(core)
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		logger.Info("failed to fetch URL",
			zap.String("url", `http://foo.com`),
			zap.Int("attempt", 3),
			zap.Duration("backoff", time.Second),
		)
	}
}
```

运行结果：
```text
goos: darwin
goarch: arm64
pkg: go.etcd.io/etcd/v3/husy/tests/zap
BenchmarkLogrus-8         616432              1904 ns/op            1365 B/op         25 allocs/op
BenchmarkZap-8           2552599               469.7 ns/op           192 B/op          1 allocs/op
PASS
ok      go.etcd.io/etcd/v3/husy/tests/zap       3.941s
```
