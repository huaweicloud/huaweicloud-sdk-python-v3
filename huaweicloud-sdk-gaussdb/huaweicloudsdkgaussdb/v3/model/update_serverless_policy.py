# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerlessPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_vcpus': 'int',
        'max_vcpus': 'int'
    }

    attribute_map = {
        'min_vcpus': 'min_vcpus',
        'max_vcpus': 'max_vcpus'
    }

    def __init__(self, min_vcpus=None, max_vcpus=None):
        r"""UpdateServerlessPolicy

        The model defined in huaweicloud sdk

        :param min_vcpus: 单节点VCPUs伸缩下限，取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-gaussdb/ShowGaussMySqlFlavors.html)接口获取。
        :type min_vcpus: int
        :param max_vcpus: 单节点VCPUs伸缩上限，取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-gaussdb/ShowGaussMySqlFlavors.html)接口获取。
        :type max_vcpus: int
        """
        
        

        self._min_vcpus = None
        self._max_vcpus = None
        self.discriminator = None

        self.min_vcpus = min_vcpus
        self.max_vcpus = max_vcpus

    @property
    def min_vcpus(self):
        r"""Gets the min_vcpus of this UpdateServerlessPolicy.

        单节点VCPUs伸缩下限，取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-gaussdb/ShowGaussMySqlFlavors.html)接口获取。

        :return: The min_vcpus of this UpdateServerlessPolicy.
        :rtype: int
        """
        return self._min_vcpus

    @min_vcpus.setter
    def min_vcpus(self, min_vcpus):
        r"""Sets the min_vcpus of this UpdateServerlessPolicy.

        单节点VCPUs伸缩下限，取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-gaussdb/ShowGaussMySqlFlavors.html)接口获取。

        :param min_vcpus: The min_vcpus of this UpdateServerlessPolicy.
        :type min_vcpus: int
        """
        self._min_vcpus = min_vcpus

    @property
    def max_vcpus(self):
        r"""Gets the max_vcpus of this UpdateServerlessPolicy.

        单节点VCPUs伸缩上限，取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-gaussdb/ShowGaussMySqlFlavors.html)接口获取。

        :return: The max_vcpus of this UpdateServerlessPolicy.
        :rtype: int
        """
        return self._max_vcpus

    @max_vcpus.setter
    def max_vcpus(self, max_vcpus):
        r"""Sets the max_vcpus of this UpdateServerlessPolicy.

        单节点VCPUs伸缩上限，取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-gaussdb/ShowGaussMySqlFlavors.html)接口获取。

        :param max_vcpus: The max_vcpus of this UpdateServerlessPolicy.
        :type max_vcpus: int
        """
        self._max_vcpus = max_vcpus

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
        if not isinstance(other, UpdateServerlessPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
