import java.util.*;

public class Graph {
    private int[][] adjMatrix;
    private int vertexCount;

    public Graph(int[][] matrix) {
        // Defensive copy to avoid external modifications
        this.vertexCount = matrix.length;
        this.adjMatrix = new int[vertexCount][vertexCount];

        for (int i = 0; i < vertexCount; i++) {
            if (matrix[i].length != vertexCount) {
                throw new IllegalArgumentException("Matrix must be square.");
            }
            for (int j = 0; j < vertexCount; j++) {
                this.adjMatrix[i][j] = matrix[i][j];
            }
        }
    }

    public Graph(int maxVertices) {
        adjMatrix = new int[maxVertices][maxVertices];
        vertexCount = 0;
    }

    public void add_vertex() {
        if (vertexCount < adjMatrix.length) {
            vertexCount++;
        }
    }

    public void add_edge(int from, int to) {
        if (from < vertexCount && to < vertexCount) {
            adjMatrix[from][to] = 1;
            adjMatrix[to][from] = 1; // For undirected graph. Remove this line for directed.
        }
    }

    public void printMatrix() {
        for (int i = 0; i < vertexCount; i++) {
            for (int j = 0; j < vertexCount; j++) {
                System.out.print(adjMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public void print_graph() {
        for (int i = 0; i < vertexCount; i++ ) {
            System.out.print(i+"-> ");
            for (int j = 0 ; j < vertexCount; j++) {
                if (this.adjMatrix[i][j] == 1) {
                    System.out.print(j+" ");
                }
            }
            System.out.println();
        }
    }
    public boolean isUndirected() {
        for (int i = 0; i < vertexCount; i++) {
            for (int j = 0 ; j < vertexCount; j++) {
                if (this.adjMatrix[i][j] != this.adjMatrix[j][i]) {
                    return false;
                }
            }
        }
        return true;
    }

    public ArrayList<Integer> getNeighbors(int node) {
        ArrayList<Integer> neighbors = new ArrayList<>();
        for (int i = 0; i < adjMatrix.length; i++) {
            if (adjMatrix[node][i] == 1) {
                neighbors.add(i);
            }
        }
        return neighbors;
    }

    public void BFS(int start) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[this.adjMatrix.length];
        queue.add(start);
        while (queue.isEmpty() == false) {
            int current_node = queue.remove();
            if (visited[current_node] == false) {
                System.out.println(current_node);
                visited[current_node] = true;
                for (int neighbor : getNeighbors(current_node)) {
                    if (visited[neighbor] == false) {
                        queue.add(neighbor);
                    }
                }
            }

        }
    }
    public ArrayList<Integer> getShortestPath(int start, int end) {
        Queue<ArrayList<Integer>> queue = new LinkedList<>();
        boolean[] visited = new boolean[this.adjMatrix.length];
        ArrayList<Integer> path = new ArrayList<>();
        path.add(start);
        queue.add(path);
        while (queue.isEmpty() == false) {
            ArrayList<Integer> current_path = queue.remove();
            int current_node = current_path.get(current_path.size() - 1);
            if (current_node == end) return current_path;
            if (visited[current_node] == false) {
                System.out.println(current_node);
                visited[current_node] = true;
                for (int neighbor : getNeighbors(current_node)) {
                    if (visited[neighbor] == false) {
                        ArrayList<Integer> new_path = new ArrayList<>(current_path);
                        new_path.add(neighbor);
                        queue.add(new_path);
                    }
                }
            }
        }
        return null;
    }


    public static void main(String[] args) {
        int[][] adjMatrix = {
            {0, 1, 1, 0, 1},  // A -> B, C, E
            {1, 0, 0, 1, 0},  // B -> A, D
            {1, 0, 0, 0, 1},  // C -> A, E
            {0, 1, 0, 0, 1},  // D -> B, E
            {1, 0, 1, 1, 0}   // E -> A, C, D
        };

        Graph graph = new Graph(adjMatrix);
        graph.BFS(0);

        for (int element : graph.getShortestPath(0, 3)){
            System.out.print(element+"->");
        }

        
    }
}
