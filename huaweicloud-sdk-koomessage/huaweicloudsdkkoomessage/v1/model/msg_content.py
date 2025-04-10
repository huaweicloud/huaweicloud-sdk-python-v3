# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MsgContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'to': 'list[str]',
        'template_id': 'str',
        'template_params': 'list[str]'
    }

    attribute_map = {
        'to': 'to',
        'template_id': 'template_id',
        'template_params': 'template_params'
    }

    def __init__(self, to=None, template_id=None, template_params=None):
        r"""MsgContent

        The model defined in huaweicloud sdk

        :param to: 群发短信接收方的号码。  标准号码格式：+{国家码}{地区码}{终端号码}。  发送国内短信：接收号码为国内手机号码时，所填号码可以不带+86，系统默认添加86。每个号码最大长度为21位，最多允许携带500个号码。 
        :type to: list[str]
        :param template_id: 短信模板ID。
        :type template_id: str
        :param template_params: 短信模板参数，字符串数组，最多20个。  短信模板中的变量类型可以是：短链、电话号码、其他号码（验证码、订单号、密码等）、日期时间、金额、其他（名称、账号、地址等）。   数组中参数按短信模板中的变量顺序进行匹配，比如短信模板内容中按顺序有3个变量：${1}、${2}、${3}，其中${1}表示手机号码，${2}表示短链，${3}表示日期，则sms_params传的是：[手机号码, 短链, 日期]。  - 电话号码：长度限制1-15个字符，可以传入手机号、座机号、95或400、800电话等。 - 其他号码：长度限制1-20个字符，不允许出现手机号、QQ号、微信号、URL等联系方式，仅支持大小写字母和数字组合。 - 时间：长度限制1-20个字符，日期格式：yyyyMMdd、yyyy-MM-dd、yyyy/MM/dd、yyyy年mm月dd日，时间格式：HH:mm:ss、HH:mm、HH点mm分、HH点mm。如果需要同时指定日期和时间，请在模板中填充两个变量，一个变量传入日期，另一个变量传入时间。 - 金额：长度限制1-20个字符，仅支持传入能够正常表达金额的数字、小数点或中文，例如壹、贰、叁、肆等，支持传入IP地址，例如：10.1.1.10。￥$等货币符号需要放在模板中，不支持变量传入。 - 其他：长度限制1-20个字符，可以设置为公司/产品/地址/姓名/内容/账号/会员名等。不允许出现QQ号/微信号（公众号）/手机号/网址/座机号等联系方式。如果确有需要，请将联系方式放入模板中，不允许在传入值中携带“.”（短链参数除外）、“。”、“&#39;”、“&lt;”、“&gt;”、“{”或“}”。否则，可能导致模板变量解析异常。不允许在传入值中携带“.”，即不支持传入IP地址，如变量取值为IP地址，请申请模板时选择变量属性为“金额”。
        :type template_params: list[str]
        """
        
        

        self._to = None
        self._template_id = None
        self._template_params = None
        self.discriminator = None

        self.to = to
        self.template_id = template_id
        if template_params is not None:
            self.template_params = template_params

    @property
    def to(self):
        r"""Gets the to of this MsgContent.

        群发短信接收方的号码。  标准号码格式：+{国家码}{地区码}{终端号码}。  发送国内短信：接收号码为国内手机号码时，所填号码可以不带+86，系统默认添加86。每个号码最大长度为21位，最多允许携带500个号码。 

        :return: The to of this MsgContent.
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this MsgContent.

        群发短信接收方的号码。  标准号码格式：+{国家码}{地区码}{终端号码}。  发送国内短信：接收号码为国内手机号码时，所填号码可以不带+86，系统默认添加86。每个号码最大长度为21位，最多允许携带500个号码。 

        :param to: The to of this MsgContent.
        :type to: list[str]
        """
        self._to = to

    @property
    def template_id(self):
        r"""Gets the template_id of this MsgContent.

        短信模板ID。

        :return: The template_id of this MsgContent.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this MsgContent.

        短信模板ID。

        :param template_id: The template_id of this MsgContent.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_params(self):
        r"""Gets the template_params of this MsgContent.

        短信模板参数，字符串数组，最多20个。  短信模板中的变量类型可以是：短链、电话号码、其他号码（验证码、订单号、密码等）、日期时间、金额、其他（名称、账号、地址等）。   数组中参数按短信模板中的变量顺序进行匹配，比如短信模板内容中按顺序有3个变量：${1}、${2}、${3}，其中${1}表示手机号码，${2}表示短链，${3}表示日期，则sms_params传的是：[手机号码, 短链, 日期]。  - 电话号码：长度限制1-15个字符，可以传入手机号、座机号、95或400、800电话等。 - 其他号码：长度限制1-20个字符，不允许出现手机号、QQ号、微信号、URL等联系方式，仅支持大小写字母和数字组合。 - 时间：长度限制1-20个字符，日期格式：yyyyMMdd、yyyy-MM-dd、yyyy/MM/dd、yyyy年mm月dd日，时间格式：HH:mm:ss、HH:mm、HH点mm分、HH点mm。如果需要同时指定日期和时间，请在模板中填充两个变量，一个变量传入日期，另一个变量传入时间。 - 金额：长度限制1-20个字符，仅支持传入能够正常表达金额的数字、小数点或中文，例如壹、贰、叁、肆等，支持传入IP地址，例如：10.1.1.10。￥$等货币符号需要放在模板中，不支持变量传入。 - 其他：长度限制1-20个字符，可以设置为公司/产品/地址/姓名/内容/账号/会员名等。不允许出现QQ号/微信号（公众号）/手机号/网址/座机号等联系方式。如果确有需要，请将联系方式放入模板中，不允许在传入值中携带“.”（短链参数除外）、“。”、“'”、“<”、“>”、“{”或“}”。否则，可能导致模板变量解析异常。不允许在传入值中携带“.”，即不支持传入IP地址，如变量取值为IP地址，请申请模板时选择变量属性为“金额”。

        :return: The template_params of this MsgContent.
        :rtype: list[str]
        """
        return self._template_params

    @template_params.setter
    def template_params(self, template_params):
        r"""Sets the template_params of this MsgContent.

        短信模板参数，字符串数组，最多20个。  短信模板中的变量类型可以是：短链、电话号码、其他号码（验证码、订单号、密码等）、日期时间、金额、其他（名称、账号、地址等）。   数组中参数按短信模板中的变量顺序进行匹配，比如短信模板内容中按顺序有3个变量：${1}、${2}、${3}，其中${1}表示手机号码，${2}表示短链，${3}表示日期，则sms_params传的是：[手机号码, 短链, 日期]。  - 电话号码：长度限制1-15个字符，可以传入手机号、座机号、95或400、800电话等。 - 其他号码：长度限制1-20个字符，不允许出现手机号、QQ号、微信号、URL等联系方式，仅支持大小写字母和数字组合。 - 时间：长度限制1-20个字符，日期格式：yyyyMMdd、yyyy-MM-dd、yyyy/MM/dd、yyyy年mm月dd日，时间格式：HH:mm:ss、HH:mm、HH点mm分、HH点mm。如果需要同时指定日期和时间，请在模板中填充两个变量，一个变量传入日期，另一个变量传入时间。 - 金额：长度限制1-20个字符，仅支持传入能够正常表达金额的数字、小数点或中文，例如壹、贰、叁、肆等，支持传入IP地址，例如：10.1.1.10。￥$等货币符号需要放在模板中，不支持变量传入。 - 其他：长度限制1-20个字符，可以设置为公司/产品/地址/姓名/内容/账号/会员名等。不允许出现QQ号/微信号（公众号）/手机号/网址/座机号等联系方式。如果确有需要，请将联系方式放入模板中，不允许在传入值中携带“.”（短链参数除外）、“。”、“'”、“<”、“>”、“{”或“}”。否则，可能导致模板变量解析异常。不允许在传入值中携带“.”，即不支持传入IP地址，如变量取值为IP地址，请申请模板时选择变量属性为“金额”。

        :param template_params: The template_params of this MsgContent.
        :type template_params: list[str]
        """
        self._template_params = template_params

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
        if not isinstance(other, MsgContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
