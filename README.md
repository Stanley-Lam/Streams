# Streams
CSC 202 Data Structures Streams Project

Description: A stream is an indefinite sequence of elements that cannot be randomly accessed and typically may only be traversed once. That is, the only supported operation is getting the next element. Functions operating on streams must typically do so under stringent memory constraints; they may not simply copy the contents of a stream into a list. Instead, one possibility is to store only the most recent elements in a "sliding window". In general, whenever a new element is encountered, an older element needs to be discarded first to maintain the size of the window. Since only the oldest or newest elements ever need to be accessed, the elements that are currently in the window can be efficiently stored in a queue. 

Function find_density: Efficiently analyze the bits drawn from a given generator by storing them in a window of a given width, computing the average number of bits set to '1' within the window

Function find_pattern: Efficiently analyze the bits drawn from a given generator by storing them in a window of a given width, computing the indices at which the generator contains a given pattern. Convert the pattern, as well as the first window, to decimal. Convert each subsequent window to decimal, in constant time, based on the previous window's conversion. Find occurrences of the pattern by comparing its decimal conversion to that of each window, without comparing any individual bits. Represent the window as a queue. 
