public class RandomizedSet {
    private Dictionary<int, int> dict = new ();
    private List<int> list = new();
    private Random random = new Random();

    public RandomizedSet() {
        
    }
    
    public bool Insert(int val) {
        if (dict.ContainsKey(val))
            return false;
        dict[val] = list.Count;
        list.Add(val);
        return true;
    }
    
    public bool Remove(int val) {
        if (!dict.ContainsKey(val)) 
            return false;
        
        var index = dict[val];
        var lastElement = list[list.Count - 1];
        
        list[index] = lastElement;
        dict[lastElement] = index;
        
        list.RemoveAt(list.Count - 1);
        dict.Remove(val);
        return true;
    }
    
    public int GetRandom() {
        return list[random.Next(0, list.Count)];
    }
}