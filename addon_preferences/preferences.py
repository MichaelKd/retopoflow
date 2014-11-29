import bpy
from bpy.types import AddonPreferences
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatVectorProperty, FloatProperty

class RetopoFlowPreferences(AddonPreferences):
    bl_idname = __package__
    
    def update_theme(self, context):
        print('theme updated to ' + str(theme))

    # Theme definitions
    theme = EnumProperty(
        items=[
            ('blue', 'Blue', 'Blue color scheme'),
            ('green', 'Green', 'Green color scheme'),
            ('orange', 'Orange', 'Orange color scheme'),
            ],
        name='theme',
        default='blue'
        )

    def rgba_to_float(r, g, b, a):
        return (r/255.0, g/255.0, b/255.0, a/255.0)

    theme_colors_active = {
        'blue': rgba_to_float(105, 246, 113, 255),
        'green': rgba_to_float(102, 165, 240, 255),
        'orange': rgba_to_float(102, 165, 240, 255)
    }
    theme_colors_selection = {
        'blue': rgba_to_float(105, 246, 113, 255),
        'green': rgba_to_float(102, 165, 240, 255),
        'orange': rgba_to_float(102, 165, 240, 255)
    }
    theme_colors_mesh = {
        'blue': rgba_to_float(102, 165, 240, 255),
        'green': rgba_to_float(105, 246, 113, 255),
        'orange': rgba_to_float(254, 145, 0, 255)
    }

    # User settings
    show_segment_count = BoolProperty(
        name='Show Selected Segment Count',
        description='Show segment count on selection',
        default=True
        )

    # Tool settings
    contour_panel_settings = BoolProperty(
        name="Show Contour Settings",
        description = "Show the Contour settings",
        default=False,
        )

    # System settings
    quad_prev_radius = IntProperty(
        name="Pixel Brush Radius",
        description="Pixel brush size",
        default=15,
        )

    undo_depth = IntProperty(
        name="Undo Depth",
        description="Max number of undo steps",
        default=15,
        )
    
    show_edges = BoolProperty(
            name="Show Span Edges",
            description = "Display the extracted mesh edges. Usually only turned off for debugging",
            default=True,
            )
    
    show_ring_edges = BoolProperty(
            name="Show Ring Edges",
            description = "Display the extracted mesh edges. Usually only turned off for debugging",
            default=True,
            )

    draw_widget = BoolProperty(
            name="Draw Widget",
            description = "Turn display of widget on or off",
            default=True,
            )
    
    show_axes = BoolProperty(
            name = "show_axes",
            description = "Show Cut Axes",
            default = False)

    show_experimental = BoolProperty(
            name="Enable Experimental",
            description = "Enable experimental features and functions that are still in development, useful for experimenting and likely to crash",
            default=False,
            )
    
    vert_size = IntProperty(
            name="Vertex Size",
            default=4,
            min = 1,
            max = 10,
            )
    edge_thick = IntProperty(
            name="Edge Thickness",
            default=1,
            min=1,
            max=10,
            )

    theme = EnumProperty(
        items=[
            ('blue', 'Blue', 'Blue color scheme'),
            ('green', 'Green', 'Green color scheme'),
            ('orange', 'Orange', 'Orange color scheme'),
            ],
        name='theme',
        default='blue'
        )
    
    #TODO  Theme this out nicely :-) 
    widget_color = FloatVectorProperty(name="Widget Color", description="Choose Widget color", min=0, max=1, default=(0,0,1), subtype="COLOR")
    widget_color2 = FloatVectorProperty(name="Widget Color", description="Choose Widget color", min=0, max=1, default=(1,0,0), subtype="COLOR")
    widget_color3 = FloatVectorProperty(name="Widget Color", description="Choose Widget color", min=0, max=1, default=(0,1,0), subtype="COLOR")
    widget_color4 = FloatVectorProperty(name="Widget Color", description="Choose Widget color", min=0, max=1, default=(0,0.2,.8), subtype="COLOR")
    widget_color5 = FloatVectorProperty(name="Widget Color", description="Choose Widget color", min=0, max=1, default=(.9,.1,0), subtype="COLOR")
 
    handle_size = IntProperty(
            name="Handle Vertex Size",
            default=8,
            min = 1,
            max = 10,
            )
    
    line_thick = IntProperty(
            name="Line Thickness",
            default=1,
            min = 1,
            max = 10,
            )
    
    stroke_thick = IntProperty(
            name="Stroke Thickness",
            description = "Width of stroke lines drawn by user",
            default=1,
            min = 1,
            max = 10,
            )
    
    auto_align = BoolProperty(
            name="Automatically Align Vertices",
            description = "Attempt to automatically align vertices in adjoining edgeloops. Improves outcome, but slows performance",
            default=True,
            )
    
    live_update = BoolProperty(
            name="Live Update",
            description = "Will live update the mesh preview when transforming cut lines. Looks good, but can get slow on large meshes",
            default=True,
            )
    
    use_x_ray = BoolProperty(
            name="X-Ray",
            description = 'Enable X-Ray on Retopo-mesh upon creation',
            default=False,
            )
    
    use_perspective = BoolProperty(
            name="Use Perspective",
            description = 'Make non parallel cuts project from the same view to improve expected outcome',
            default=True,
            )
    
    widget_radius = IntProperty(
            name="Widget Radius",
            description = "Size of cutline widget radius",
            default=25,
            min = 20,
            max = 100,
            )
    
    widget_radius_inner = IntProperty(
            name="Widget Inner Radius",
            description = "Size of cutline widget inner radius",
            default=10,
            min = 5,
            max = 30,
            )
    
    widget_thickness = IntProperty(
            name="Widget Line Thickness",
            description = "Width of lines used to draw widget",
            default=2,
            min = 1,
            max = 10,
            )
    
    widget_thickness2 = IntProperty(
            name="Widget 2nd Line Thick",
            description = "Width of lines used to draw widget",
            default=4,
            min = 1,
            max = 10,
            )
        
    arrow_size = IntProperty(
            name="Arrow Size",
            default=12,
            min=5,
            max=50,
            )   
    
    arrow_size2 = IntProperty(
            name="Translate Arrow Size",
            default=10,
            min=5,
            max=50,
            )      
    
    vertex_count = IntProperty(
            name = "Vertex Count",
            description = "The Number of Vertices Per Edge Ring",
            default=10,
            min = 3,
            max = 250,
            )
    
    ring_count = IntProperty(
        name="Ring Count",
        description="The Number of Segments Per Guide Stroke",
        default=10,
        min=3,
        max=100,
        )

    cyclic = BoolProperty(
            name = "Cyclic",
            description = "Make contour loops cyclic",
            default = False)
    
    recover = BoolProperty(
            name = "Recover",
            description = "Recover strokes from last session",
            default = False)
    
    recover_clip = IntProperty(
            name = "Recover Clip",
            description = "Number of cuts to leave out, usually set to 0 or 1",
            default=1,
            min = 0,
            max = 10,
            )
    
    search_factor = FloatProperty(
            name = "Search Factor",
            description = "Factor of existing segment length to connect a new cut",
            default=5,
            min = 0,
            max = 30,
            )
        
    intersect_threshold = FloatProperty(
            name = "Intersect Factor",
            description = "Stringence for connecting new strokes",
            default=1.,
            min = .000001,
            max = 1,
            )
    
    merge_threshold = FloatProperty(
            name = "Intersect Factor",
            description = "Distance below which to snap strokes together",
            default=1.,
            min = .000001,
            max = 1,
            )
    
    cull_factor = IntProperty(
            name = "Cull Factor",
            description = "Fraction of screen drawn points to throw away. Bigger = less detail",
            default = 4,
            min = 1,
            max = 10,
            )
    
    smooth_factor = IntProperty(
            name = "Smooth Factor",
            description = "Number of iterations to smooth drawn strokes",
            default = 5,
            min = 1,
            max = 10,
            )
    
    feature_factor = IntProperty(
            name = "Smooth Factor",
            description = "Fraction of sketch bounding box to be considered feature. Bigger = More Detail",
            default = 4,
            min = 1,
            max = 20,
            )
    
    extend_radius = IntProperty(
            name="Snap/Extend Radius",
            default=20,
            min=5,
            max=100,
            )

    undo_depth = IntProperty(
            name="Undo Depth",
            default=10,
            min = 0,
            max = 100,
            )

    ## Debug Settings
    show_debug = BoolProperty(
            name="Show Debug Settings",
            description = "Show the debug settings, useful for troubleshooting",
            default=False,
            )

    debug = IntProperty(
        name="Debug Level",
        default=1,
        min=0,
        max=4,
        )

    raw_vert_size = IntProperty(
            name="Raw Vertex Size",
            default=1,
            min = 1,
            max = 10,
            )

    simple_vert_inds = BoolProperty(
            name="Simple Inds",
            default=False,
            )
    
    vert_inds = BoolProperty(
            name="Vert Inds",
            description = "Display indices of the raw contour verts",
            default=False,
            )

    show_backbone = BoolProperty(
            name = "show_backbone",
            description = "Show Cut Series Backbone",
            default = False)

    show_nodes = BoolProperty(
            name = "show_nodes",
            description = "Show Cut Nodes",
            default = False)

    show_ring_inds = BoolProperty(
            name = "show_ring_inds",
            description = "Show Ring Indices",
            default = False)

    show_verts = BoolProperty(
            name="Show Raw Verts",
            description = "Display the raw contour verts",
            default=False,
            )

    show_cut_indices = BoolProperty(
            name="Show Cut Indices",
            description = "Display the order the operator stores cuts. Usually only turned on for debugging",
            default=False,
            )

    new_method = BoolProperty(
            name="New Method",
            description = "Use robust cutting, may be slower, more accurate on dense meshes",
            default=True,
            )


    def draw(self, context):
        
        # Polystrips 
        layout = self.layout

        row = layout.row(align=True)
        row.prop(self, "theme", "Theme")

        row = layout.row(align=True)
        row.prop(self, "show_segment_count")

        row = layout.row(align=True)
        row.prop(self, "debug") 

        # Contours
        layout = self.layout

        # Interaction Settings
        row = layout.row(align=True)
        row.prop(self, "auto_align")
        row.prop(self, "live_update")
        row.prop(self, "use_perspective")
        
        row = layout.row()
        row.prop(self, "use_x_ray", "Enable X-Ray at Mesh Creation")
        
        # Visualization Settings
        box = layout.box().column(align=False)
        row = box.row()
        row.label(text="Stroke And Loop Settings")        

        row = box.row(align=False)
        row.prop(self, "handle_size", text="Handle Size")
        row.prop(self, "stroke_thick", text="Stroke Thickness")

        row = box.row(align=False)
        row.prop(self, "show_edges", text="Show Edge Loops")
        row.prop(self, "line_thick", text ="Edge Thickness")
        
        row = box.row(align=False)
        row.prop(self, "show_ring_edges", text="Show Edge Rings")
        row.prop(self, "vert_size")

        row = box.row(align=True)
        row.prop(self, "show_cut_indices", text = "Edge Indices")
        
        # Widget Settings
        box = layout.box().column(align=False)
        row = box.row()
        row.label(text="Widget Settings")

        row = box.row()
        row.prop(self,"draw_widget", text = "Display Widget")

        if self.draw_widget:
            row = box.row()
            row.prop(self, "widget_radius", text="Radius")
            row.prop(self,"widget_radius_inner", text="Active Radius")
            
            row = box.row()
            row.prop(self, "widget_thickness", text="Line Thickness")
            row.prop(self, "widget_thickness2", text="2nd Line Thickness")
            row.prop(self, "arrow_size", text="Arrow Size")
            row.prop(self, "arrow_size2", text="Translate Arrow Size")

        # Debug Settings
        box = layout.box().column(align=False)
        row = box.row()
        row.label(text="Debug Settings")

        row = box.row()
        row.prop(self, "show_debug", text="Show Debug Settings")
        
        if self.show_debug:
            row = box.row()
            row.prop(self, "new_method")
            row.prop(self, "debug")
            
            
            row = box.row()
            row.prop(self, "vert_inds", text="Show Vertex Indices")
            row.prop(self, "simple_vert_inds", text="Show Simple Indices")

            row = box.row()
            row.prop(self, "show_verts", text="Show Raw Vertices")
            row.prop(self, "raw_vert_size")
            
            row = box.row()
            row.prop(self, "show_backbone", text="Show Backbone")
            row.prop(self, "show_nodes", text="Show Cut Nodes")
            row.prop(self, "show_ring_inds", text="Show Ring Indices")


def register():
    bpy.utils.register_class(RetopoFlowPreferences)

def unregister():
    bpy.utils.unregister_class(RetopoFlowPreferences)
