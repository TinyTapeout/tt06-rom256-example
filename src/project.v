/*
 * tt_um_rom256_example.v
 *
 * SPDX-License-Identifier: Apache-2.0
 * Copyright (c) 2024 Tiny Tapeout
 * Author: Uri Shaked
 */

`default_nettype none

module tt_um_rom256_example (
	input  wire [7:0] ui_in,	// Dedicated inputs
	output wire [7:0] uo_out,	// Dedicated outputs
	input  wire [7:0] uio_in,	// IOs: Input path
	output wire [7:0] uio_out,	// IOs: Output path
	output wire [7:0] uio_oe,	// IOs: Enable path (active high: 0=input, 1=output)
	input  wire       ena,
	input  wire       clk,
	input  wire       rst_n
);

	assign uio_oe  = 8'h00;
	assign uio_out = 8'h00;

	sky130_rom_256 rom1 (
		.clk0(clk),
		.cs0(rst_n),
		.addr0(ui_in),
		.dout0(uo_out)
	);

endmodule // tt_um_rom256_example
