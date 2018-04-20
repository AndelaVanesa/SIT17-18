import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.TreeMap;

public class App_6_2 {

	public static void main(String[] args) {
		
		HashMap<Integer, String> hash = new HashMap<Integer, String>();		
		LinkedHashMap<Integer, String> lhash = new LinkedHashMap<Integer,String>();
		hash.put(21, "Stipe");
		hash.put(455, "Petar");
		hash.put(985, "Etna");
		hash.put(5788, "Vlatka");
		hash.put(159, "Divna");
		
		for (Integer key: hash.keySet()) {
			System.out.println( key + " = " +hash.get(key));
		}
		
		System.out.println("**********Tree Map**********");
		TreeMap<Integer, String> tree = new TreeMap<Integer, String>();
		tree.putAll(hash);
		
		for (Integer key: tree.keySet()) {
			System.out.println( key + " = " +tree.get(key));
	}
}
}
		
		
		

