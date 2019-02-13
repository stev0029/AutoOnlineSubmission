public class $CLASS_NAME$ {
    static final String[] CASE_OUTPUTS = $CASE_OUTPUTS$;
    public static void main(String[] args) throws Exception {
        int caseNum = getCaseNum();
        if (caseNum != -1)
            System.out.print(CASE_OUTPUTS[caseNum]);
        sleepUntil($CODED_START$ + (caseNum + 1) * $RUN_MS$);
    }
    static int getCaseNum() {
        long current = System.currentTimeMillis();
        long match = $CODED_START$;
        int i = 0;
        while (i < CASE_OUTPUTS.length) {
            if (current - match < $RUN_MS$)
                return i;
            match += $RUN_MS$;
            i++;
        }
        return -1;
    }
    static void sleepUntil(long time) throws Exception {
        while(System.currentTimeMillis() < time)
            Thread.sleep(1);
    }
}
