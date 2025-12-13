# Makefile for Advent of Code 2025 Day 1 (Assembly)

CC = clang
ASM = as
CFLAGS = -g
ASMFLAGS = -arch arm64

TARGET1 = day1
SOURCE1 = 1.s
TARGET2 = day1_part2
SOURCE2 = 2.s

all: $(TARGET1) $(TARGET2)

$(TARGET1): $(SOURCE1)
	$(ASM) $(ASMFLAGS) $(SOURCE1) -o $(SOURCE1:.s=.o)
	$(CC) $(CFLAGS) $(SOURCE1:.s=.o) -o $(TARGET1)

$(TARGET2): $(SOURCE2)
	$(ASM) $(ASMFLAGS) $(SOURCE2) -o $(SOURCE2:.s=.o)
	$(CC) $(CFLAGS) $(SOURCE2:.s=.o) -o $(TARGET2)

run: $(TARGET1)
	./$(TARGET1)

run2: $(TARGET2)
	./$(TARGET2)

clean:
	rm -f $(TARGET1) $(TARGET2) $(SOURCE1:.s=.o) $(SOURCE2:.s=.o)

.PHONY: all run run2 clean

