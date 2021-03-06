import unittest,inspect

def get_prop_set(class_object):
    #all this does is get a list of every property implemented by the object that is not present in the baseclasses of said object
    #note it wont detect overridden properties!
    base_classes = list(inspect.getmro(class_object))
    base_classes.remove(class_object)
    base_properties = []
    for base_class in base_classes:
        base_properties.extend(dir(base_class))
    class_properties = set(dir(class_object)).difference(set(base_properties))
    return class_properties


#Glyph Baseclasses
class TestBaseGlyph(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import BaseGlyph
        self.test_glyph = BaseGlyph()        

    def test_expected_properties(self):
        expected_properties = set(['visible','margin','halign','valign','radius_units','length_units','angle_units','start_angle_units','end_angle_units'])
        actual_properties = get_prop_set(type(self.test_glyph))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):                
        self.assertEqual(self.test_glyph.radius_units, 'screen')        
        self.assertEqual(self.test_glyph.length_units, 'screen')        
        self.assertEqual(self.test_glyph.angle_units, 'deg')        
        self.assertEqual(self.test_glyph.start_angle_units, 'deg')        
        self.assertEqual(self.test_glyph.end_angle_units, 'deg')

        self.test_glyph.radius_units = 'data'   
        self.test_glyph.length_units = 'data'
        self.test_glyph.angle_units = 'rad'
        self.test_glyph.start_angle_units = 'rad'
        self.test_glyph.end_angle_units = 'rad'     

    def test_to_glyphspec(self):
        self.assertEqual(self.test_glyph.to_glyphspec(), {'type':'BaseGlyph'})
        self.test_glyph.visible = False
        self.test_glyph.margin = 5
        self.assertEqual(self.test_glyph.to_glyphspec(), {'visible': False, 'margin': 5, 'type': 'BaseGlyph'})
    
    def test_constructor(self):
        from bokeh.glyphs import BaseGlyph
        test_glyph = BaseGlyph(visible=True,margin=8)
        self.assertEqual(test_glyph.to_glyphspec(), {'visible': True, 'margin': 8, 'type': 'BaseGlyph'})

#Basic Shapes
class TestMarker(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Marker
        self.test_marker = Marker()

    def test_expected_properties(self):
        expected_properties = set(['x','y','size'])
        actual_properties = get_prop_set(type(self.test_marker))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_marker.size , {'default':4,'field':None})
        self.assertEqual(self.test_marker.x ,'x')
        self.assertEqual(self.test_marker.y ,'y')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_marker.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'Marker', 'size': {'units': 'screen', 'field': None, 'default': 4}})
        self.test_marker.x = 20
        self.test_marker.y = 50
        self.test_marker.size = 100
        self.assertEqual(self.test_marker.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'value': 50}, 'x': {'units': 'data', 'value': 20}, 'type': 'Marker', 'size': {'units': 'screen', 'value': 100}})

class TestCircle(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Circle
        self.test_circle = Circle()

    def test_expected_properties(self):        
        expected_properties = set(['radius'])
        actual_properties = get_prop_set(type(self.test_circle))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_circle.radius , {'default':4,'field':None})
        self.assertEqual(self.test_circle.__view_model__,'circle')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_circle.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'radius': {'units': 'screen', 'field': None, 'default': 4}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'circle', 'size': {'units': 'screen', 'field': None, 'default': 4}})
        self.test_circle.radius = 500
        self.assertEqual(self.test_circle.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'radius': {'units': 'screen', 'value': 500}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'circle', 'size': {'units': 'screen', 'field': None, 'default': 4}})


