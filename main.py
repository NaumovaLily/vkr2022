import argparse
import run

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--test_path", "-t", action="store", dest="test_path", 
                      help="путь к файлу с тестовым датасетом",
                      default="test.csv")
  parser.add_argument("--model_path", "-m", action="store", dest="model_path", 
                      help="путь к файлу с моделью",
                      default="model")
  args = parser.parse_args()

  run.run(args.test_path, args.model_path)

main()