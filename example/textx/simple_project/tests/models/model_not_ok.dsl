ASPECT NetworkTraffic
ASPECT FileAccess
SCENARIO S001 BEGIN
    CONFIG HeavyNetworkTraffic HAS (NetworkTraffic)
    CONFIG NoNetworkTraffic HAS ()
END
SCENARIO S002 BEGIN
    CONFIG WithFileAccess HAS (NetworkTraffic FileAccess)
    CONFIG NoFileAccess HAS (NetworkTraffic)
END
TESTCASE T001 BEGIN
    USES S001 WITH HeavyNetworkTraffic
    NEEDS (NetworkTraffic)
END
TESTCASE T002 BEGIN
    USES S001 WITH NoNetworkTraffic // Error
    //USES S002 WITH NoFileAccess
    NEEDS (NetworkTraffic)
END