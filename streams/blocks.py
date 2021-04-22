from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        requried=True,
        help_text='Text to display',
    )

    class Meta:
        template = "streams/title_block.html"
        icon = " edit"
        label = "Title"
        help_text = " Center text to display"

class CardsBlock (blocks.StructBlock):

    cards= blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(max_length=100, help_text="Bold text for this card max length of 100 characters.")),
                ("text", blocks.TextBlock(max_length=355, help_text="Optional text for the card. Max length is 355 characters.", required=False)),
                ("image", ImageChooserBlock(help_text="Image will me auto cropped to 570px by 370px")),
            ]
        )
    )
    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"


