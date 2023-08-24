# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_num': 'str',
        'template_id': 'str',
        'signature': 'str',
        'task_name': 'str',
        'to': 'list[str]',
        'template_params': 'list[str]',
        'extend': 'str'
    }

    attribute_map = {
        'channel_num': 'channel_num',
        'template_id': 'template_id',
        'signature': 'signature',
        'task_name': 'task_name',
        'to': 'to',
        'template_params': 'template_params',
        'extend': 'extend'
    }

    def __init__(self, channel_num=None, template_id=None, signature=None, task_name=None, to=None, template_params=None, extend=None):
        """SmsTaskReq

        The model defined in huaweicloud sdk

        :param channel_num: 短信通道号。  &gt; 模板所属签名的通道号，可以从“云消息服务KooMessage-管理控制台-短消息配置（国内）-短消息签名管理-通道号”中获取。未填写时默认取模板所属签名通道号。
        :type channel_num: str
        :param template_id: 短信模板ID。  &gt; 可以从“云消息服务KooMessage-管理控制台-短消息配置（国内）-短消息模板管理-模板ID”中获取。
        :type template_id: str
        :param signature: 短信签名名称(暂不支持)。  &gt; 签名名称，必须是已审核通过的，与模板类型一致的签名名称。 仅在template_id指定的模板类型为通用模板时生效且必填，用于指定在通用模板短信内容前面补充的签名。
        :type signature: str
        :param task_name: 发送任务名称。  &gt; 不能为空白字符串，允许重复，为空时默认为Task_拼接当前时间值。
        :type task_name: str
        :param to: 短信接收方的号码。  所填号码可以不带+86，系统默认添加+86，最多允许携带500个号码。  示例：131****5678，+86155****6666。
        :type to: list[str]
        :param template_params: 短信模板参数，字符串数组，最多20个。  短信模板中的变量类型可以是：短链、电话号码、其他号码（验证码、订单号、密码等）、日期时间、金额、其他（名称、帐号、地址等）。   数组中参数按短信模板中的变量顺序进行匹配，比如短信模板内容中按顺序有3个变量：${1}、${2}、${3}，其中${1}表示手机号码，${2}表示短链，${3}表示日期，则sms_params传的是：[手机号码, 短链, 日期]。  - 电话号码：长度限制1-15个字符，可以传入手机号、座机号、95或400、800电话等。 - 其他号码：长度限制1-20个字符，不允许出现手机号、QQ号、微信号、URL等联系方式，仅支持大小写字母和数字组合。 - 时间：长度限制1-20个字符，日期格式：yyyyMMdd、yyyy-MM-dd、yyyy/MM/dd、yyyy年mm月dd日，时间格式：HH:mm:ss、HH:mm、HH点mm分、HH点mm。如果需要同时指定日期和时间，请在模板中填充两个变量，一个变量传入日期，另一个变量传入时间。 - 金额：长度限制1-20个字符，仅支持传入能够正常表达金额的数字、小数点或中文，例如壹、贰、叁、肆等，支持传入IP地址，例如：10.1.1.10。￥$等货币符号需要放在模板中，不支持变量传入。 - 其他：长度限制1-20个字符，可以设置为公司/产品/地址/姓名/内容/帐号/会员名等。不允许出现QQ号/微信号（公众号）/手机号/网址/座机号等联系方式。如果确有需要，请将联系方式放入模板中，不允许在传入值中携带“.”（短链参数除外）、“。”、“&#39;”、“&lt;”、“&gt;”、“{”或“}”。否则，可能导致模板变量解析异常。不允许在传入值中携带“.”，即不支持传入IP地址，如变量取值为IP地址，请申请模板时选择变量属性为“金额”。
        :type template_params: list[str]
        :param extend: 扩展参数。  在状态报告中会原样返回。  不允许赋空值，不允许携带以下字符：“{”，“}”（即大括号）。
        :type extend: str
        """
        
        

        self._channel_num = None
        self._template_id = None
        self._signature = None
        self._task_name = None
        self._to = None
        self._template_params = None
        self._extend = None
        self.discriminator = None

        if channel_num is not None:
            self.channel_num = channel_num
        self.template_id = template_id
        if signature is not None:
            self.signature = signature
        if task_name is not None:
            self.task_name = task_name
        self.to = to
        self.template_params = template_params
        if extend is not None:
            self.extend = extend

    @property
    def channel_num(self):
        """Gets the channel_num of this SmsTaskReq.

        短信通道号。  > 模板所属签名的通道号，可以从“云消息服务KooMessage-管理控制台-短消息配置（国内）-短消息签名管理-通道号”中获取。未填写时默认取模板所属签名通道号。

        :return: The channel_num of this SmsTaskReq.
        :rtype: str
        """
        return self._channel_num

    @channel_num.setter
    def channel_num(self, channel_num):
        """Sets the channel_num of this SmsTaskReq.

        短信通道号。  > 模板所属签名的通道号，可以从“云消息服务KooMessage-管理控制台-短消息配置（国内）-短消息签名管理-通道号”中获取。未填写时默认取模板所属签名通道号。

        :param channel_num: The channel_num of this SmsTaskReq.
        :type channel_num: str
        """
        self._channel_num = channel_num

    @property
    def template_id(self):
        """Gets the template_id of this SmsTaskReq.

        短信模板ID。  > 可以从“云消息服务KooMessage-管理控制台-短消息配置（国内）-短消息模板管理-模板ID”中获取。

        :return: The template_id of this SmsTaskReq.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this SmsTaskReq.

        短信模板ID。  > 可以从“云消息服务KooMessage-管理控制台-短消息配置（国内）-短消息模板管理-模板ID”中获取。

        :param template_id: The template_id of this SmsTaskReq.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def signature(self):
        """Gets the signature of this SmsTaskReq.

        短信签名名称(暂不支持)。  > 签名名称，必须是已审核通过的，与模板类型一致的签名名称。 仅在template_id指定的模板类型为通用模板时生效且必填，用于指定在通用模板短信内容前面补充的签名。

        :return: The signature of this SmsTaskReq.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this SmsTaskReq.

        短信签名名称(暂不支持)。  > 签名名称，必须是已审核通过的，与模板类型一致的签名名称。 仅在template_id指定的模板类型为通用模板时生效且必填，用于指定在通用模板短信内容前面补充的签名。

        :param signature: The signature of this SmsTaskReq.
        :type signature: str
        """
        self._signature = signature

    @property
    def task_name(self):
        """Gets the task_name of this SmsTaskReq.

        发送任务名称。  > 不能为空白字符串，允许重复，为空时默认为Task_拼接当前时间值。

        :return: The task_name of this SmsTaskReq.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this SmsTaskReq.

        发送任务名称。  > 不能为空白字符串，允许重复，为空时默认为Task_拼接当前时间值。

        :param task_name: The task_name of this SmsTaskReq.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def to(self):
        """Gets the to of this SmsTaskReq.

        短信接收方的号码。  所填号码可以不带+86，系统默认添加+86，最多允许携带500个号码。  示例：131****5678，+86155****6666。

        :return: The to of this SmsTaskReq.
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SmsTaskReq.

        短信接收方的号码。  所填号码可以不带+86，系统默认添加+86，最多允许携带500个号码。  示例：131****5678，+86155****6666。

        :param to: The to of this SmsTaskReq.
        :type to: list[str]
        """
        self._to = to

    @property
    def template_params(self):
        """Gets the template_params of this SmsTaskReq.

        短信模板参数，字符串数组，最多20个。  短信模板中的变量类型可以是：短链、电话号码、其他号码（验证码、订单号、密码等）、日期时间、金额、其他（名称、帐号、地址等）。   数组中参数按短信模板中的变量顺序进行匹配，比如短信模板内容中按顺序有3个变量：${1}、${2}、${3}，其中${1}表示手机号码，${2}表示短链，${3}表示日期，则sms_params传的是：[手机号码, 短链, 日期]。  - 电话号码：长度限制1-15个字符，可以传入手机号、座机号、95或400、800电话等。 - 其他号码：长度限制1-20个字符，不允许出现手机号、QQ号、微信号、URL等联系方式，仅支持大小写字母和数字组合。 - 时间：长度限制1-20个字符，日期格式：yyyyMMdd、yyyy-MM-dd、yyyy/MM/dd、yyyy年mm月dd日，时间格式：HH:mm:ss、HH:mm、HH点mm分、HH点mm。如果需要同时指定日期和时间，请在模板中填充两个变量，一个变量传入日期，另一个变量传入时间。 - 金额：长度限制1-20个字符，仅支持传入能够正常表达金额的数字、小数点或中文，例如壹、贰、叁、肆等，支持传入IP地址，例如：10.1.1.10。￥$等货币符号需要放在模板中，不支持变量传入。 - 其他：长度限制1-20个字符，可以设置为公司/产品/地址/姓名/内容/帐号/会员名等。不允许出现QQ号/微信号（公众号）/手机号/网址/座机号等联系方式。如果确有需要，请将联系方式放入模板中，不允许在传入值中携带“.”（短链参数除外）、“。”、“'”、“<”、“>”、“{”或“}”。否则，可能导致模板变量解析异常。不允许在传入值中携带“.”，即不支持传入IP地址，如变量取值为IP地址，请申请模板时选择变量属性为“金额”。

        :return: The template_params of this SmsTaskReq.
        :rtype: list[str]
        """
        return self._template_params

    @template_params.setter
    def template_params(self, template_params):
        """Sets the template_params of this SmsTaskReq.

        短信模板参数，字符串数组，最多20个。  短信模板中的变量类型可以是：短链、电话号码、其他号码（验证码、订单号、密码等）、日期时间、金额、其他（名称、帐号、地址等）。   数组中参数按短信模板中的变量顺序进行匹配，比如短信模板内容中按顺序有3个变量：${1}、${2}、${3}，其中${1}表示手机号码，${2}表示短链，${3}表示日期，则sms_params传的是：[手机号码, 短链, 日期]。  - 电话号码：长度限制1-15个字符，可以传入手机号、座机号、95或400、800电话等。 - 其他号码：长度限制1-20个字符，不允许出现手机号、QQ号、微信号、URL等联系方式，仅支持大小写字母和数字组合。 - 时间：长度限制1-20个字符，日期格式：yyyyMMdd、yyyy-MM-dd、yyyy/MM/dd、yyyy年mm月dd日，时间格式：HH:mm:ss、HH:mm、HH点mm分、HH点mm。如果需要同时指定日期和时间，请在模板中填充两个变量，一个变量传入日期，另一个变量传入时间。 - 金额：长度限制1-20个字符，仅支持传入能够正常表达金额的数字、小数点或中文，例如壹、贰、叁、肆等，支持传入IP地址，例如：10.1.1.10。￥$等货币符号需要放在模板中，不支持变量传入。 - 其他：长度限制1-20个字符，可以设置为公司/产品/地址/姓名/内容/帐号/会员名等。不允许出现QQ号/微信号（公众号）/手机号/网址/座机号等联系方式。如果确有需要，请将联系方式放入模板中，不允许在传入值中携带“.”（短链参数除外）、“。”、“'”、“<”、“>”、“{”或“}”。否则，可能导致模板变量解析异常。不允许在传入值中携带“.”，即不支持传入IP地址，如变量取值为IP地址，请申请模板时选择变量属性为“金额”。

        :param template_params: The template_params of this SmsTaskReq.
        :type template_params: list[str]
        """
        self._template_params = template_params

    @property
    def extend(self):
        """Gets the extend of this SmsTaskReq.

        扩展参数。  在状态报告中会原样返回。  不允许赋空值，不允许携带以下字符：“{”，“}”（即大括号）。

        :return: The extend of this SmsTaskReq.
        :rtype: str
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this SmsTaskReq.

        扩展参数。  在状态报告中会原样返回。  不允许赋空值，不允许携带以下字符：“{”，“}”（即大括号）。

        :param extend: The extend of this SmsTaskReq.
        :type extend: str
        """
        self._extend = extend

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
        if not isinstance(other, SmsTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
