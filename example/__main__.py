# The MIT License (MIT)
#
# Copyright (c) 2020 Artipie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import tempfile
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import requests


def get_values(file_name):
    """
    Download and read file from Artipie central
    :type file_name: str File name
    :return Array obtained from the downloaded file
    """
    rq = requests.get('https://central.artipie.com/olenagerasimova/data/' + file_name)
    if rq.status_code == 200:
        fd, path = tempfile.mkstemp()
        try:
            open(path, 'w').write(rq.text)
            return np.fromfile(path, sep='\r\n')
        finally:
            os.close(fd)


labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L']
red = '#FFE9E9'
yellow = '#FFFFED'
green = '#F6FFF6'

maximum = 8
phi = np.arange(0, 2 * np.pi + 0.1, 0.1)
circle1 = [8 for _ in range(len(phi))]
circle2 = [6 for _ in range(len(phi))]
circle3 = [5 for _ in range(len(phi))]
circle4 = [3 for _ in range(len(phi))]
circle5 = [2 for _ in range(len(phi))]

x = np.arange(0, 2 * np.pi + np.pi / 7, np.pi / 6)
y1 = get_values('y1.dat')
y2 = get_values('y2.dat')
y3 = get_values('y3.dat')

ax = plt.subplot(111, projection='polar')
ax.set_rmax(maximum)

ax.plot(phi, circle1, color='black', lw='0.5')
ax.fill(phi, circle1, red)

ax.plot(phi, circle2, color='black', lw='0.5')
ax.fill(phi, circle2, yellow)

ax.plot(phi, circle3, color='black', lw='0.5')
ax.fill(phi, circle3, green)

ax.plot(phi, circle4, color='black', lw='0.5')
ax.fill(phi, circle4, yellow)

ax.plot(phi, circle5, color='black', lw='0.5')
ax.fill(phi, circle5, red)

ax.plot(x, y1, c='r', lw=3)
ax.plot(x, y2, c='b', lw=3)
ax.plot(x, y3, c='green', lw=3)

ax.xaxis.set_major_locator(ticker.IndexLocator(base=np.pi / 6, offset=0))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(labels))

ax.set_rticks([])

if __name__ == '__main__':
    plt.show()
