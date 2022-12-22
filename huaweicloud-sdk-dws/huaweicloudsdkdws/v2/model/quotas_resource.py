# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotasResource:

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
        'used': 'str',
        'quota': 'int',
        'unit': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'quota': 'quota',
        'unit': 'unit'
    }

    def __init__(self, type=None, used=None, quota=None, unit=None):
        """QuotasResource

        The model defined in huaweicloud sdk

        :param type: 项目资源类型。
        :type type: str
        :param used: 已使用的资源数量。
        :type used: str
        :param quota: 项目资源配额。
        :type quota: int
        :param unit: 资源计量单位。
        :type unit: int
        """
        
        

        self._type = None
        self._used = None
        self._quota = None
        self._unit = None
        self.discriminator = None

        self.type = type
        self.used = used
        self.quota = quota
        self.unit = unit

    @property
    def type(self):
        """Gets the type of this QuotasResource.

        项目资源类型。

        :return: The type of this QuotasResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotasResource.

        项目资源类型。

        :param type: The type of this QuotasResource.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this QuotasResource.

        已使用的资源数量。

        :return: The used of this QuotasResource.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this QuotasResource.

        已使用的资源数量。

        :param used: The used of this QuotasResource.
        :type used: str
        """
        self._used = used

    @property
    def quota(self):
        """Gets the quota of this QuotasResource.

        项目资源配额。

        :return: The quota of this QuotasResource.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this QuotasResource.

        项目资源配额。

        :param quota: The quota of this QuotasResource.
        :type quota: int
        """
        self._quota = quota

    @property
    def unit(self):
        """Gets the unit of this QuotasResource.

        资源计量单位。

        :return: The unit of this QuotasResource.
        :rtype: int
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this QuotasResource.

        资源计量单位。

        :param unit: The unit of this QuotasResource.
        :type unit: int
        """
        self._unit = unit

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
        if not isinstance(other, QuotasResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
