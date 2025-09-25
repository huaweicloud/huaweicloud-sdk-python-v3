# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReduceDnRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'contraction_num': 'int'
    }

    attribute_map = {
        'contraction_num': 'contraction_num'
    }

    def __init__(self, contraction_num=None):
        r"""ReduceDnRequestBody

        The model defined in huaweicloud sdk

        :param contraction_num: **参数解释**: 缩容分片数量。 **约束限制**: 缩容分片数量需要大于0且集群至少保留一个分片。 **取值范围**: 大于0的正整数。 **默认取值**: 不涉及。
        :type contraction_num: int
        """
        
        

        self._contraction_num = None
        self.discriminator = None

        self.contraction_num = contraction_num

    @property
    def contraction_num(self):
        r"""Gets the contraction_num of this ReduceDnRequestBody.

        **参数解释**: 缩容分片数量。 **约束限制**: 缩容分片数量需要大于0且集群至少保留一个分片。 **取值范围**: 大于0的正整数。 **默认取值**: 不涉及。

        :return: The contraction_num of this ReduceDnRequestBody.
        :rtype: int
        """
        return self._contraction_num

    @contraction_num.setter
    def contraction_num(self, contraction_num):
        r"""Sets the contraction_num of this ReduceDnRequestBody.

        **参数解释**: 缩容分片数量。 **约束限制**: 缩容分片数量需要大于0且集群至少保留一个分片。 **取值范围**: 大于0的正整数。 **默认取值**: 不涉及。

        :param contraction_num: The contraction_num of this ReduceDnRequestBody.
        :type contraction_num: int
        """
        self._contraction_num = contraction_num

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
        if not isinstance(other, ReduceDnRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
