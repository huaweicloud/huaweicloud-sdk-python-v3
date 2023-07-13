# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PremiumWafInstances:

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
        'name': 'str',
        'accessed': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'accessed': 'accessed'
    }

    def __init__(self, id=None, name=None, accessed=None):
        """PremiumWafInstances

        The model defined in huaweicloud sdk

        :param id: 引擎实例id
        :type id: str
        :param name: 引擎实例名
        :type name: str
        :param accessed: 引擎实例是否已接入，false：未接入；true：已接入
        :type accessed: bool
        """
        
        

        self._id = None
        self._name = None
        self._accessed = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if accessed is not None:
            self.accessed = accessed

    @property
    def id(self):
        """Gets the id of this PremiumWafInstances.

        引擎实例id

        :return: The id of this PremiumWafInstances.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PremiumWafInstances.

        引擎实例id

        :param id: The id of this PremiumWafInstances.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PremiumWafInstances.

        引擎实例名

        :return: The name of this PremiumWafInstances.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PremiumWafInstances.

        引擎实例名

        :param name: The name of this PremiumWafInstances.
        :type name: str
        """
        self._name = name

    @property
    def accessed(self):
        """Gets the accessed of this PremiumWafInstances.

        引擎实例是否已接入，false：未接入；true：已接入

        :return: The accessed of this PremiumWafInstances.
        :rtype: bool
        """
        return self._accessed

    @accessed.setter
    def accessed(self, accessed):
        """Sets the accessed of this PremiumWafInstances.

        引擎实例是否已接入，false：未接入；true：已接入

        :param accessed: The accessed of this PremiumWafInstances.
        :type accessed: bool
        """
        self._accessed = accessed

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
        if not isinstance(other, PremiumWafInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
