import bge
import Rasterizer

PLAYER_MAX_SPEED = 10
PLAYER_ACCEL = 80

def main():
    print("Player script start :p")

    cont = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    player = cont.owner
    
    keyboard = bge.logic.keyboard
    mouse = bge.logic.mouse
    cam = scene.objects.get("Camera") 
    k = bge.logic.KX_INPUT_ACTIVE
    
    ground_sensor = cont.sensors["touch_ground"]
    #print(bge.types.KX_TouchSensor(ground_sensor).hitObject)
    #print(ground_sensor.status == bge.logic.KX_SENSOR_ACTIVE)

    # mouse look
    # apply rotation and reset mouse position
    cam.applyRotation([mouse.position[1]* -1, 0, 0], True)
    player.applyRotation([0, 0, mouse.position[0]* -1], True)
    Rasterizer.setMousePosition(0,0)
    
    player_vel = player.getLinearVelocity(True)

    # controls
    
    # crouching
    if k == keyboard.events[bge.events.LEFTCTRLKEY]:
        player.localScale.z = 0.9
    else:
        player.localScale.z = 1.8
        
    # if touching ground
    if ground_sensor.hitObject != None:
        if keyboard.events[bge.events.COMMAKEY] == k:
            if player_vel[1] < PLAYER_MAX_SPEED:
                player.applyForce([0,80,0], True)
        if keyboard.events[bge.events.OKEY] == k:
            if player_vel[1] > -PLAYER_MAX_SPEED:
                player.applyForce([0,-80,0], True)
        if keyboard.events[bge.events.AKEY] == k:
            if player_vel[0] > -PLAYER_MAX_SPEED:
                player.applyForce([-80,0,0], True)
        if keyboard.events[bge.events.EKEY] == k:
            if player_vel[0] < PLAYER_MAX_SPEED:
                player.applyForce([80,0,0], True)
        if keyboard.events[bge.events.SPACEKEY] == k:
            if player_vel[0] < PLAYER_MAX_SPEED:
                player.applyForce([0,0,160], True)

            
main()
