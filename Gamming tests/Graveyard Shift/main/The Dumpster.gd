extends KinematicBody2D

class_name Player

var speed = 50
var jump_power = 800
var stopping_friction = 0.6
var running_friction = 0.9
var gravity = 30

var vel = Vector2()

var jumps_left = 2
var dash_direction = Vector2(1,0)
var can_dash = false
var dashing = false




func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_HIDDEN)

func _input(event):
	if Input.is_action_just_pressed("ui_cancel"):
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)

func _physics_process(delta):
	run(delta)
	jump()
	dash()
	friction()
	gravity()
	vel = move_and_slide(vel, Vector2.UP)


func run(delta):
	if Input.is_action_pressed("right"):
		vel.x += speed
		$Steven.flip_h = false
	if Input.is_action_pressed("left"):
		vel.x -= speed
		$Steven.flip_h = true


func jump():
	# I can jump when I'm on floor or next to the wall
	if is_on_floor() or next_to_wall():
		jumps_left = 2 # Recharge double-jump. 
	
	if Input.is_action_just_pressed("jump") and jumps_left > 0:
		if vel.y > 0: vel.y = 0 # if I'm falling - ignore fall velocity
		vel.y -= jump_power
		jumps_left -= 1
		# Jump away from the wall
		if not is_on_floor() and next_to_left_wall():
			vel.x += jump_power
		if not is_on_floor() and next_to_right_wall():
			vel.x -= jump_power
	
	# If I'm still going up and have released the jump button - cut off the jump and start falling down
	if Input.is_action_just_released("jump") and vel.y < 0:
		vel.y = 0


func friction():
	# When I hold the key
	var running = Input.is_action_pressed("left") or Input.is_action_pressed("right")
	if not running and is_on_floor():
		vel.x *= stopping_friction
	else:
		vel.x *= running_friction


func gravity():
	if not dashing:
		vel.y += gravity
	if vel.y > 800: 
		vel.y = 800 # clamp falling speed
	if next_to_wall() and vel.y > 100: 
		vel.y = 100 # wall slide


func dash():
	if is_on_floor():
		can_dash = true # recharges when player touches the floor

	if Input.is_action_pressed("right"):
		dash_direction = Vector2(1,0)
	if Input.is_action_pressed("left"):
		dash_direction = Vector2(-1,0)

	if Input.is_action_just_pressed("dash") and can_dash:
		vel = dash_direction.normalized() * 2000
		can_dash = false
		dashing = true # turn off gravity while dashing
		yield(get_tree().create_timer(0.5), "timeout")
		dashing = false


func next_to_wall():
	return next_to_left_wall() or next_to_right_wall()
	
func next_to_left_wall():
	return $LeftWallRaycast1.is_colliding() or $LeftWallRaycast2.is_colliding()

func next_to_right_wall():
	return $RightWallRaycast1.is_colliding() or $RightWallRaycast2.is_colliding()


func take_damage():
	get_tree().change_scene("res://Levels/Level02.tscn")