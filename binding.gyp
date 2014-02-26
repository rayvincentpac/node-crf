{
  "targets": [
    {
      "target_name": "nodecrf",
      "sources": [ "node-crf.cpp" ],
      "include_dirs":[
        "include"
      ],
      "link_settings":{
        "libraries":[
          "libcrfpp.dylib"
        ]
      },
      "conditions":[
        ['OS=="win"',{
          "link_settings":{
            "libraries":{
              "libcrfpp.dll"
            }
          }
        }]
      ]
    }
  ]
}
