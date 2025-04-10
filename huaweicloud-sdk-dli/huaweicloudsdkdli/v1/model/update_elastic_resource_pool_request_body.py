# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateElasticResourcePoolRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'max_cu': 'int',
        'min_cu': 'int'
    }

    attribute_map = {
        'description': 'description',
        'max_cu': 'max_cu',
        'min_cu': 'min_cu'
    }

    def __init__(self, description=None, max_cu=None, min_cu=None):
        r"""UpdateElasticResourcePoolRequestBody

        The model defined in huaweicloud sdk

        :param description: 描述信息。长度限制：256个字符以内。
        :type description: str
        :param max_cu: max_cu大于等于该弹性资源池下任意一个队列的最大CU。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。
        :type max_cu: int
        :param min_cu: min_cu大于等于该弹性资源池下所有队列最小CU之和，且小于等于max_cu。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。
        :type min_cu: int
        """
        
        

        self._description = None
        self._max_cu = None
        self._min_cu = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if max_cu is not None:
            self.max_cu = max_cu
        if min_cu is not None:
            self.min_cu = min_cu

    @property
    def description(self):
        r"""Gets the description of this UpdateElasticResourcePoolRequestBody.

        描述信息。长度限制：256个字符以内。

        :return: The description of this UpdateElasticResourcePoolRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateElasticResourcePoolRequestBody.

        描述信息。长度限制：256个字符以内。

        :param description: The description of this UpdateElasticResourcePoolRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def max_cu(self):
        r"""Gets the max_cu of this UpdateElasticResourcePoolRequestBody.

        max_cu大于等于该弹性资源池下任意一个队列的最大CU。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。

        :return: The max_cu of this UpdateElasticResourcePoolRequestBody.
        :rtype: int
        """
        return self._max_cu

    @max_cu.setter
    def max_cu(self, max_cu):
        r"""Sets the max_cu of this UpdateElasticResourcePoolRequestBody.

        max_cu大于等于该弹性资源池下任意一个队列的最大CU。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。

        :param max_cu: The max_cu of this UpdateElasticResourcePoolRequestBody.
        :type max_cu: int
        """
        self._max_cu = max_cu

    @property
    def min_cu(self):
        r"""Gets the min_cu of this UpdateElasticResourcePoolRequestBody.

        min_cu大于等于该弹性资源池下所有队列最小CU之和，且小于等于max_cu。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。

        :return: The min_cu of this UpdateElasticResourcePoolRequestBody.
        :rtype: int
        """
        return self._min_cu

    @min_cu.setter
    def min_cu(self, min_cu):
        r"""Sets the min_cu of this UpdateElasticResourcePoolRequestBody.

        min_cu大于等于该弹性资源池下所有队列最小CU之和，且小于等于max_cu。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。

        :param min_cu: The min_cu of this UpdateElasticResourcePoolRequestBody.
        :type min_cu: int
        """
        self._min_cu = min_cu

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
        if not isinstance(other, UpdateElasticResourcePoolRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
