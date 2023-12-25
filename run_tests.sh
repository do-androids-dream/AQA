#!/bin/bash

echo "available commands:"
echo "--printall"
echo "--run --device <device_name> --test <test_name> (use --test before each <test_name>)"
echo "--run all <device_name>"
declare -a tests=(
  "test_positive_addition"
  "test_positive_subtraction"
  "test_negative_zerodivision"
  "test_negative_tolarge"
  )

print_all() {
  echo "Available tests:"
  for test in "${tests[@]}"; do
    echo "$test"
  done
  }

run_test() {
  echo "lets test..."
  tests_to_run=()
  if [ "$#" -eq 0 ]; then
    echo "No test specified. Please provide test name"
    print_all
    exit 1
  fi

  while [ "$#" -gt 0 ]; do
    case "$1" in
      --device)
        shift
        device="$1"
        ;;
      --test)
        shift
        tests_to_run+=("$1")
        ;;
    esac
    shift
  done

  if [[ -z "$device" ]]; then
    echo "No device specified"
    exit 1
  fi

  if [[ -z "$tests_to_run" ]]; then
  echo "No test specified"
  exit 1
  fi

  for test in "${tests_to_run[@]}"; do
    if [[ " ${tests[@]} " =~ " $test " ]]; then
      echo "Running test: $test on device: $device"
      DEVICE="$device" python -m unittest tests.test_calc.CalculatorTests.$test
    else
      echo "Test '$test' not found."
      print_all
    fi
  done
}

run_all() {
  echo "lets test..."
  if [ "$#" -eq 0 ]; then
    echo "No device specified"
    exit 1
  fi

  device="$2"
  echo "Running all tests on device: $device"
  DEVICE="$device" python -m unittest tests.test_calc
}


while [ "$#" -gt 0 ]; do
  case "$1" in
    --printall)
      print_all
      exit 0
      ;;
    --run)
      shift
      if [ "$1" == "all" ]; then
        echo "all tests"
        run_all "$@"
        exit 0
      fi

      run_test "$@"
      exit 0
      ;;
  esac
done