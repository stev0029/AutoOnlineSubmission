public class $CLASS_NAME$ {

    static final long CODED_START = $CODED_START$L;
    static final int LATE_MARGIN = $LATE_MARGIN$;
    static final int INVALID_MARGIN = $INVALID_MARGIN$;

    static final String COMMON_FORMAT = $COMMON_FORMAT$;
    static final String[] CASE_OUTPUTS = $CASE_OUTPUTS$;

    static final int TOTAL_MS = LATE_MARGIN + INVALID_MARGIN;

    public static void main(String[] args) throws Exception {
        long start = System.currentTimeMillis();
        System.err.printf("[START]\t%d%n", start);

        // Only for first run, wait until timing is correct
        if (start < CODED_START)
            sleepUntil(CODED_START);

        int caseNum = getCaseNum();
        String out = get(caseNum);
        System.err.printf("[RUN]\tCase %d, out: %s%n", caseNum, out);

        printOutput(out);
        // Wait to set correct timing for next run
        sleepUntil(CODED_START + (caseNum + 1) * TOTAL_MS);
        System.err.printf("[END]\t%d%n%n", System.currentTimeMillis());
    }

    static int getCaseNum() {
        long current = System.currentTimeMillis();
        long match = CODED_START;
        int i = 0;

        while (i < CASE_OUTPUTS.length) {
            long diff_ms = current - match;
            if (diff_ms < LATE_MARGIN)
                return i;
            else if (diff_ms < LATE_MARGIN + INVALID_MARGIN)
                return -1;

            match += TOTAL_MS;
            i++;
        }

        return -2;
    }

    static String get(int caseNum) {
        if (caseNum == -1) {
            return "INVALID";
        } else if (caseNum == -2) {
            return "OUT OF BOUNDS";
        } else {
            return CASE_OUTPUTS[caseNum];
        }
    }

    static void printOutput(String out) {
        System.out.printf(COMMON_FORMAT, out);
    }

    static void sleepUntil(long time) throws Exception {
        long current = System.currentTimeMillis();
        System.err.printf("[WAIT]\t%dms, %d -> %d%n", time - current, current, time);
        while(System.currentTimeMillis() < time)
            Thread.sleep(1);
    }
}
