# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTenant:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'type': 'type'
    }

    def __init__(self, domain_id=None, domain_name=None, type=None):
        r"""ResourceTenant

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param domain_name: 账号名称
        :type domain_name: str
        :param type: 创建的委托类型
        :type type: str
        """
        
        

        self._domain_id = None
        self._domain_name = None
        self._type = None
        self.discriminator = None

        self.domain_id = domain_id
        self.domain_name = domain_name
        self.type = type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ResourceTenant.

        账号ID

        :return: The domain_id of this ResourceTenant.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ResourceTenant.

        账号ID

        :param domain_id: The domain_id of this ResourceTenant.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ResourceTenant.

        账号名称

        :return: The domain_name of this ResourceTenant.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ResourceTenant.

        账号名称

        :param domain_name: The domain_name of this ResourceTenant.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def type(self):
        r"""Gets the type of this ResourceTenant.

        创建的委托类型

        :return: The type of this ResourceTenant.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceTenant.

        创建的委托类型

        :param type: The type of this ResourceTenant.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ResourceTenant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
