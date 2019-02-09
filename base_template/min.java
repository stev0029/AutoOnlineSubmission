public class $CLASS_NAME$ {
    static final String[] CASE_OUTPUTS = $CASE_OUTPUTS$;
    public static void main(String[] args) throws Exception {
        long start = System.currentTimeMillis();
        if (start < $CODED_START$)
            sleepUntil($CODED_START$);
        int caseNum = getCaseNum();
        System.out.print(CASE_OUTPUTS[caseNum]);
        sleepUntil($CODED_START$ + (caseNum + 1) * $TOTAL_MS$);
    }
    static int getCaseNum() {
        long current = System.currentTimeMillis();
        long match = $CODED_START$;
        int i = 0;
        while (i < CASE_OUTPUTS.length) {
            if (current - match < $TOTAL_MS$)
                return i;
            match += $TOTAL_MS$;
            i++;
        }
        return -1;
    }
    static void sleepUntil(long time) throws Exception {
        while(System.currentTimeMillis() < time)
            Thread.sleep(1);
    }
}
