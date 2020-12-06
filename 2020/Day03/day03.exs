defmodule Main do
  def calc(lines, rgt, dwn) do
    p_calc(lines, rgt, dwn, rgt, dwn)
  end
  defp p_calc([h | t], rgt, dwn, r, 0) do
    case Enum.at(String.to_charlist(h), rem(r, String.length(h))) == 35 do
      true -> 1 + p_calc(t, rgt, dwn, r + rgt, dwn - 1)
      false -> p_calc(t, rgt, dwn, r + rgt, dwn - 1)
    end
  end
  defp p_calc([_ | t], rgt, dwn, r, d), do: p_calc(t, rgt, dwn, r, d - 1)
  defp p_calc([], _, _, _, _), do: 0
  def trees(_, []), do: 1
  def trees(lines, [h | t]) do
    [rgt, dwn] = h
    calc(lines, rgt, dwn) * trees(lines, t)
  end
end

input = File.read!("inp03")
lines = String.split(input)
IO.inspect Main.calc(lines, 3, 1)
IO.inspect Main.trees(lines, [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]])
