# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClouddcnSubnetOption:

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
        'description': 'str',
        'dns_nameservers': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'dns_nameservers': 'dns_nameservers'
    }

    def __init__(self, name=None, description=None, dns_nameservers=None):
        r"""UpdateClouddcnSubnetOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：子网名称 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：子网描述 取值范围：0-255个字符，不能包含\&quot;&lt;\&quot;和\&quot;&gt;\&quot;。
        :type description: str
        :param dns_nameservers: 功能说明：子网关联的DNS服务器信息。
        :type dns_nameservers: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._dns_nameservers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if dns_nameservers is not None:
            self.dns_nameservers = dns_nameservers

    @property
    def name(self):
        r"""Gets the name of this UpdateClouddcnSubnetOption.

        功能说明：子网名称 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this UpdateClouddcnSubnetOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateClouddcnSubnetOption.

        功能说明：子网名称 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this UpdateClouddcnSubnetOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateClouddcnSubnetOption.

        功能说明：子网描述 取值范围：0-255个字符，不能包含\"<\"和\">\"。

        :return: The description of this UpdateClouddcnSubnetOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateClouddcnSubnetOption.

        功能说明：子网描述 取值范围：0-255个字符，不能包含\"<\"和\">\"。

        :param description: The description of this UpdateClouddcnSubnetOption.
        :type description: str
        """
        self._description = description

    @property
    def dns_nameservers(self):
        r"""Gets the dns_nameservers of this UpdateClouddcnSubnetOption.

        功能说明：子网关联的DNS服务器信息。

        :return: The dns_nameservers of this UpdateClouddcnSubnetOption.
        :rtype: list[str]
        """
        return self._dns_nameservers

    @dns_nameservers.setter
    def dns_nameservers(self, dns_nameservers):
        r"""Sets the dns_nameservers of this UpdateClouddcnSubnetOption.

        功能说明：子网关联的DNS服务器信息。

        :param dns_nameservers: The dns_nameservers of this UpdateClouddcnSubnetOption.
        :type dns_nameservers: list[str]
        """
        self._dns_nameservers = dns_nameservers

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateClouddcnSubnetOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
