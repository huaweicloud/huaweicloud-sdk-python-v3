# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkCapability:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'domain_id': 'str',
        'capability': 'CentralNetworkCapabilityEnum'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'capability': 'capability'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, id=None, domain_id=None, capability=None):
        """CentralNetworkCapability

        The model defined in huaweicloud sdk

        :param id: 资源ID标识符。
        :type id: str
        :param domain_id: 实例所属帐号ID。
        :type domain_id: str
        :param capability: 
        :type capability: :class:`huaweicloudsdkcc.v3.CentralNetworkCapabilityEnum`
        """
        
        

        self._id = None
        self._domain_id = None
        self._capability = None
        self.discriminator = 'capability'

        self.id = id
        self.domain_id = domain_id
        self.capability = capability

    @property
    def id(self):
        """Gets the id of this CentralNetworkCapability.

        资源ID标识符。

        :return: The id of this CentralNetworkCapability.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CentralNetworkCapability.

        资源ID标识符。

        :param id: The id of this CentralNetworkCapability.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        """Gets the domain_id of this CentralNetworkCapability.

        实例所属帐号ID。

        :return: The domain_id of this CentralNetworkCapability.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CentralNetworkCapability.

        实例所属帐号ID。

        :param domain_id: The domain_id of this CentralNetworkCapability.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def capability(self):
        """Gets the capability of this CentralNetworkCapability.

        :return: The capability of this CentralNetworkCapability.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkCapabilityEnum`
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """Sets the capability of this CentralNetworkCapability.

        :param capability: The capability of this CentralNetworkCapability.
        :type capability: :class:`huaweicloudsdkcc.v3.CentralNetworkCapabilityEnum`
        """
        self._capability = capability

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)
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
        if not isinstance(other, CentralNetworkCapability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
