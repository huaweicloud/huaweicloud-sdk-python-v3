# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalIdDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('id')
    sensitive_list.append('issuer')

    openapi_types = {
        'id': 'str',
        'issuer': 'str'
    }

    attribute_map = {
        'id': 'id',
        'issuer': 'issuer'
    }

    def __init__(self, id=None, issuer=None):
        """ExternalIdDto

        The model defined in huaweicloud sdk

        :param id: 外部身份提供商颁发给此资源的标识符
        :type id: str
        :param issuer: 外部标识符的颁发者
        :type issuer: str
        """
        
        

        self._id = None
        self._issuer = None
        self.discriminator = None

        self.id = id
        self.issuer = issuer

    @property
    def id(self):
        """Gets the id of this ExternalIdDto.

        外部身份提供商颁发给此资源的标识符

        :return: The id of this ExternalIdDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalIdDto.

        外部身份提供商颁发给此资源的标识符

        :param id: The id of this ExternalIdDto.
        :type id: str
        """
        self._id = id

    @property
    def issuer(self):
        """Gets the issuer of this ExternalIdDto.

        外部标识符的颁发者

        :return: The issuer of this ExternalIdDto.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this ExternalIdDto.

        外部标识符的颁发者

        :param issuer: The issuer of this ExternalIdDto.
        :type issuer: str
        """
        self._issuer = issuer

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
        if not isinstance(other, ExternalIdDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
