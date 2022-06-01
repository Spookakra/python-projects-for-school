extends Control

func _ready():
	pass 


func _on_resume_pressed():
		Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
		get_tree().paused = false
		$CenterContainer.hide()
		
func _on_Quit_pressed():
	get_tree().quit()
