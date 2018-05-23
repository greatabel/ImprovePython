import dis

dis.dis(compile("(23, 'a', 'b', 'c')", '', 'eval'))
dis.dis(compile("[23, 'a', 'b', 'c']", '', 'eval'))