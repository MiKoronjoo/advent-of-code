defmodule Main do
  defp _lc(_, _, []), do: 0
  defp _lc(gp, pn, [h | t]) do
    case pn == Enum.count(gp, & &1 == h) do
      true -> 1 + _lc(gp, pn, t)
      false -> _lc(gp, pn, t)
    end
  end
  def calc([]), do: {0, 0}
  def calc([h | t]) do
    questions = Enum.uniq(String.graphemes(String.replace(h, "\n", "")))
    pn = Enum.count(String.graphemes(String.trim(h)), & &1 == "\n")
    m1 = length(questions)
    m2 = _lc(String.graphemes(h), pn + 1, questions)
    {p1, p2} = calc(t)
    {m1 + p1, m2 + p2}
  end
end

{p1, p2} = Main.calc(String.split(File.read!("inp06"), "\n\n"))
IO.inspect(p1)
IO.inspect(p2)
