homeURL = 'http://selfreport.shu.edu.cn/'
loginURL = 'https://newsso.shu.edu.cn/login'
reportURL = 'http://selfreport.shu.edu.cn/DayReport.aspx'
template = [
    'eyJwMV9CYW9TUlEiOnsiVGV4dCI6IiVzIn0sInAxX0RhbmdRU1RaSyI6eyJGX0l0ZW1zIjpbWyLoia/lpb0iLCLoia/lpb0iLDFdLFsi5LiN6YCCIiwi5LiN6YCCIiwxXV0sIlNlbGVjdGVkVmFsdWUiOiLoia/lpb0ifSwicDFfWmhlbmdaaHVhbmciOnsiSGlkZGVuIjp0cnVlLCJGX0l0ZW1zIjpbWyLmhJ/lhpIiLCLmhJ/lhpIiLDFdLFsi5ZKz5Ze9Iiwi5ZKz5Ze9IiwxXSxbIuWPkeeDrSIsIuWPkeeDrSIsMV1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOltdfSwicDFfWmFpWGlhbyI6eyJGX0l0ZW1zIjpbWyLkuI3lnKjmoKEiLCLkuI3lnKjmoKEiLDFdLFsi5a6d5bGxIiwi5a6d5bGx5qCh5Yy6IiwxXSxbIuW7tumVvyIsIuW7tumVv+agoeWMuiIsMV0sWyLlmInlrpoiLCLlmInlrprmoKHljLoiLDFdLFsi5paw6Ze46LevIiwi5paw6Ze46Lev5qCh5Yy6IiwxXV0sIlNlbGVjdGVkVmFsdWUiOiIlcyJ9LCJwMV9HdW9OZWkiOnsiRl9JdGVtcyI6W1si5Zu95YaFIiwi5Zu95YaFIiwxXSxbIuWbveWkliIsIuWbveWkliIsMV1dLCJTZWxlY3RlZFZhbHVlIjoiJXMifSwicDFfZGRsU2hlbmciOnsiRl9JdGVtcyI6W1siLTEiLCLpgInmi6nnnIHku70iLDEsIiIsIiJdLFsi5YyX5LqsIiwi5YyX5LqsIiwxLCIiLCIiXSxbIuWkqea0pSIsIuWkqea0pSIsMSwiIiwiIl0sWyLkuIrmtbciLCLkuIrmtbciLDEsIiIsIiJdLFsi6YeN5bqGIiwi6YeN5bqGIiwxLCIiLCIiXSxbIuays+WMlyIsIuays+WMlyIsMSwiIiwiIl0sWyLlsbHopb8iLCLlsbHopb8iLDEsIiIsIiJdLFsi6L695a6BIiwi6L695a6BIiwxLCIiLCIiXSxbIuWQieaelyIsIuWQieaelyIsMSwiIiwiIl0sWyLpu5HpvpnmsZ8iLCLpu5HpvpnmsZ8iLDEsIiIsIiJdLFsi5rGf6IuPIiwi5rGf6IuPIiwxLCIiLCIiXSxbIua1meaxnyIsIua1meaxnyIsMSwiIiwiIl0sWyLlronlvr0iLCLlronlvr0iLDEsIiIsIiJdLFsi56aP5bu6Iiwi56aP5bu6IiwxLCIiLCIiXSxbIuaxn+ilvyIsIuaxn+ilvyIsMSwiIiwiIl0sWyLlsbHkuJwiLCLlsbHkuJwiLDEsIiIsIiJdLFsi5rKz5Y2XIiwi5rKz5Y2XIiwxLCIiLCIiXSxbIua5luWMlyIsIua5luWMlyIsMSwiIiwiIl0sWyLmuZbljZciLCLmuZbljZciLDEsIiIsIiJdLFsi5bm/5LicIiwi5bm/5LicIiwxLCIiLCIiXSxbIua1t+WNlyIsIua1t+WNlyIsMSwiIiwiIl0sWyLlm5vlt50iLCLlm5vlt50iLDEsIiIsIiJdLFsi6LS15beeIiwi6LS15beeIiwxLCIiLCIiXSxbIuS6keWNlyIsIuS6keWNlyIsMSwiIiwiIl0sWyLpmZXopb8iLCLpmZXopb8iLDEsIiIsIiJdLFsi55SY6IKDIiwi55SY6IKDIiwxLCIiLCIiXSxbIumdkua1tyIsIumdkua1tyIsMSwiIiwiIl0sWyLlhoXokpnlj6QiLCLlhoXokpnlj6QiLDEsIiIsIiJdLFsi5bm/6KW/Iiwi5bm/6KW/IiwxLCIiLCIiXSxbIuilv+iXjyIsIuilv+iXjyIsMSwiIiwiIl0sWyLlroHlpI8iLCLlroHlpI8iLDEsIiIsIiJdLFsi5paw55aGIiwi5paw55aGIiwxLCIiLCIiXSxbIummmea4ryIsIummmea4ryIsMSwiIiwiIl0sWyLmvrPpl6giLCLmvrPpl6giLDEsIiIsIiJdLFsi5Y+w5rm+Iiwi5Y+w5rm+IiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyIlcyJdfSwicDFfZGRsU2hpIjp7IkVuYWJsZWQiOnRydWUsIkZfSXRlbXMiOiVzLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsiJXMiXX0sInAxX2RkbFhpYW4iOnsiRW5hYmxlZCI6dHJ1ZSwiRl9JdGVtcyI6JXMsIlNlbGVjdGVkVmFsdWVBcnJheSI6WyIlcyJdfSwicDFfVG9uZ1pXRExIIjp7IlJlcXVpcmVkIjp0cnVlLCJGX0l0ZW1zIjpbWyLmmK8iLCLmmK8iLDFdLFsi5ZCmIiwi5ZCmIiwxXV0sIlNlbGVjdGVkVmFsdWUiOiIlcyJ9LCJwMV9YaWFuZ1hEWiI6eyJMYWJlbCI6IuWbveWGheivpue7huWcsOWdgCIsIlRleHQiOiIlcyJ9LCJwMV9RdWVaSFpKQyI6eyJGX0l0ZW1zIjpbWyLmmK8iLCLmmK8iLDEsIiIsIiJdLFsi5ZCmIiwi5ZCmIiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyIlcyJdfSwicDFfQ2VuZ0ZXSCI6eyJMYWJlbCI6IjIwMjDlubQx5pyIMTDml6XlkI7mmK/lkKblnKjmuZbljJfpgJfnlZnov4cifSwicDFfQ2VuZ0ZXSF9SaVFpIjp7IkhpZGRlbiI6dHJ1ZX0sInAxX0NlbmdGV0hfQmVpWmh1Ijp7IkhpZGRlbiI6dHJ1ZX0sInAxX0ppZUNodSI6eyJMYWJlbCI6IjAx5pyIMjbml6Xoh7MwMuaciDA55pel5piv5ZCm5LiO5p2l6Ieq5rmW5YyX5Y+R54Ot5Lq65ZGY5a+G5YiH5o6l6KemIn0sInAxX0ppZUNodV9SaVFpIjp7IkhpZGRlbiI6dHJ1ZX0sInAxX0ppZUNodV9CZWlaaHUiOnsiSGlkZGVuIjp0cnVlfSwicDFfVHVKV0giOnsiTGFiZWwiOiIwMeaciDI25pel6IezMDLmnIgwOeaXpeaYr+WQpuS5mOWdkOWFrOWFseS6pOmAmumAlOW+hOa5luWMlyJ9LCJwMV9UdUpXSF9SaVFpIjp7IkhpZGRlbiI6dHJ1ZX0sInAxX1R1SldIX0JlaVpodSI6eyJIaWRkZW4iOnRydWV9LCJwMV9KaWFSZW4iOnsiTGFiZWwiOiIwMeaciDI25pel6IezMDLmnIgwOeaXpeWutuS6uuaYr+WQpuacieWPkeeDreetieeXh+eKtiJ9LCJwMV9KaWFSZW5fQmVpWmh1Ijp7IkhpZGRlbiI6dHJ1ZX0sInAxX1N1aVNNIjp7IlJlcXVpcmVkIjp0cnVlLCJGX0l0ZW1zIjpbWyLnuqLoibIiLCLnuqLoibIiLDFdLFsi6buE6ImyIiwi6buE6ImyIiwxXSxbIue7v+iJsiIsIue7v+iJsiIsMV1dLCJTZWxlY3RlZFZhbHVlIjoiJXMifSwicDFfU3VpU01TTSI6eyJJRnJhbWVBdHRyaWJ1dGVzIjp7fX0sInAxIjp7IklGcmFtZUF0dHJpYnV0ZXMiOnt9fX0=',
    'eyJwMV9CYW9TUlEiOnsiVGV4dCI6IiVzIn0sInAxX0RhbmdRU1RaSyI6eyJGX0l0ZW1zIjpbWyLoia/lpb0iLCLoia/lpb0iLDFdLFsi5LiN6YCCIiwi5LiN6YCCIiwxXV0sIlNlbGVjdGVkVmFsdWUiOiLoia/lpb0ifSwicDFfWmhlbmdaaHVhbmciOnsiSGlkZGVuIjp0cnVlLCJGX0l0ZW1zIjpbWyLmhJ/lhpIiLCLmhJ/lhpIiLDFdLFsi5ZKz5Ze9Iiwi5ZKz5Ze9IiwxXSxbIuWPkeeDrSIsIuWPkeeDrSIsMV1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOltdfSwicDFfWmFpWGlhbyI6eyJGX0l0ZW1zIjpbWyLkuI3lnKjmoKEiLCLkuI3lnKjmoKEiLDFdLFsi5a6d5bGxIiwi5a6d5bGx5qCh5Yy6IiwxXSxbIuW7tumVvyIsIuW7tumVv+agoeWMuiIsMV0sWyLlmInlrpoiLCLlmInlrprmoKHljLoiLDFdLFsi5paw6Ze46LevIiwi5paw6Ze46Lev5qCh5Yy6IiwxXV0sIlNlbGVjdGVkVmFsdWUiOiIlcyJ9LCJwMV9HdW9OZWkiOnsiRl9JdGVtcyI6W1si5Zu95YaFIiwi5Zu95YaFIiwxXSxbIuWbveWkliIsIuWbveWkliIsMV1dLCJTZWxlY3RlZFZhbHVlIjoiJXMifSwicDFfZGRsU2hlbmciOnsiRl9JdGVtcyI6W1siLTEiLCLpgInmi6nnnIHku70iLDEsIiIsIiJdLFsi5YyX5LqsIiwi5YyX5LqsIiwxLCIiLCIiXSxbIuWkqea0pSIsIuWkqea0pSIsMSwiIiwiIl0sWyLkuIrmtbciLCLkuIrmtbciLDEsIiIsIiJdLFsi6YeN5bqGIiwi6YeN5bqGIiwxLCIiLCIiXSxbIuays+WMlyIsIuays+WMlyIsMSwiIiwiIl0sWyLlsbHopb8iLCLlsbHopb8iLDEsIiIsIiJdLFsi6L695a6BIiwi6L695a6BIiwxLCIiLCIiXSxbIuWQieaelyIsIuWQieaelyIsMSwiIiwiIl0sWyLpu5HpvpnmsZ8iLCLpu5HpvpnmsZ8iLDEsIiIsIiJdLFsi5rGf6IuPIiwi5rGf6IuPIiwxLCIiLCIiXSxbIua1meaxnyIsIua1meaxnyIsMSwiIiwiIl0sWyLlronlvr0iLCLlronlvr0iLDEsIiIsIiJdLFsi56aP5bu6Iiwi56aP5bu6IiwxLCIiLCIiXSxbIuaxn+ilvyIsIuaxn+ilvyIsMSwiIiwiIl0sWyLlsbHkuJwiLCLlsbHkuJwiLDEsIiIsIiJdLFsi5rKz5Y2XIiwi5rKz5Y2XIiwxLCIiLCIiXSxbIua5luWMlyIsIua5luWMlyIsMSwiIiwiIl0sWyLmuZbljZciLCLmuZbljZciLDEsIiIsIiJdLFsi5bm/5LicIiwi5bm/5LicIiwxLCIiLCIiXSxbIua1t+WNlyIsIua1t+WNlyIsMSwiIiwiIl0sWyLlm5vlt50iLCLlm5vlt50iLDEsIiIsIiJdLFsi6LS15beeIiwi6LS15beeIiwxLCIiLCIiXSxbIuS6keWNlyIsIuS6keWNlyIsMSwiIiwiIl0sWyLpmZXopb8iLCLpmZXopb8iLDEsIiIsIiJdLFsi55SY6IKDIiwi55SY6IKDIiwxLCIiLCIiXSxbIumdkua1tyIsIumdkua1tyIsMSwiIiwiIl0sWyLlhoXokpnlj6QiLCLlhoXokpnlj6QiLDEsIiIsIiJdLFsi5bm/6KW/Iiwi5bm/6KW/IiwxLCIiLCIiXSxbIuilv+iXjyIsIuilv+iXjyIsMSwiIiwiIl0sWyLlroHlpI8iLCLlroHlpI8iLDEsIiIsIiJdLFsi5paw55aGIiwi5paw55aGIiwxLCIiLCIiXSxbIummmea4ryIsIummmea4ryIsMSwiIiwiIl0sWyLmvrPpl6giLCLmvrPpl6giLDEsIiIsIiJdLFsi5Y+w5rm+Iiwi5Y+w5rm+IiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyIlcyJdfSwicDFfZGRsU2hpIjp7IkVuYWJsZWQiOnRydWUsIkZfSXRlbXMiOiVzLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsiJXMiXX0sInAxX2RkbFhpYW4iOnsiRW5hYmxlZCI6dHJ1ZSwiRl9JdGVtcyI6JXMsIlNlbGVjdGVkVmFsdWVBcnJheSI6WyIlcyJdfSwicDFfVG9uZ1pXRExIIjp7IlJlcXVpcmVkIjpmYWxzZSwiSGlkZGVuIjp0cnVlLCJGX0l0ZW1zIjpbWyLmmK8iLCLmmK8iLDFdLFsi5ZCmIiwi5ZCmIiwxXV0sIlNlbGVjdGVkVmFsdWUiOm51bGx9LCJwMV9YaWFuZ1hEWiI6eyJMYWJlbCI6IuWbveWGheivpue7huWcsOWdgCIsIlRleHQiOiIlcyJ9LCJwMV9RdWVaSFpKQyI6eyJGX0l0ZW1zIjpbWyLmmK8iLCLmmK8iLDEsIiIsIiJdLFsi5ZCmIiwi5ZCmIiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyIlcyJdfSwicDFfRmFuWFJRIjp7IkhpZGRlbiI6dHJ1ZX0sInAxX1dlaUZIWVkiOnsiSGlkZGVuIjp0cnVlfSwicDFfU2hhbmdISlpEIjp7IkhpZGRlbiI6dHJ1ZX0sInAxX0NlbmdGV0giOnsiTGFiZWwiOiIyMDIw5bm0MeaciDEw5pel5ZCO5piv5ZCm5Zyo5rmW5YyX6YCX55WZ6L+HIn0sInAxX0NlbmdGV0hfUmlRaSI6eyJIaWRkZW4iOnRydWV9LCJwMV9DZW5nRldIX0JlaVpodSI6eyJIaWRkZW4iOnRydWV9LCJwMV9KaWVDaHUiOnsiTGFiZWwiOiIwMeaciDI25pel6IezMDLmnIgwOeaXpeaYr+WQpuS4juadpeiHqua5luWMl+WPkeeDreS6uuWRmOWvhuWIh+aOpeinpiJ9LCJwMV9KaWVDaHVfUmlRaSI6eyJIaWRkZW4iOnRydWV9LCJwMV9KaWVDaHVfQmVpWmh1Ijp7IkhpZGRlbiI6dHJ1ZX0sInAxX1R1SldIIjp7IkxhYmVsIjoiMDHmnIgyNuaXpeiHszAy5pyIMjnml6XmmK/lkKbkuZjlnZDlhazlhbHkuqTpgJrpgJTlvoTmuZbljJcifSwicDFfVHVKV0hfUmlRaSI6eyJIaWRkZW4iOnRydWV9LCJwMV9UdUpXSF9CZWlaaHUiOnsiSGlkZGVuIjp0cnVlfSwicDFfSmlhUmVuIjp7IkxhYmVsIjoiMDHmnIgyNuaXpeiHszAy5pyIMjnml6XlrrbkurrmmK/lkKbmnInlj5Hng63nrYnnl4fnirYifSwicDFfSmlhUmVuX0JlaVpodSI6eyJIaWRkZW4iOnRydWV9LCJwMV9TdWlTTSI6eyJSZXF1aXJlZCI6ZmFsc2UsIkhpZGRlbiI6dHJ1ZSwiRl9JdGVtcyI6W1si57qi6ImyIiwi57qi6ImyIiwxXSxbIum7hOiJsiIsIum7hOiJsiIsMV0sWyLnu7/oibIiLCLnu7/oibIiLDFdXSwiU2VsZWN0ZWRWYWx1ZSI6bnVsbH0sInAxX1N1aVNNU00iOnsiSGlkZGVuIjp0cnVlLCJJRnJhbWVBdHRyaWJ1dGVzIjp7fX0sInAxIjp7IklGcmFtZUF0dHJpYnV0ZXMiOnt9fX0='
]