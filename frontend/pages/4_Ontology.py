import streamlit as st
from pyvis.network import Network
import pandas as pd
    
data = {
  "superclasses": [
    "Decor",
    "Accessories",
    "Clothing",
    "Footwear"
  ],
  "Decor": {
    "classes": [
      "Home Decor",
      "Furniture"
    ],
    "Home Decor": {
      "types": [
        "Home Decor",
        "Furniture",
        "Decor",
        "Wall Art",
        "Topwear"
      ],
      "Home Decor": {
        "variants": [
          "Decorating Element",
          "Home Decor Fabric",
          "Bathroom Vanity",
          "Saree"
        ],
        "styles": [
          "Elegant Modern",
          "Patterned Crepe Fabric",
          "Modern",
          "Elegant",
          "Plain Crepe Fabric"
        ]
      },
      "Furniture": {
        "variants": [
          "Transitional Bathroom Vanity with White Carrara Quartz Top",
          "Freestanding Bathroom Vanity with White Quartz Stone Top",
          "Cultured Marble Vanity Top",
          "Modern Bathroom Vanity with White Quartz Stone Top",
          "Freestanding Bathroom Vanity",
          "Carrara Marble Vanity Top",
          "Transitional Bathroom Vanity with White Quartz Stone Top",
          "Modern Bathroom Vanity with White Quartz Top",
          "Transitional Bathroom Vanity with Brushed Nickel Accents",
          "Transitional Bathroom Vanity with Carrara Marble Top"
        ],
        "styles": [
          "Rustic Traditional",
          "Traditional",
          "Transitional Classic",
          "Modern Classic",
          "Rustic Modern",
          "Classic",
          "Traditional Classic",
          "Modern Minimalist"
        ]
      },
      "Decor": {
        "variants": [
          "Modern Vanity"
        ],
        "styles": [
          "Modern",
          "Modern Classic"
        ]
      },
      "Wall Art": {
        "variants": [
          "Wall Art"
        ],
        "styles": [
          "Minimalist",
          "Modern"
        ]
      },
      "Topwear": {
        "variants": [
          "Bathroom Countertop",
          "Counter Top"
        ],
        "styles": [
          "Carrara Marble",
          "Granite Countertop"
        ]
      }
    },
    "Furniture": {
      "types": [
        "Decor",
        "Furniture"
      ],
      "Decor": {
        "variants": [
          "Decor",
          "Modern Vanity"
        ],
        "styles": [
          "Luxury",
          "Modern",
          "Traditional"
        ]
      },
      "Furniture": {
        "variants": [
          "Bathroom Vanity",
          "Vanity"
        ],
        "styles": [
          "Decor",
          "Design Accent",
          "Furniture"
        ]
      }
    }
  },
  "Accessories": {
    "classes": [
      "Fashion Accessory",
      "Traditional Wear",
      "Timepiece",
      "Jewelry"
    ],
    "Fashion Accessory": {
      "types": [
        "Handbag",
        "Accessories",
        "Top-wear"
      ],
      "Handbag": {
        "variants": [
          "Fashion Accessory",
          "Handbag"
        ],
        "styles": [
          "Fashion Accessory",
          "Luxury Watch"
        ]
      },
      "Accessories": {
        "variants": [
          "Fashion Accessory",
          "Accessories"
        ],
        "styles": [
          "Fashion Accessory",
          "Accessories"
        ]
      },
      "Top-wear": {
        "variants": [
          "Fashion Accessory - Accessory Sub-Type: Belt",
          "Watch - Fashion Accessory - Accessory Sub-Type: Quartz Watch",
          "Fashion Accessory - Fashion Accessory Sub-Type: Quartz Watch",
          "Watch - Watch - Accessory Sub-Type: General Quartz Watch",
          "Fashion Accessory - Fashion Accessory - Accessory Sub-Type: Watch"
        ],
        "styles": [
          "Fashion Accessory",
          "Fashion Watch",
          "Accessories"
        ]
      }
    },
    "Traditional Wear": {
      "types": [
        "Headwear"
      ],
      "Headwear": {
        "variants": [
          "Subtype of Traditional Wear"
        ],
        "styles": [
          "Embroidered Saree"
        ]
      }
    },
    "Timepiece": {
      "types": [
        "Watch",
        "Timepiece",
        "Timepieces",
        "Accessories",
        "Watches"
      ],
      "Watch": {
        "variants": [
          "Accessories/Subtype - Timepiece/Variant: Watch Style (e.g. Rectangular, Round, Square)",
          "Watch Style - Round",
          "Accessories/Subtype - Timepiece/Variant: Watch Style (e.g. Rectangular, Round, Square) - Accessory/Subtype - Timepiece/Variant: Dress Watch or Formal Wear",
          "Accessories/Subtype - Timepiece/Variant: Watch Style (e.g. Rectangular, Round, Square) - Accessories/Subtype - Timepiece/Variant: Watch Style - Round",
          "Accessories/Subtype - Timepiece/Variant: Watch Style - Round",
          "Accessories/Subtype - Timepiece/Variant: Watch Style (e.g. Rectangular, Round, Square) - Accessories/Subtype - Timepiece/Variant: Strap Material (e.g. Stainless Steel, Leather, etc.)"
        ],
        "styles": [
          "Timepiece",
          "Color Accent"
        ]
      },
      "Timepiece": {
        "variants": [
          "Timepiece",
          "Saree"
        ],
        "styles": [
          "Fashion Accessory",
          "Accessories"
        ]
      },
      "Timepieces": {
        "variants": [
          "Timepiece",
          "Accessories"
        ],
        "styles": [
          "Fashion Accessory",
          "Accessories"
        ]
      },
      "Accessories": {
        "variants": [
          "Accessories Subtype: Timepiece",
          "Accessory Subtype"
        ],
        "styles": [
          "Leather Accessory",
          "Accessories"
        ]
      },
      "Watches": {
        "variants": [
          "Analog Watch",
          "Leather Strap Analog Watch",
          "Accessories",
          "Analogue Watch",
          [
            "Accessories",
            "Analog Watch"
          ]
        ],
        "styles": [
          "Premium Stainless Steel Strap",
          "Leather Strap with Exquisite Detailing",
          "Rubber Strap",
          "Silicone Strap",
          "Accessories",
          "Leather Strap"
        ]
      }
    },
    "Jewelry": {
      "types": [
        "Hand Accessories",
        "Jewelry Accessory",
        "Head Accessories",
        "Jhumkas",
        "Handbag",
        "Handwear",
        "Earrings",
        "Earring"
      ],
      "Hand Accessories": {
        "variants": [
          "Hand Accessories",
          "Fashion Accessories",
          "Jewelry Accessories",
          "Hand Jewelry",
          "Fashion Jewelry"
        ],
        "styles": [
          "Contemporary Accessories",
          "Fashion Accessories",
          "Contemporary Jewelry",
          "Patterned Jewelry"
        ]
      },
      "Jewelry Accessory": {
        "variants": [
          "Jhumkas Earrings",
          "Earrings",
          "Jewelry Accessory Earrings"
        ],
        "styles": [
          "Jewelry Accessory",
          "Fashion Jewelry",
          "Floral Design"
        ]
      },
      "Head Accessories": {
        "variants": [
          "Western Ear Hoop",
          "Contemporary Drop Earrings",
          "Western Drop Earrings",
          "Contemporary Ear Cuff"
        ],
        "styles": [
          "Western",
          "Traditional",
          "Contemporary"
        ]
      },
      "Jhumkas": {
        "variants": [
          "Subtype of Earrings",
          "Earrings",
          "Subtype of Jhumkas"
        ],
        "styles": [
          "Luxury Jhumkas",
          "Vintage Jhumkas",
          "Elegant Jhumkas"
        ]
      },
      "Handbag": {
        "variants": [
          "Fashion Jewelry"
        ],
        "styles": [
          "Geometric"
        ]
      },
      "Handwear": {
        "variants": [
          "Jewelry",
          "Type",
          "Handwear"
        ],
        "styles": [
          "Luxurious Jewelry",
          "Western Earrings"
        ]
      },
      "Earrings": {
        "variants": [
          "Abstract Drop Earrings",
          "Chandelier Earrings",
          "Tribal Jhumkas",
          "Hoop Earrings",
          "Cluster Earrings",
          "Half Hoop Earrings",
          "Abstract Earrings"
        ],
        "styles": [
          "Gold Plated",
          "Silver Plated",
          "Sterling Silver Plated",
          "Synthetic Metal Plated",
          "Brass",
          "Silver Finish",
          "Rose Gold Plated"
        ]
      },
      "Earring": {
        "variants": [
          "Fashion Jewelry Earring",
          "Jewelry Earring",
          "Fashion Jewelry"
        ],
        "styles": [
          "Contemporary Chic",
          "Luxury",
          "Affordable Luxury",
          "Vintage Chic"
        ]
      }
    }
  },
  "Clothing": {
    "classes": [
      "Traditional Wear",
      "Formal Wear Traditional",
      "Casual Wear",
      "Casual Traditional Wear",
      "Formal Wear",
      "Traditional Wear Traditional",
      "Luxury Traditional Wear",
      "Luxury Casual Wear Traditional",
      "Formal Traditional Wear"
    ],
    "Traditional Wear": {
      "types": [
        "Others",
        "Bottom-wear",
        "Other",
        "Top-wear",
        "Headwear"
      ],
      "Others": {
        "variants": [
          "Traditional Wear",
          "Kurti",
          "Saree"
        ],
        "styles": [
          "Handwoven",
          "Traditional Wear",
          "Silk"
        ]
      },
      "Bottom-wear": {
        "variants": [
          "Anarkali",
          "Lehenga",
          "Kurti"
        ],
        "styles": [
          "Traditional"
        ]
      },
      "Other": {
        "variants": [
          "Traditional Formal Wear"
        ],
        "styles": [
          "Traditional Wear",
          "Hand Block Printed"
        ]
      },
      "Top-wear": {
        "variants": [
          "Traditional Wear",
          "Cotton Kurti",
          "Cotton Saree",
          "Silk Kurti"
        ],
        "styles": [
          "Handwoven",
          "Printed",
          "Embroidered"
        ]
      },
      "Headwear": {
        "variants": [
          "Saree"
        ],
        "styles": [
          "Embroidered Headwear"
        ]
      }
    },
    "Formal Wear Traditional": {
      "types": [
        "Bodyware",
        "Saree"
      ],
      "Bodyware": {
        "variants": [
          "Saree"
        ],
        "styles": [
          "Embroidered Saree"
        ]
      },
      "Saree": {
        "variants": [
          "Traditional Saree",
          "Formal Traditional Saree"
        ],
        "styles": [
          "Saree",
          "Embroidered Saree"
        ]
      }
    },
    "Casual Wear": {
      "types": [
        "Otherwear",
        "Midi-wear",
        "Maxi-wear",
        "Halter Dress",
        "Asymmetric Dress",
        "Bottom-wear",
        "Kurta",
        "Tie-front Dress",
        "Anarkali",
        "Top-wear",
        "A-line Dress",
        "Bandeau-wear",
        "Bodycon Dress",
        "Jacket-wear",
        "SWEATSHIRT",
        "Mini-wear",
        "Draped-wear"
      ],
      "Otherwear": {
        "variants": [
          "Subtype of Casual Wear",
          "Otherwear",
          "Type of Garment: Pant",
          "Type of Garment: Dress - A-line Dress",
          "Casual Wear"
        ],
        "styles": [
          "Strappy dress",
          "Flounce-trimmed dress",
          "Printed",
          "Solid Color",
          "Casual Suit"
        ]
      },
      "Midi-wear": {
        "variants": [
          "Flared Midi Dress variation",
          "Bubble-hem dress variation",
          "Bodycon Dress variation",
          "A-line Dress variation",
          "Pleated Midi Dress variation"
        ],
        "styles": [
          "Slim Fit Dress",
          "Embellished Midi Dress"
        ]
      },
      "Maxi-wear": {
        "variants": [
          "A-line Dress",
          "Maxi Dress"
        ],
        "styles": [
          "Smocked A-line Dress",
          "Crochet-look",
          "A-line Dress",
          "Bead-detail A-line Dress",
          "Draped Style Dress"
        ]
      },
      "Halter Dress": {
        "variants": [
          "Sportswear"
        ],
        "styles": [
          "Solid Colour"
        ]
      },
      "Asymmetric Dress": {
        "variants": [
          "Voluminous Tie-Belt Dress",
          "Subtype",
          "Off-the-Shoulder Dress"
        ],
        "styles": [
          "Lace-detail Dress",
          "Stud-detail Dress",
          "Twist-strap Dress",
          "Flounce-trimmed Dress",
          "Embroidered Dress",
          "Off-the-shoulder Dress"
        ]
      },
      "Bottom-wear": {
        "variants": [
          "Trousers",
          "Shorts",
          "High-waist Jeans",
          "Distressed Jeans",
          "Cargo Jeans",
          "Skinny Jeans",
          "Slim Fit Jeans",
          "Saree",
          "Jeans"
        ],
        "styles": [
          "Distressed Jeans",
          "Regular Fit Jeans",
          "Flared Slim Fit",
          "Distressed Straight Fit",
          "Premium Slim Fit Jeans",
          "Contrast Distressed Jeans",
          "Distressed Loose Fit Jeans",
          "Fine-grained descriptor: Printed Saree",
          "Ripped Jeans"
        ]
      },
      "Kurta": {
        "variants": [
          "Subtype of Kurta",
          "Casual Kurti",
          "Casual Kurta"
        ],
        "styles": [
          "Printed Embellishments",
          "Casual Wear"
        ]
      },
      "Tie-front Dress": {
        "variants": [
          "High-neck Frill-collar Dress variant",
          "Tie-front Dress variant"
        ],
        "styles": [
          "Tie-front Dress with Frill Collar",
          "Tie-front Dress with Detachable Belt",
          "Tie-front Dress with Puff Sleeves",
          "Tie-front Dress with Crinkled Weave Collar"
        ]
      },
      "Anarkali": {
        "variants": [
          "Anarkali Kurti",
          "Subtype",
          "Casual Wear"
        ],
        "styles": [
          "Solid Anarkali",
          "Printed Anarkali"
        ]
      },
      "Top-wear": {
        "variants": [
          "Print Digital Loose Fit Shirt",
          "Layered Casual Wear",
          "Short Sleeve Graphic T-shirt",
          "Short Sleeve Graphic T-Shirt",
          "Patched Button Shirt",
          "Casual Cartoon Print Tee",
          "Graphic T-shirt",
          "Solid Color Short-sleeve Casual T-shirt",
          "Floral Shirt",
          "Long Sleeve T-shirt",
          "Short-sleeve Button Shirt",
          "Seersucker Shirt",
          "Digital Print Relaxed Fit Shirt",
          "Guayabera",
          "Patchwork Button Shirt",
          "Casual Long Sleeve Henley Shirt"
        ],
        "styles": [
          "Anime-Inspired Graphic Tee",
          "Relaxed Fit Classic Button-Down",
          "Horror-Themed Graphic Print",
          "Solid Color Minimalist Long Sleeve Casual Shirt",
          "Classic Crew Neck Thermal Shirt",
          "Solid Color Casual Tee",
          "Solid Color T-Shirt",
          "Simple Button-Down Casual Shirt",
          "Casual Long Sleeve Regular Fit Autumn Western",
          "Refined Aesthetic",
          "Plain Cotton Shirt",
          "Regular Fit Long Sleeve Button-Down",
          "Casual Island Print",
          "AmbientElegance",
          "Eclectic Aesthetic Elements - Patterned Accent",
          "Regular Fit Solid Color Button-Down Shirt",
          "Aesthetic Element",
          "Ambient Enhancements",
          "Graphic Print with Cartoon Elements",
          "Popover Shirt",
          "Butterfly Print Shirt",
          "Atmospheric Accents",
          "Unique Aesthetic Elements",
          "Eclectic Fashion Piece",
          "Christmas Cartoon Character Graphic Print Casual Wear",
          "Floral Digital Print",
          "Casual Long Sleeve All Over Print Shirt",
          "Eclectic Aesthetic Elements",
          "Mixed Print Casual Wear"
        ]
      },
      "A-line Dress": {
        "variants": [
          "Subtype",
          "Flared Dress"
        ],
        "styles": [
          "A-line Dress with Frill Trim",
          "A-line Dress with Pleats",
          "A-line Dress",
          "A-line Dress with Flared Skirt",
          "Minimalist Dress"
        ]
      },
      "Bandeau-wear": {
        "variants": [
          "Strappy Dress",
          "Bandeau Dress",
          "High-low dress"
        ],
        "styles": [
          "V-Neck Dress",
          "Smocked Bandeau Dress",
          "Viscose Beige Midi Dress",
          "Distressed Cotton"
        ]
      },
      "Bodycon Dress": {
        "variants": [
          "Bodycon Dress Type",
          "Mermaid Skirt Dress Type"
        ],
        "styles": [
          "Bodycon",
          "Ribbed"
        ]
      },
      "Jacket-wear": {
        "variants": [
          "Subtype of Jacket-wear"
        ],
        "styles": [
          "Colorblock"
        ]
      },
      "SWEATSHIRT": {
        "variants": [
          "SWEATSHIRT JUMPER"
        ],
        "styles": [
          "Distressed Jeans",
          "All Over Print Casual Style",
          "Cable-knit pattern"
        ]
      },
      "Mini-wear": {
        "variants": [
          "A-line Dress",
          "Bodycon Dress",
          "Flared Dress"
        ],
        "styles": [
          "Overseas",
          "A-line Dress",
          "Bodycon Dress",
          "Turtleneck Dress with Turtle Neckline"
        ]
      },
      "Draped-wear": {
        "variants": [
          "Jumper Dress",
          "Bodycon Dress",
          "T-shirt Dress"
        ],
        "styles": [
          "Solid Colour",
          "Embroidered Saree"
        ]
      }
    },
    "Casual Traditional Wear": {
      "types": [
        "Headwear",
        "Saree"
      ],
      "Headwear": {
        "variants": [
          "Saree"
        ],
        "styles": [
          "Embroidered Saree"
        ]
      },
      "Saree": {
        "variants": [
          "Sub-Type of Traditional Wear",
          "Sub-Type of Traditional Wear - Saree"
        ],
        "styles": [
          "Casual Traditional Wear",
          "Saree",
          "Embroidered Saree"
        ]
      }
    },
    "Formal Wear": {
      "types": [
        "Wrapwear",
        "Bodycon",
        "Dress",
        "Bottom-wear",
        "Formal Wear",
        "Top-wear",
        "Kurta-wear"
      ],
      "Wrapwear": {
        "variants": [
          "Formal Wrap",
          "Formal Wrap Dress"
        ],
        "styles": [
          "Blazer Dress",
          "Sequined"
        ]
      },
      "Bodycon": {
        "variants": [
          "Blazer Dress",
          "Bodycon Dress"
        ],
        "styles": [
          "Blazer dress",
          "Tie-detail strappy dress",
          "Bodycon Dress"
        ]
      },
      "Dress": {
        "variants": [
          "Formal Chiffon Dress",
          "Formal Viscose Dress",
          "Formal Lace Dress",
          "Formal Bodycon Dress",
          "Formal Sequined Dress"
        ],
        "styles": [
          "Bodycon",
          "Sequined",
          "Flounced"
        ]
      },
      "Bottom-wear": {
        "variants": [
          "Bandeau Dress",
          "Saree"
        ],
        "styles": [
          "Formal Wear",
          "Layered Ruffles",
          "Embroidered"
        ]
      },
      "Formal Wear": {
        "variants": [
          "Formal Wear Variation - Printed Gown",
          "Formal Wear Variation"
        ],
        "styles": [
          "Floral Printed Western Dress",
          "Western Dress",
          "Formal Wear"
        ]
      },
      "Top-wear": {
        "variants": [
          "Shirt",
          "Gown",
          "Blazer Dress",
          "Top-wear"
        ],
        "styles": [
          "Formal Wear",
          "Minimalist",
          "Sequin",
          "Satin Finish"
        ]
      },
      "Kurta-wear": {
        "variants": [
          "Kurta-wear variation",
          "Formal Kurta"
        ],
        "styles": [
          "Formal Wear",
          "Embroidered"
        ]
      }
    },
    "Traditional Wear Traditional": {
      "types": [
        "Headwear",
        "Bottom-wear"
      ],
      "Headwear": {
        "variants": [
          "Traditional Wear"
        ],
        "styles": [
          "Embroidered"
        ]
      },
      "Bottom-wear": {
        "variants": [
          "Traditional Wear",
          "Saree"
        ],
        "styles": [
          "Traditional Wear",
          "Embroidered Saree"
        ]
      }
    },
    "Luxury Traditional Wear": {
      "types": [
        "Mekhla Chador",
        "Bottom-wear",
        "Top-wear",
        "Other-wear"
      ],
      "Mekhla Chador": {
        "variants": [
          "Luxury Saree",
          "Variation"
        ],
        "styles": [
          "Printed Traditional Wear",
          "Printed Embroidered Design",
          "Embroidered Traditional Wear",
          "Embroidered Saree",
          "Luxury Traditional Wear"
        ]
      },
      "Bottom-wear": {
        "variants": [
          "Luxury Traditional Wear Sari"
        ],
        "styles": [
          "Luxury Traditional Wear",
          "Zari Weaved"
        ]
      },
      "Top-wear": {
        "variants": [
          "Clothing - Saree",
          "Luxury Traditional Wear - Saree"
        ],
        "styles": [
          "Luxury Traditional Wear",
          "Embroidered Saree",
          "Organza Embellished garment"
        ]
      },
      "Other-wear": {
        "variants": [
          "Banarasi Silk Saree",
          "Fancy Cotton Saree",
          "Saree",
          "Silk Saree",
          "Khadi Silk Saree"
        ],
        "styles": [
          "Printed Embroidered Saree",
          "Applique Saree",
          "Printed Saree",
          "Zari Woven Saree"
        ]
      }
    },
    "Luxury Casual Wear Traditional": {
      "types": [
        "Headwear",
        "Bottom-wear",
        "Top-wear"
      ],
      "Headwear": {
        "variants": [
          "Saree"
        ],
        "styles": [
          "Luxurious Embellishments"
        ]
      },
      "Bottom-wear": {
        "variants": [
          "Saree"
        ],
        "styles": [
          "Luxury Casual Wear Traditional Saree",
          "Embroidered Saree"
        ]
      },
      "Top-wear": {
        "variants": [
          "Saree"
        ],
        "styles": [
          "Embroidered Blouse",
          "Embroidered Saree"
        ]
      }
    },
    "Formal Traditional Wear": {
      "types": [
        "Bottom-wear",
        "Formal Traditional Wear",
        "Saree",
        "Mekhla Sador"
      ],
      "Bottom-wear": {
        "variants": [
          "Formal Traditional Saree"
        ],
        "styles": [
          "Formal Traditional Wear",
          "Embroidered Saree"
        ]
      },
      "Formal Traditional Wear": {
        "variants": [
          "Formal Traditional Wear",
          "Saree",
          "Silk Saree"
        ],
        "styles": [
          "Printed Embroidered Georgette Saree",
          "Formal Traditional Wear"
        ]
      },
      "Saree": {
        "variants": [
          "Formal Traditional Wear",
          "Saree"
        ],
        "styles": [
          "Printed Saree",
          "Formal Traditional Wear Saree",
          "Embroidered Saree"
        ]
      },
      "Mekhla Sador": {
        "variants": [
          "Subtype"
        ],
        "styles": [
          "Embroidered Mekhla Sador"
        ]
      }
    }
  },
  "Footwear": {
    "classes": [
      "Smart Casual Shoes",
      "Casual Shoes",
      "Semi Formal Shoes"
    ],
    "Smart Casual Shoes": {
      "types": [
        "Footwear"
      ],
      "Footwear": {
        "variants": [
          "Sneakers",
          "High-top Sneakers"
        ],
        "styles": [
          "Patterned Footwear",
          "Patterned Sneakers"
        ]
      }
    },
    "Casual Shoes": {
      "types": [
        "Footwear/Sneakers",
        "Footwear"
      ],
      "Footwear/Sneakers": {
        "variants": [
          "Sneaker",
          "High-top Sneakers"
        ],
        "styles": [
          "Solid Pattern",
          "Colourblocked"
        ]
      },
      "Footwear": {
        "variants": [
          "Sneaker"
        ],
        "styles": [
          "Patterned Footwear"
        ]
      }
    },
    "Semi Formal Shoes": {
      "types": [
        "Footwear"
      ],
      "Footwear": {
        "variants": [
          "Sneakers"
        ],
        "styles": [
          "Tan Leather"
        ]
      }
    }
  }
}

