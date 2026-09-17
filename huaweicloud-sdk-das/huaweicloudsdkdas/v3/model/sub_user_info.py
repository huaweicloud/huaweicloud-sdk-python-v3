# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubUserInfo:

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
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, domain_id=None, id=None, name=None):
        r"""SubUserInfo

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param id: 用户ID
        :type id: str
        :param name: 用户名
        :type name: str
        """
        
        

        self._domain_id = None
        self._id = None
        self._name = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this SubUserInfo.

        租户ID

        :return: The domain_id of this SubUserInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this SubUserInfo.

        租户ID

        :param domain_id: The domain_id of this SubUserInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def id(self):
        r"""Gets the id of this SubUserInfo.

        用户ID

        :return: The id of this SubUserInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubUserInfo.

        用户ID

        :param id: The id of this SubUserInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SubUserInfo.

        用户名

        :return: The name of this SubUserInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubUserInfo.

        用户名

        :param name: The name of this SubUserInfo.
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
        if not isinstance(other, SubUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
