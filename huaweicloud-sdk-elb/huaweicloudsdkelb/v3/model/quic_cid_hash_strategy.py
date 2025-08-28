# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuicCidHashStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'len': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'len': 'len',
        'offset': 'offset'
    }

    def __init__(self, len=None, offset=None):
        r"""QuicCidHashStrategy

        The model defined in huaweicloud sdk

        :param len: **参数解释**：表示hash的时候取CID的长度。  **约束限制**：仅当负载均衡算法为QUIC_CID的时候才生效。  **取值范围**：1-20  **默认取值**：3
        :type len: int
        :param offset: **参数解释**：表示hash的时候取CID的偏移量。  **约束限制**：仅当负载均衡算法为QUIC_CID的时候才生效。  **取值范围**：0-19  **默认取值**：1
        :type offset: int
        """
        
        

        self._len = None
        self._offset = None
        self.discriminator = None

        self.len = len
        self.offset = offset

    @property
    def len(self):
        r"""Gets the len of this QuicCidHashStrategy.

        **参数解释**：表示hash的时候取CID的长度。  **约束限制**：仅当负载均衡算法为QUIC_CID的时候才生效。  **取值范围**：1-20  **默认取值**：3

        :return: The len of this QuicCidHashStrategy.
        :rtype: int
        """
        return self._len

    @len.setter
    def len(self, len):
        r"""Sets the len of this QuicCidHashStrategy.

        **参数解释**：表示hash的时候取CID的长度。  **约束限制**：仅当负载均衡算法为QUIC_CID的时候才生效。  **取值范围**：1-20  **默认取值**：3

        :param len: The len of this QuicCidHashStrategy.
        :type len: int
        """
        self._len = len

    @property
    def offset(self):
        r"""Gets the offset of this QuicCidHashStrategy.

        **参数解释**：表示hash的时候取CID的偏移量。  **约束限制**：仅当负载均衡算法为QUIC_CID的时候才生效。  **取值范围**：0-19  **默认取值**：1

        :return: The offset of this QuicCidHashStrategy.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this QuicCidHashStrategy.

        **参数解释**：表示hash的时候取CID的偏移量。  **约束限制**：仅当负载均衡算法为QUIC_CID的时候才生效。  **取值范围**：0-19  **默认取值**：1

        :param offset: The offset of this QuicCidHashStrategy.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, QuicCidHashStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
