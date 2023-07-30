def pid_tuning(Kp,Kd,Ki):
    if(rc.controller.is_down(rc.controller.Button.A)):
        if(rc.controller.is_down(rc.controller.Trigger.RIGHT)):
            Kp+=0.05
        else:
            Kp-=0.05
    if(rc.controller.is_down(rc.controller.Button.B)):
        if(rc.controller.is_down(rc.controller.Trigger.RIGHT)):
            Kd+=0.05
        else:
            Kd-=0.05
    if(rc.controller.is_down(rc.controller.Button.X)):
        if(rc.controller.is_down(rc.controller.Trigger.RIGHT)):
            Ki+=0.05
        else:
            Ki-=0.05
