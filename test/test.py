# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT
# Author: Uri Shaked

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_rom(dut):
  dut._log.info("Start")
  
  # Our example module doesn't use clock and reset, but we show how to use them here anyway.
  clock = Clock(dut.clk, 10, units="us")
  cocotb.start_soon(clock.start())

  # Reset
  dut._log.info("Reset")
  dut.ena.value = 1
  dut.ui_in.value = 0
  dut.uio_in.value = 0
  dut.rst_n.value = 0
  await ClockCycles(dut.clk, 10)
  dut.rst_n.value = 1
  await ClockCycles(dut.clk, 1)

  # Set the input values, wait one clock cycle, and check the output
  dut._log.info("Test ROM byte @ 0x00")
  dut.ui_in.value = 0
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 0x1f

  dut._log.info("Test ROM byte @ 0xef")
  dut.ui_in.value = 0xef
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 0xd1
