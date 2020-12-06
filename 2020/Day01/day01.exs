defmodule Main do
    def get_list(s), do: _get_list(String.split(s))
    defp _get_list([]), do: []
    defp _get_list([head|tail]), do: [String.to_integer(head)] ++ _get_list(tail)
    def star(l), do: _star(l, l, 2020)
    def star(l, goal), do: _star(l, l, goal)
    defp _find(n, [h|_t], goal) when n + h == goal, do: n * h
    defp _find(_n, [_h|t], _goal) when t == [], do: nil
    defp _find(n, [_h|t], goal), do: _find(n, t, goal)
    defp _star([], _l, _goal), do: nil
    defp _star([h|t], l, goal) do
        res = _find(h, l, goal)
        case res do
            nil -> _star(t, l, goal)
            _ -> res
        end
    end
    def star3(l), do: _star3(l, l)
    defp _star3([h|t], l) do
        res = star(l, 2020 - h)
        case res do
            nil -> _star3(t, l)
            _ -> res * h
        end
    end
end

input = File.read!("inp01")
ll = Main.get_list(input)
IO.inspect Main.star(ll)
IO.inspect Main.star3(ll)