# Define node types and colors
NODE_TYPES = {
    "superclass": "lightblue",
    "class": "lightgreen",
    "type": "lightpink",
    "variant": "lightyellow",
    "style": "lightgray",
}

SEQUENCE = ["superclass", "class", "type", "variant", "style"]

def add_nodes_and_edges(net, parent, node, node_type_ind=0):
    node_type = SEQUENCE[node_type_ind]
    if isinstance(node, dict):
        for key, value in node.items():
            if key not in ["variants", "styles"]:  # Skip leaf lists
                net.add_node(key, label=key, color=NODE_TYPES.get(node_type, "white"))
                net.add_edge(parent, key)
                add_nodes_and_edges(net, key, value, node_type_ind=node_type_ind+1)
    elif isinstance(node, list):
        for item in node:
            net.add_node(item, label=item, color=NODE_TYPES.get(node_type, "white"))
            net.add_edge(parent, item)

def get_dropdown_options(data, selected_path):
    """Traverse the data to get dropdown options based on the current selection path."""
    node = data
    for key in selected_path:
        if isinstance(node, dict) and key in node:
            node = node[key]
        else:
            return []
    if isinstance(node, dict):
        if "variants" in node and "styles" in node:
            return {"variants": node["variants"], "styles": node["styles"]}
        return list(node.keys())
    elif isinstance(node, list):
        return node
    return []

