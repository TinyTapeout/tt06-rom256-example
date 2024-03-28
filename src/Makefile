# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024, Tiny Tapeout LTD
# Author: Uri Shaked

ROM_BIN = rom256.bin
ROM_HEX = $(ROM_BIN:.bin=.hex)

$(ROM_HEX): $(ROM_BIN)
	hexdump -v -e '1/1 "0x%02x "' $< > $@

.PHONY: clean
clean:
	rm -f $(ROM_HEX)