# Copyright 2017-present Samsung Electronics Co., Ltd. and other contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from jstest.testrunner.devices import artik053, artik530, rpi2, stm32f4dis


DEVICES = {
    "stm32f4dis": stm32f4dis.STM32F4Device,
    "rpi2": rpi2.RPi2Device,
    "artik053": artik053.ARTIK053Device,
    "artik530": artik530.ARTIK530Device
}


def create_device(env):
    '''
    Create a device object for testing.
    '''
    device_class = DEVICES[env.options.device]

    return device_class(env)
