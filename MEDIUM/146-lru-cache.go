/*
https://leetcode.com/problems/lru-cache/
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int Get(int key) Return the value of the key if the key exists, otherwise return -1.
void Put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions Get and Put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "Put", "Put", "Get", "Put", "Get", "Put", "Get", "Get", "Get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.Put(1, 1); // cache is {1=1}
lRUCache.Put(2, 2); // cache is {1=1, 2=2}
lRUCache.Get(1);    // return 1
lRUCache.Put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.Get(2);    // returns -1 (not found)
lRUCache.Put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.Get(1);    // return -1 (not found)
lRUCache.Get(3);    // return 3
lRUCache.Get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to Get and Put.
"""
"""
Time Complexity: O(1)
Space Complexity: O(n)
"""
*/

/*package main

import "fmt"

type lruList struct {
	key int
}

type LRUCache struct {
	capacity int
	cache    map[int]int
	lru      []lruList
}

func Constructor(capacity int) LRUCache {
	lrulist := make([]lruList, 0)
	return LRUCache{
		capacity: capacity,
		cache:    make(map[int]int, capacity),
		lru:      lrulist,
	}
}

func (this *LRUCache) Get(key int) int {
	// fmt.Println("before Get", key, this.cache, this.lru)
	if v, found := this.cache[key]; found {
		// fmt.Println(v)
		for i, v := range this.lru {
			if v.key == key {
				// fmt.Println("befire",len(this.lru))
				this.lru = append(this.lru[:i], this.lru[i+1:]...)
				// fmt.Println("after",len(this.lru), this.lru)
				break
			}
		}
		// fmt.Println(len(this.lru), this.lru)
		this.lru = append(this.lru, lruList{key: key})
		// fmt.Println("after Get", key, this.cache, this.lru)
		return v
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	// fmt.Println("before", key, value, this.cache, this.lru)
	if _, found := this.cache[key]; found {
		for i, v := range this.lru {
			if v.key == key {
				// fmt.Println("befire",len(this.lru))
				this.lru = append(this.lru[:i], this.lru[i+1:]...)
				// fmt.Println("after",len(this.lru), this.lru)
				break
			}
		}
		// this.lru = this.lru[1:]

	} else {
		if len(this.cache) == this.capacity {
			deleteCacheKey := this.lru[0]
			this.lru = this.lru[1:]
			delete(this.cache, deleteCacheKey.key)
		}
	}
	this.cache[key] = value
	this.lru = append(this.lru, lruList{key: key})
	// fmt.Println("after", key, value, this.cache, this.lru)
}*/
package main

import (
	"container/list"
	"fmt"
)

type LRUCache struct {
	capacity   int
	cache      map[int]*list.Element
	linkedList *list.List
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity:   capacity,
		cache:      make(map[int]*list.Element, capacity),
		linkedList: list.New(),
	}
}

func (this *LRUCache) Get(key int) int {
	// fmt.Println("before get", key, this.cache, this.lru)
	if element, found := this.cache[key]; found {
		this.linkedList.MoveToFront(element)
		// fmt.Println("after get", key, this.cache, this.lru)
		return element.Value.([]int)[1]
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	// fmt.Println("before", key, value, this.cache, this.lru)
	if element, found := this.cache[key]; found {
		this.linkedList.Remove(element)
	} else {
		if len(this.cache) == this.capacity {
			lastElement := this.linkedList.Back()
			v := this.linkedList.Remove(lastElement)
			delete(this.cache, v.([]int)[0])
		}
	}
	newElement := this.linkedList.PushFront([]int{key, value})
	this.cache[key] = newElement
	// fmt.Println("after", key, value, this.cache, this.lru)
}

func main() {
	// Your LRUCache object will be instantiated and called as such:
	obj := Constructor(2)
	obj.Put(1, 1)
	obj.Put(2, 2)
	fmt.Println(obj.Get(1))
	obj.Put(3, 3)
	fmt.Println(obj.Get(2))
	obj.Put(4, 4)
	fmt.Println(obj.Get(1))
	fmt.Println(obj.Get(3))
	fmt.Println(obj.Get(4))
}
