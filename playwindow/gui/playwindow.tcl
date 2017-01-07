#!/usr/bin/wish

### INIT

set version {1.0}

if [info exists env(playwindow_debug)] {
    set debug $env(playwindow_debug)
} else {
    set debug 0
}

proc log {message} {
    global debug
    if {$debug} {
        set process_id [pid]
        puts "$process_id $message"
    }
}

log "start tcl_version=$tcl_version app_version=$version"

# title have to be touched before appname
wm title . PlayWindow
set target_name {playwindow}
set actual_name [tk appname $target_name]
if {$actual_name != $target_name} {
     log "already runing found. exiting"
     exit
}

canvas .r -bg black -width 100 -height 100 -highlightthickness 0 -borderwidth 0
pack .r -fill both -expand 1

### MANIPULATOR

proc canvas_manipulator {args} {
    log "canvas_manipulator: $args"
    return [.r {*}$args]
}

### INTERNALS

proc ping {{echo hi}} {
    return $echo
}

proc stop {} {
    # rename app synchronously to avoid race condition
    tk appname {hidden}
    after idle {exit 0}
}

### EVENTS

set events_queue [list]
set event_signal 0

proc reg_event {event} {
    global events_queue event_signal
    incr event_signal
    set etype [lindex $event 0]
    if {[lsearch -exact {internal_tik mouse_move mouse_leave mouse_enter configure} $etype] >= 0} {
        # collapse tiks and mouse movements
        set res {}
        foreach e $events_queue {
            if {[lindex $e 0] ne $etype} {
                 lappend res $e
            }
        }
        set events_queue $res
    }
    lappend events_queue $event
    log "events: $events_queue"
}

proc internal_tik {} {
    after 500 internal_tik
    reg_event internal_tik
}

internal_tik

bind .r <Motion> {
    reg_event [list mouse_move %x %y]
}

bind .r <ButtonPress> {
    reg_event [list mouse_button_press %x %y %b]
}

bind .r <ButtonRelease> {
    reg_event [list mouse_button_release %x %y %b]
}

bind .r <Enter> {
    reg_event [list mouse_enter %x %y]
}

bind .r <Leave> {
    reg_event [list mouse_leave %x %y]
}

bind .r <Configure> {
    reg_event [list configure %w %h]
}

bind . <KeyPress> {
    reg_event [list key_press %k %s %K]
}

bind . <KeyRelease> {
    reg_event [list key_release %k %s %K]
}

proc queue_pop {} {
    global events_queue
    set res [lindex $events_queue 0]
    set events_queue [lreplace $events_queue 0 0]
    return $res
}

proc wait {} {
    global events_queue
    if {[llength $events_queue] > 0} {
        return [queue_pop]
    }
    vwait event_signal
    return [queue_pop]
}

proc schedule {delay name} {
    after $delay [list reg_event [list alert $name]]
}

after idle {raise .}

log {mainloop...}
