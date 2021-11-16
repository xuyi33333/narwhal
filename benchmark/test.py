from benchmark.utils import PathMaker
from benchmark.logs import LogParser


logger = LogParser.process('logs', faults=0)  
logger.print(PathMaker.result_file(
                            0,
                            4, 
                            1,
                            True,
                            800, 
                            100, 
                        ))
