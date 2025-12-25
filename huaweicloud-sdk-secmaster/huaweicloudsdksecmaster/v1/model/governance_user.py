# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GovernanceUser:

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
        'name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, type=None, name=None):
        r"""GovernanceUser

        The model defined in huaweicloud sdk

        :param type: 资产治理责任人类型
        :type type: str
        :param name: 资产治理责任人名称，为空则忽略，不存在则创建
        :type name: str
        """
        
        

        self._type = None
        self._name = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name

    @property
    def type(self):
        r"""Gets the type of this GovernanceUser.

        资产治理责任人类型

        :return: The type of this GovernanceUser.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GovernanceUser.

        资产治理责任人类型

        :param type: The type of this GovernanceUser.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this GovernanceUser.

        资产治理责任人名称，为空则忽略，不存在则创建

        :return: The name of this GovernanceUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GovernanceUser.

        资产治理责任人名称，为空则忽略，不存在则创建

        :param name: The name of this GovernanceUser.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, GovernanceUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
