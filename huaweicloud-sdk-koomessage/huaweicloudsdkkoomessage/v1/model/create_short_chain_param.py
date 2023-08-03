# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateShortChainParam:

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
        'dync_params': 'dict(str, str)',
        'custom_url': 'str',
        'custom_short_code': 'str'
    }

    attribute_map = {
        'cust_flag': 'cust_flag',
        'dync_params': 'dync_params',
        'custom_url': 'custom_url',
        'custom_short_code': 'custom_short_code'
    }

    def __init__(self, cust_flag=None, dync_params=None, custom_url=None, custom_short_code=None):
        """CreateShortChainParam

        The model defined in huaweicloud sdk

        :param cust_flag: 创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。 发送智能信息时则必须填客户的手机号码。样例为：130****0001。
        :type cust_flag: str
        :param dync_params: 动态参数。  &gt; 使用动态参数模板时，aim_code_type字段只能为individual。 
        :type dync_params: dict(str, str)
        :param custom_url: 自定义跳转地址。长度要求不超过2048。 &gt; - 未填时，终端用户点击短信原文中的短链后，跳转智能信息模板H5页 &gt; - 已填时，终端用户点击短信原文中的短链后，跳转该字段对应的页面，填写时必须为http或https作为前缀 &gt; - 使用自定义跳转链接功能请联系KooMessage运营人员进行域名备案 &gt; - 自定义短码时即generation_type为2时不支持自定义跳转链接功能，传入的参数值无效 
        :type custom_url: str
        :param custom_short_code: 自定义短码，支持长度为3到10位的数字或大小写字母。样例为：aDC123。 &gt; 自定义短码时即generation_type为2时，此参数为必填。
        :type custom_short_code: str
        """
        
        

        self._cust_flag = None
        self._dync_params = None
        self._custom_url = None
        self._custom_short_code = None
        self.discriminator = None

        self.cust_flag = cust_flag
        if dync_params is not None:
            self.dync_params = dync_params
        if custom_url is not None:
            self.custom_url = custom_url
        if custom_short_code is not None:
            self.custom_short_code = custom_short_code

    @property
    def cust_flag(self):
        """Gets the cust_flag of this CreateShortChainParam.

        创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。 发送智能信息时则必须填客户的手机号码。样例为：130****0001。

        :return: The cust_flag of this CreateShortChainParam.
        :rtype: str
        """
        return self._cust_flag

    @cust_flag.setter
    def cust_flag(self, cust_flag):
        """Sets the cust_flag of this CreateShortChainParam.

        创建解析任务时填写用户唯一标识，手机号码或者任何的唯一标识，唯一标识不超过64个字符。 发送智能信息时则必须填客户的手机号码。样例为：130****0001。

        :param cust_flag: The cust_flag of this CreateShortChainParam.
        :type cust_flag: str
        """
        self._cust_flag = cust_flag

    @property
    def dync_params(self):
        """Gets the dync_params of this CreateShortChainParam.

        动态参数。  > 使用动态参数模板时，aim_code_type字段只能为individual。 

        :return: The dync_params of this CreateShortChainParam.
        :rtype: dict(str, str)
        """
        return self._dync_params

    @dync_params.setter
    def dync_params(self, dync_params):
        """Sets the dync_params of this CreateShortChainParam.

        动态参数。  > 使用动态参数模板时，aim_code_type字段只能为individual。 

        :param dync_params: The dync_params of this CreateShortChainParam.
        :type dync_params: dict(str, str)
        """
        self._dync_params = dync_params

    @property
    def custom_url(self):
        """Gets the custom_url of this CreateShortChainParam.

        自定义跳转地址。长度要求不超过2048。 > - 未填时，终端用户点击短信原文中的短链后，跳转智能信息模板H5页 > - 已填时，终端用户点击短信原文中的短链后，跳转该字段对应的页面，填写时必须为http或https作为前缀 > - 使用自定义跳转链接功能请联系KooMessage运营人员进行域名备案 > - 自定义短码时即generation_type为2时不支持自定义跳转链接功能，传入的参数值无效 

        :return: The custom_url of this CreateShortChainParam.
        :rtype: str
        """
        return self._custom_url

    @custom_url.setter
    def custom_url(self, custom_url):
        """Sets the custom_url of this CreateShortChainParam.

        自定义跳转地址。长度要求不超过2048。 > - 未填时，终端用户点击短信原文中的短链后，跳转智能信息模板H5页 > - 已填时，终端用户点击短信原文中的短链后，跳转该字段对应的页面，填写时必须为http或https作为前缀 > - 使用自定义跳转链接功能请联系KooMessage运营人员进行域名备案 > - 自定义短码时即generation_type为2时不支持自定义跳转链接功能，传入的参数值无效 

        :param custom_url: The custom_url of this CreateShortChainParam.
        :type custom_url: str
        """
        self._custom_url = custom_url

    @property
    def custom_short_code(self):
        """Gets the custom_short_code of this CreateShortChainParam.

        自定义短码，支持长度为3到10位的数字或大小写字母。样例为：aDC123。 > 自定义短码时即generation_type为2时，此参数为必填。

        :return: The custom_short_code of this CreateShortChainParam.
        :rtype: str
        """
        return self._custom_short_code

    @custom_short_code.setter
    def custom_short_code(self, custom_short_code):
        """Sets the custom_short_code of this CreateShortChainParam.

        自定义短码，支持长度为3到10位的数字或大小写字母。样例为：aDC123。 > 自定义短码时即generation_type为2时，此参数为必填。

        :param custom_short_code: The custom_short_code of this CreateShortChainParam.
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
        if not isinstance(other, CreateShortChainParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
