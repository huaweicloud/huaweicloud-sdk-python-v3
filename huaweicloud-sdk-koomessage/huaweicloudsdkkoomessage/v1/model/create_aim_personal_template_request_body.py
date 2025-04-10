# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAimPersonalTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'card_id': 'str',
        'tpl_name': 'str',
        'scene': 'str',
        'use_id': 'int',
        'sub_type': 'int',
        'sms_example': 'str',
        'sms_signs': 'list[str]',
        'sms_template': 'str',
        'pages': 'list[AimPersonalTemplatePage]',
        'params': 'list[AimPersonalTemplateParam]',
        'factorys': 'list[AimPersonalTemplateFactory]'
    }

    attribute_map = {
        'card_id': 'card_id',
        'tpl_name': 'tpl_name',
        'scene': 'scene',
        'use_id': 'use_id',
        'sub_type': 'sub_type',
        'sms_example': 'sms_example',
        'sms_signs': 'sms_signs',
        'sms_template': 'sms_template',
        'pages': 'pages',
        'params': 'params',
        'factorys': 'factorys'
    }

    def __init__(self, card_id=None, tpl_name=None, scene=None, use_id=None, sub_type=None, sms_example=None, sms_signs=None, sms_template=None, pages=None, params=None, factorys=None):
        r"""CreateAimPersonalTemplateRequestBody

        The model defined in huaweicloud sdk

        :param card_id: 布局类型。 - MultipleImageAndText：多图文类 - StandardImageAndText：图文类 - PureText：长文本类 - VideoImageAndText：视频图文类 - Video：视频类 - ECImageAndText：电商类 - RedPacket：红包类 - RedPacketPersonal：个性化红包类 - ImageTextAndVideo：图文视频类 - Notification1：一般通知类 - Notification2：增强通知类 - Carousel：横滑类1 - CarouselTitle：横滑类2 - CarouselSquareImage：图片轮播类（1:1） - CarouselImageSixteenToNine：图片轮播类（16:9） - CarouselVerticalImage：图片轮播类（48:65） - CardVoucher：单卡券 - CardVouchers：多卡券（最多支持四张卡券） - Ecommerce：电商多商品类 - Trip1：机票类 - Trip2：火车票类 - Trip3：汽车票类 - PlaneTrip：增强机票类 - SimplePoster：海报类 - NativePureText：超文本普通类 - NativeImageAndText：超文本增强类 - ShortVideo：短剧视频类 - ShortVideoImage：短剧图片类 - EcommerceCouponVertical：电商领券类竖版  &gt; 当送审厂商包含vivo时，各布局类型上传的图片最小像素要求如下： &gt; - card_id为StandardImageAndText，宽高比为16:9时，图片的最小像素为1088px*612px。 &gt; - card_id为MultipleImageAndText，宽高比为16:9时，图片的最小像素为1088px*612px。 &gt; - card_id为MultipleImageAndText，宽高比为1:1时，图片的最小像素为320px*320px。 &gt; - card_id为Video，宽高比为16:9时，视频封面图片的最小像素为1088px*612px。 &gt; - card_id为RedPacket，宽高比为1:1时，图片的最小像素为320px*320px。 &gt; - card_id为CarouselImageSixteenToNine，宽高比为16:9时，图片的最小像素为1088px*612px。 &gt; - card_id为CarouselSquareImage，宽高比为1:1时，图片的最小像素为1088px*1088px。 &gt; - card_id为CarouselVerticalImage，宽高比为48:65时，图片的最小像素为960px*1300px。 &gt; - card_id为Notification1，宽高比为3:1时，图片的最小像素为576px*192px。 &gt; - card_id为Notification2，宽高比为3:1时，图片的最小像素为576px*192px。 &gt; - card_id为ECImageAndText，宽高比为1:1时，图片的最小像素为1088px*1088px。 
        :type card_id: str
        :param tpl_name: 智能信息模板名称。
        :type tpl_name: str
        :param scene: 模板使用场景类型。
        :type scene: str
        :param use_id: 模板用途。  - 1：表示商用 - 2：表示试商用   &gt; - 模板用途为1，即“商用”时，所有字段中不允许有测试字样，否则影响送审 &gt; - 模板用途为2，即“试商用”时，请在模板名称（tpl_name）、模板主标题中增加测试字样 
        :type use_id: int
        :param sub_type: 版式子类型。 &gt; - 当card_id为RedPacket和RedPacketPersonal时，sub_type用于设置按钮样式，1表示静态按钮，2表示动态按钮。目前仅华为厂商支持动态按钮。 &gt; - 当card_id为ECImageAndText时，sub_type用于设置左右按钮组合颜色，默认值为1，1表示左边按钮为橙色，右边按钮为红色；2表示左边按钮为绿色，右边按钮为黄色；3表示左边按钮为绿色，右边按钮为蓝色；4表示左边按钮为紫色，右边按钮为蓝色；5表示左边按钮为黑色，右边按钮为玫粉色。仅华为厂商支持sub_type取值为2、3、4、5。 &gt; - 当card_id为CarouselVerticalImage时，sub_type用于设置按钮颜色，1表示蓝色(默认颜色)、2表示黑色、3表示紫色、4表示金色、5表示粉色、6表示玫粉。仅华为厂商支持sub_type取值为2、3、4、5、6。 &gt; - 当card_id为CardVoucher时，sub_type用于设置按钮样式，1表示静态按钮，2表示动态按钮。目前仅华为厂商支持动态按钮。 &gt; - 当card_id为ShortVideoImage时，sub_type用于设置是否显示播放图标，1表示不显示，2表示显示。 &gt; - 当card_id为EcommerceCouponVertical和EcommerceCouponHorizontal时，sub_type用于设置卡券区是否隐藏。sub_type设置为1，卡券区（position_number为4~7）的visible设置为1，且卡券区（position_number为7）的button_type设置为static或dynamic时，显示卡券区；sub_type设置为2，卡券区（position_number为4~7）的visible设置为0，且卡券区（position_number为7）的button_type设置为空值或不带该字段时，卡券区被隐藏。
        :type sub_type: int
        :param sms_example: 要发送的原始文本消息示例。
        :type sms_example: str
        :param sms_signs: 短信签名。最多可以传三个签名，发送短信时，只要能匹配其中一个即可。填写的短信签名为企业绑定的签名，每个签名最多20个字，支持输入中文，英文，数字，符号，单个签名内容不包括中括号。  &gt; 选择厂商包含VIVO时，此参数必填。 
        :type sms_signs: list[str]
        :param sms_template: 短信原文模板。参数示例：尊敬的客户，截至[文本0-20]，您本月国内通用流量已使用[数字0-4]GB，使用到[数字0-4]GB ，整体上网速度将不高于[数字0-2]Mbps。您可点击[字母0-20]获取[文本0-20]。  &gt; - 正则类型仅支持文本、字母、数字三种，且长度最大为99，且中括号为英文中括号。静态短信文案加正则动态文案最大值的总字数不超过370个字符 &gt; - 选择厂商包含VIVO时，此参数必填 
        :type sms_template: str
        :param pages: 模板协议，最大支持10页协议。
        :type pages: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplatePage`]
        :param params: 模板参数集。
        :type params: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateParam`]
        :param factorys: 需要提交的厂商列表。
        :type factorys: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateFactory`]
        """
        
        

        self._card_id = None
        self._tpl_name = None
        self._scene = None
        self._use_id = None
        self._sub_type = None
        self._sms_example = None
        self._sms_signs = None
        self._sms_template = None
        self._pages = None
        self._params = None
        self._factorys = None
        self.discriminator = None

        self.card_id = card_id
        self.tpl_name = tpl_name
        if scene is not None:
            self.scene = scene
        self.use_id = use_id
        if sub_type is not None:
            self.sub_type = sub_type
        if sms_example is not None:
            self.sms_example = sms_example
        if sms_signs is not None:
            self.sms_signs = sms_signs
        if sms_template is not None:
            self.sms_template = sms_template
        self.pages = pages
        if params is not None:
            self.params = params
        if factorys is not None:
            self.factorys = factorys

    @property
    def card_id(self):
        r"""Gets the card_id of this CreateAimPersonalTemplateRequestBody.

        布局类型。 - MultipleImageAndText：多图文类 - StandardImageAndText：图文类 - PureText：长文本类 - VideoImageAndText：视频图文类 - Video：视频类 - ECImageAndText：电商类 - RedPacket：红包类 - RedPacketPersonal：个性化红包类 - ImageTextAndVideo：图文视频类 - Notification1：一般通知类 - Notification2：增强通知类 - Carousel：横滑类1 - CarouselTitle：横滑类2 - CarouselSquareImage：图片轮播类（1:1） - CarouselImageSixteenToNine：图片轮播类（16:9） - CarouselVerticalImage：图片轮播类（48:65） - CardVoucher：单卡券 - CardVouchers：多卡券（最多支持四张卡券） - Ecommerce：电商多商品类 - Trip1：机票类 - Trip2：火车票类 - Trip3：汽车票类 - PlaneTrip：增强机票类 - SimplePoster：海报类 - NativePureText：超文本普通类 - NativeImageAndText：超文本增强类 - ShortVideo：短剧视频类 - ShortVideoImage：短剧图片类 - EcommerceCouponVertical：电商领券类竖版  > 当送审厂商包含vivo时，各布局类型上传的图片最小像素要求如下： > - card_id为StandardImageAndText，宽高比为16:9时，图片的最小像素为1088px*612px。 > - card_id为MultipleImageAndText，宽高比为16:9时，图片的最小像素为1088px*612px。 > - card_id为MultipleImageAndText，宽高比为1:1时，图片的最小像素为320px*320px。 > - card_id为Video，宽高比为16:9时，视频封面图片的最小像素为1088px*612px。 > - card_id为RedPacket，宽高比为1:1时，图片的最小像素为320px*320px。 > - card_id为CarouselImageSixteenToNine，宽高比为16:9时，图片的最小像素为1088px*612px。 > - card_id为CarouselSquareImage，宽高比为1:1时，图片的最小像素为1088px*1088px。 > - card_id为CarouselVerticalImage，宽高比为48:65时，图片的最小像素为960px*1300px。 > - card_id为Notification1，宽高比为3:1时，图片的最小像素为576px*192px。 > - card_id为Notification2，宽高比为3:1时，图片的最小像素为576px*192px。 > - card_id为ECImageAndText，宽高比为1:1时，图片的最小像素为1088px*1088px。 

        :return: The card_id of this CreateAimPersonalTemplateRequestBody.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        r"""Sets the card_id of this CreateAimPersonalTemplateRequestBody.

        布局类型。 - MultipleImageAndText：多图文类 - StandardImageAndText：图文类 - PureText：长文本类 - VideoImageAndText：视频图文类 - Video：视频类 - ECImageAndText：电商类 - RedPacket：红包类 - RedPacketPersonal：个性化红包类 - ImageTextAndVideo：图文视频类 - Notification1：一般通知类 - Notification2：增强通知类 - Carousel：横滑类1 - CarouselTitle：横滑类2 - CarouselSquareImage：图片轮播类（1:1） - CarouselImageSixteenToNine：图片轮播类（16:9） - CarouselVerticalImage：图片轮播类（48:65） - CardVoucher：单卡券 - CardVouchers：多卡券（最多支持四张卡券） - Ecommerce：电商多商品类 - Trip1：机票类 - Trip2：火车票类 - Trip3：汽车票类 - PlaneTrip：增强机票类 - SimplePoster：海报类 - NativePureText：超文本普通类 - NativeImageAndText：超文本增强类 - ShortVideo：短剧视频类 - ShortVideoImage：短剧图片类 - EcommerceCouponVertical：电商领券类竖版  > 当送审厂商包含vivo时，各布局类型上传的图片最小像素要求如下： > - card_id为StandardImageAndText，宽高比为16:9时，图片的最小像素为1088px*612px。 > - card_id为MultipleImageAndText，宽高比为16:9时，图片的最小像素为1088px*612px。 > - card_id为MultipleImageAndText，宽高比为1:1时，图片的最小像素为320px*320px。 > - card_id为Video，宽高比为16:9时，视频封面图片的最小像素为1088px*612px。 > - card_id为RedPacket，宽高比为1:1时，图片的最小像素为320px*320px。 > - card_id为CarouselImageSixteenToNine，宽高比为16:9时，图片的最小像素为1088px*612px。 > - card_id为CarouselSquareImage，宽高比为1:1时，图片的最小像素为1088px*1088px。 > - card_id为CarouselVerticalImage，宽高比为48:65时，图片的最小像素为960px*1300px。 > - card_id为Notification1，宽高比为3:1时，图片的最小像素为576px*192px。 > - card_id为Notification2，宽高比为3:1时，图片的最小像素为576px*192px。 > - card_id为ECImageAndText，宽高比为1:1时，图片的最小像素为1088px*1088px。 

        :param card_id: The card_id of this CreateAimPersonalTemplateRequestBody.
        :type card_id: str
        """
        self._card_id = card_id

    @property
    def tpl_name(self):
        r"""Gets the tpl_name of this CreateAimPersonalTemplateRequestBody.

        智能信息模板名称。

        :return: The tpl_name of this CreateAimPersonalTemplateRequestBody.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        r"""Sets the tpl_name of this CreateAimPersonalTemplateRequestBody.

        智能信息模板名称。

        :param tpl_name: The tpl_name of this CreateAimPersonalTemplateRequestBody.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def scene(self):
        r"""Gets the scene of this CreateAimPersonalTemplateRequestBody.

        模板使用场景类型。

        :return: The scene of this CreateAimPersonalTemplateRequestBody.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this CreateAimPersonalTemplateRequestBody.

        模板使用场景类型。

        :param scene: The scene of this CreateAimPersonalTemplateRequestBody.
        :type scene: str
        """
        self._scene = scene

    @property
    def use_id(self):
        r"""Gets the use_id of this CreateAimPersonalTemplateRequestBody.

        模板用途。  - 1：表示商用 - 2：表示试商用   > - 模板用途为1，即“商用”时，所有字段中不允许有测试字样，否则影响送审 > - 模板用途为2，即“试商用”时，请在模板名称（tpl_name）、模板主标题中增加测试字样 

        :return: The use_id of this CreateAimPersonalTemplateRequestBody.
        :rtype: int
        """
        return self._use_id

    @use_id.setter
    def use_id(self, use_id):
        r"""Sets the use_id of this CreateAimPersonalTemplateRequestBody.

        模板用途。  - 1：表示商用 - 2：表示试商用   > - 模板用途为1，即“商用”时，所有字段中不允许有测试字样，否则影响送审 > - 模板用途为2，即“试商用”时，请在模板名称（tpl_name）、模板主标题中增加测试字样 

        :param use_id: The use_id of this CreateAimPersonalTemplateRequestBody.
        :type use_id: int
        """
        self._use_id = use_id

    @property
    def sub_type(self):
        r"""Gets the sub_type of this CreateAimPersonalTemplateRequestBody.

        版式子类型。 > - 当card_id为RedPacket和RedPacketPersonal时，sub_type用于设置按钮样式，1表示静态按钮，2表示动态按钮。目前仅华为厂商支持动态按钮。 > - 当card_id为ECImageAndText时，sub_type用于设置左右按钮组合颜色，默认值为1，1表示左边按钮为橙色，右边按钮为红色；2表示左边按钮为绿色，右边按钮为黄色；3表示左边按钮为绿色，右边按钮为蓝色；4表示左边按钮为紫色，右边按钮为蓝色；5表示左边按钮为黑色，右边按钮为玫粉色。仅华为厂商支持sub_type取值为2、3、4、5。 > - 当card_id为CarouselVerticalImage时，sub_type用于设置按钮颜色，1表示蓝色(默认颜色)、2表示黑色、3表示紫色、4表示金色、5表示粉色、6表示玫粉。仅华为厂商支持sub_type取值为2、3、4、5、6。 > - 当card_id为CardVoucher时，sub_type用于设置按钮样式，1表示静态按钮，2表示动态按钮。目前仅华为厂商支持动态按钮。 > - 当card_id为ShortVideoImage时，sub_type用于设置是否显示播放图标，1表示不显示，2表示显示。 > - 当card_id为EcommerceCouponVertical和EcommerceCouponHorizontal时，sub_type用于设置卡券区是否隐藏。sub_type设置为1，卡券区（position_number为4~7）的visible设置为1，且卡券区（position_number为7）的button_type设置为static或dynamic时，显示卡券区；sub_type设置为2，卡券区（position_number为4~7）的visible设置为0，且卡券区（position_number为7）的button_type设置为空值或不带该字段时，卡券区被隐藏。

        :return: The sub_type of this CreateAimPersonalTemplateRequestBody.
        :rtype: int
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        r"""Sets the sub_type of this CreateAimPersonalTemplateRequestBody.

        版式子类型。 > - 当card_id为RedPacket和RedPacketPersonal时，sub_type用于设置按钮样式，1表示静态按钮，2表示动态按钮。目前仅华为厂商支持动态按钮。 > - 当card_id为ECImageAndText时，sub_type用于设置左右按钮组合颜色，默认值为1，1表示左边按钮为橙色，右边按钮为红色；2表示左边按钮为绿色，右边按钮为黄色；3表示左边按钮为绿色，右边按钮为蓝色；4表示左边按钮为紫色，右边按钮为蓝色；5表示左边按钮为黑色，右边按钮为玫粉色。仅华为厂商支持sub_type取值为2、3、4、5。 > - 当card_id为CarouselVerticalImage时，sub_type用于设置按钮颜色，1表示蓝色(默认颜色)、2表示黑色、3表示紫色、4表示金色、5表示粉色、6表示玫粉。仅华为厂商支持sub_type取值为2、3、4、5、6。 > - 当card_id为CardVoucher时，sub_type用于设置按钮样式，1表示静态按钮，2表示动态按钮。目前仅华为厂商支持动态按钮。 > - 当card_id为ShortVideoImage时，sub_type用于设置是否显示播放图标，1表示不显示，2表示显示。 > - 当card_id为EcommerceCouponVertical和EcommerceCouponHorizontal时，sub_type用于设置卡券区是否隐藏。sub_type设置为1，卡券区（position_number为4~7）的visible设置为1，且卡券区（position_number为7）的button_type设置为static或dynamic时，显示卡券区；sub_type设置为2，卡券区（position_number为4~7）的visible设置为0，且卡券区（position_number为7）的button_type设置为空值或不带该字段时，卡券区被隐藏。

        :param sub_type: The sub_type of this CreateAimPersonalTemplateRequestBody.
        :type sub_type: int
        """
        self._sub_type = sub_type

    @property
    def sms_example(self):
        r"""Gets the sms_example of this CreateAimPersonalTemplateRequestBody.

        要发送的原始文本消息示例。

        :return: The sms_example of this CreateAimPersonalTemplateRequestBody.
        :rtype: str
        """
        return self._sms_example

    @sms_example.setter
    def sms_example(self, sms_example):
        r"""Sets the sms_example of this CreateAimPersonalTemplateRequestBody.

        要发送的原始文本消息示例。

        :param sms_example: The sms_example of this CreateAimPersonalTemplateRequestBody.
        :type sms_example: str
        """
        self._sms_example = sms_example

    @property
    def sms_signs(self):
        r"""Gets the sms_signs of this CreateAimPersonalTemplateRequestBody.

        短信签名。最多可以传三个签名，发送短信时，只要能匹配其中一个即可。填写的短信签名为企业绑定的签名，每个签名最多20个字，支持输入中文，英文，数字，符号，单个签名内容不包括中括号。  > 选择厂商包含VIVO时，此参数必填。 

        :return: The sms_signs of this CreateAimPersonalTemplateRequestBody.
        :rtype: list[str]
        """
        return self._sms_signs

    @sms_signs.setter
    def sms_signs(self, sms_signs):
        r"""Sets the sms_signs of this CreateAimPersonalTemplateRequestBody.

        短信签名。最多可以传三个签名，发送短信时，只要能匹配其中一个即可。填写的短信签名为企业绑定的签名，每个签名最多20个字，支持输入中文，英文，数字，符号，单个签名内容不包括中括号。  > 选择厂商包含VIVO时，此参数必填。 

        :param sms_signs: The sms_signs of this CreateAimPersonalTemplateRequestBody.
        :type sms_signs: list[str]
        """
        self._sms_signs = sms_signs

    @property
    def sms_template(self):
        r"""Gets the sms_template of this CreateAimPersonalTemplateRequestBody.

        短信原文模板。参数示例：尊敬的客户，截至[文本0-20]，您本月国内通用流量已使用[数字0-4]GB，使用到[数字0-4]GB ，整体上网速度将不高于[数字0-2]Mbps。您可点击[字母0-20]获取[文本0-20]。  > - 正则类型仅支持文本、字母、数字三种，且长度最大为99，且中括号为英文中括号。静态短信文案加正则动态文案最大值的总字数不超过370个字符 > - 选择厂商包含VIVO时，此参数必填 

        :return: The sms_template of this CreateAimPersonalTemplateRequestBody.
        :rtype: str
        """
        return self._sms_template

    @sms_template.setter
    def sms_template(self, sms_template):
        r"""Sets the sms_template of this CreateAimPersonalTemplateRequestBody.

        短信原文模板。参数示例：尊敬的客户，截至[文本0-20]，您本月国内通用流量已使用[数字0-4]GB，使用到[数字0-4]GB ，整体上网速度将不高于[数字0-2]Mbps。您可点击[字母0-20]获取[文本0-20]。  > - 正则类型仅支持文本、字母、数字三种，且长度最大为99，且中括号为英文中括号。静态短信文案加正则动态文案最大值的总字数不超过370个字符 > - 选择厂商包含VIVO时，此参数必填 

        :param sms_template: The sms_template of this CreateAimPersonalTemplateRequestBody.
        :type sms_template: str
        """
        self._sms_template = sms_template

    @property
    def pages(self):
        r"""Gets the pages of this CreateAimPersonalTemplateRequestBody.

        模板协议，最大支持10页协议。

        :return: The pages of this CreateAimPersonalTemplateRequestBody.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplatePage`]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        r"""Sets the pages of this CreateAimPersonalTemplateRequestBody.

        模板协议，最大支持10页协议。

        :param pages: The pages of this CreateAimPersonalTemplateRequestBody.
        :type pages: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplatePage`]
        """
        self._pages = pages

    @property
    def params(self):
        r"""Gets the params of this CreateAimPersonalTemplateRequestBody.

        模板参数集。

        :return: The params of this CreateAimPersonalTemplateRequestBody.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this CreateAimPersonalTemplateRequestBody.

        模板参数集。

        :param params: The params of this CreateAimPersonalTemplateRequestBody.
        :type params: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateParam`]
        """
        self._params = params

    @property
    def factorys(self):
        r"""Gets the factorys of this CreateAimPersonalTemplateRequestBody.

        需要提交的厂商列表。

        :return: The factorys of this CreateAimPersonalTemplateRequestBody.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateFactory`]
        """
        return self._factorys

    @factorys.setter
    def factorys(self, factorys):
        r"""Sets the factorys of this CreateAimPersonalTemplateRequestBody.

        需要提交的厂商列表。

        :param factorys: The factorys of this CreateAimPersonalTemplateRequestBody.
        :type factorys: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateFactory`]
        """
        self._factorys = factorys

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
        if not isinstance(other, CreateAimPersonalTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
