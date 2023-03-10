import asyncio
import sys

async def run_code_async(code):

    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Read one line of output.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Wait for the subprocess exit.
    await proc.wait()
    return line

if __name__ == '__main__':
    code = 'import datetime; print(datetime.datetime.now())'

    date = asyncio.run(run_code_async(code))
    print(f"Current date: {date}")