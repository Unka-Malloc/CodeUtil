package JavaUtil;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class ArrayListUtil {

	public static void remove(ArrayList<String> arrayList, String element) {
		Iterator<String> iterator = arrayList.iterator();

		while (iterator.hasNext()) {
			if (element.equals(iterator.next())) {
				iterator.remove();
			}
		}
	}

	public static void main(String[] args){

		ArrayList<String> words = new ArrayList<>(
			Arrays.asList("a", "b", "c", "d")
		);

		remove(words, "a");
		
		System.out.println(words);
	}
}