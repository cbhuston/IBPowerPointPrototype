from pptx import Presentation
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
prs = Presentation()
title_only_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(title_only_slide_layout)
shapes = slide.shapes


left = Inches(0.93)  # 0.93" centers this overall set of shapes
top = Inches(3.0)
width = Inches(1.75)
height = Inches(1.0)

shape = shapes.add_shape(MSO_SHAPE.PENTAGON, left, top, width, height)
shape.text = 'Step 1'

left = left + width - Inches(0.4)
width = Inches(2.0)  # chevrons need more width for visual balance

for n in range(2, 6):
    shape = shapes.add_shape(MSO_SHAPE.CHEVRON, left, top, width, height)
    shape.text = 'Step %d' % n
    left = left + width - Inches(0.4)

left = top = width = height = Inches(1.0)
slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
)

title_only_slide_layout = prs.slide_layouts[6]
slide2 = prs.slides.add_slide(title_only_slide_layout)
shapes = slide2.shapes

height = Inches(1.5) 
width = Inches(1)
left = Inches(.5)
top = Inches(1) 

for y in range(1, 4):
    left = Inches(.5)
    for x in range(1,8):
        shape = shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)

        fill = shape.fill.type
        str(fill)

        textFotDateShape = shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height/4)
        txBoxHeight = Inches(.25)
        txBox = slide2.shapes.add_textbox(left, top, width, txBoxHeight)
        tf = txBox.text_frame
        p = tf.add_paragraph()
        p.text = "June 2018"
        p.font.size = Pt(14)

        picTop = top+Inches(.5)
        pic = slide2.shapes.add_picture('key_social_logo.png', left, picTop, height=Inches(.25))

        txBoxTop = top + Inches(1.5)
        txBox = slide2.shapes.add_textbox(left, top, width, Inches(.25))
        tf = txBox.text_frame
        p = tf.add_paragraph()
        p.text = "Bookrunner"
        p.font.size = Pt(12)
        left = left + width + Inches(.285)
    top = top + height + Inches(.33)

title_only_slide_layout = prs.slide_layouts[6]
slide3 = prs.slides.add_slide(title_only_slide_layout)
shapes = slide3.shapes

height = Inches(1.5) 
width = Inches(1)
left = Inches(.5)
top = Inches(1) 
#slide 3
for y in range(1, 4):
    left = Inches(.5)
    for x in range(1,9):
        fill = shape.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(255, 255, 255)

        shape = shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        txBoxHeight = Inches(.25)
        txBox1 = slide3.shapes.add_textbox(left, top-Inches(.33), width, txBoxHeight)
        tf = txBox1.text_frame
        p = tf.add_paragraph()
        p.alignment = PP_ALIGN.CENTER
        p.text = "June 2018"
        p.font.size = Pt(10)

        picTop = top+Inches(.4)
        pic = slide3.shapes.add_picture('key_social_logo.png', left, picTop, height=Inches(.4))
        pic.alignment = PP_ALIGN.CENTER
        txBoxTop = top + Inches(1.5)
        
        txBox3 = slide3.shapes.add_textbox(left, picTop+Inches(.1), width, Inches(.25))
        tf = txBox3.text_frame
        p = tf.add_paragraph()
        p.text = "200,000,000"
        p.font.size = Pt(10)
        p.alignment = PP_ALIGN.CENTER

        txBox3 = slide3.shapes.add_textbox(left, picTop+Inches(.23), width, Inches(.25))
        tf = txBox3.text_frame
        p = tf.add_paragraph()
        p.text = "IPO"
        p.font.size = Pt(10)
        p.alignment = PP_ALIGN.CENTER

        txBox2 = slide3.shapes.add_textbox(left, top+Inches(1), width, Inches(.25))
        tf = txBox2.text_frame
        p = tf.add_paragraph()
        p.text = "Bookrunner"
        p.font.size = Pt(10)
        p.alignment = PP_ALIGN.CENTER
        left = left + width + Inches(.285)
    top = top + height + Inches(.33)

prs.save('test.pptx')