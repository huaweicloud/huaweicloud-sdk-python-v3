# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyInstanceResources:


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
        'used': 'int',
        'quota': 'int',
        'max': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'quota': 'quota',
        'max': 'max'
    }

    def __init__(self, type=None, used=None, quota=None, max=None):
        """PolicyInstanceResources - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._used = None
        self._quota = None
        self._max = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if used is not None:
            self.used = used
        if quota is not None:
            self.quota = quota
        if max is not None:
            self.max = max

    @property
    def type(self):
        """Gets the type of this PolicyInstanceResources.

        查询配额的类型。

        :return: The type of this PolicyInstanceResources.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyInstanceResources.

        查询配额的类型。

        :param type: The type of this PolicyInstanceResources.
        :type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this PolicyInstanceResources.

        已使用的配额数量。

        :return: The used of this PolicyInstanceResources.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this PolicyInstanceResources.

        已使用的配额数量。

        :param used: The used of this PolicyInstanceResources.
        :type: int
        """
        self._used = used

    @property
    def quota(self):
        """Gets the quota of this PolicyInstanceResources.

        配额总数量。

        :return: The quota of this PolicyInstanceResources.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this PolicyInstanceResources.

        配额总数量。

        :param quota: The quota of this PolicyInstanceResources.
        :type: int
        """
        self._quota = quota

    @property
    def max(self):
        """Gets the max of this PolicyInstanceResources.

        配额上限。

        :return: The max of this PolicyInstanceResources.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this PolicyInstanceResources.

        配额上限。

        :param max: The max of this PolicyInstanceResources.
        :type: int
        """
        self._max = max

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyInstanceResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
