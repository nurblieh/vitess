// Copyright 2015, Google Inc. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package tabletserver

import (
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"regexp"
	"strings"
	"testing"
	"time"

	"github.com/youtube/vitess/go/vt/tabletserver/planbuilder"
)

func TestQueryzHandler(t *testing.T) {
	resp := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/schemaz", nil)
	schemaInfo := newTestSchemaInfo(100, 10*time.Second, 10*time.Second, false)

	plan1 := &ExecPlan{
		ExecPlan: &planbuilder.ExecPlan{
			TableName: "test_table",
			PlanId:    planbuilder.PLAN_PASS_SELECT,
			Reason:    planbuilder.REASON_SELECT,
		},
	}
	plan1.AddStats(10, 1*time.Second, 2, 0)
	schemaInfo.queries.Set("select name from test_table", plan1)

	plan2 := &ExecPlan{
		ExecPlan: &planbuilder.ExecPlan{
			TableName: "test_table",
			PlanId:    planbuilder.PLAN_DDL,
			Reason:    planbuilder.REASON_DEFAULT,
		},
	}
	plan2.AddStats(1, 1*time.Millisecond, 1, 0)
	schemaInfo.queries.Set("insert into test_table values 1", plan2)

	plan3 := &ExecPlan{
		ExecPlan: &planbuilder.ExecPlan{
			TableName: "",
			PlanId:    planbuilder.PLAN_OTHER,
			Reason:    planbuilder.REASON_DEFAULT,
		},
	}
	plan3.AddStats(1, 50*time.Millisecond, 1, 0)
	schemaInfo.queries.Set("show tables", plan3)
	schemaInfo.queries.Set("", (*ExecPlan)(nil))

	queryzHandler(schemaInfo, resp, req)
	body, _ := ioutil.ReadAll(resp.Body)
	planPattern1 := []string{
		`<tr class="high">`,
		`<td>select name from test_table</td>`,
		`<td>test_table</td>`,
		`<td>PASS_SELECT</td>`,
		`<td>SELECT</td>`,
		`<td>10</td>`,
		`<td>1.000000</td>`,
		`<td>2</td>`,
		`<td>0</td>`,
		`<td>0.100000</td>`,
		`<td>0.200000</td>`,
		`<td>0.000000</td>`,
	}
	checkQueryzHasPlan(t, planPattern1, plan1, body)
	planPattern2 := []string{
		`<tr class="low">`,
		`<td>insert into test_table values 1</td>`,
		`<td>test_table</td>`,
		`<td>DDL</td>`,
		`<td>DEFAULT</td>`,
		`<td>1</td>`,
		`<td>0.001000</td>`,
		`<td>1</td>`,
		`<td>0</td>`,
		`<td>0.001000</td>`,
		`<td>1.000000</td>`,
		`<td>0.000000</td>`,
	}
	checkQueryzHasPlan(t, planPattern2, plan2, body)
	planPattern3 := []string{
		`<tr class="medium">`,
		`<td>show tables</td>`,
		`<td></td>`,
		`<td>OTHER</td>`,
		`<td>DEFAULT</td>`,
		`<td>1</td>`,
		`<td>0.050000</td>`,
		`<td>1</td>`,
		`<td>0</td>`,
		`<td>0.050000</td>`,
		`<td>1.000000</td>`,
		`<td>0.000000</td>`,
	}
	checkQueryzHasPlan(t, planPattern3, plan3, body)
}

func checkQueryzHasPlan(t *testing.T, planPattern []string, plan *ExecPlan, page []byte) {
	matcher := regexp.MustCompile(strings.Join(planPattern, `\s*`))
	if !matcher.Match(page) {
		t.Fatalf("queryz page does not contain plan: %v, page: %s", plan, string(page))
	}
}
