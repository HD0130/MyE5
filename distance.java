public class DistanceCalculator {
    private static final double EARTH_RADIUS = 6371.0; // 地球半径（单位：公里）

    // 将角度转换为弧度
    private static double toRadians(double degrees) {
        return degrees * Math.PI / 180.0;
    }

    // 计算两个经纬度之间的距离（单位：公里）
    public static double calculateDistance(double lat1, double lon1, double lat2, double lon2) {
        double lat1Rad = toRadians(lat1);
        double lon1Rad = toRadians(lon1);
        double lat2Rad = toRadians(lat2);
        double lon2Rad = toRadians(lon2);

        double dlon = lon2Rad - lon1Rad;
        double dlat = lat2Rad - lat1Rad;

        double a = Math.pow(Math.sin(dlat / 2), 2) + Math.cos(lat1Rad) * Math.cos(lat2Rad) * Math.pow(Math.sin(dlon / 2), 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

        double distance = EARTH_RADIUS * c;
        return distance;
    }

    public static void main(String[] args) {
        double lat1 = 40.7128; // 纽约市纬度
        double lon1 = -74.0060; // 纽约市经度
        double lat2 = 34.0522; // 洛杉矶纬度
        double lon2 = -118.2437; // 洛杉矶经度

        double distance = calculateDistance(lat1, lon1, lat2, lon2);
        System.out.println("两地距离：" + distance + " 公里");
    }
}
