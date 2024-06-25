from typing import Any

class Parser:
    def __init__(self, context:Any):
        self.context = context
        self.image_tokens = []
        self.block_map={}

feishu_code_map = {
    "plain_text": "",
    "abap": "abap",
    "ada": "ada",
    "apache": "apache",
    "apex": "apex",
    "assembly": "assembly",
    "bash": "bash",
    "csharp": "csharp",
    "cpp": "cpp",
    "c": "c",
    "cobol": "cobol",
    "css": "css",
    "coffeescript": "coffeescript",
    "d": "d",
    "dart": "dart",
    "delphi": "delphi",
    "django": "django",
    "dockerfile": "dockerfile",
    "erlang": "erlang",
    "fortran": "fortran",
    "foxpro": "foxpro",
    "go": "go",
    "groovy": "groovy",
    "html": "html",
    "htmlbars": "htmlbars",
    "http": "http",
    "haskell": "haskell",
    "json": "json",
    "java": "java",
    "javascript": "javascript",
    "julia": "julia",
    "kotlin": "kotlin",
    "latex": "latex",
    "lisp": "lisp",
    "logo": "logo",
    "lua": "lua",
    "matlab": "matlab",
    "makefile": "makefile",
    "markdown": "markdown",
    "nginx": "nginx",
    "objectivec": "objectivec",
    "openedge-abl": "openedge-abl",
    "php": "php",
    "perl": "perl",
    "postscript": "postscript",
    "powershell": "powershell",
    "prolog": "prolog",
    "protobuf": "protobuf",
    "python": "python",
    "r": "r",
    "rpg": "rpg",
    "ruby": "ruby",
    "rust": "rust",
    "sas": "sas",
    "scss": "scss",
    "sql": "sql",
    "scala": "scala",
    "scheme": "scheme",
    "scratch": "scratch",
    "shell": "shell",
    "swift": "swift",
    "thrift": "thrift",
    "typescript": "typescript",
    "vbscript": "vbscript",
    "vbnet": "vbnet",
    "xml": "xml",
    "yaml": "yaml",
}
