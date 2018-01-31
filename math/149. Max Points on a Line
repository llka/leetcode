/*
https://leetcode.com/problems/max-points-on-a-line/description/
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
*/

public class Solution {
    private static final Logger logger = LogManager.getLogger(Solution.class);

    public int maxPoints(Point[] points) {
        int size = points.length;
        if (size < 2) {
            return size;
        }
        int maxOnLine = 2;

        for (int i = 0; i < size; i++) {
            int duplicates = 0;
            for (int j = i + 1; j < size; j++) {
                int lineIJCount = 2 + duplicates;
                if (areDuplicates(points[i], points[j])) {
                    ++duplicates;
                    maxOnLine = lineIJCount > maxOnLine ? lineIJCount : maxOnLine;
                    continue;
                }
                for (int k = j + 1; k < size; k++) {
                    if (areOnOneLine(points[i], points[j], points[k])) {
                        lineIJCount++;
                    }
                }
                maxOnLine = lineIJCount > maxOnLine ? lineIJCount : maxOnLine;
            }
        }

        return maxOnLine;
    }

    private boolean areOnOneLine(Point a, Point b, Point c) {
        double epsilon = 0.00001;
        long A = c.x - a.x;
        long B = b.x - a.x;
        long C = c.y - a.y;
        long D = b.y - a.y;

        if (A == 0 && B != 0 && C != 0) {
            return false;
        }
        if (A == 0 && (B == 0 || C == 0)) {
            return true;
        }

        if (B == 0 && A != 0 && D != 0) {
            return false;
        }
        if (B == 0 && (A == 0 || D == 0)) {
            return true;
        }

        if (C == 0 && A != 0 && D != 0) {
            return false;
        }
        if (C == 0 && (A == 0 || D == 0)) {
            return true;
        }

        if (D == 0 && B != 0 && C != 0) {
            return false;
        }
        if (D == 0 && (B == 0 || C == 0)) {
            return true;
        }

        return Math.abs(A * D - B * C) < epsilon;
    }

    private boolean areDuplicates(Point a, Point b) {
        return a.x == b.x && a.y == b.y;
    }

    private boolean areVertical(Point a, Point b) {
        return a.x == b.x;
    }


    static class Point {
        int x;
        int y;

        Point() {
            x = 0;
            y = 0;
        }

        Point(int a, int b) {
            x = a;
            y = b;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Point point = (Point) o;

            if (x != point.x) return false;
            return y == point.y;
        }

        @Override
        public int hashCode() {
            int result = x;
            result = 31 * result + y;
            return result;
        }

        @Override
        public String toString() {
            return "{x=" + x +
                    ", y=" + y +
                    '}';
        }
    }
}
