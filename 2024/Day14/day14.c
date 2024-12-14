#include <stdio.h>

#define WIDE 101
#define TALL 103
#define SIZE 500

int robots[SIZE][4];
int tiles[TALL][WIDE] = {0};

void print_tiles() {
    for (int i = 0; i < TALL; ++i) {
        for (int j = 0; j < WIDE; ++j) {
            if (tiles[i][j] == 0) putchar('.');
            else putchar('0' + tiles[i][j]);
        }
        putchar('\n');
    }
}

int check_christmas_tree() {
    for (int i = 0; i < TALL; ++i) {
        int count = 0;
        for (int j = 0; j < WIDE; ++j) {
            if (tiles[i][j])
                count += 1;
            else
                count = 0;
            if (count >= 10)
                return 1;
        }
    }
    return 0;
}

int main() {
    int px, py, vx, vy;
    for (int i = 0; i < SIZE; ++i) {
        scanf("p=%d,%d v=%d,%d\n", &px, &py, &vx, &vy);
        robots[i][0] = px;
        robots[i][1] = py;
        robots[i][2] = vx;
        robots[i][3] = vy;
        tiles[py][px] += 1;
    }

    int ranges[4][4] = {
            {0, WIDE / 2,        0, TALL / 2},
            {WIDE / 2 + 1, WIDE, 0, TALL / 2},
            {0, WIDE / 2,        TALL / 2 + 1, TALL},
            {WIDE / 2 + 1, WIDE, TALL / 2 + 1, TALL}
    };
    for (int sec = 0; sec < 10000; ++sec) {
        for (int i = 0; i < SIZE; ++i) {
            px = robots[i][0];
            py = robots[i][1];
            vx = robots[i][2];
            vy = robots[i][3];

            tiles[py][px] -= 1;
            px += vx;
            if (px < 0) px += WIDE;
            px %= WIDE;
            py += vy;
            if (py < 0) py += TALL;
            py %= TALL;
            tiles[py][px] += 1;
            robots[i][0] = px;
            robots[i][1] = py;
        }
        if (check_christmas_tree()) {
            print_tiles();
            printf("Part2: %d\n", sec + 1);
            if (sec > 99)
                break;
        }
        if (sec == 99) {
            int ans1 = 1;
            int w0, w1, t0, t1;
            for (int j = 0; j < 4; ++j) {
                w0 = ranges[j][0];
                w1 = ranges[j][1];
                t0 = ranges[j][2];
                t1 = ranges[j][3];
                int n = 0;
                for (int x = w0; x < w1; ++x)
                    for (int y = t0; y < t1; ++y)
                        n += tiles[y][x];
                ans1 *= n;
            }
            printf("Part1: %d\n", ans1);
        }
    }
    return 0;
}
