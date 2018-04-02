#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPL v3 Copyright: 2017, Kovid Goyal <kovid at kovidgoyal.net>

import re
from collections import namedtuple

Color = namedtuple('Color', 'red green blue')


def parse_single_color(c):
    if len(c) == 1:
        c += c
    return int(c[:2], 16)


def parse_sharp(spec):
    if len(spec) in (3, 6, 9, 12):
        part_len = len(spec) // 3
        colors = re.findall(r'[a-fA-F0-9]{%d}' % part_len, spec)
        return Color(*map(parse_single_color, colors))


def parse_rgb(spec):
    colors = spec.split('/')
    if len(colors) == 3:
        return Color(*map(parse_single_color, colors))


def color_from_int(x):
    return Color((x >> 16) & 255, (x >> 8) & 255, x & 255)


def color_as_int(x):
    return x.red << 16 | x.green << 8 | x.blue


def to_color(raw, validate=False):
    # See man XParseColor
    x = raw.strip().lower()
    ans = color_names.get(x)
    if ans is not None:
        return ans
    val = None
    try:
        if raw.startswith('#'):
            val = parse_sharp(raw[1:])
        elif raw[:4].lower() == 'rgb:':
            val = parse_rgb(raw[4:])
    except Exception:
        pass
    if val is None and validate:
        raise ValueError('Invalid color name: {}'.format(raw))
    return val


