import bge
import Rasterizer

PLAYER_MAX_SPEED = 10
PLAYER_ACCEL = 80

def main():

    cont = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    player = cont.owner
    
    keyboard = bge.logic.keyboard
    mouse = bge.logic.mouse
    cam = scene.objects.get("Camera")
    k = bge.logic.KX_INPUT_ACTIVE
    
    # apply rotation and reset mouse position
    cam.applyRotation([mouse.position[1]* -1, 0, 0], True)
    player.applyRotation([0, 0, mouse.position[0]* -1], True)
    Rasterizer.setMousePosition(0,0)
    
    player_vel = player.getLinearVelocity(True)

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
            player.applyForce([0,0,80], True)
            
main()