class TestSquare(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Square
        self.test_square = Square()

    def test_expected_properties(self):
        expected_properties = set(['angle'])
        actual_properties = get_prop_set(type(self.test_square))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_square.__view_model__,'square')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_square.to_glyphspec(), {'line_color': {'value': 'black'}, 'angle': {'units': 'data', 'field': 'angle'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'square', 'size': {'units': 'screen', 'field': None, 'default': 4}})
        self.test_square.angle = 90
        self.assertEqual(self.test_square.to_glyphspec(), {'line_color': {'value': 'black'}, 'angle': {'units': 'data', 'value': 90}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'square', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestTriangle(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Triangle
        self.test_triangle = Triangle()

    def test_expected_values(self):
        self.assertEqual(self.test_triangle.__view_model__,'triangle')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_triangle.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'triangle', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestCross(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Cross
        self.test_cross = Cross()

    def test_expected_values(self):
        self.assertEqual(self.test_cross.__view_model__,'cross')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_cross.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'cross', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestXmarker(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Xmarker
        self.test_x_marker = Xmarker()

    def test_expected_values(self):
        self.assertEqual(self.test_x_marker.__view_model__,'x')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_x_marker.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'x', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestDiamond(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Diamond
        self.test_diamond = Diamond()

    def test_expected_values(self):
        self.assertEqual(self.test_diamond.__view_model__,'diamond')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_diamond.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'diamond', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestInvertedTriangle(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import InvertedTriangle
        self.test_inverted_triangle = InvertedTriangle()

    def test_expected_values(self):
        self.assertEqual(self.test_inverted_triangle.__view_model__,'inverted_triangle')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_inverted_triangle.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'inverted_triangle', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestSquareX(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import SquareX
        self.test_square_x = SquareX()

    def test_expected_values(self):
        self.assertEqual(self.test_square_x.__view_model__,'square_x')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_square_x.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'square_x', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestAsterisk(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Asterisk
        self.test_asterisk = Asterisk()

    def test_expected_values(self):
        self.assertEqual(self.test_asterisk.__view_model__,'asterisk')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_asterisk.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'asterisk', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestDiamondCross(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import DiamondCross
        self.test_diamond_cross = DiamondCross()

    def test_expected_values(self):
        self.assertEqual(self.test_diamond_cross.__view_model__,'diamond_cross')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_diamond_cross.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'diamond_cross', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestCircleCross(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import CircleCross
        self.test_circle_cross =CircleCross()

    def test_expected_values(self):
        self.assertEqual(self.test_circle_cross.__view_model__,'circle_cross')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_circle_cross.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'circle_cross', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestHexStar(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import HexStar
        self.test_hex_star = HexStar()

    def test_expected_values(self):
        self.assertEqual(self.test_hex_star.__view_model__,'hexstar')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_hex_star.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'hexstar', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestSquareCross(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import SquareCross
        self.test_square_cross = SquareCross()

    def test_expected_values(self):
        self.assertEqual(self.test_square_cross.__view_model__,'square_cross')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_square_cross.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'square_cross', 'size': {'units': 'screen', 'field': None, 'default': 4}})

class TestCircleX(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import CircleX
        self.test_circle_x = CircleX()

    def test_expected_values(self):
        self.assertEqual(self.test_circle_x.__view_model__,'circle_x')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_circle_x.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'circle_x', 'size': {'units': 'screen', 'field': None, 'default': 4}})

#More complicated shapes
class TestAnnularWedge(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import AnnularWedge
        self.test_annular_wedge = AnnularWedge()

    def test_expected_properties(self):
        expected_properties = set(['x','y','inner_radius','outer_radius','start_angle','end_angle','direction'])
        actual_properties = get_prop_set(type(self.test_annular_wedge))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_annular_wedge.__view_model__,'annular_wedge')
        self.assertEqual(self.test_annular_wedge.x,'x')
        self.assertEqual(self.test_annular_wedge.y,'y')
        self.assertEqual(self.test_annular_wedge.inner_radius, None)
        self.assertEqual(self.test_annular_wedge.outer_radius,None)
        self.assertEqual(self.test_annular_wedge.start_angle,'start_angle')
        self.assertEqual(self.test_annular_wedge.end_angle,'end_angle')

        self.assertEqual(self.test_annular_wedge.direction,'clock')
        self.test_annular_wedge.direction = 'anticlock'

    def test_to_glyphspec(self):
        self.assertEqual(self.test_annular_wedge.to_glyphspec(),{'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'start_angle': {'units': 'data', 'field': 'start_angle'}, 'end_angle': {'units': 'data', 'field': 'end_angle'}, 'outer_radius': {'units': 'data', 'field': None}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'annular_wedge', 'inner_radius': {'units': 'data', 'field': None}})
        self.test_annular_wedge.x = 50
        self.test_annular_wedge.y = 100
        self.test_annular_wedge.inner_radius = 50
        self.test_annular_wedge.outer_radius = 51
        self.test_annular_wedge.start_angle = 91 
        self.test_annular_wedge.end_angle = 92
        self.test_annular_wedge.direction = 'anticlock'
        self.assertEqual(self.test_annular_wedge.to_glyphspec(), {'line_color': {'value': 'black'}, 'direction': 'anticlock', 'inner_radius': {'units': 'data', 'value': 50}, 'start_angle': {'units': 'data', 'value': 91}, 'end_angle': {'units': 'data', 'value': 92}, 'outer_radius': {'units': 'data', 'value': 51}, 'y': {'units': 'data', 'value': 100}, 'x': {'units': 'data', 'value': 50}, 'type': 'annular_wedge', 'fill_color': {'value': 'gray'}})

class TestAnnulus(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Annulus
        self.test_annulus = Annulus()

    def test_expected_properties(self):
        expected_properties = set(['x','y','inner_radius','outer_radius'])
        actual_properties = get_prop_set(type(self.test_annulus))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_annulus.__view_model__,'annulus')
        self.assertEqual(self.test_annulus.x,'x')
        self.assertEqual(self.test_annulus.y,'y')
        self.assertEqual(self.test_annulus.inner_radius,None)
        self.assertEqual(self.test_annulus.outer_radius,None)

    def test_to_glyphspec(self):
        self.assertEqual(self.test_annulus.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'outer_radius': {'units': 'data', 'field': None}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'annulus', 'inner_radius': {'units': 'data', 'field': None}})
        self.test_annulus.x = 50
        self.test_annulus.y = 100
        self.test_annulus.inner_radius = 61
        self.test_annulus.outer_radius = 62
        self.assertEqual(self.test_annulus.to_glyphspec(), {'line_color': {'value': 'black'}, 'inner_radius': {'units': 'data', 'value': 61}, 'outer_radius': {'units': 'data', 'value': 62}, 'y': {'units': 'data', 'value': 100}, 'x': {'units': 'data', 'value': 50}, 'type': 'annulus', 'fill_color': {'value': 'gray'}})

class TestArc(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Arc
        self.test_arc = Arc()

    def test_expected_properties(self):
        expected_properties = set(['x','y','radius','start_angle','end_angle','direction'])
        actual_properties = get_prop_set(type(self.test_arc))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_arc.__view_model__,'arc')
        self.assertEqual(self.test_arc.x,'x')
        self.assertEqual(self.test_arc.y,'y')
        self.assertEqual(self.test_arc.radius,None)
        self.assertEqual(self.test_arc.start_angle,'start_angle')
        self.assertEqual(self.test_arc.end_angle,'end_angle')
        self.assertEqual(self.test_arc.direction,'clock')
        self.test_arc.direction = 'anticlock'

    def test_to_glyphspec(self):
        self.assertEqual(self.test_arc.to_glyphspec(), {'line_color': {'value': 'black'}, 'start_angle': {'units': 'data', 'field': 'start_angle'}, 'end_angle': {'units': 'data', 'field': 'end_angle'}, 'radius': {'units': 'data', 'field': None}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'arc'})
        self.test_arc.x = 50
        self.test_arc.y = 100
        self.test_arc.radius = 51
        self.test_arc.start_angle = 52
        self.test_arc.end_angle = 53
        self.test_arc.direction = 'anticlock'
        self.assertEqual(self.test_arc.to_glyphspec(), {'line_color': {'value': 'black'}, 'direction': 'anticlock', 'start_angle': {'units': 'data', 'value': 52}, 'end_angle': {'units': 'data', 'value': 53}, 'radius': {'units': 'data', 'value': 51}, 'y': {'units': 'data', 'value': 100}, 'x': {'units': 'data', 'value': 50}, 'type': 'arc'})

class TestBezier(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Bezier
        self.test_bezier = Bezier()

    def test_expected_properties(self):
        expected_properties = set(['x0','y0','x1','y1','cx0','cy0','cx1','cy1'])
        actual_properties = get_prop_set(type(self.test_bezier))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_bezier.__view_model__,'bezier')
        self.assertEqual(self.test_bezier.x0,'x0')
        self.assertEqual(self.test_bezier.y0,'y0')
        self.assertEqual(self.test_bezier.x1,'x1')
        self.assertEqual(self.test_bezier.y1,'y1')
        self.assertEqual(self.test_bezier.cx0,'cx0')
        self.assertEqual(self.test_bezier.cy0,'cy0')
        self.assertEqual(self.test_bezier.cx1,'cx1')
        self.assertEqual(self.test_bezier.cy1,'cy1')     

    def test_to_glyphspec(self):
        self.assertEqual(self.test_bezier.to_glyphspec(), {'line_color': {'value': 'black'}, 'cx0': {'units': 'data', 'field': 'cx0'}, 'cy1': {'units': 'data', 'field': 'cy1'}, 'cy0': {'units': 'data', 'field': 'cy0'}, 'cx1': {'units': 'data', 'field': 'cx1'}, 'y1': {'units': 'data', 'field': 'y1'}, 'y0': {'units': 'data', 'field': 'y0'}, 'x0': {'units': 'data', 'field': 'x0'}, 'x1': {'units': 'data', 'field': 'x1'}, 'type': 'bezier'})
        self.test_bezier.x0 = 1
        self.test_bezier.x1 = 2
        self.test_bezier.cx0 = 3
        self.test_bezier.cx1 = 4
        self.test_bezier.y0 = 5
        self.test_bezier.y1 = 6
        self.test_bezier.cy0 = 7
        self.test_bezier.cy1 = 8
        self.assertEqual(self.test_bezier.to_glyphspec(), {'cx0': {'units': 'data', 'value': 3}, 'cx1': {'units': 'data', 'value': 4}, 'cy1': {'units': 'data', 'value': 8}, 'cy0': {'units': 'data', 'value': 7}, 'line_color': {'value': 'black'}, 'y1': {'units': 'data', 'value': 6}, 'y0': {'units': 'data', 'value': 5}, 'x0': {'units': 'data', 'value': 1}, 'x1': {'units': 'data', 'value': 2}, 'type': 'bezier'})

class TestImageURI(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import ImageURI
        self.test_imageuri = ImageURI()

    def test_expected_properties(self):
        expected_properties = set(['x','y','angle',])
        actual_properties = get_prop_set(type(self.test_imageuri))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_imageuri.__view_model__,'image_uri')
        self.assertEqual(self.test_imageuri.x,'x')
        self.assertEqual(self.test_imageuri.y,'y')
        self.assertEqual(self.test_imageuri.angle,'angle')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_imageuri.to_glyphspec(), {'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'angle': {'units': 'data', 'field': 'angle'}, 'type': 'image_uri'})
        self.test_imageuri.x = 50
        self.test_imageuri.y = 51
        self.test_imageuri.angle = 90
        self.assertEqual(self.test_imageuri.to_glyphspec(), {'y': {'units': 'data', 'value': 51}, 'x': {'units': 'data', 'value': 50}, 'angle': {'units': 'data', 'value': 90}, 'type': 'image_uri'})


class TestImageRGBA(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import ImageRGBA
        self.test_imagergba = ImageRGBA()

    def test_expected_properties(self):
        expected_properties = set(['image','width','height','x','y','dw','dh',])
        actual_properties = get_prop_set(type(self.test_imagergba))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_imagergba.image,'image')
        self.assertEqual(self.test_imagergba.width,'width')
        self.assertEqual(self.test_imagergba.height,'height')
        self.assertEqual(self.test_imagergba.x,'x')
        self.assertEqual(self.test_imagergba.y,'y')
        self.assertEqual(self.test_imagergba.dw,'dw')
        self.assertEqual(self.test_imagergba.dh,'dh')
        self.assertEqual(self.test_imagergba.__view_model__,'image_rgba')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_imagergba.to_glyphspec(), {'dh': {'units': 'data', 'field': 'dh'}, 'image': {'units': 'data', 'field': 'image'}, 'height': {'units': 'data', 'field': 'height'}, 'width': {'units': 'data', 'field': 'width'}, 'dw': {'units': 'data', 'field': 'dw'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'image_rgba'})
        self.test_imagergba.image = 'image image image'
        self.test_imagergba.width = 500
        self.test_imagergba.height = 600
        self.test_imagergba.x = 50
        self.test_imagergba.y = 51
        self.test_imagergba.dw = 53
        self.test_imagergba.dh = 54
        self.assertEqual(self.test_imagergba.to_glyphspec(), {'dh': {'units': 'data', 'value': 54}, 'image': {'units': 'data', 'field': 'image image image'}, 'height': {'units': 'data', 'value': 600}, 'width': {'units': 'data', 'value': 500}, 'x': {'units': 'data', 'value': 50}, 'y': {'units': 'data', 'value': 51}, 'dw': {'units': 'data', 'value': 53}, 'type': 'image_rgba'})

class TestLine(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Line
        self.test_line = Line()

    def test_expected_properties(self):
        expected_properties = set(['x','y'])
        actual_properties = get_prop_set(type(self.test_line))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_line.x,'x')
        self.assertEqual(self.test_line.y,'y')
        self.assertEqual(self.test_line.__view_model__,'line')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_line.to_glyphspec(), {'line_color': {'value': 'black'}, 'y': {'units': 'data', 'field': 'y'}, 'type': 'line', 'x': {'units': 'data', 'field': 'x'}})
        self.test_line.x = 50
        self.test_line.y = 51
        self.assertEqual(self.test_line.to_glyphspec(), {'y': {'units': 'data', 'value': 51}, 'x': {'units': 'data', 'value': 50}, 'type': 'line', 'line_color': {'value': 'black'}})

class TestMultiLine(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import MultiLine
        self.test_multiline = MultiLine()

    def test_expected_properties(self):
        expected_properties = set(['xs','ys'])
        actual_properties = get_prop_set(type(self.test_multiline))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_multiline.xs,'xs')
        self.assertEqual(self.test_multiline.ys,'ys')
        self.assertEqual(self.test_multiline.__view_model__,'multi_line')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_multiline.to_glyphspec(), {'line_color': {'value': 'black'}, 'xs': {'units': 'data', 'field': 'xs'}, 'ys': {'units': 'data', 'field': 'ys'}, 'type': 'multi_line'})
        self.test_multiline.xs = 50
        self.test_multiline.ys = 51
        self.assertEqual(self.test_multiline.to_glyphspec(), {'line_color': {'value': 'black'}, 'xs': {'units': 'data', 'value': 50}, 'ys': {'units': 'data', 'value': 51}, 'type': 'multi_line'})

class TestOval(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Oval
        self.test_oval = Oval()

    def test_expected_properties(self):
        expected_properties = set(['x','y','width','height','angle'])
        actual_properties = get_prop_set(type(self.test_oval))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_oval.x,'x')
        self.assertEqual(self.test_oval.y,'y')
        self.assertEqual(self.test_oval.width,'width')
        self.assertEqual(self.test_oval.height,'height')
        self.assertEqual(self.test_oval.angle,'angle')
        self.assertEqual(self.test_oval.__view_model__,'oval')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_oval.to_glyphspec(), {'line_color': {'value': 'black'}, 'angle': {'units': 'data', 'field': 'angle'}, 'fill_color': {'value': 'gray'}, 'height': {'units': 'data', 'field': 'height'}, 'width': {'units': 'data', 'field': 'width'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'oval'})
        self.test_oval.x = 50
        self.test_oval.y = 51
        self.test_oval.width = 500
        self.test_oval.height = 501
        self.test_oval.angle = 90
        self.assertEqual(self.test_oval.to_glyphspec(), {'line_color': {'value': 'black'}, 'angle': {'units': 'data', 'value': 90}, 'fill_color': {'value': 'gray'}, 'height': {'units': 'data', 'value': 501}, 'width': {'units': 'data', 'value': 500}, 'y': {'units': 'data', 'value': 51}, 'x': {'units': 'data', 'value': 50}, 'type': 'oval'})


class TestPatch(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Patch
        self.test_patch = Patch()

    def test_expected_properties(self):
        expected_properties = set(['x','y'])
        actual_properties = get_prop_set(type(self.test_patch))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_patch.x,'x')
        self.assertEqual(self.test_patch.y,'y')
        self.assertEqual(self.test_patch.__view_model__,'patch')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_patch.to_glyphspec(), {'line_color': {'value': 'black'}, 'y': {'units': 'data', 'field': 'y'}, 'type': 'patch', 'fill_color': {'value': 'gray'}, 'x': {'units': 'data', 'field': 'x'}})
        self.test_patch.x = 50
        self.test_patch.y = 51
        self.assertEqual(self.test_patch.to_glyphspec(), {'y': {'units': 'data', 'value': 51}, 'x': {'units': 'data', 'value': 50}, 'type': 'patch', 'fill_color': {'value': 'gray'}, 'line_color': {'value': 'black'}})

class TestPatches(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Patches
        self.test_patches = Patches()

    def test_expected_properties(self):
        expected_properties = set(['xs','ys'])
        actual_properties = get_prop_set(type(self.test_patches))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_patches.xs,'xs')
        self.assertEqual(self.test_patches.ys,'ys')
        self.assertEqual(self.test_patches.__view_model__,'patches')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_patches.to_glyphspec(), {'line_color': {'value': 'black'}, 'xs': {'units': 'data', 'field': 'xs'}, 'ys': {'units': 'data', 'field': 'ys'}, 'type': 'patches', 'fill_color': {'value': 'gray'}})
        self.test_patches.xs = 50
        self.test_patches.ys = 51
        self.assertEqual(self.test_patches.to_glyphspec(), {'line_color': {'value': 'black'}, 'xs': {'units': 'data', 'value': 50}, 'ys': {'units': 'data', 'value': 51}, 'type': 'patches', 'fill_color': {'value': 'gray'}})

class TestQuad(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Quad
        self.test_quad = Quad()

    def test_expected_properties(self):
        expected_properties = set(['left','right','bottom','top'])
        actual_properties = get_prop_set(type(self.test_quad))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_quad.left,'left')
        self.assertEqual(self.test_quad.right,'right')
        self.assertEqual(self.test_quad.bottom,'bottom')
        self.assertEqual(self.test_quad.top,'top')
        self.assertEqual(self.test_quad.__view_model__,'quad')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_quad.to_glyphspec(), {'line_color': {'value': 'black'}, 'right': {'units': 'data', 'field': 'right'}, 'fill_color': {'value': 'gray'}, 'bottom': {'units': 'data', 'field': 'bottom'}, 'top': {'units': 'data', 'field': 'top'}, 'type': 'quad', 'left': {'units': 'data', 'field': 'left'}})
        self.test_quad.left = 50
        self.test_quad.right = 51
        self.test_quad.bottom = 52
        self.test_quad.top = 53
        self.assertEqual(self.test_quad.to_glyphspec(), {'line_color': {'value': 'black'}, 'right': {'units': 'data', 'value': 51}, 'fill_color': {'value': 'gray'}, 'bottom': {'units': 'data', 'value': 52}, 'top': {'units': 'data', 'value': 53}, 'type': 'quad', 'left': {'units': 'data', 'value': 50}})

class TestQuadratic(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Quadratic
        self.test_quadratic = Quadratic()

    def test_expected_properties(self):
        expected_properties = set(['x0','y0','x1','y1','cx','cy'])
        actual_properties = get_prop_set(type(self.test_quadratic))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_quadratic.x0,'x0')
        self.assertEqual(self.test_quadratic.y0,'y0')
        self.assertEqual(self.test_quadratic.x1,'x1')
        self.assertEqual(self.test_quadratic.y1,'y1')
        self.assertEqual(self.test_quadratic.cx,'cx')
        self.assertEqual(self.test_quadratic.cy,'cy')
        self.assertEqual(self.test_quadratic.__view_model__,'quadratic')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_quadratic.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'cy': {'units': 'data', 'field': 'cy'}, 'cx': {'units': 'data', 'field': 'cx'}, 'y1': {'units': 'data', 'field': 'y1'}, 'y0': {'units': 'data', 'field': 'y0'}, 'x0': {'units': 'data', 'field': 'x0'}, 'x1': {'units': 'data', 'field': 'x1'}, 'type': 'quadratic'})
        self.test_quadratic.x0 = 1
        self.test_quadratic.x1 = 2
        self.test_quadratic.cx = 3
        self.test_quadratic.y0 = 4
        self.test_quadratic.y1 = 5
        self.test_quadratic.cy = 6
        self.assertEqual(self.test_quadratic.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'cy': {'units': 'data', 'value': 6}, 'cx': {'units': 'data', 'value': 3}, 'y1': {'units': 'data', 'value': 5}, 'y0': {'units': 'data', 'value': 4}, 'x0': {'units': 'data', 'value': 1}, 'x1': {'units': 'data', 'value': 2}, 'type': 'quadratic'})

class TestRay(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Ray
        self.test_ray = Ray()

    def test_expected_properties(self):
        expected_properties = set(['x','y','angle','length'])
        actual_properties = get_prop_set(type(self.test_ray))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_ray.x,'x')
        self.assertEqual(self.test_ray.y,'y')
        self.assertEqual(self.test_ray.angle,'angle')
        self.assertEqual(self.test_ray.length,'length')
        self.assertEqual(self.test_ray.__view_model__,'ray')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_ray.to_glyphspec(), {'line_color': {'value': 'black'}, 'angle': {'units': 'data', 'field': 'angle'}, 'length': {'units': 'data', 'field': 'length'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'ray'})
        self.test_ray.x = 50
        self.test_ray.y = 51
        self.test_ray.angle = 90
        self.test_ray.length = 100
        self.assertEqual(self.test_ray.to_glyphspec(), {'line_color': {'value': 'black'}, 'angle': {'units': 'data', 'value': 90}, 'length': {'units': 'data', 'value': 100}, 'y': {'units': 'data', 'value': 51}, 'x': {'units': 'data', 'value': 50}, 'type': 'ray'})

class TestRect(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Rect
        self.test_rect = Rect()

    def test_expected_properties(self):
        expected_properties = set(['x','y','width','height','angle'])
        actual_properties = get_prop_set(type(self.test_rect))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_rect.x,'x')
        self.assertEqual(self.test_rect.y,'y')
        self.assertEqual(self.test_rect.width,'width')
        self.assertEqual(self.test_rect.height,'height')   
        self.assertEqual(self.test_rect.angle,'angle')
        self.assertEqual(self.test_rect.__view_model__,'rect')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_rect.to_glyphspec(), {'line_color': {'value': 'black'}, 'angle': {'units': 'data', 'field': 'angle'}, 'fill_color': {'value': 'gray'}, 'height': {'units': 'data', 'field': 'height'}, 'width': {'units': 'data', 'field': 'width'}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'rect'})
        self.test_rect.x = 50
        self.test_rect.y = 51
        self.test_rect.width = 100
        self.test_rect.height = 200
        self.test_rect.angle = 90
        self.assertEqual(self.test_rect.to_glyphspec(), {'line_color': {'value': 'black'}, 'angle': {'units': 'data', 'value': 90}, 'fill_color': {'value': 'gray'}, 'height': {'units': 'data', 'value': 200}, 'width': {'units': 'data', 'value': 100}, 'y': {'units': 'data', 'value': 51}, 'x': {'units': 'data', 'value': 50}, 'type': 'rect'})

class TestSegment(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Segment
        self.test_segment = Segment()

    def test_expected_properties(self):
        expected_properties = set(['x0','y0','x1','y1'])
        actual_properties = get_prop_set(type(self.test_segment))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_segment.x0,'x0')
        self.assertEqual(self.test_segment.y0,'y0')
        self.assertEqual(self.test_segment.x1,'x1')
        self.assertEqual(self.test_segment.y1,'y1')
        self.assertEqual(self.test_segment.__view_model__,'segment')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_segment.to_glyphspec(), {'line_color': {'value': 'black'}, 'y1': {'units': 'data', 'field': 'y1'}, 'y0': {'units': 'data', 'field': 'y0'}, 'x0': {'units': 'data', 'field': 'x0'}, 'x1': {'units': 'data', 'field': 'x1'}, 'type': 'segment'})
        self.test_segment.x0 = 1
        self.test_segment.y0 = 2
        self.test_segment.x1 = 3
        self.test_segment.y1 = 4
        self.assertEqual(self.test_segment.to_glyphspec(), {'line_color': {'value': 'black'}, 'y1': {'units': 'data', 'value': 4}, 'y0': {'units': 'data', 'value': 2}, 'x0': {'units': 'data', 'value': 1}, 'x1': {'units': 'data', 'value': 3}, 'type': 'segment'})

class TestText(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Text
        self.test_text = Text()

    def test_expected_properties(self):
        expected_properties = set(['x','y','text','angle'])
        actual_properties = get_prop_set(type(self.test_text))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_text.x,'x')
        self.assertEqual(self.test_text.y,'y')
        self.assertEqual(self.test_text.text,None)
        self.assertEqual(self.test_text.angle,'angle')
        self.assertEqual(self.test_text.__view_model__,'text')

    def test_to_glyphspec(self):
        self.assertEqual(self.test_text.to_glyphspec(), {'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'angle': {'units': 'data', 'field': 'angle'}, 'type': 'text'})
        self.test_text.x = 50
        self.test_text.y = 51
        self.test_text.angle = 90
        self.test_text.text = 'colourless green sheep sleep furiously'
        self.assertEqual(self.test_text.to_glyphspec(), {'y': {'units': 'data', 'value': 51}, 'x': {'units': 'data', 'value': 50}, 'type': 'text', 'angle': {'units': 'data', 'value': 90}, 'text': 'colourless green sheep sleep furiously'})

class TestWedge(unittest.TestCase):
    def setUp(self):
        from bokeh.glyphs import Wedge
        self.test_wedge = Wedge()

    def test_expected_properties(self):
        expected_properties = set(['x','y','radius','start_angle','end_angle','direction'])
        actual_properties = get_prop_set(type(self.test_wedge))
        self.assertTrue(expected_properties.issubset(actual_properties))

    def test_expected_values(self):
        self.assertEqual(self.test_wedge.x,'x')
        self.assertEqual(self.test_wedge.y,'y')
        self.assertEqual(self.test_wedge.radius,None)
        self.assertEqual(self.test_wedge.start_angle,'start_angle')
        self.assertEqual(self.test_wedge.end_angle,'end_angle')
        self.assertEqual(self.test_wedge.__view_model__,'wedge')

        self.assertEqual(self.test_wedge.direction,'clock')
        self.test_wedge.direction = 'anticlock'

    def test_to_glyphspec(self):
        self.assertEqual(self.test_wedge.to_glyphspec(), {'line_color': {'value': 'black'}, 'fill_color': {'value': 'gray'}, 'start_angle': {'units': 'data', 'field': 'start_angle'}, 'end_angle': {'units': 'data', 'field': 'end_angle'}, 'radius': {'units': 'data', 'field': None}, 'y': {'units': 'data', 'field': 'y'}, 'x': {'units': 'data', 'field': 'x'}, 'type': 'wedge'})
        self.test_wedge.x = 50
        self.test_wedge.y = 51
        self.test_wedge.radius = 52
        self.test_wedge.start_angle = 53
        self.test_wedge.end_angle = 54
        self.test_wedge.direction = 'anticlock'
        self.assertEqual(self.test_wedge.to_glyphspec(), {'line_color': {'value': 'black'}, 'direction': 'anticlock', 'fill_color': {'value': 'gray'}, 'start_angle': {'units': 'data', 'value': 53}, 'end_angle': {'units': 'data', 'value': 54}, 'radius': {'units': 'data', 'value': 52}, 'y': {'units': 'data', 'value': 51}, 'x': {'units': 'data', 'value': 50}, 'type': 'wedge'})

if __name__ == "__main__":
    unittest.main()