# BEGIN_DATA_SECTION {{{
color_names = {
 'alice blue': Color(240, 248, 255),
 'aliceblue': Color(240, 248, 255),
 'antique white': Color(250, 235, 215),
 'antiquewhite': Color(250, 235, 215),
 'antiquewhite1': Color(255, 239, 219),
 'antiquewhite2': Color(238, 223, 204),
 'antiquewhite3': Color(205, 192, 176),
 'antiquewhite4': Color(139, 131, 120),
 'aquamarine': Color(127, 255, 212),
 'aquamarine1': Color(127, 255, 212),
 'aquamarine2': Color(118, 238, 198),
 'aquamarine3': Color(102, 205, 170),
 'aquamarine4': Color(69, 139, 116),
 'azure': Color(240, 255, 255),
 'azure1': Color(240, 255, 255),
 'azure2': Color(224, 238, 238),
 'azure3': Color(193, 205, 205),
 'azure4': Color(131, 139, 139),
 'beige': Color(245, 245, 220),
 'bisque': Color(255, 228, 196),
 'bisque1': Color(255, 228, 196),
 'bisque2': Color(238, 213, 183),
 'bisque3': Color(205, 183, 158),
 'bisque4': Color(139, 125, 107),
 'black': Color(0, 0, 0),
 'blanched almond': Color(255, 235, 205),
 'blanchedalmond': Color(255, 235, 205),
 'blue': Color(0, 0, 255),
 'blue violet': Color(138, 43, 226),
 'blue1': Color(0, 0, 255),
 'blue2': Color(0, 0, 238),
 'blue3': Color(0, 0, 205),
 'blue4': Color(0, 0, 139),
 'blueviolet': Color(138, 43, 226),
 'brown': Color(165, 42, 42),
 'brown1': Color(255, 64, 64),
 'brown2': Color(238, 59, 59),
 'brown3': Color(205, 51, 51),
 'brown4': Color(139, 35, 35),
 'burlywood': Color(222, 184, 135),
 'burlywood1': Color(255, 211, 155),
 'burlywood2': Color(238, 197, 145),
 'burlywood3': Color(205, 170, 125),
 'burlywood4': Color(139, 115, 85),
 'cadet blue': Color(95, 158, 160),
 'cadetblue': Color(95, 158, 160),
 'cadetblue1': Color(152, 245, 255),
 'cadetblue2': Color(142, 229, 238),
 'cadetblue3': Color(122, 197, 205),
 'cadetblue4': Color(83, 134, 139),
 'chartreuse': Color(127, 255, 0),
 'chartreuse1': Color(127, 255, 0),
 'chartreuse2': Color(118, 238, 0),
 'chartreuse3': Color(102, 205, 0),
 'chartreuse4': Color(69, 139, 0),
 'chocolate': Color(210, 105, 30),
 'chocolate1': Color(255, 127, 36),
 'chocolate2': Color(238, 118, 33),
 'chocolate3': Color(205, 102, 29),
 'chocolate4': Color(139, 69, 19),
 'coral': Color(255, 127, 80),
 'coral1': Color(255, 114, 86),
 'coral2': Color(238, 106, 80),
 'coral3': Color(205, 91, 69),
 'coral4': Color(139, 62, 47),
 'cornflower blue': Color(100, 149, 237),
 'cornflowerblue': Color(100, 149, 237),
 'cornsilk': Color(255, 248, 220),
 'cornsilk1': Color(255, 248, 220),
 'cornsilk2': Color(238, 232, 205),
 'cornsilk3': Color(205, 200, 177),
 'cornsilk4': Color(139, 136, 120),
 'cyan': Color(0, 255, 255),
 'cyan1': Color(0, 255, 255),
 'cyan2': Color(0, 238, 238),
 'cyan3': Color(0, 205, 205),
 'cyan4': Color(0, 139, 139),
 'dark blue': Color(0, 0, 139),
 'dark cyan': Color(0, 139, 139),
 'dark goldenrod': Color(184, 134, 11),
 'dark gray': Color(169, 169, 169),
 'dark green': Color(0, 100, 0),
 'dark grey': Color(169, 169, 169),
 'dark khaki': Color(189, 183, 107),
 'dark magenta': Color(139, 0, 139),
 'dark olive green': Color(85, 107, 47),
 'dark orange': Color(255, 140, 0),
 'dark orchid': Color(153, 50, 204),
 'dark red': Color(139, 0, 0),
 'dark salmon': Color(233, 150, 122),
 'dark sea green': Color(143, 188, 143),
 'dark slate blue': Color(72, 61, 139),
 'dark slate gray': Color(47, 79, 79),
 'dark slate grey': Color(47, 79, 79),
 'dark turquoise': Color(0, 206, 209),
 'dark violet': Color(148, 0, 211),
 'darkblue': Color(0, 0, 139),
 'darkcyan': Color(0, 139, 139),
 'darkgoldenrod': Color(184, 134, 11),
 'darkgoldenrod1': Color(255, 185, 15),
 'darkgoldenrod2': Color(238, 173, 14),
 'darkgoldenrod3': Color(205, 149, 12),
 'darkgoldenrod4': Color(139, 101, 8),
 'darkgray': Color(169, 169, 169),
 'darkgreen': Color(0, 100, 0),
 'darkgrey': Color(169, 169, 169),
 'darkkhaki': Color(189, 183, 107),
 'darkmagenta': Color(139, 0, 139),
 'darkolivegreen': Color(85, 107, 47),
 'darkolivegreen1': Color(202, 255, 112),
 'darkolivegreen2': Color(188, 238, 104),
 'darkolivegreen3': Color(162, 205, 90),
 'darkolivegreen4': Color(110, 139, 61),
 'darkorange': Color(255, 140, 0),
 'darkorange1': Color(255, 127, 0),
 'darkorange2': Color(238, 118, 0),
 'darkorange3': Color(205, 102, 0),
 'darkorange4': Color(139, 69, 0),
 'darkorchid': Color(153, 50, 204),
 'darkorchid1': Color(191, 62, 255),
 'darkorchid2': Color(178, 58, 238),
 'darkorchid3': Color(154, 50, 205),
 'darkorchid4': Color(104, 34, 139),
 'darkred': Color(139, 0, 0),
 'darksalmon': Color(233, 150, 122),
 'darkseagreen': Color(143, 188, 143),
 'darkseagreen1': Color(193, 255, 193),
 'darkseagreen2': Color(180, 238, 180),
 'darkseagreen3': Color(155, 205, 155),
 'darkseagreen4': Color(105, 139, 105),
 'darkslateblue': Color(72, 61, 139),
 'darkslategray': Color(47, 79, 79),
 'darkslategray1': Color(151, 255, 255),
 'darkslategray2': Color(141, 238, 238),
 'darkslategray3': Color(121, 205, 205),
 'darkslategray4': Color(82, 139, 139),
 'darkslategrey': Color(47, 79, 79),
 'darkturquoise': Color(0, 206, 209),
 'darkviolet': Color(148, 0, 211),
 'debianred': Color(215, 7, 81),
 'deep pink': Color(255, 20, 147),
 'deep sky blue': Color(0, 191, 255),
 'deeppink': Color(255, 20, 147),
 'deeppink1': Color(255, 20, 147),
 'deeppink2': Color(238, 18, 137),
 'deeppink3': Color(205, 16, 118),
 'deeppink4': Color(139, 10, 80),
 'deepskyblue': Color(0, 191, 255),
 'deepskyblue1': Color(0, 191, 255),
 'deepskyblue2': Color(0, 178, 238),
 'deepskyblue3': Color(0, 154, 205),
 'deepskyblue4': Color(0, 104, 139),
 'dim gray': Color(105, 105, 105),
 'dim grey': Color(105, 105, 105),
 'dimgray': Color(105, 105, 105),
 'dimgrey': Color(105, 105, 105),
 'dodger blue': Color(30, 144, 255),
 'dodgerblue': Color(30, 144, 255),
 'dodgerblue1': Color(30, 144, 255),
 'dodgerblue2': Color(28, 134, 238),
 'dodgerblue3': Color(24, 116, 205),
 'dodgerblue4': Color(16, 78, 139),
 'firebrick': Color(178, 34, 34),
 'firebrick1': Color(255, 48, 48),
 'firebrick2': Color(238, 44, 44),
 'firebrick3': Color(205, 38, 38),
 'firebrick4': Color(139, 26, 26),
 'floral white': Color(255, 250, 240),
 'floralwhite': Color(255, 250, 240),
 'forest green': Color(34, 139, 34),
 'forestgreen': Color(34, 139, 34),
 'gainsboro': Color(220, 220, 220),
 'ghost white': Color(248, 248, 255),
 'ghostwhite': Color(248, 248, 255),
 'gold': Color(255, 215, 0),
 'gold1': Color(255, 215, 0),
 'gold2': Color(238, 201, 0),
 'gold3': Color(205, 173, 0),
 'gold4': Color(139, 117, 0),
 'goldenrod': Color(218, 165, 32),
 'goldenrod1': Color(255, 193, 37),
 'goldenrod2': Color(238, 180, 34),
 'goldenrod3': Color(205, 155, 29),
 'goldenrod4': Color(139, 105, 20),
 'gray': Color(190, 190, 190),
 'gray0': Color(0, 0, 0),
 'gray1': Color(3, 3, 3),
 'gray10': Color(26, 26, 26),
 'gray100': Color(255, 255, 255),
 'gray11': Color(28, 28, 28),
 'gray12': Color(31, 31, 31),
 'gray13': Color(33, 33, 33),
 'gray14': Color(36, 36, 36),
 'gray15': Color(38, 38, 38),
 'gray16': Color(41, 41, 41),
 'gray17': Color(43, 43, 43),
 'gray18': Color(46, 46, 46),
 'gray19': Color(48, 48, 48),
 'gray2': Color(5, 5, 5),
 'gray20': Color(51, 51, 51),
 'gray21': Color(54, 54, 54),
 'gray22': Color(56, 56, 56),
 'gray23': Color(59, 59, 59),
 'gray24': Color(61, 61, 61),
 'gray25': Color(64, 64, 64),
 'gray26': Color(66, 66, 66),
 'gray27': Color(69, 69, 69),
 'gray28': Color(71, 71, 71),
 'gray29': Color(74, 74, 74),
 'gray3': Color(8, 8, 8),
 'gray30': Color(77, 77, 77),
 'gray31': Color(79, 79, 79),
 'gray32': Color(82, 82, 82),
 'gray33': Color(84, 84, 84),
 'gray34': Color(87, 87, 87),
 'gray35': Color(89, 89, 89),
 'gray36': Color(92, 92, 92),
 'gray37': Color(94, 94, 94),
 'gray38': Color(97, 97, 97),
 'gray39': Color(99, 99, 99),
 'gray4': Color(10, 10, 10),
 'gray40': Color(102, 102, 102),
 'gray41': Color(105, 105, 105),
 'gray42': Color(107, 107, 107),
 'gray43': Color(110, 110, 110),
 'gray44': Color(112, 112, 112),
 'gray45': Color(115, 115, 115),
 'gray46': Color(117, 117, 117),
 'gray47': Color(120, 120, 120),
 'gray48': Color(122, 122, 122),
 'gray49': Color(125, 125, 125),
 'gray5': Color(13, 13, 13),
 'gray50': Color(127, 127, 127),
 'gray51': Color(130, 130, 130),
 'gray52': Color(133, 133, 133),
 'gray53': Color(135, 135, 135),
 'gray54': Color(138, 138, 138),
 'gray55': Color(140, 140, 140),
 'gray56': Color(143, 143, 143),
 'gray57': Color(145, 145, 145),
 'gray58': Color(148, 148, 148),
 'gray59': Color(150, 150, 150),
 'gray6': Color(15, 15, 15),
 'gray60': Color(153, 153, 153),
 'gray61': Color(156, 156, 156),
 'gray62': Color(158, 158, 158),
 'gray63': Color(161, 161, 161),
 'gray64': Color(163, 163, 163),
 'gray65': Color(166, 166, 166),
 'gray66': Color(168, 168, 168),
 'gray67': Color(171, 171, 171),
 'gray68': Color(173, 173, 173),
 'gray69': Color(176, 176, 176),
 'gray7': Color(18, 18, 18),
 'gray70': Color(179, 179, 179),
 'gray71': Color(181, 181, 181),
 'gray72': Color(184, 184, 184),
 'gray73': Color(186, 186, 186),
 'gray74': Color(189, 189, 189),
 'gray75': Color(191, 191, 191),
 'gray76': Color(194, 194, 194),
 'gray77': Color(196, 196, 196),
 'gray78': Color(199, 199, 199),
 'gray79': Color(201, 201, 201),
 'gray8': Color(20, 20, 20),
 'gray80': Color(204, 204, 204),
 'gray81': Color(207, 207, 207),
 'gray82': Color(209, 209, 209),
 'gray83': Color(212, 212, 212),
 'gray84': Color(214, 214, 214),
 'gray85': Color(217, 217, 217),
 'gray86': Color(219, 219, 219),
 'gray87': Color(222, 222, 222),
 'gray88': Color(224, 224, 224),
 'gray89': Color(227, 227, 227),
 'gray9': Color(23, 23, 23),
 'gray90': Color(229, 229, 229),
 'gray91': Color(232, 232, 232),
 'gray92': Color(235, 235, 235),
 'gray93': Color(237, 237, 237),
 'gray94': Color(240, 240, 240),
 'gray95': Color(242, 242, 242),
 'gray96': Color(245, 245, 245),
 'gray97': Color(247, 247, 247),
 'gray98': Color(250, 250, 250),
 'gray99': Color(252, 252, 252),
 'green': Color(0, 255, 0),
 'green yellow': Color(173, 255, 47),
 'green1': Color(0, 255, 0),
 'green2': Color(0, 238, 0),
 'green3': Color(0, 205, 0),
 'green4': Color(0, 139, 0),
 'greenyellow': Color(173, 255, 47),
 'grey': Color(190, 190, 190),
 'grey0': Color(0, 0, 0),
 'grey1': Color(3, 3, 3),
 'grey10': Color(26, 26, 26),
 'grey100': Color(255, 255, 255),
 'grey11': Color(28, 28, 28),
 'grey12': Color(31, 31, 31),
 'grey13': Color(33, 33, 33),
 'grey14': Color(36, 36, 36),
 'grey15': Color(38, 38, 38),
 'grey16': Color(41, 41, 41),
 'grey17': Color(43, 43, 43),
 'grey18': Color(46, 46, 46),
 'grey19': Color(48, 48, 48),
 'grey2': Color(5, 5, 5),
 'grey20': Color(51, 51, 51),
 'grey21': Color(54, 54, 54),
 'grey22': Color(56, 56, 56),
 'grey23': Color(59, 59, 59),
 'grey24': Color(61, 61, 61),
 'grey25': Color(64, 64, 64),
 'grey26': Color(66, 66, 66),
 'grey27': Color(69, 69, 69),
 'grey28': Color(71, 71, 71),
 'grey29': Color(74, 74, 74),
 'grey3': Color(8, 8, 8),
 'grey30': Color(77, 77, 77),
 'grey31': Color(79, 79, 79),
 'grey32': Color(82, 82, 82),
 'grey33': Color(84, 84, 84),
 'grey34': Color(87, 87, 87),
 'grey35': Color(89, 89, 89),
 'grey36': Color(92, 92, 92),
 'grey37': Color(94, 94, 94),
 'grey38': Color(97, 97, 97),
 'grey39': Color(99, 99, 99),
 'grey4': Color(10, 10, 10),
 'grey40': Color(102, 102, 102),
 'grey41': Color(105, 105, 105),
 'grey42': Color(107, 107, 107),
 'grey43': Color(110, 110, 110),
 'grey44': Color(112, 112, 112),
 'grey45': Color(115, 115, 115),
 'grey46': Color(117, 117, 117),
 'grey47': Color(120, 120, 120),
 'grey48': Color(122, 122, 122),
 'grey49': Color(125, 125, 125),
 'grey5': Color(13, 13, 13),
 'grey50': Color(127, 127, 127),
 'grey51': Color(130, 130, 130),
 'grey52': Color(133, 133, 133),
 'grey53': Color(135, 135, 135),
 'grey54': Color(138, 138, 138),
 'grey55': Color(140, 140, 140),
 'grey56': Color(143, 143, 143),
 'grey57': Color(145, 145, 145),
 'grey58': Color(148, 148, 148),
 'grey59': Color(150, 150, 150),
 'grey6': Color(15, 15, 15),
 'grey60': Color(153, 153, 153),
 'grey61': Color(156, 156, 156),
 'grey62': Color(158, 158, 158),
 'grey63': Color(161, 161, 161),
 'grey64': Color(163, 163, 163),
 'grey65': Color(166, 166, 166),
 'grey66': Color(168, 168, 168),
 'grey67': Color(171, 171, 171),
 'grey68': Color(173, 173, 173),
 'grey69': Color(176, 176, 176),
 'grey7': Color(18, 18, 18),
 'grey70': Color(179, 179, 179),
 'grey71': Color(181, 181, 181),
 'grey72': Color(184, 184, 184),
 'grey73': Color(186, 186, 186),
 'grey74': Color(189, 189, 189),
 'grey75': Color(191, 191, 191),
 'grey76': Color(194, 194, 194),
 'grey77': Color(196, 196, 196),
 'grey78': Color(199, 199, 199),
 'grey79': Color(201, 201, 201),
 'grey8': Color(20, 20, 20),
 'grey80': Color(204, 204, 204),
 'grey81': Color(207, 207, 207),
 'grey82': Color(209, 209, 209),
 'grey83': Color(212, 212, 212),
 'grey84': Color(214, 214, 214),
 'grey85': Color(217, 217, 217),
 'grey86': Color(219, 219, 219),
 'grey87': Color(222, 222, 222),
 'grey88': Color(224, 224, 224),
 'grey89': Color(227, 227, 227),
 'grey9': Color(23, 23, 23),
 'grey90': Color(229, 229, 229),
 'grey91': Color(232, 232, 232),
 'grey92': Color(235, 235, 235),
 'grey93': Color(237, 237, 237),
 'grey94': Color(240, 240, 240),
 'grey95': Color(242, 242, 242),
 'grey96': Color(245, 245, 245),
 'grey97': Color(247, 247, 247),
 'grey98': Color(250, 250, 250),
 'grey99': Color(252, 252, 252),
 'honeydew': Color(240, 255, 240),
 'honeydew1': Color(240, 255, 240),
 'honeydew2': Color(224, 238, 224),
 'honeydew3': Color(193, 205, 193),
 'honeydew4': Color(131, 139, 131),
 'hot pink': Color(255, 105, 180),
 'hotpink': Color(255, 105, 180),
 'hotpink1': Color(255, 110, 180),
 'hotpink2': Color(238, 106, 167),
 'hotpink3': Color(205, 96, 144),
 'hotpink4': Color(139, 58, 98),
 'indian red': Color(205, 92, 92),
 'indianred': Color(205, 92, 92),
 'indianred1': Color(255, 106, 106),
 'indianred2': Color(238, 99, 99),
 'indianred3': Color(205, 85, 85),
 'indianred4': Color(139, 58, 58),
 'ivory': Color(255, 255, 240),
 'ivory1': Color(255, 255, 240),
 'ivory2': Color(238, 238, 224),
 'ivory3': Color(205, 205, 193),
 'ivory4': Color(139, 139, 131),
 'khaki': Color(240, 230, 140),
 'khaki1': Color(255, 246, 143),
 'khaki2': Color(238, 230, 133),
 'khaki3': Color(205, 198, 115),
 'khaki4': Color(139, 134, 78),
 'lavender': Color(230, 230, 250),
 'lavender blush': Color(255, 240, 245),
 'lavenderblush': Color(255, 240, 245),
 'lavenderblush1': Color(255, 240, 245),
 'lavenderblush2': Color(238, 224, 229),
 'lavenderblush3': Color(205, 193, 197),
 'lavenderblush4': Color(139, 131, 134),
 'lawn green': Color(124, 252, 0),
 'lawngreen': Color(124, 252, 0),
 'lemon chiffon': Color(255, 250, 205),
 'lemonchiffon': Color(255, 250, 205),
 'lemonchiffon1': Color(255, 250, 205),
 'lemonchiffon2': Color(238, 233, 191),
 'lemonchiffon3': Color(205, 201, 165),
 'lemonchiffon4': Color(139, 137, 112),
 'light blue': Color(173, 216, 230),
 'light coral': Color(240, 128, 128),
 'light cyan': Color(224, 255, 255),
 'light goldenrod': Color(238, 221, 130),
 'light goldenrod yellow': Color(250, 250, 210),
 'light gray': Color(211, 211, 211),
 'light green': Color(144, 238, 144),
 'light grey': Color(211, 211, 211),
 'light pink': Color(255, 182, 193),
 'light salmon': Color(255, 160, 122),
 'light sea green': Color(32, 178, 170),
 'light sky blue': Color(135, 206, 250),
 'light slate blue': Color(132, 112, 255),
 'light slate gray': Color(119, 136, 153),
 'light slate grey': Color(119, 136, 153),
 'light steel blue': Color(176, 196, 222),
 'light yellow': Color(255, 255, 224),
 'lightblue': Color(173, 216, 230),
 'lightblue1': Color(191, 239, 255),
 'lightblue2': Color(178, 223, 238),
 'lightblue3': Color(154, 192, 205),
 'lightblue4': Color(104, 131, 139),
 'lightcoral': Color(240, 128, 128),
 'lightcyan': Color(224, 255, 255),
 'lightcyan1': Color(224, 255, 255),
 'lightcyan2': Color(209, 238, 238),
 'lightcyan3': Color(180, 205, 205),
 'lightcyan4': Color(122, 139, 139),
 'lightgoldenrod': Color(238, 221, 130),
 'lightgoldenrod1': Color(255, 236, 139),
 'lightgoldenrod2': Color(238, 220, 130),
 'lightgoldenrod3': Color(205, 190, 112),
 'lightgoldenrod4': Color(139, 129, 76),
 'lightgoldenrodyellow': Color(250, 250, 210),
 'lightgray': Color(211, 211, 211),
 'lightgreen': Color(144, 238, 144),
 'lightgrey': Color(211, 211, 211),
 'lightpink': Color(255, 182, 193),
 'lightpink1': Color(255, 174, 185),
 'lightpink2': Color(238, 162, 173),
 'lightpink3': Color(205, 140, 149),
 'lightpink4': Color(139, 95, 101),
 'lightsalmon': Color(255, 160, 122),
 'lightsalmon1': Color(255, 160, 122),
 'lightsalmon2': Color(238, 149, 114),
 'lightsalmon3': Color(205, 129, 98),
 'lightsalmon4': Color(139, 87, 66),
 'lightseagreen': Color(32, 178, 170),
 'lightskyblue': Color(135, 206, 250),
 'lightskyblue1': Color(176, 226, 255),
 'lightskyblue2': Color(164, 211, 238),
 'lightskyblue3': Color(141, 182, 205),
 'lightskyblue4': Color(96, 123, 139),
 'lightslateblue': Color(132, 112, 255),
 'lightslategray': Color(119, 136, 153),
 'lightslategrey': Color(119, 136, 153),
 'lightsteelblue': Color(176, 196, 222),
 'lightsteelblue1': Color(202, 225, 255),
 'lightsteelblue2': Color(188, 210, 238),
 'lightsteelblue3': Color(162, 181, 205),
 'lightsteelblue4': Color(110, 123, 139),
 'lightyellow': Color(255, 255, 224),
 'lightyellow1': Color(255, 255, 224),
 'lightyellow2': Color(238, 238, 209),
 'lightyellow3': Color(205, 205, 180),
 'lightyellow4': Color(139, 139, 122),
 'lime green': Color(50, 205, 50),
 'limegreen': Color(50, 205, 50),
 'linen': Color(250, 240, 230),
 'magenta': Color(255, 0, 255),
 'magenta1': Color(255, 0, 255),
 'magenta2': Color(238, 0, 238),
 'magenta3': Color(205, 0, 205),
 'magenta4': Color(139, 0, 139),
 'maroon': Color(176, 48, 96),
 'maroon1': Color(255, 52, 179),
 'maroon2': Color(238, 48, 167),
 'maroon3': Color(205, 41, 144),
 'maroon4': Color(139, 28, 98),
 'medium aquamarine': Color(102, 205, 170),
 'medium blue': Color(0, 0, 205),
 'medium orchid': Color(186, 85, 211),
 'medium purple': Color(147, 112, 219),
 'medium sea green': Color(60, 179, 113),
 'medium slate blue': Color(123, 104, 238),
 'medium spring green': Color(0, 250, 154),
 'medium turquoise': Color(72, 209, 204),
 'medium violet red': Color(199, 21, 133),
 'mediumaquamarine': Color(102, 205, 170),
 'mediumblue': Color(0, 0, 205),
 'mediumorchid': Color(186, 85, 211),
 'mediumorchid1': Color(224, 102, 255),
 'mediumorchid2': Color(209, 95, 238),
 'mediumorchid3': Color(180, 82, 205),
 'mediumorchid4': Color(122, 55, 139),
 'mediumpurple': Color(147, 112, 219),
 'mediumpurple1': Color(171, 130, 255),
 'mediumpurple2': Color(159, 121, 238),
 'mediumpurple3': Color(137, 104, 205),
 'mediumpurple4': Color(93, 71, 139),
 'mediumseagreen': Color(60, 179, 113),
 'mediumslateblue': Color(123, 104, 238),
 'mediumspringgreen': Color(0, 250, 154),
 'mediumturquoise': Color(72, 209, 204),
 'mediumvioletred': Color(199, 21, 133),
 'midnight blue': Color(25, 25, 112),
 'midnightblue': Color(25, 25, 112),
 'mint cream': Color(245, 255, 250),
 'mintcream': Color(245, 255, 250),
 'misty rose': Color(255, 228, 225),
 'mistyrose': Color(255, 228, 225),
 'mistyrose1': Color(255, 228, 225),
 'mistyrose2': Color(238, 213, 210),
 'mistyrose3': Color(205, 183, 181),
 'mistyrose4': Color(139, 125, 123),
 'moccasin': Color(255, 228, 181),
 'navajo white': Color(255, 222, 173),
 'navajowhite': Color(255, 222, 173),
 'navajowhite1': Color(255, 222, 173),
 'navajowhite2': Color(238, 207, 161),
 'navajowhite3': Color(205, 179, 139),
 'navajowhite4': Color(139, 121, 94),
 'navy': Color(0, 0, 128),
 'navy blue': Color(0, 0, 128),
 'navyblue': Color(0, 0, 128),
 'old lace': Color(253, 245, 230),
 'oldlace': Color(253, 245, 230),
 'olive drab': Color(107, 142, 35),
 'olivedrab': Color(107, 142, 35),
 'olivedrab1': Color(192, 255, 62),
 'olivedrab2': Color(179, 238, 58),
 'olivedrab3': Color(154, 205, 50),
 'olivedrab4': Color(105, 139, 34),
 'orange': Color(255, 165, 0),
 'orange red': Color(255, 69, 0),
 'orange1': Color(255, 165, 0),
 'orange2': Color(238, 154, 0),
 'orange3': Color(205, 133, 0),
 'orange4': Color(139, 90, 0),
 'orangered': Color(255, 69, 0),
 'orangered1': Color(255, 69, 0),
 'orangered2': Color(238, 64, 0),
 'orangered3': Color(205, 55, 0),
 'orangered4': Color(139, 37, 0),
 'orchid': Color(218, 112, 214),
 'orchid1': Color(255, 131, 250),
 'orchid2': Color(238, 122, 233),
 'orchid3': Color(205, 105, 201),
 'orchid4': Color(139, 71, 137),
 'pale goldenrod': Color(238, 232, 170),
 'pale green': Color(152, 251, 152),
 'pale turquoise': Color(175, 238, 238),
 'pale violet red': Color(219, 112, 147),
 'palegoldenrod': Color(238, 232, 170),
 'palegreen': Color(152, 251, 152),
 'palegreen1': Color(154, 255, 154),
 'palegreen2': Color(144, 238, 144),
 'palegreen3': Color(124, 205, 124),
 'palegreen4': Color(84, 139, 84),
 'paleturquoise': Color(175, 238, 238),
 'paleturquoise1': Color(187, 255, 255),
 'paleturquoise2': Color(174, 238, 238),
 'paleturquoise3': Color(150, 205, 205),
 'paleturquoise4': Color(102, 139, 139),
 'palevioletred': Color(219, 112, 147),
 'palevioletred1': Color(255, 130, 171),
 'palevioletred2': Color(238, 121, 159),
 'palevioletred3': Color(205, 104, 137),
 'palevioletred4': Color(139, 71, 93),
 'papaya whip': Color(255, 239, 213),
 'papayawhip': Color(255, 239, 213),
 'peach puff': Color(255, 218, 185),
 'peachpuff': Color(255, 218, 185),
 'peachpuff1': Color(255, 218, 185),
 'peachpuff2': Color(238, 203, 173),
 'peachpuff3': Color(205, 175, 149),
 'peachpuff4': Color(139, 119, 101),
 'peru': Color(205, 133, 63),
 'pink': Color(255, 192, 203),
 'pink1': Color(255, 181, 197),
 'pink2': Color(238, 169, 184),
 'pink3': Color(205, 145, 158),
 'pink4': Color(139, 99, 108),
 'plum': Color(221, 160, 221),
 'plum1': Color(255, 187, 255),
 'plum2': Color(238, 174, 238),
 'plum3': Color(205, 150, 205),
 'plum4': Color(139, 102, 139),
 'powder blue': Color(176, 224, 230),
 'powderblue': Color(176, 224, 230),
 'purple': Color(160, 32, 240),
 'purple1': Color(155, 48, 255),
 'purple2': Color(145, 44, 238),
 'purple3': Color(125, 38, 205),
 'purple4': Color(85, 26, 139),
 'red': Color(255, 0, 0),
 'red1': Color(255, 0, 0),
 'red2': Color(238, 0, 0),
 'red3': Color(205, 0, 0),
 'red4': Color(139, 0, 0),
 'rosy brown': Color(188, 143, 143),
 'rosybrown': Color(188, 143, 143),
 'rosybrown1': Color(255, 193, 193),
 'rosybrown2': Color(238, 180, 180),
 'rosybrown3': Color(205, 155, 155),
 'rosybrown4': Color(139, 105, 105),
 'royal blue': Color(65, 105, 225),
 'royalblue': Color(65, 105, 225),
 'royalblue1': Color(72, 118, 255),
 'royalblue2': Color(67, 110, 238),
 'royalblue3': Color(58, 95, 205),
 'royalblue4': Color(39, 64, 139),
 'saddle brown': Color(139, 69, 19),
 'saddlebrown': Color(139, 69, 19),
 'salmon': Color(250, 128, 114),
 'salmon1': Color(255, 140, 105),
 'salmon2': Color(238, 130, 98),
 'salmon3': Color(205, 112, 84),
 'salmon4': Color(139, 76, 57),
 'sandy brown': Color(244, 164, 96),
 'sandybrown': Color(244, 164, 96),
 'sea green': Color(46, 139, 87),
 'seagreen': Color(46, 139, 87),
 'seagreen1': Color(84, 255, 159),
 'seagreen2': Color(78, 238, 148),
 'seagreen3': Color(67, 205, 128),
 'seagreen4': Color(46, 139, 87),
 'seashell': Color(255, 245, 238),
 'seashell1': Color(255, 245, 238),
 'seashell2': Color(238, 229, 222),
 'seashell3': Color(205, 197, 191),
 'seashell4': Color(139, 134, 130),
 'sienna': Color(160, 82, 45),
 'sienna1': Color(255, 130, 71),
 'sienna2': Color(238, 121, 66),
 'sienna3': Color(205, 104, 57),
 'sienna4': Color(139, 71, 38),
 'sky blue': Color(135, 206, 235),
 'skyblue': Color(135, 206, 235),
 'skyblue1': Color(135, 206, 255),
 'skyblue2': Color(126, 192, 238),
 'skyblue3': Color(108, 166, 205),
 'skyblue4': Color(74, 112, 139),
 'slate blue': Color(106, 90, 205),
 'slate gray': Color(112, 128, 144),
 'slate grey': Color(112, 128, 144),
 'slateblue': Color(106, 90, 205),
 'slateblue1': Color(131, 111, 255),
 'slateblue2': Color(122, 103, 238),
 'slateblue3': Color(105, 89, 205),
 'slateblue4': Color(71, 60, 139),
 'slategray': Color(112, 128, 144),
 'slategray1': Color(198, 226, 255),
 'slategray2': Color(185, 211, 238),
 'slategray3': Color(159, 182, 205),
 'slategray4': Color(108, 123, 139),
 'slategrey': Color(112, 128, 144),
 'snow': Color(255, 250, 250),
 'snow1': Color(255, 250, 250),
 'snow2': Color(238, 233, 233),
 'snow3': Color(205, 201, 201),
 'snow4': Color(139, 137, 137),
 'spring green': Color(0, 255, 127),
 'springgreen': Color(0, 255, 127),
 'springgreen1': Color(0, 255, 127),
 'springgreen2': Color(0, 238, 118),
 'springgreen3': Color(0, 205, 102),
 'springgreen4': Color(0, 139, 69),
 'steel blue': Color(70, 130, 180),
 'steelblue': Color(70, 130, 180),
 'steelblue1': Color(99, 184, 255),
 'steelblue2': Color(92, 172, 238),
 'steelblue3': Color(79, 148, 205),
 'steelblue4': Color(54, 100, 139),
 'tan': Color(210, 180, 140),
 'tan1': Color(255, 165, 79),
 'tan2': Color(238, 154, 73),
 'tan3': Color(205, 133, 63),
 'tan4': Color(139, 90, 43),
 'thistle': Color(216, 191, 216),
 'thistle1': Color(255, 225, 255),
 'thistle2': Color(238, 210, 238),
 'thistle3': Color(205, 181, 205),
 'thistle4': Color(139, 123, 139),
 'tomato': Color(255, 99, 71),
 'tomato1': Color(255, 99, 71),
 'tomato2': Color(238, 92, 66),
 'tomato3': Color(205, 79, 57),
 'tomato4': Color(139, 54, 38),
 'turquoise': Color(64, 224, 208),
 'turquoise1': Color(0, 245, 255),
 'turquoise2': Color(0, 229, 238),
 'turquoise3': Color(0, 197, 205),
 'turquoise4': Color(0, 134, 139),
 'violet': Color(238, 130, 238),
 'violet red': Color(208, 32, 144),
 'violetred': Color(208, 32, 144),
 'violetred1': Color(255, 62, 150),
 'violetred2': Color(238, 58, 140),
 'violetred3': Color(205, 50, 120),
 'violetred4': Color(139, 34, 82),
 'wheat': Color(245, 222, 179),
 'wheat1': Color(255, 231, 186),
 'wheat2': Color(238, 216, 174),
 'wheat3': Color(205, 186, 150),
 'wheat4': Color(139, 126, 102),
 'white': Color(255, 255, 255),
 'white smoke': Color(245, 245, 245),
 'whitesmoke': Color(245, 245, 245),
 'yellow': Color(255, 255, 0),
 'yellow green': Color(154, 205, 50),
 'yellow1': Color(255, 255, 0),
 'yellow2': Color(238, 238, 0),
 'yellow3': Color(205, 205, 0),
 'yellow4': Color(139, 139, 0),
 'yellowgreen': Color(154, 205, 50)}
# END_DATA_SECTION }}}

if __name__ == '__main__':
    # Read RGB color table from specified rgb.txt file
    import sys
    import pprint
    data = {}
    for line in open(sys.argv[-1]):
        line = line.strip()
        if not line or line.startswith('!'):
            continue
        parts = line.split()
        r, g, b = map(int, parts[:3])
        name = ' '.join(parts[3:]).lower()
        data[name] = data[name.replace(' ', '')] = r, g, b
    data = pprint.pformat(data).replace('{', '{\n ').replace('(', 'Color(')
    with open(__file__, 'r+') as src:
        raw = src.read()
        raw = re.sub(
            r'^# BEGIN_DATA_SECTION {{{$.*^# END_DATA_SECTION }}}',
            '# BEGIN_DATA_SECTION {{{\ncolor_names = %s\n# END_DATA_SECTION }}}' % data,
            raw, flags=re.DOTALL | re.MULTILINE
        )
        src.seek(0), src.truncate(), src.write(raw)
