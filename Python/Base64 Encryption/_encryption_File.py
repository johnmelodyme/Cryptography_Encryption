#!/usr/bin/env python
      #              Copyright 2020 © John Melody Me
      #
      # Licensed under the Apache License, Version 2.0 (the "License");
      # you may not use this file except in compliance with the License.
      # You may obtain a copy of the License at
      #             http://www.apache.org/licenses/LICENSE-2.0
      # Unless required by applicable law or agreed to in writing, software
      # distributed under the License is distributed on an "AS IS" BASIS,
      # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
      # See the License for the specific language governing permissions and
      # limitations under the License.
      # @Author : John Melody Me
      # @Copyright: John Melody Me & Tan Sin Dee © Copyright 2020
      # @INPIREDBYGF: Cindy Tan Sin Dee <3
import base64

_userOriginalBinaryfile = input("Please Enter the Location of the file design to encrypt:  ")
with open(_userOriginalBinaryfile, "rb") as _inputFile:
      _input_file_data = _inputFile.read()
      _encodeData = base64.b64encode(_input_file_data)
      _encodeMessage = _encodeData.decode("utf-8")

      print(_encodeMessage)