# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoSqlEpsQuotaTotal:

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
        """NoSqlEpsQuotaTotal

        The model defined in huaweicloud sdk

        :param instance: 实例配额。
        :type instance: int
        :param vcpus: vcpus配额。
        :type vcpus: int
        :param ram: ram配额。
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
        """Gets the instance of this NoSqlEpsQuotaTotal.

        实例配额。

        :return: The instance of this NoSqlEpsQuotaTotal.
        :rtype: int
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this NoSqlEpsQuotaTotal.

        实例配额。

        :param instance: The instance of this NoSqlEpsQuotaTotal.
        :type instance: int
        """
        self._instance = instance

    @property
    def vcpus(self):
        """Gets the vcpus of this NoSqlEpsQuotaTotal.

        vcpus配额。

        :return: The vcpus of this NoSqlEpsQuotaTotal.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this NoSqlEpsQuotaTotal.

        vcpus配额。

        :param vcpus: The vcpus of this NoSqlEpsQuotaTotal.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this NoSqlEpsQuotaTotal.

        ram配额。

        :return: The ram of this NoSqlEpsQuotaTotal.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this NoSqlEpsQuotaTotal.

        ram配额。

        :param ram: The ram of this NoSqlEpsQuotaTotal.
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
        if not isinstance(other, NoSqlEpsQuotaTotal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
