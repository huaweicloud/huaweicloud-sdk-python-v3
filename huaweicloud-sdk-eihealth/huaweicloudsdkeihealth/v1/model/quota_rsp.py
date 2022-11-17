# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'total': 'int',
        'unit': 'str',
        'usage': 'int'
    }

    attribute_map = {
        'name': 'name',
        'total': 'total',
        'unit': 'unit',
        'usage': 'usage'
    }

    def __init__(self, name=None, total=None, unit=None, usage=None):
        """QuotaRsp

        The model defined in huaweicloud sdk

        :param name: 配额项名称，支持USER,PROJECT,USER_PROJECT,STORAGE,PROJECT_APP,PROJECT_NOTEBOOK,PROJECT_WORKFLOW,PROJECT_IMAGE
        :type name: str
        :param total: 配额
        :type total: int
        :param unit: 配额项单位
        :type unit: str
        :param usage: 配额使用量
        :type usage: int
        """
        
        

        self._name = None
        self._total = None
        self._unit = None
        self._usage = None
        self.discriminator = None

        self.name = name
        self.total = total
        self.unit = unit
        self.usage = usage

    @property
    def name(self):
        """Gets the name of this QuotaRsp.

        配额项名称，支持USER,PROJECT,USER_PROJECT,STORAGE,PROJECT_APP,PROJECT_NOTEBOOK,PROJECT_WORKFLOW,PROJECT_IMAGE

        :return: The name of this QuotaRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QuotaRsp.

        配额项名称，支持USER,PROJECT,USER_PROJECT,STORAGE,PROJECT_APP,PROJECT_NOTEBOOK,PROJECT_WORKFLOW,PROJECT_IMAGE

        :param name: The name of this QuotaRsp.
        :type name: str
        """
        self._name = name

    @property
    def total(self):
        """Gets the total of this QuotaRsp.

        配额

        :return: The total of this QuotaRsp.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this QuotaRsp.

        配额

        :param total: The total of this QuotaRsp.
        :type total: int
        """
        self._total = total

    @property
    def unit(self):
        """Gets the unit of this QuotaRsp.

        配额项单位

        :return: The unit of this QuotaRsp.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this QuotaRsp.

        配额项单位

        :param unit: The unit of this QuotaRsp.
        :type unit: str
        """
        self._unit = unit

    @property
    def usage(self):
        """Gets the usage of this QuotaRsp.

        配额使用量

        :return: The usage of this QuotaRsp.
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this QuotaRsp.

        配额使用量

        :param usage: The usage of this QuotaRsp.
        :type usage: int
        """
        self._usage = usage

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
        if not isinstance(other, QuotaRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
