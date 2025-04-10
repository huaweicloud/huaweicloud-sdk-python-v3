# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AimPersonalTemplateContentAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target': 'str',
        'content': 'str',
        'package_name': 'str',
        'floor_url': 'str',
        'floor_type': 'int',
        'subject': 'str',
        'body': 'str',
        'description': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'address': 'str',
        'longitude': 'str',
        'latitude': 'str',
        'text_button': 'str',
        'mode': 'int'
    }

    attribute_map = {
        'target': 'target',
        'content': 'content',
        'package_name': 'package_name',
        'floor_url': 'floor_url',
        'floor_type': 'floor_type',
        'subject': 'subject',
        'body': 'body',
        'description': 'description',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'address': 'address',
        'longitude': 'longitude',
        'latitude': 'latitude',
        'text_button': 'text_button',
        'mode': 'mode'
    }

    def __init__(self, target=None, content=None, package_name=None, floor_url=None, floor_type=None, subject=None, body=None, description=None, begin_time=None, end_time=None, address=None, longitude=None, latitude=None, text_button=None, mode=None):
        r"""AimPersonalTemplateContentAction

        The model defined in huaweicloud sdk

        :param target: 此字段根据action_type对应不同的含义，具体对应如下。  - action_type&#x3D;OPEN_URL：表示H5访问地址。必须为HTTPS，支持含动态参数。字符长度为1-1000。示例：https://XXXXX/${param1} - action_type&#x3D;OPEN_QUICK：表示快应用deeplink地址。支持含动态参数，字符长度为1-1000。示例：hap://app/xxx/${param1} - action_type&#x3D;OPEN_APP：表示APP的deeplink地址。支持含动态参数，字符长度为1-1000。示例：weixin:// - action_type&#x3D;DIAL_PHONE：表示电话号码。不能超过20个字符。示例：18600000000 - action_type&#x3D;OPEN_SMS：表示电话号码。不能超过20个字符。示例：18600000000 - action_type&#x3D;OPEN_EMAIL：表示邮箱地址。不能超过100个字符。示例：1046520406@qq.com - action_type&#x3D;OPEN_SCHEDULE：表示日程标题。不能超过100个字符。示例：日常需求评审 - action_type&#x3D;OPEN_MAP：表示位置名。不能超过100个字符。示例：龙泰利科技大厦 - action_type&#x3D;OPEN_BROWSER：表示网址。支持HTTPS或HTTP，支持含动态参数，不能超过1000个字符。示例：https://XXXXX/${param1} - action_type&#x3D;OPEN_POPUP：表示弹窗标题。不能超过30个字符。参数示例：xxx商品 - action_type&#x3D;COPY_PARAMETER：表示复制的内容。支持含动态参数，不能超过20个字符。复制验证码示例：83721 - action_type&#x3D;VIEW_PIC：表示要打开的大图ID。配置在打开大图的资源地址与模板上的图片资源地址一致。如果模板资源类型是ID，则传ID，如果是资源地址，则使用资源地址。最大长度不能超过1000个字符。例如：当src_type为1时，传入ID：691996319597764608。当src_type为2时，使用资源地址：https://www.xxxx.cn/src/image/head.jpg 
        :type target: str
        :param content: 弹窗内容。  &gt; action_type&#x3D;OPEN_POPUP为必填。不能超过100个字符。示例：是否喜欢该商品。 
        :type content: str
        :param package_name: 包名。  &gt; action_type&#x3D;OPEN_APP为必填。不能超过50个字符。示例：com.xxxx.service.koomsg。 
        :type package_name: str
        :param floor_url: 兜底URL。支持快应用deeplink或H5的HTTPS网址，不能超过1000个字。  &gt; - action_type&#x3D;OPEN_APP为选填，其他类型不填 &gt; - 兜底类型为0时，可不填 &gt; - 当兜底类型为2并且提交厂商列表中包含OPPO厂商时为必填 
        :type floor_url: str
        :param floor_type: 兜底类型。如果传入的厂商不支持该兜底类型，接口会返回错误。如果不传入厂商，则不对兜底类型进行校。 - 0：打开应用市场 - 1：打开H5页面（通过收件箱内置浏览器打开） - 2：打开浏览器 - 3：打开快应用  &gt; action_type&#x3D;OPEN_APP为选填，其他类型不填；action_type&#x3D;OPEN_APP时此参数不填则默认打开应用市场。打开链接为http格式时必须选择打开浏览器；打开链接为https格式且内容只是一个普通页面时，可以使用打开H5页面，当链接中有下载指引或打开小程序由于部分内置浏览器功能不全可能导致打开异常，建议使用打开浏览器，请按需选择兜底类型。 &gt; - 华为：支持以上4种兜底 &gt; - 魅族：支持以上4种兜底 &gt; - 小米：不支持打开H5页面兜底 &gt; - OPPO：不支持打开快应用兜底 &gt; - VIVO：不支持打开快应用兜底 &gt; - 三星：不支持打开应用市场和打开浏览器。当创建的模板仅包含三星厂商时，兜底URL不支持打开浏览器和打开应用市场；当创建的模板包含三星和其它厂商时，以其它厂商的限制为准，三星的兜底链接将不生效 
        :type floor_type: int
        :param subject: 邮件标题。  &gt; action_type&#x3D;OPEN_EMAIL为必填。不能超过100个字符。示例：618活动促销。 
        :type subject: str
        :param body: 邮件正文/短信正文。  &gt; action_type&#x3D;OPEN_SMS或OPEN_EMAIL为必填。不能超过100个字符。 &gt; &gt; 短信正文示例1：今天回家吃饭吗； &gt; &gt; 邮件正文示例2：您有一张优惠券领取。 
        :type body: str
        :param description: 日程内容描述。  &gt; action_type&#x3D;OPEN_SCHEDULE为必填。不能超过100个字符。示例：评审这个月版本需求。 
        :type description: str
        :param begin_time: 日程开始时间。格式为：yyyy-MM-dd HH:mm:ss。  &gt; 当action_type&#x3D;OPEN_SCHEDULE时为必填。 
        :type begin_time: str
        :param end_time: 日程结束时间。格式为：yyyy-MM-dd HH:mm:ss。  &gt; 当action_type&#x3D;OPEN_SCHEDULE时为必填。 
        :type end_time: str
        :param address: 地址的详细说明。  &gt; action_type&#x3D;OPEN_MAP为必填。不能超过100个字符。示例：高新中四道龙泰利科技大厦。 
        :type address: str
        :param longitude: 地图经度。  &gt; action_type&#x3D;OPEN_MAP为必填。不能超过20个字符。示例：113.941618。 
        :type longitude: str
        :param latitude: 地图纬度。  &gt; action_type&#x3D;OPEN_MAP为必填。不能超过20个字符。示例：22.548804。 
        :type latitude: str
        :param text_button: 按钮展示文本。  &gt; action_type&#x3D;OPEN_POPUP为必填。不能超过12个字符。示例：确定。 
        :type text_button: str
        :param mode: 弹窗模态。  - 0：模态（默认） - 1：非模态（暂不支持）  &gt; action_type&#x3D;OPEN_POPUP为必填。 
        :type mode: int
        """
        
        

        self._target = None
        self._content = None
        self._package_name = None
        self._floor_url = None
        self._floor_type = None
        self._subject = None
        self._body = None
        self._description = None
        self._begin_time = None
        self._end_time = None
        self._address = None
        self._longitude = None
        self._latitude = None
        self._text_button = None
        self._mode = None
        self.discriminator = None

        self.target = target
        if content is not None:
            self.content = content
        if package_name is not None:
            self.package_name = package_name
        if floor_url is not None:
            self.floor_url = floor_url
        if floor_type is not None:
            self.floor_type = floor_type
        if subject is not None:
            self.subject = subject
        if body is not None:
            self.body = body
        if description is not None:
            self.description = description
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if address is not None:
            self.address = address
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude
        if text_button is not None:
            self.text_button = text_button
        if mode is not None:
            self.mode = mode

    @property
    def target(self):
        r"""Gets the target of this AimPersonalTemplateContentAction.

        此字段根据action_type对应不同的含义，具体对应如下。  - action_type=OPEN_URL：表示H5访问地址。必须为HTTPS，支持含动态参数。字符长度为1-1000。示例：https://XXXXX/${param1} - action_type=OPEN_QUICK：表示快应用deeplink地址。支持含动态参数，字符长度为1-1000。示例：hap://app/xxx/${param1} - action_type=OPEN_APP：表示APP的deeplink地址。支持含动态参数，字符长度为1-1000。示例：weixin:// - action_type=DIAL_PHONE：表示电话号码。不能超过20个字符。示例：18600000000 - action_type=OPEN_SMS：表示电话号码。不能超过20个字符。示例：18600000000 - action_type=OPEN_EMAIL：表示邮箱地址。不能超过100个字符。示例：1046520406@qq.com - action_type=OPEN_SCHEDULE：表示日程标题。不能超过100个字符。示例：日常需求评审 - action_type=OPEN_MAP：表示位置名。不能超过100个字符。示例：龙泰利科技大厦 - action_type=OPEN_BROWSER：表示网址。支持HTTPS或HTTP，支持含动态参数，不能超过1000个字符。示例：https://XXXXX/${param1} - action_type=OPEN_POPUP：表示弹窗标题。不能超过30个字符。参数示例：xxx商品 - action_type=COPY_PARAMETER：表示复制的内容。支持含动态参数，不能超过20个字符。复制验证码示例：83721 - action_type=VIEW_PIC：表示要打开的大图ID。配置在打开大图的资源地址与模板上的图片资源地址一致。如果模板资源类型是ID，则传ID，如果是资源地址，则使用资源地址。最大长度不能超过1000个字符。例如：当src_type为1时，传入ID：691996319597764608。当src_type为2时，使用资源地址：https://www.xxxx.cn/src/image/head.jpg 

        :return: The target of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this AimPersonalTemplateContentAction.

        此字段根据action_type对应不同的含义，具体对应如下。  - action_type=OPEN_URL：表示H5访问地址。必须为HTTPS，支持含动态参数。字符长度为1-1000。示例：https://XXXXX/${param1} - action_type=OPEN_QUICK：表示快应用deeplink地址。支持含动态参数，字符长度为1-1000。示例：hap://app/xxx/${param1} - action_type=OPEN_APP：表示APP的deeplink地址。支持含动态参数，字符长度为1-1000。示例：weixin:// - action_type=DIAL_PHONE：表示电话号码。不能超过20个字符。示例：18600000000 - action_type=OPEN_SMS：表示电话号码。不能超过20个字符。示例：18600000000 - action_type=OPEN_EMAIL：表示邮箱地址。不能超过100个字符。示例：1046520406@qq.com - action_type=OPEN_SCHEDULE：表示日程标题。不能超过100个字符。示例：日常需求评审 - action_type=OPEN_MAP：表示位置名。不能超过100个字符。示例：龙泰利科技大厦 - action_type=OPEN_BROWSER：表示网址。支持HTTPS或HTTP，支持含动态参数，不能超过1000个字符。示例：https://XXXXX/${param1} - action_type=OPEN_POPUP：表示弹窗标题。不能超过30个字符。参数示例：xxx商品 - action_type=COPY_PARAMETER：表示复制的内容。支持含动态参数，不能超过20个字符。复制验证码示例：83721 - action_type=VIEW_PIC：表示要打开的大图ID。配置在打开大图的资源地址与模板上的图片资源地址一致。如果模板资源类型是ID，则传ID，如果是资源地址，则使用资源地址。最大长度不能超过1000个字符。例如：当src_type为1时，传入ID：691996319597764608。当src_type为2时，使用资源地址：https://www.xxxx.cn/src/image/head.jpg 

        :param target: The target of this AimPersonalTemplateContentAction.
        :type target: str
        """
        self._target = target

    @property
    def content(self):
        r"""Gets the content of this AimPersonalTemplateContentAction.

        弹窗内容。  > action_type=OPEN_POPUP为必填。不能超过100个字符。示例：是否喜欢该商品。 

        :return: The content of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this AimPersonalTemplateContentAction.

        弹窗内容。  > action_type=OPEN_POPUP为必填。不能超过100个字符。示例：是否喜欢该商品。 

        :param content: The content of this AimPersonalTemplateContentAction.
        :type content: str
        """
        self._content = content

    @property
    def package_name(self):
        r"""Gets the package_name of this AimPersonalTemplateContentAction.

        包名。  > action_type=OPEN_APP为必填。不能超过50个字符。示例：com.xxxx.service.koomsg。 

        :return: The package_name of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this AimPersonalTemplateContentAction.

        包名。  > action_type=OPEN_APP为必填。不能超过50个字符。示例：com.xxxx.service.koomsg。 

        :param package_name: The package_name of this AimPersonalTemplateContentAction.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def floor_url(self):
        r"""Gets the floor_url of this AimPersonalTemplateContentAction.

        兜底URL。支持快应用deeplink或H5的HTTPS网址，不能超过1000个字。  > - action_type=OPEN_APP为选填，其他类型不填 > - 兜底类型为0时，可不填 > - 当兜底类型为2并且提交厂商列表中包含OPPO厂商时为必填 

        :return: The floor_url of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._floor_url

    @floor_url.setter
    def floor_url(self, floor_url):
        r"""Sets the floor_url of this AimPersonalTemplateContentAction.

        兜底URL。支持快应用deeplink或H5的HTTPS网址，不能超过1000个字。  > - action_type=OPEN_APP为选填，其他类型不填 > - 兜底类型为0时，可不填 > - 当兜底类型为2并且提交厂商列表中包含OPPO厂商时为必填 

        :param floor_url: The floor_url of this AimPersonalTemplateContentAction.
        :type floor_url: str
        """
        self._floor_url = floor_url

    @property
    def floor_type(self):
        r"""Gets the floor_type of this AimPersonalTemplateContentAction.

        兜底类型。如果传入的厂商不支持该兜底类型，接口会返回错误。如果不传入厂商，则不对兜底类型进行校。 - 0：打开应用市场 - 1：打开H5页面（通过收件箱内置浏览器打开） - 2：打开浏览器 - 3：打开快应用  > action_type=OPEN_APP为选填，其他类型不填；action_type=OPEN_APP时此参数不填则默认打开应用市场。打开链接为http格式时必须选择打开浏览器；打开链接为https格式且内容只是一个普通页面时，可以使用打开H5页面，当链接中有下载指引或打开小程序由于部分内置浏览器功能不全可能导致打开异常，建议使用打开浏览器，请按需选择兜底类型。 > - 华为：支持以上4种兜底 > - 魅族：支持以上4种兜底 > - 小米：不支持打开H5页面兜底 > - OPPO：不支持打开快应用兜底 > - VIVO：不支持打开快应用兜底 > - 三星：不支持打开应用市场和打开浏览器。当创建的模板仅包含三星厂商时，兜底URL不支持打开浏览器和打开应用市场；当创建的模板包含三星和其它厂商时，以其它厂商的限制为准，三星的兜底链接将不生效 

        :return: The floor_type of this AimPersonalTemplateContentAction.
        :rtype: int
        """
        return self._floor_type

    @floor_type.setter
    def floor_type(self, floor_type):
        r"""Sets the floor_type of this AimPersonalTemplateContentAction.

        兜底类型。如果传入的厂商不支持该兜底类型，接口会返回错误。如果不传入厂商，则不对兜底类型进行校。 - 0：打开应用市场 - 1：打开H5页面（通过收件箱内置浏览器打开） - 2：打开浏览器 - 3：打开快应用  > action_type=OPEN_APP为选填，其他类型不填；action_type=OPEN_APP时此参数不填则默认打开应用市场。打开链接为http格式时必须选择打开浏览器；打开链接为https格式且内容只是一个普通页面时，可以使用打开H5页面，当链接中有下载指引或打开小程序由于部分内置浏览器功能不全可能导致打开异常，建议使用打开浏览器，请按需选择兜底类型。 > - 华为：支持以上4种兜底 > - 魅族：支持以上4种兜底 > - 小米：不支持打开H5页面兜底 > - OPPO：不支持打开快应用兜底 > - VIVO：不支持打开快应用兜底 > - 三星：不支持打开应用市场和打开浏览器。当创建的模板仅包含三星厂商时，兜底URL不支持打开浏览器和打开应用市场；当创建的模板包含三星和其它厂商时，以其它厂商的限制为准，三星的兜底链接将不生效 

        :param floor_type: The floor_type of this AimPersonalTemplateContentAction.
        :type floor_type: int
        """
        self._floor_type = floor_type

    @property
    def subject(self):
        r"""Gets the subject of this AimPersonalTemplateContentAction.

        邮件标题。  > action_type=OPEN_EMAIL为必填。不能超过100个字符。示例：618活动促销。 

        :return: The subject of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this AimPersonalTemplateContentAction.

        邮件标题。  > action_type=OPEN_EMAIL为必填。不能超过100个字符。示例：618活动促销。 

        :param subject: The subject of this AimPersonalTemplateContentAction.
        :type subject: str
        """
        self._subject = subject

    @property
    def body(self):
        r"""Gets the body of this AimPersonalTemplateContentAction.

        邮件正文/短信正文。  > action_type=OPEN_SMS或OPEN_EMAIL为必填。不能超过100个字符。 > > 短信正文示例1：今天回家吃饭吗； > > 邮件正文示例2：您有一张优惠券领取。 

        :return: The body of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AimPersonalTemplateContentAction.

        邮件正文/短信正文。  > action_type=OPEN_SMS或OPEN_EMAIL为必填。不能超过100个字符。 > > 短信正文示例1：今天回家吃饭吗； > > 邮件正文示例2：您有一张优惠券领取。 

        :param body: The body of this AimPersonalTemplateContentAction.
        :type body: str
        """
        self._body = body

    @property
    def description(self):
        r"""Gets the description of this AimPersonalTemplateContentAction.

        日程内容描述。  > action_type=OPEN_SCHEDULE为必填。不能超过100个字符。示例：评审这个月版本需求。 

        :return: The description of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AimPersonalTemplateContentAction.

        日程内容描述。  > action_type=OPEN_SCHEDULE为必填。不能超过100个字符。示例：评审这个月版本需求。 

        :param description: The description of this AimPersonalTemplateContentAction.
        :type description: str
        """
        self._description = description

    @property
    def begin_time(self):
        r"""Gets the begin_time of this AimPersonalTemplateContentAction.

        日程开始时间。格式为：yyyy-MM-dd HH:mm:ss。  > 当action_type=OPEN_SCHEDULE时为必填。 

        :return: The begin_time of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this AimPersonalTemplateContentAction.

        日程开始时间。格式为：yyyy-MM-dd HH:mm:ss。  > 当action_type=OPEN_SCHEDULE时为必填。 

        :param begin_time: The begin_time of this AimPersonalTemplateContentAction.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this AimPersonalTemplateContentAction.

        日程结束时间。格式为：yyyy-MM-dd HH:mm:ss。  > 当action_type=OPEN_SCHEDULE时为必填。 

        :return: The end_time of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this AimPersonalTemplateContentAction.

        日程结束时间。格式为：yyyy-MM-dd HH:mm:ss。  > 当action_type=OPEN_SCHEDULE时为必填。 

        :param end_time: The end_time of this AimPersonalTemplateContentAction.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def address(self):
        r"""Gets the address of this AimPersonalTemplateContentAction.

        地址的详细说明。  > action_type=OPEN_MAP为必填。不能超过100个字符。示例：高新中四道龙泰利科技大厦。 

        :return: The address of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this AimPersonalTemplateContentAction.

        地址的详细说明。  > action_type=OPEN_MAP为必填。不能超过100个字符。示例：高新中四道龙泰利科技大厦。 

        :param address: The address of this AimPersonalTemplateContentAction.
        :type address: str
        """
        self._address = address

    @property
    def longitude(self):
        r"""Gets the longitude of this AimPersonalTemplateContentAction.

        地图经度。  > action_type=OPEN_MAP为必填。不能超过20个字符。示例：113.941618。 

        :return: The longitude of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        r"""Sets the longitude of this AimPersonalTemplateContentAction.

        地图经度。  > action_type=OPEN_MAP为必填。不能超过20个字符。示例：113.941618。 

        :param longitude: The longitude of this AimPersonalTemplateContentAction.
        :type longitude: str
        """
        self._longitude = longitude

    @property
    def latitude(self):
        r"""Gets the latitude of this AimPersonalTemplateContentAction.

        地图纬度。  > action_type=OPEN_MAP为必填。不能超过20个字符。示例：22.548804。 

        :return: The latitude of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        r"""Sets the latitude of this AimPersonalTemplateContentAction.

        地图纬度。  > action_type=OPEN_MAP为必填。不能超过20个字符。示例：22.548804。 

        :param latitude: The latitude of this AimPersonalTemplateContentAction.
        :type latitude: str
        """
        self._latitude = latitude

    @property
    def text_button(self):
        r"""Gets the text_button of this AimPersonalTemplateContentAction.

        按钮展示文本。  > action_type=OPEN_POPUP为必填。不能超过12个字符。示例：确定。 

        :return: The text_button of this AimPersonalTemplateContentAction.
        :rtype: str
        """
        return self._text_button

    @text_button.setter
    def text_button(self, text_button):
        r"""Sets the text_button of this AimPersonalTemplateContentAction.

        按钮展示文本。  > action_type=OPEN_POPUP为必填。不能超过12个字符。示例：确定。 

        :param text_button: The text_button of this AimPersonalTemplateContentAction.
        :type text_button: str
        """
        self._text_button = text_button

    @property
    def mode(self):
        r"""Gets the mode of this AimPersonalTemplateContentAction.

        弹窗模态。  - 0：模态（默认） - 1：非模态（暂不支持）  > action_type=OPEN_POPUP为必填。 

        :return: The mode of this AimPersonalTemplateContentAction.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this AimPersonalTemplateContentAction.

        弹窗模态。  - 0：模态（默认） - 1：非模态（暂不支持）  > action_type=OPEN_POPUP为必填。 

        :param mode: The mode of this AimPersonalTemplateContentAction.
        :type mode: int
        """
        self._mode = mode

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
        if not isinstance(other, AimPersonalTemplateContentAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
