import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
public class App_6 {
	

	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<String>();
		
		list.add("A");
		list.add("B");
		list.add("C");
		list.add("D");
		list.add("E");
		
		LinkedList<String> lista = new LinkedList<String>();
		lista.addAll(list);
		list.add("F");
		lista.addFirst("G");
		lista.addLast("H");
		
		System.out.println(list);
		System.out.println(lista);
		
		for (String txt: lista) {
			System.out.println(txt);
		}
		clearElement(4,"novi_el", lista);
	}
	
public static void clearElement(int i,String str,List<String> lst) {
	lst.set(i, str);
	System.out.println(lst);
}
}


		


