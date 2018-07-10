import platform

print('Hello World!')

current_platform = platform.platform()
current_computer = platform.node()

print('We run here on "' + current_computer +
      '" under ' + current_platform + ".")
