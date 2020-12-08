defmodule Main do
  def part2(_, n, _, i, acc, _) when i >= n, do: acc
  def part2(lns, n, vis, i, acc, use) do
    if i in vis do
      nil
    else
      vis = [i | vis]
      [opr, arg] = String.split(Enum.at(lns, i))
      arg = String.to_integer(arg)
      {ax, bx} = if opr == "nop", do: {1, arg}, else: {arg, 1}
      case opr do
        "acc" -> part2(lns, n, vis, i + 1, acc + arg, use)
        _ -> if res = part2(lns, n, vis, i + ax, acc, use) do
               res
             else
               if !use do
                 part2(lns, n, vis, i + bx, acc, true)
               else
                 nil
               end
             end
      end
    end
  end
  def part1(lns, vis, i, acc) do
    if i in vis do
      acc
    else
      vis = [i | vis]
      [opr, arg] = String.split(Enum.at(lns, i))
      arg = String.to_integer(arg)
      case opr do
        "acc" -> part1(lns, vis, i + 1, acc + arg)
        "nop" -> part1(lns, vis, i + 1, acc)
        _ -> part1(lns, vis, i + arg, acc)
      end
    end
  end
end

lines = String.split(String.trim(File.read!("inp08")), "\n")
n = Enum.count(lines)
IO.inspect(Main.part1(lines, [], 0, 0))
IO.inspect(Main.part2(lines, n, [], 0, 0, false))
