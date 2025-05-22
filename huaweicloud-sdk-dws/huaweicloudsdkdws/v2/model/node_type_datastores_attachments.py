# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeTypeDatastoresAttachments:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_cn': 'int',
        'max_cn': 'int'
    }

    attribute_map = {
        'min_cn': 'min_cn',
        'max_cn': 'max_cn'
    }

    def __init__(self, min_cn=None, max_cn=None):
        r"""NodeTypeDatastoresAttachments

        The model defined in huaweicloud sdk

        :param min_cn: **参数解释**： 内核版本支持的最小CN。 **取值范围**： 大于0的正整数。
        :type min_cn: int
        :param max_cn: **参数解释**： 内核版本支持的最大CN。 **取值范围**： 大于0的正整数。
        :type max_cn: int
        """
        
        

        self._min_cn = None
        self._max_cn = None
        self.discriminator = None

        if min_cn is not None:
            self.min_cn = min_cn
        if max_cn is not None:
            self.max_cn = max_cn

    @property
    def min_cn(self):
        r"""Gets the min_cn of this NodeTypeDatastoresAttachments.

        **参数解释**： 内核版本支持的最小CN。 **取值范围**： 大于0的正整数。

        :return: The min_cn of this NodeTypeDatastoresAttachments.
        :rtype: int
        """
        return self._min_cn

    @min_cn.setter
    def min_cn(self, min_cn):
        r"""Sets the min_cn of this NodeTypeDatastoresAttachments.

        **参数解释**： 内核版本支持的最小CN。 **取值范围**： 大于0的正整数。

        :param min_cn: The min_cn of this NodeTypeDatastoresAttachments.
        :type min_cn: int
        """
        self._min_cn = min_cn

    @property
    def max_cn(self):
        r"""Gets the max_cn of this NodeTypeDatastoresAttachments.

        **参数解释**： 内核版本支持的最大CN。 **取值范围**： 大于0的正整数。

        :return: The max_cn of this NodeTypeDatastoresAttachments.
        :rtype: int
        """
        return self._max_cn

    @max_cn.setter
    def max_cn(self, max_cn):
        r"""Sets the max_cn of this NodeTypeDatastoresAttachments.

        **参数解释**： 内核版本支持的最大CN。 **取值范围**： 大于0的正整数。

        :param max_cn: The max_cn of this NodeTypeDatastoresAttachments.
        :type max_cn: int
        """
        self._max_cn = max_cn

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
        if not isinstance(other, NodeTypeDatastoresAttachments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
