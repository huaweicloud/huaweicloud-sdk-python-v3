# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResolveTaskParamMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cust_flag': 'str',
        'cust_id': 'str',
        'dync_params': 'dict(str, str)',
        'custom_url': 'str',
        'aim_url': 'str',
        'aim_code': 'str',
        'ext_data': 'str',
        'result_code': 'str',
        'error_message': 'str',
        'generate_date': 'str',
        'expire_date': 'str',
        'resolved_date': 'str',
        'resolved_times': 'int',
        'custom_short_code': 'str'
    }

    attribute_map = {
        'cust_flag': 'cust_flag',
        'cust_id': 'cust_id',
        'dync_params': 'dync_params',
        'custom_url': 'custom_url',
        'aim_url': 'aim_url',
        'aim_code': 'aim_code',
        'ext_data': 'ext_data',
        'result_code': 'result_code',
        'error_message': 'error_message',
        'generate_date': 'generate_date',
        'expire_date': 'expire_date',
        'resolved_date': 'resolved_date',
        'resolved_times': 'resolved_times',
        'custom_short_code': 'custom_short_code'
    }

    def __init__(self, cust_flag=None, cust_id=None, dync_params=None, custom_url=None, aim_url=None, aim_code=None, ext_data=None, result_code=None, error_message=None, generate_date=None, expire_date=None, resolved_date=None, resolved_times=None, custom_short_code=None):
        """CreateResolveTaskParamMode

        The model defined in huaweicloud sdk

        :param cust_flag: 创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。 发送智能信息时则必须填客户的手机号码。样例为：130****0001。
        :type cust_flag: str
        :param cust_id: 租户ID。
        :type cust_id: str
        :param dync_params: 动态参数。
        :type dync_params: dict(str, str)
        :param custom_url: 自定义跳转地址。 &gt; - 未填时，终端用户点击访问短信原文中的短链，跳转智能信息H5页 &gt; - 已填时，终端用户点击访问短信原文中的短链，跳转客户填写的链接落地页，填写时必须为http或https作为前缀 
        :type custom_url: str
        :param aim_url: 完整的短链连接地址，通过自己的短信渠道发送时，需要把该短链添加到短信模板中，并确保发送短信时的签名与创建短链时的签名保持一致。样例：km2g.cn/PDiWqc。
        :type aim_url: str
        :param aim_code: 智能信息编码，样例：PDiWqc。
        :type aim_code: str
        :param ext_data: 自定义扩展参数。  &gt;预留字段。 
        :type ext_data: str
        :param result_code: 短链申请结果返回码。 - 0：成功 - 非0：失败，具体请参见错误码 
        :type result_code: str
        :param error_message: 短链申请结果错误描述。 
        :type error_message: str
        :param generate_date: 短链生成时间。样例为：2019-10-12T07:20:50Z。
        :type generate_date: str
        :param expire_date: 短链到期时间。样例为：2019-10-12T07:20:50Z。
        :type expire_date: str
        :param resolved_date: 解析时间。样例为：2019-10-12T07:20:50Z。  &gt;预留字段。 
        :type resolved_date: str
        :param resolved_times: 短链实际解析次数。  &gt;预留字段。 
        :type resolved_times: int
        :param custom_short_code: 自定义短码，支持长度为3到10位的数字或大小写字母。样例为：aDC123。
        :type custom_short_code: str
        """
        
        

        self._cust_flag = None
        self._cust_id = None
        self._dync_params = None
        self._custom_url = None
        self._aim_url = None
        self._aim_code = None
        self._ext_data = None
        self._result_code = None
        self._error_message = None
        self._generate_date = None
        self._expire_date = None
        self._resolved_date = None
        self._resolved_times = None
        self._custom_short_code = None
        self.discriminator = None

        if cust_flag is not None:
            self.cust_flag = cust_flag
        if cust_id is not None:
            self.cust_id = cust_id
        if dync_params is not None:
            self.dync_params = dync_params
        if custom_url is not None:
            self.custom_url = custom_url
        if aim_url is not None:
            self.aim_url = aim_url
        if aim_code is not None:
            self.aim_code = aim_code
        if ext_data is not None:
            self.ext_data = ext_data
        if result_code is not None:
            self.result_code = result_code
        if error_message is not None:
            self.error_message = error_message
        if generate_date is not None:
            self.generate_date = generate_date
        if expire_date is not None:
            self.expire_date = expire_date
        if resolved_date is not None:
            self.resolved_date = resolved_date
        if resolved_times is not None:
            self.resolved_times = resolved_times
        if custom_short_code is not None:
            self.custom_short_code = custom_short_code

    @property
    def cust_flag(self):
        """Gets the cust_flag of this CreateResolveTaskParamMode.

        创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。 发送智能信息时则必须填客户的手机号码。样例为：130****0001。

        :return: The cust_flag of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._cust_flag

    @cust_flag.setter
    def cust_flag(self, cust_flag):
        """Sets the cust_flag of this CreateResolveTaskParamMode.

        创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。 发送智能信息时则必须填客户的手机号码。样例为：130****0001。

        :param cust_flag: The cust_flag of this CreateResolveTaskParamMode.
        :type cust_flag: str
        """
        self._cust_flag = cust_flag

    @property
    def cust_id(self):
        """Gets the cust_id of this CreateResolveTaskParamMode.

        租户ID。

        :return: The cust_id of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._cust_id

    @cust_id.setter
    def cust_id(self, cust_id):
        """Sets the cust_id of this CreateResolveTaskParamMode.

        租户ID。

        :param cust_id: The cust_id of this CreateResolveTaskParamMode.
        :type cust_id: str
        """
        self._cust_id = cust_id

    @property
    def dync_params(self):
        """Gets the dync_params of this CreateResolveTaskParamMode.

        动态参数。

        :return: The dync_params of this CreateResolveTaskParamMode.
        :rtype: dict(str, str)
        """
        return self._dync_params

    @dync_params.setter
    def dync_params(self, dync_params):
        """Sets the dync_params of this CreateResolveTaskParamMode.

        动态参数。

        :param dync_params: The dync_params of this CreateResolveTaskParamMode.
        :type dync_params: dict(str, str)
        """
        self._dync_params = dync_params

    @property
    def custom_url(self):
        """Gets the custom_url of this CreateResolveTaskParamMode.

        自定义跳转地址。 > - 未填时，终端用户点击访问短信原文中的短链，跳转智能信息H5页 > - 已填时，终端用户点击访问短信原文中的短链，跳转客户填写的链接落地页，填写时必须为http或https作为前缀 

        :return: The custom_url of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._custom_url

    @custom_url.setter
    def custom_url(self, custom_url):
        """Sets the custom_url of this CreateResolveTaskParamMode.

        自定义跳转地址。 > - 未填时，终端用户点击访问短信原文中的短链，跳转智能信息H5页 > - 已填时，终端用户点击访问短信原文中的短链，跳转客户填写的链接落地页，填写时必须为http或https作为前缀 

        :param custom_url: The custom_url of this CreateResolveTaskParamMode.
        :type custom_url: str
        """
        self._custom_url = custom_url

    @property
    def aim_url(self):
        """Gets the aim_url of this CreateResolveTaskParamMode.

        完整的短链连接地址，通过自己的短信渠道发送时，需要把该短链添加到短信模板中，并确保发送短信时的签名与创建短链时的签名保持一致。样例：km2g.cn/PDiWqc。

        :return: The aim_url of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._aim_url

    @aim_url.setter
    def aim_url(self, aim_url):
        """Sets the aim_url of this CreateResolveTaskParamMode.

        完整的短链连接地址，通过自己的短信渠道发送时，需要把该短链添加到短信模板中，并确保发送短信时的签名与创建短链时的签名保持一致。样例：km2g.cn/PDiWqc。

        :param aim_url: The aim_url of this CreateResolveTaskParamMode.
        :type aim_url: str
        """
        self._aim_url = aim_url

    @property
    def aim_code(self):
        """Gets the aim_code of this CreateResolveTaskParamMode.

        智能信息编码，样例：PDiWqc。

        :return: The aim_code of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._aim_code

    @aim_code.setter
    def aim_code(self, aim_code):
        """Sets the aim_code of this CreateResolveTaskParamMode.

        智能信息编码，样例：PDiWqc。

        :param aim_code: The aim_code of this CreateResolveTaskParamMode.
        :type aim_code: str
        """
        self._aim_code = aim_code

    @property
    def ext_data(self):
        """Gets the ext_data of this CreateResolveTaskParamMode.

        自定义扩展参数。  >预留字段。 

        :return: The ext_data of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._ext_data

    @ext_data.setter
    def ext_data(self, ext_data):
        """Sets the ext_data of this CreateResolveTaskParamMode.

        自定义扩展参数。  >预留字段。 

        :param ext_data: The ext_data of this CreateResolveTaskParamMode.
        :type ext_data: str
        """
        self._ext_data = ext_data

    @property
    def result_code(self):
        """Gets the result_code of this CreateResolveTaskParamMode.

        短链申请结果返回码。 - 0：成功 - 非0：失败，具体请参见错误码 

        :return: The result_code of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this CreateResolveTaskParamMode.

        短链申请结果返回码。 - 0：成功 - 非0：失败，具体请参见错误码 

        :param result_code: The result_code of this CreateResolveTaskParamMode.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def error_message(self):
        """Gets the error_message of this CreateResolveTaskParamMode.

        短链申请结果错误描述。 

        :return: The error_message of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this CreateResolveTaskParamMode.

        短链申请结果错误描述。 

        :param error_message: The error_message of this CreateResolveTaskParamMode.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def generate_date(self):
        """Gets the generate_date of this CreateResolveTaskParamMode.

        短链生成时间。样例为：2019-10-12T07:20:50Z。

        :return: The generate_date of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._generate_date

    @generate_date.setter
    def generate_date(self, generate_date):
        """Sets the generate_date of this CreateResolveTaskParamMode.

        短链生成时间。样例为：2019-10-12T07:20:50Z。

        :param generate_date: The generate_date of this CreateResolveTaskParamMode.
        :type generate_date: str
        """
        self._generate_date = generate_date

    @property
    def expire_date(self):
        """Gets the expire_date of this CreateResolveTaskParamMode.

        短链到期时间。样例为：2019-10-12T07:20:50Z。

        :return: The expire_date of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this CreateResolveTaskParamMode.

        短链到期时间。样例为：2019-10-12T07:20:50Z。

        :param expire_date: The expire_date of this CreateResolveTaskParamMode.
        :type expire_date: str
        """
        self._expire_date = expire_date

    @property
    def resolved_date(self):
        """Gets the resolved_date of this CreateResolveTaskParamMode.

        解析时间。样例为：2019-10-12T07:20:50Z。  >预留字段。 

        :return: The resolved_date of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._resolved_date

    @resolved_date.setter
    def resolved_date(self, resolved_date):
        """Sets the resolved_date of this CreateResolveTaskParamMode.

        解析时间。样例为：2019-10-12T07:20:50Z。  >预留字段。 

        :param resolved_date: The resolved_date of this CreateResolveTaskParamMode.
        :type resolved_date: str
        """
        self._resolved_date = resolved_date

    @property
    def resolved_times(self):
        """Gets the resolved_times of this CreateResolveTaskParamMode.

        短链实际解析次数。  >预留字段。 

        :return: The resolved_times of this CreateResolveTaskParamMode.
        :rtype: int
        """
        return self._resolved_times

    @resolved_times.setter
    def resolved_times(self, resolved_times):
        """Sets the resolved_times of this CreateResolveTaskParamMode.

        短链实际解析次数。  >预留字段。 

        :param resolved_times: The resolved_times of this CreateResolveTaskParamMode.
        :type resolved_times: int
        """
        self._resolved_times = resolved_times

    @property
    def custom_short_code(self):
        """Gets the custom_short_code of this CreateResolveTaskParamMode.

        自定义短码，支持长度为3到10位的数字或大小写字母。样例为：aDC123。

        :return: The custom_short_code of this CreateResolveTaskParamMode.
        :rtype: str
        """
        return self._custom_short_code

    @custom_short_code.setter
    def custom_short_code(self, custom_short_code):
        """Sets the custom_short_code of this CreateResolveTaskParamMode.

        自定义短码，支持长度为3到10位的数字或大小写字母。样例为：aDC123。

        :param custom_short_code: The custom_short_code of this CreateResolveTaskParamMode.
        :type custom_short_code: str
        """
        self._custom_short_code = custom_short_code

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
        if not isinstance(other, CreateResolveTaskParamMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
