defmodule Main do
    def std([]), do: []
    def std(["" | _tail]), do: []
    def std([head | tail]), do: [{String.first(head), String.to_integer(hd(tl(String.split(head))))}] ++ std(tail)
    def solve(list), do: _solve(list, 0, 0, 0, 0)
    defp _solve([], h, d1, _a2, d2), do: {h * d1, h * d2}
    defp _solve([{"f", n} | tail], h, d1, a2, d2), do: _solve(tail, h + n, d1, a2, d2 + n * a2)
    defp _solve([{"d", n} | tail], h, d1, a2, d2), do: _solve(tail, h, d1 + n, a2 + n, d2)
    defp _solve([{"u", n} | tail], h, d1, a2, d2), do: _solve(tail, h, d1 - n, a2 - n, d2)
end

input = File.read!("inp02")
IO.inspect Main.solve(Main.std(String.split(input, "\n")))
