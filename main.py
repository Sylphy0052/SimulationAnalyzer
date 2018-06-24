## sample main program
from src.analyzer import Analyzer

# Analyzerクラスを呼び出すだけの簡単なお仕事
def main():
    analyzer = Analyzer()
    # analyzer.draw_rtt_graph()
    analyzer.write_info_csv()
    analyzer.draw_adjust_graph()

if __name__ == '__main__':
    main()
