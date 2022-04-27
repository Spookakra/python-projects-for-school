extends KinematicBody2D

var speed = 650  # speed in pixels/sec
var stopping_friction = 0.6
var running_friction = 0.9

var velocity = Vector2.ZERO
var vel = Vector2()

const BULLET = preload("res://Bullet.tscn")

func _physics_process(delta):
	move(delta)
	friction()
	shoot()
	velocity = move_and_slide(velocity)

func shoot():
		var bullet = BULLET.instance()
		if Input.is_action_just_pressed("shoot_right"):
			bullet.set_bullet_direction(1)
			get_parent().add_child(bullet)
			bullet.position = $Position2D.global_position
		elif Input.is_action_just_pressed("shoot_left"):
			bullet.set_bullet_direction(-1)
			get_parent().add_child(bullet)
			bullet.position = $Position2D.global_position
		elif Input.is_action_just_pressed("shoot_up"):
			bullet.set_bullet_direction(-0.5)
			get_parent().add_child(bullet)
			bullet.position = $Position2D.global_position
		elif Input.is_action_just_pressed("shoot_down"):
			bullet.set_bullet_direction(0.5)
			get_parent().add_child(bullet)
			bullet.position = $Position2D.global_position


		


func friction():
	# When I hold the key
	var running = Input.is_action_pressed("left") or Input.is_action_pressed("right") or Input.is_action_pressed("up") or Input.is_action_pressed("down")
	if not running:
		vel.x *= stopping_friction
		vel.y *= stopping_friction
	else:
		vel.x *= running_friction
		vel.y *= running_friction

func move(delta):
	velocity = Vector2.ZERO
	if Input.is_action_pressed('right'):
		velocity.x += 1
	if Input.is_action_pressed('left'):
		velocity.x -= 1
	if Input.is_action_pressed('down'):
		velocity.y += 1
	if Input.is_action_pressed('up'):
		velocity.y -= 1
	# Make sure diagonal movement isn't faster
	velocity = velocity.normalized() * speed


