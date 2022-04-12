extends KinematicBody2D

class_name player

#they dont change
var speed = 50
var jump_power = 900
var stopping_friction = 0.6
var running_friction = 0.9
var gravity = 45
#things that do change (sorrta)
var ammo = 30 
var jumps_left = 2
var dash_direction = Vector2(1,0)
var can_dash = false
var dashing = false
var health = 3
var can_shoot = true

#misc
var vel = Vector2()

#preloads the bullet
const BULLET = preload("res://main/Character Controller/bullet.gd")



func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_HIDDEN)

	

func _physics_process(delta):
	run(delta)
	jump()
	dash()
	friction()
	gravity()
	vel = move_and_slide(vel, Vector2.UP)
	
#shooting
	if Input.is_action_just_pressed("shoot") and can_shoot and ammo > 0:
		var bullet = BULLET.instance()
		if sign($Position2D.position.x) == 1:
			bullet.set_bullet_direction(1)
		else:
			bullet.set_bullet_direction(-1)
		get_parent().add_child(bullet)
		bullet.position = $Position2D.global_position






func run(delta):
	#print(health)
	#print(ammo)
	if Input.is_action_pressed("right"):
		vel.x += speed
		$Sprite.flip_h = false
		if sign ($Position2D.position.x) == -1:
			$Position2D.position.x *= -1
	if Input.is_action_pressed("left"):
		vel.x -= speed
		$Sprite.flip_h = true
		if sign ($Position2D.position.x) == 1:
			$Position2D.position.x *= -1
	if Input.is_action_just_pressed("shoot"):
		ammo -= 1
		




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
		yield(get_tree().create_timer(0.2), "timeout")
		dashing = false


func next_to_wall():
	return next_to_left_wall() or next_to_right_wall()
	
func next_to_left_wall():
	return $LeftWallRaycast1.is_colliding() or $LeftWallRaycast2.is_colliding()

func next_to_right_wall():
	return $RightWallRaycast1.is_colliding() or $RightWallRaycast2.is_colliding()


func take_damage():
	get_tree().change_scene("res://main.tscn")
	health =- 1


#i forgor
#most of this is someone elses code
#dont know who though



func _on_VisibilityNotifier2D_screen_exited():
	health =- 1
	take_damage()

