# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AimPersonalTemplateContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'content': 'str',
        'content_child': 'str',
        'src_type': 'int',
        'src': 'str',
        'cover': 'str',
        'is_text_title': 'str',
        'action_type': 'str',
        'position_number': 'int',
        'visible': 'int',
        'currency_display': 'int',
        'oppo_background': 'str',
        'vivo_background': 'str',
        'ratio': 'str',
        'action': 'AimPersonalTemplateContentAction',
        'button_type': 'str'
    }

    attribute_map = {
        'type': 'type',
        'content': 'content',
        'content_child': 'content_child',
        'src_type': 'src_type',
        'src': 'src',
        'cover': 'cover',
        'is_text_title': 'is_text_title',
        'action_type': 'action_type',
        'position_number': 'position_number',
        'visible': 'visible',
        'currency_display': 'currency_display',
        'oppo_background': 'oppo_background',
        'vivo_background': 'vivo_background',
        'ratio': 'ratio',
        'action': 'action',
        'button_type': 'button_type'
    }

    def __init__(self, type=None, content=None, content_child=None, src_type=None, src=None, cover=None, is_text_title=None, action_type=None, position_number=None, visible=None, currency_display=None, oppo_background=None, vivo_background=None, ratio=None, action=None, button_type=None):
        r"""AimPersonalTemplateContent

        The model defined in huaweicloud sdk

        :param type: 模板资源类型。 - text：表示文本 - image：表示图片 - video：表示视频 - button：表示按钮 - followPub：表示华为服务号，暂不支持  &gt; 图片轮播类模板最多可以放5张图片，即card_id为CarouselSquareImage、CarouselImageSixteenToNine、CarouselVerticalImage时，type为image的资源最多有5个。 
        :type type: str
        :param content: 资源类型为Text或Button时，为必填。文本长度限制请按智能短信模板版式格式标准。  &gt; 智能信息模板标准版式要求可登录KooMessage控制台，在创建智能信息模板中查看。 
        :type content: str
        :param content_child: 子内容。非必填，文本长度限制请参考智能信息模板标准版式要求。  &gt; 智能信息模板标准版式要求可登录KooMessage控制台，在创建智能信息模板中查看。 
        :type content_child: str
        :param src_type: src类型。资源类型为Image或Video时，该项为必填项。 - 1：指资源ID  - 2：指资源地址  &gt; src_type为2，即资源地址时，src或cover内容必须是存储在客户侧服务器上的资源地址。 
        :type src_type: int
        :param src: 资源来源，资源类型为Image或Video时，为必填，通过设置视频模板封面图接口设置视频封面。 &gt; - 如上src_type为1，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 &gt; - 如上src_type为2，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符  
        :type src: str
        :param cover: 视频封面。 &gt; 资源类型为Video时，为必填。 &gt; - 如上src_type为1，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 &gt; - 如上src_type为2，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符 
        :type cover: str
        :param is_text_title: 是否为文本标题。  - true：是 - false：不是  &gt; 不填默认为false。 
        :type is_text_title: str
        :param action_type: 功能类型。  - OPEN_URL：表示跳转H5 - OPEN_QUICK：表示跳转快应用 - OPEN_APP：表示跳转APP - DIAL_PHONE：表示拉起拨号盘 - OPEN_SMS：表示新建短信息 - OPEN_EMAIL：表示打开邮箱 - OPEN_SCHEDULE：表示新建日程 - OPEN_MAP：表示位置定位 - OPEN_BROWSER：表示打开浏览器 - OPEN_POPUP：表示弹窗 - COPY_PARAMETER：表示复制 - VIEW_PIC：表示打开大图  &gt; - type为Image和Button时为必填项，必须绑定事件 &gt; - type为其他类型时则不必填 &gt; - OPPO厂商点击事件类型只支持打开浏览器、打开快应用、打开APP、跳转H5 &gt; - VIVO厂商点击事件类型不支持打开邮箱、打开地图 &gt; - MEIZU厂商点击事件类型不支持打开大图 &gt; - 横滑类1、横滑类2版式的图片不支持绑定事件，默认与按钮事件一致 &gt; - 三星厂商点击事件类型不支持新建日程、打开大图  
        :type action_type: str
        :param position_number: 卡片组件的位置序号。 &gt; 资源在卡片上相对的位置序号，按照优先从左到右，再从上到下的编排原则，统一编号。 
        :type position_number: int
        :param visible: 组件是否可见。 - 0：隐藏（某些组件可设置隐藏） - 1：可见  &gt; 目前仅针对电商多商品（Ecommerce）、多卡券（CardVouchers）、增强机票类（PlaneTrip）这三种版式起效。 
        :type visible: int
        :param currency_display: 是否显示货币符号。  - 0：隐藏  - 1：可见  &gt; 当模板为电商类时是否显示￥符号，默认可见。 
        :type currency_display: int
        :param oppo_background: OPPO红包背景。  &gt; - 当src_type为1时，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 &gt; - 当src_type为2时，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符 &gt;- 当模板为红包类，即card_id为RedPacket时用于指定OPPO厂商红包背景图，具体使用可参考创建红包类模板请求示例 
        :type oppo_background: str
        :param vivo_background: VIVO红包背景。  &gt; - 当src_type为1时，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 &gt; - 当src_type为2时，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符 
        :type vivo_background: str
        :param ratio: 表示短视频模板视频和封面的宽高比。即card_id为ShortVideo时，此项有值。 - threeToFour: 宽高比为3:4 - oneToOne: 宽高比为1:1 
        :type ratio: str
        :param action: 
        :type action: :class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateContentAction`
        :param button_type: 当模板为电商领券类竖版，即card_id为EcommerceCouponVertical时用于指定按钮类型，具体使用可参考创建电商领券类竖版模板请求示例。 - static：静态按钮 - dynamic：动态按钮 
        :type button_type: str
        """
        
        

        self._type = None
        self._content = None
        self._content_child = None
        self._src_type = None
        self._src = None
        self._cover = None
        self._is_text_title = None
        self._action_type = None
        self._position_number = None
        self._visible = None
        self._currency_display = None
        self._oppo_background = None
        self._vivo_background = None
        self._ratio = None
        self._action = None
        self._button_type = None
        self.discriminator = None

        self.type = type
        if content is not None:
            self.content = content
        if content_child is not None:
            self.content_child = content_child
        if src_type is not None:
            self.src_type = src_type
        if src is not None:
            self.src = src
        if cover is not None:
            self.cover = cover
        if is_text_title is not None:
            self.is_text_title = is_text_title
        if action_type is not None:
            self.action_type = action_type
        self.position_number = position_number
        if visible is not None:
            self.visible = visible
        if currency_display is not None:
            self.currency_display = currency_display
        if oppo_background is not None:
            self.oppo_background = oppo_background
        if vivo_background is not None:
            self.vivo_background = vivo_background
        if ratio is not None:
            self.ratio = ratio
        if action is not None:
            self.action = action
        if button_type is not None:
            self.button_type = button_type

    @property
    def type(self):
        r"""Gets the type of this AimPersonalTemplateContent.

        模板资源类型。 - text：表示文本 - image：表示图片 - video：表示视频 - button：表示按钮 - followPub：表示华为服务号，暂不支持  > 图片轮播类模板最多可以放5张图片，即card_id为CarouselSquareImage、CarouselImageSixteenToNine、CarouselVerticalImage时，type为image的资源最多有5个。 

        :return: The type of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AimPersonalTemplateContent.

        模板资源类型。 - text：表示文本 - image：表示图片 - video：表示视频 - button：表示按钮 - followPub：表示华为服务号，暂不支持  > 图片轮播类模板最多可以放5张图片，即card_id为CarouselSquareImage、CarouselImageSixteenToNine、CarouselVerticalImage时，type为image的资源最多有5个。 

        :param type: The type of this AimPersonalTemplateContent.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        r"""Gets the content of this AimPersonalTemplateContent.

        资源类型为Text或Button时，为必填。文本长度限制请按智能短信模板版式格式标准。  > 智能信息模板标准版式要求可登录KooMessage控制台，在创建智能信息模板中查看。 

        :return: The content of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this AimPersonalTemplateContent.

        资源类型为Text或Button时，为必填。文本长度限制请按智能短信模板版式格式标准。  > 智能信息模板标准版式要求可登录KooMessage控制台，在创建智能信息模板中查看。 

        :param content: The content of this AimPersonalTemplateContent.
        :type content: str
        """
        self._content = content

    @property
    def content_child(self):
        r"""Gets the content_child of this AimPersonalTemplateContent.

        子内容。非必填，文本长度限制请参考智能信息模板标准版式要求。  > 智能信息模板标准版式要求可登录KooMessage控制台，在创建智能信息模板中查看。 

        :return: The content_child of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._content_child

    @content_child.setter
    def content_child(self, content_child):
        r"""Sets the content_child of this AimPersonalTemplateContent.

        子内容。非必填，文本长度限制请参考智能信息模板标准版式要求。  > 智能信息模板标准版式要求可登录KooMessage控制台，在创建智能信息模板中查看。 

        :param content_child: The content_child of this AimPersonalTemplateContent.
        :type content_child: str
        """
        self._content_child = content_child

    @property
    def src_type(self):
        r"""Gets the src_type of this AimPersonalTemplateContent.

        src类型。资源类型为Image或Video时，该项为必填项。 - 1：指资源ID  - 2：指资源地址  > src_type为2，即资源地址时，src或cover内容必须是存储在客户侧服务器上的资源地址。 

        :return: The src_type of this AimPersonalTemplateContent.
        :rtype: int
        """
        return self._src_type

    @src_type.setter
    def src_type(self, src_type):
        r"""Sets the src_type of this AimPersonalTemplateContent.

        src类型。资源类型为Image或Video时，该项为必填项。 - 1：指资源ID  - 2：指资源地址  > src_type为2，即资源地址时，src或cover内容必须是存储在客户侧服务器上的资源地址。 

        :param src_type: The src_type of this AimPersonalTemplateContent.
        :type src_type: int
        """
        self._src_type = src_type

    @property
    def src(self):
        r"""Gets the src of this AimPersonalTemplateContent.

        资源来源，资源类型为Image或Video时，为必填，通过设置视频模板封面图接口设置视频封面。 > - 如上src_type为1，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 > - 如上src_type为2，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符  

        :return: The src of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        r"""Sets the src of this AimPersonalTemplateContent.

        资源来源，资源类型为Image或Video时，为必填，通过设置视频模板封面图接口设置视频封面。 > - 如上src_type为1，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 > - 如上src_type为2，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符  

        :param src: The src of this AimPersonalTemplateContent.
        :type src: str
        """
        self._src = src

    @property
    def cover(self):
        r"""Gets the cover of this AimPersonalTemplateContent.

        视频封面。 > 资源类型为Video时，为必填。 > - 如上src_type为1，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 > - 如上src_type为2，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符 

        :return: The cover of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        r"""Sets the cover of this AimPersonalTemplateContent.

        视频封面。 > 资源类型为Video时，为必填。 > - 如上src_type为1，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 > - 如上src_type为2，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符 

        :param cover: The cover of this AimPersonalTemplateContent.
        :type cover: str
        """
        self._cover = cover

    @property
    def is_text_title(self):
        r"""Gets the is_text_title of this AimPersonalTemplateContent.

        是否为文本标题。  - true：是 - false：不是  > 不填默认为false。 

        :return: The is_text_title of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._is_text_title

    @is_text_title.setter
    def is_text_title(self, is_text_title):
        r"""Sets the is_text_title of this AimPersonalTemplateContent.

        是否为文本标题。  - true：是 - false：不是  > 不填默认为false。 

        :param is_text_title: The is_text_title of this AimPersonalTemplateContent.
        :type is_text_title: str
        """
        self._is_text_title = is_text_title

    @property
    def action_type(self):
        r"""Gets the action_type of this AimPersonalTemplateContent.

        功能类型。  - OPEN_URL：表示跳转H5 - OPEN_QUICK：表示跳转快应用 - OPEN_APP：表示跳转APP - DIAL_PHONE：表示拉起拨号盘 - OPEN_SMS：表示新建短信息 - OPEN_EMAIL：表示打开邮箱 - OPEN_SCHEDULE：表示新建日程 - OPEN_MAP：表示位置定位 - OPEN_BROWSER：表示打开浏览器 - OPEN_POPUP：表示弹窗 - COPY_PARAMETER：表示复制 - VIEW_PIC：表示打开大图  > - type为Image和Button时为必填项，必须绑定事件 > - type为其他类型时则不必填 > - OPPO厂商点击事件类型只支持打开浏览器、打开快应用、打开APP、跳转H5 > - VIVO厂商点击事件类型不支持打开邮箱、打开地图 > - MEIZU厂商点击事件类型不支持打开大图 > - 横滑类1、横滑类2版式的图片不支持绑定事件，默认与按钮事件一致 > - 三星厂商点击事件类型不支持新建日程、打开大图  

        :return: The action_type of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this AimPersonalTemplateContent.

        功能类型。  - OPEN_URL：表示跳转H5 - OPEN_QUICK：表示跳转快应用 - OPEN_APP：表示跳转APP - DIAL_PHONE：表示拉起拨号盘 - OPEN_SMS：表示新建短信息 - OPEN_EMAIL：表示打开邮箱 - OPEN_SCHEDULE：表示新建日程 - OPEN_MAP：表示位置定位 - OPEN_BROWSER：表示打开浏览器 - OPEN_POPUP：表示弹窗 - COPY_PARAMETER：表示复制 - VIEW_PIC：表示打开大图  > - type为Image和Button时为必填项，必须绑定事件 > - type为其他类型时则不必填 > - OPPO厂商点击事件类型只支持打开浏览器、打开快应用、打开APP、跳转H5 > - VIVO厂商点击事件类型不支持打开邮箱、打开地图 > - MEIZU厂商点击事件类型不支持打开大图 > - 横滑类1、横滑类2版式的图片不支持绑定事件，默认与按钮事件一致 > - 三星厂商点击事件类型不支持新建日程、打开大图  

        :param action_type: The action_type of this AimPersonalTemplateContent.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def position_number(self):
        r"""Gets the position_number of this AimPersonalTemplateContent.

        卡片组件的位置序号。 > 资源在卡片上相对的位置序号，按照优先从左到右，再从上到下的编排原则，统一编号。 

        :return: The position_number of this AimPersonalTemplateContent.
        :rtype: int
        """
        return self._position_number

    @position_number.setter
    def position_number(self, position_number):
        r"""Sets the position_number of this AimPersonalTemplateContent.

        卡片组件的位置序号。 > 资源在卡片上相对的位置序号，按照优先从左到右，再从上到下的编排原则，统一编号。 

        :param position_number: The position_number of this AimPersonalTemplateContent.
        :type position_number: int
        """
        self._position_number = position_number

    @property
    def visible(self):
        r"""Gets the visible of this AimPersonalTemplateContent.

        组件是否可见。 - 0：隐藏（某些组件可设置隐藏） - 1：可见  > 目前仅针对电商多商品（Ecommerce）、多卡券（CardVouchers）、增强机票类（PlaneTrip）这三种版式起效。 

        :return: The visible of this AimPersonalTemplateContent.
        :rtype: int
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this AimPersonalTemplateContent.

        组件是否可见。 - 0：隐藏（某些组件可设置隐藏） - 1：可见  > 目前仅针对电商多商品（Ecommerce）、多卡券（CardVouchers）、增强机票类（PlaneTrip）这三种版式起效。 

        :param visible: The visible of this AimPersonalTemplateContent.
        :type visible: int
        """
        self._visible = visible

    @property
    def currency_display(self):
        r"""Gets the currency_display of this AimPersonalTemplateContent.

        是否显示货币符号。  - 0：隐藏  - 1：可见  > 当模板为电商类时是否显示￥符号，默认可见。 

        :return: The currency_display of this AimPersonalTemplateContent.
        :rtype: int
        """
        return self._currency_display

    @currency_display.setter
    def currency_display(self, currency_display):
        r"""Sets the currency_display of this AimPersonalTemplateContent.

        是否显示货币符号。  - 0：隐藏  - 1：可见  > 当模板为电商类时是否显示￥符号，默认可见。 

        :param currency_display: The currency_display of this AimPersonalTemplateContent.
        :type currency_display: int
        """
        self._currency_display = currency_display

    @property
    def oppo_background(self):
        r"""Gets the oppo_background of this AimPersonalTemplateContent.

        OPPO红包背景。  > - 当src_type为1时，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 > - 当src_type为2时，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符 >- 当模板为红包类，即card_id为RedPacket时用于指定OPPO厂商红包背景图，具体使用可参考创建红包类模板请求示例 

        :return: The oppo_background of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._oppo_background

    @oppo_background.setter
    def oppo_background(self, oppo_background):
        r"""Sets the oppo_background of this AimPersonalTemplateContent.

        OPPO红包背景。  > - 当src_type为1时，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 > - 当src_type为2时，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符 >- 当模板为红包类，即card_id为RedPacket时用于指定OPPO厂商红包背景图，具体使用可参考创建红包类模板请求示例 

        :param oppo_background: The oppo_background of this AimPersonalTemplateContent.
        :type oppo_background: str
        """
        self._oppo_background = oppo_background

    @property
    def vivo_background(self):
        r"""Gets the vivo_background of this AimPersonalTemplateContent.

        VIVO红包背景。  > - 当src_type为1时，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 > - 当src_type为2时，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符 

        :return: The vivo_background of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._vivo_background

    @vivo_background.setter
    def vivo_background(self, vivo_background):
        r"""Sets the vivo_background of this AimPersonalTemplateContent.

        VIVO红包背景。  > - 当src_type为1时，即资源ID时，参数填入上传模板素材接口中返回的aim_resource_id，如：691996319597764608 > - 当src_type为2时，即资源地址时，参数填写资源完整的URL，最大长度不超过1000个字符 

        :param vivo_background: The vivo_background of this AimPersonalTemplateContent.
        :type vivo_background: str
        """
        self._vivo_background = vivo_background

    @property
    def ratio(self):
        r"""Gets the ratio of this AimPersonalTemplateContent.

        表示短视频模板视频和封面的宽高比。即card_id为ShortVideo时，此项有值。 - threeToFour: 宽高比为3:4 - oneToOne: 宽高比为1:1 

        :return: The ratio of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        r"""Sets the ratio of this AimPersonalTemplateContent.

        表示短视频模板视频和封面的宽高比。即card_id为ShortVideo时，此项有值。 - threeToFour: 宽高比为3:4 - oneToOne: 宽高比为1:1 

        :param ratio: The ratio of this AimPersonalTemplateContent.
        :type ratio: str
        """
        self._ratio = ratio

    @property
    def action(self):
        r"""Gets the action of this AimPersonalTemplateContent.

        :return: The action of this AimPersonalTemplateContent.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateContentAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this AimPersonalTemplateContent.

        :param action: The action of this AimPersonalTemplateContent.
        :type action: :class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateContentAction`
        """
        self._action = action

    @property
    def button_type(self):
        r"""Gets the button_type of this AimPersonalTemplateContent.

        当模板为电商领券类竖版，即card_id为EcommerceCouponVertical时用于指定按钮类型，具体使用可参考创建电商领券类竖版模板请求示例。 - static：静态按钮 - dynamic：动态按钮 

        :return: The button_type of this AimPersonalTemplateContent.
        :rtype: str
        """
        return self._button_type

    @button_type.setter
    def button_type(self, button_type):
        r"""Sets the button_type of this AimPersonalTemplateContent.

        当模板为电商领券类竖版，即card_id为EcommerceCouponVertical时用于指定按钮类型，具体使用可参考创建电商领券类竖版模板请求示例。 - static：静态按钮 - dynamic：动态按钮 

        :param button_type: The button_type of this AimPersonalTemplateContent.
        :type button_type: str
        """
        self._button_type = button_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AimPersonalTemplateContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
