
import hashlib
import select
import time
import sys


def process(text: str, qty: int):
    time.sleep(2)
    result = text
    for _ in range(qty):
        result = hashlib.sha256(result.encode()).hexdigest()
    return {"input": text, "result": result}


if __name__ == "__main__":
    try:
        args = sys.argv

        if len(args) == 1:
            qty = 1
        elif len(args) == 3 and args[1] == "--qty":
            qty = int(args[2])
        else:
            print("Invalid args. usage {qty: [int]}")
            sys.exit(1)
    
        input, output, error = select.select( [sys.stdin], [], [], 0.000001 )
        if input:
            text = sys.stdin.readline()
        else:
            raise RuntimeError()
        print(process(text, qty))
        sys.exit(0)
    except RuntimeError:
        print(f"No Text to process")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error Occurred {str(e)}")
        sys.exit(2)
    
    sys.exit(0)

