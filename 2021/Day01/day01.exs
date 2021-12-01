defmodule Main do
    def get_list(s), do: _get_list(String.split(s))
    defp _get_list([]), do: []
    defp _get_list([h | t]), do: [String.to_integer(h)] ++ _get_list(t)

    def part1([_h | []]), do: 0
    def part1([h | t]) when h < hd(t), do: 1 + part1(t)
    def part1([_h | t]), do: part1(t)

    def part2([_h | []]), do: 0
    def part2([h | t]) when h < hd(tl(tl(t))), do: 1 + part2(t)
    def part2([_h | t]), do: part2(t)
end

input = File.read!("inp01")
nums = Main.get_list(input)
IO.inspect Main.part1(nums)
IO.inspect Main.part2(nums)
