# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCustomLineRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'ip_segments': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'ip_segments': 'ip_segments',
        'description': 'description'
    }

    def __init__(self, name=None, ip_segments=None, description=None):
        r"""CreateCustomLineRequestBody

        The model defined in huaweicloud sdk

        :param name: 解析线路名称。  长度限制为1-80个字符，只允许包含中文、字母、数字、&#39;-&#39;、&#39;_&#39;、&#39;.&#39;字符。  租户内，解析线路名称是唯一的。
        :type name: str
        :param ip_segments: IP地址段。  以“-”分隔，小IP地址在前，大IP地址在后。IP段之间不能有交叉。当只有一个IP时，填写IP1-IP1。 目前只支持IPV4。  最多支持50个。
        :type ip_segments: list[str]
        :param description: 自定义线路的描述信息。长度不超过255个字符。  默认值为空。
        :type description: str
        """
        
        

        self._name = None
        self._ip_segments = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.ip_segments = ip_segments
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this CreateCustomLineRequestBody.

        解析线路名称。  长度限制为1-80个字符，只允许包含中文、字母、数字、'-'、'_'、'.'字符。  租户内，解析线路名称是唯一的。

        :return: The name of this CreateCustomLineRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCustomLineRequestBody.

        解析线路名称。  长度限制为1-80个字符，只允许包含中文、字母、数字、'-'、'_'、'.'字符。  租户内，解析线路名称是唯一的。

        :param name: The name of this CreateCustomLineRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def ip_segments(self):
        r"""Gets the ip_segments of this CreateCustomLineRequestBody.

        IP地址段。  以“-”分隔，小IP地址在前，大IP地址在后。IP段之间不能有交叉。当只有一个IP时，填写IP1-IP1。 目前只支持IPV4。  最多支持50个。

        :return: The ip_segments of this CreateCustomLineRequestBody.
        :rtype: list[str]
        """
        return self._ip_segments

    @ip_segments.setter
    def ip_segments(self, ip_segments):
        r"""Sets the ip_segments of this CreateCustomLineRequestBody.

        IP地址段。  以“-”分隔，小IP地址在前，大IP地址在后。IP段之间不能有交叉。当只有一个IP时，填写IP1-IP1。 目前只支持IPV4。  最多支持50个。

        :param ip_segments: The ip_segments of this CreateCustomLineRequestBody.
        :type ip_segments: list[str]
        """
        self._ip_segments = ip_segments

    @property
    def description(self):
        r"""Gets the description of this CreateCustomLineRequestBody.

        自定义线路的描述信息。长度不超过255个字符。  默认值为空。

        :return: The description of this CreateCustomLineRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCustomLineRequestBody.

        自定义线路的描述信息。长度不超过255个字符。  默认值为空。

        :param description: The description of this CreateCustomLineRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateCustomLineRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
