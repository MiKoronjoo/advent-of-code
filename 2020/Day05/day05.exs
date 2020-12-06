defmodule Main do
  def seat_ids([]), do: []
  def seat_ids([h | t]), do: [String.to_integer(h, 2)] ++ seat_ids(t)
  def my_seat([h | _], prv) when prv - h != 1, do: h + 1
  def my_seat([h | t], _), do: my_seat(t, h)
end

input = File.read!("inp05")
input = String.replace(input, "L", "0")
input = String.replace(input, "R", "1")
input = String.replace(input, "F", "0")
input = String.replace(input, "B", "1")
codes = Main.seat_ids(String.split(input))
[h | t] = codes
          |> Enum.sort(:desc)
IO.inspect(h)
IO.inspect(Main.my_seat(t, h))
