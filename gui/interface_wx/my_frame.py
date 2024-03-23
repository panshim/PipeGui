import sys
import wx
from gsnodegraph import EVT_GSNODEGRAPH_ADDNODEBTN
from nodes import OutputNode, MixNode, ImageNode, BlurNode, BlendNode, ValueNode
from gui.interface_gs import NodeGraph

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name="frame"):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)

        # Setup the node registry
        node_registry = {
            "image_nodeid": ImageNode,
            "mix_nodeid": MixNode,
            "blur_nodeid": BlurNode,
            "blend_nodeid": BlendNode,
            "value_nodeid": ValueNode,
            "output_nodeid": OutputNode
        }
        # Setup the config with datatypes and node categories
        config = {
            "image_datatype": "IMAGE",
            "node_datatypes": {
                "IMAGE": "#C6C62D",  # Yellow
                "INTEGER": "#A0A0A0",  # Grey
                "FLOAT": "#A0A0A0",  # Grey
                "VALUE": "#A0A0A0",  # Depreciated!
            },
            "input_nodes_categories": ["INPUT"],
            "node_categories": {
                "INPUT": "#E64555",  # Burgendy
                "DRAW": "#AF4467",  # Pink
                "MASK": "#084D4D",  # Blue-green
                "CONVERT": "#564B7C",  # Purple
                "FILTER": "#558333",  # Green
                "BLEND": "#498DB8",  # Light blue
                "COLOR": "#C2AF3A",  # Yellow
                "TRANSFORM": "#6B8B8B", # Blue-grey
                "OUTPUT": "#B33641"  # Red
            }
        }

        # Init the nodegraph
        ng = NodeGraph(self, registry=node_registry, config=config)

        # Add nodes to the node graph
        node1 = ng.AddNode("image_nodeid", pos=wx.Point(100, 10))
        node2 = ng.AddNode("image_nodeid", pos=wx.Point(450, 400))
        node3 = ng.AddNode("mix_nodeid", pos=wx.Point(400, 100))
        node4 = ng.AddNode("blur_nodeid", pos=wx.Point(700, 100))
        node5 = ng.AddNode("blend_nodeid", pos=wx.Point(720, 300))
        node6 = ng.AddNode("value_nodeid", pos=wx.Point(620, 430))
        node7 = ng.AddNode("output_nodeid", pos=wx.Point(1000, 290))

        # Maximize the window
        self.Maximize(True)

        # Bind events
        ng.Bind(EVT_GSNODEGRAPH_ADDNODEBTN, self.OnAddNodeMenuBtn)
        self.Bind(wx.EVT_CLOSE, self.OnDestroy)

    def OnAddNodeMenuBtn(self, event):
        print("Open add node menu")

    def OnDestroy(self, event):
        self.Destroy()