# Streamlit App
st.title("Interactive Ontology Visualization")

# Add Legend
st.subheader("Legend")
legend_html = """
<div style="display: flex; flex-direction: row;">
    <div style="margin: 5px;">
        <span style="background-color: lightblue; padding: 5px; margin-right: 5px; border-radius: 3px;">&nbsp;</span>
        Superclass
    </div>
    <div style="margin: 5px;">
        <span style="background-color: lightgreen; padding: 5px; margin-right: 5px; border-radius: 3px;">&nbsp;</span>
        Class
    </div>
    <div style="margin: 5px;">
        <span style="background-color: lightpink; padding: 5px; margin-right: 5px; border-radius: 3px;">&nbsp;</span>
        Type
    </div>
</div>
"""
st.markdown(legend_html, unsafe_allow_html=True)

# Create a PyVis network
net = Network(height="750px", width="100%", directed=True)

# Add top-level superclasses
for superclass in data["superclasses"]:
    net.add_node(superclass, label=superclass, color=NODE_TYPES["superclass"])
    add_nodes_and_edges(net, superclass, data.get(superclass, {}))

# Render PyVis Graph
html_content = net.generate_html()
st.components.v1.html(html_content, height=800, scrolling=True)

# Check a Specific Ontology Subtree Section
st.subheader("Check a Specific Ontology Subtree")

selected_path = []

# Superclass Dropdown
superclass_options = data["superclasses"]
selected_superclass = st.selectbox("Select a Superclass", superclass_options, key="superclass")
if selected_superclass:
    selected_path.append(selected_superclass)
    class_options = get_dropdown_options(data, selected_path)
    
    # Class Dropdown
    selected_class = st.selectbox("Select a Class", class_options, key="class")
    if selected_class:
        selected_path.append(selected_class)
        type_options = get_dropdown_options(data, selected_path)
        
        # Type Dropdown
        selected_type = st.selectbox("Select a Type", type_options, key="type")
        if selected_type:
            selected_path.append(selected_type)
            final_data = get_dropdown_options(data, selected_path)
            
            if isinstance(final_data, dict):
                st.write("### Variants")
                st.write(final_data.get("variants", []))
                st.write("### Styles")
                st.write(final_data.get("styles", []))