# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoSqlEpsQuotaUsed:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'int',
        'vcpus': 'int',
        'ram': 'int'
    }

    attribute_map = {
        'instance': 'instance',
        'vcpus': 'vcpus',
        'ram': 'ram'
    }

    def __init__(self, instance=None, vcpus=None, ram=None):
        """NoSqlEpsQuotaUsed

        The model defined in huaweicloud sdk

        :param instance: 已使用实例配额。
        :type instance: int
        :param vcpus: 已使用vcpus配额。
        :type vcpus: int
        :param ram: 已使用ram配额。
        :type ram: int
        """
        
        

        self._instance = None
        self._vcpus = None
        self._ram = None
        self.discriminator = None

        self.instance = instance
        self.vcpus = vcpus
        self.ram = ram

    @property
    def instance(self):
        """Gets the instance of this NoSqlEpsQuotaUsed.

        已使用实例配额。

        :return: The instance of this NoSqlEpsQuotaUsed.
        :rtype: int
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this NoSqlEpsQuotaUsed.

        已使用实例配额。

        :param instance: The instance of this NoSqlEpsQuotaUsed.
        :type instance: int
        """
        self._instance = instance

    @property
    def vcpus(self):
        """Gets the vcpus of this NoSqlEpsQuotaUsed.

        已使用vcpus配额。

        :return: The vcpus of this NoSqlEpsQuotaUsed.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this NoSqlEpsQuotaUsed.

        已使用vcpus配额。

        :param vcpus: The vcpus of this NoSqlEpsQuotaUsed.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this NoSqlEpsQuotaUsed.

        已使用ram配额。

        :return: The ram of this NoSqlEpsQuotaUsed.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this NoSqlEpsQuotaUsed.

        已使用ram配额。

        :param ram: The ram of this NoSqlEpsQuotaUsed.
        :type ram: int
        """
        self._ram = ram

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
        if not isinstance(other, NoSqlEpsQuotaUsed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
