class pull():
	def __init__(self):
		activeNode = comp.ActiveTool
		self.flow = comp.CurrentFrame.FlowView
		self.saverPath = activeNode.GetInput("Clip")
		self.ActivenodeX, self.ActivenodeY= self.flow.GetPosTable(activeNode).values()


	def loader(self):
		comp.Lock()
		loader = comp.Loader({"Clip":self.saverPath})
		self.flow.SetPos(loader,self.ActivenodeX,self.ActivenodeY+2)
		comp.Unlock()

pull().loader()
