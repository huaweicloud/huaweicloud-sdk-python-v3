# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Channel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'by_lte_pc5': 'bool',
        'by_lte_uu': 'bool'
    }

    attribute_map = {
        'by_lte_pc5': 'by_lte_pc5',
        'by_lte_uu': 'by_lte_uu'
    }

    def __init__(self, by_lte_pc5=None, by_lte_uu=None):
        """Channel

        The model defined in huaweicloud sdk

        :param by_lte_pc5: **参数说明**：LTE-PC5传输通道。若通过LTE-PC5传输通道下发事件，该字段为true。
        :type by_lte_pc5: bool
        :param by_lte_uu: **参数说明**：LTE-Uu的传输通道。若通过LTE-Uu的传输通道下发事件，该字段为true。
        :type by_lte_uu: bool
        """
        
        

        self._by_lte_pc5 = None
        self._by_lte_uu = None
        self.discriminator = None

        if by_lte_pc5 is not None:
            self.by_lte_pc5 = by_lte_pc5
        if by_lte_uu is not None:
            self.by_lte_uu = by_lte_uu

    @property
    def by_lte_pc5(self):
        """Gets the by_lte_pc5 of this Channel.

        **参数说明**：LTE-PC5传输通道。若通过LTE-PC5传输通道下发事件，该字段为true。

        :return: The by_lte_pc5 of this Channel.
        :rtype: bool
        """
        return self._by_lte_pc5

    @by_lte_pc5.setter
    def by_lte_pc5(self, by_lte_pc5):
        """Sets the by_lte_pc5 of this Channel.

        **参数说明**：LTE-PC5传输通道。若通过LTE-PC5传输通道下发事件，该字段为true。

        :param by_lte_pc5: The by_lte_pc5 of this Channel.
        :type by_lte_pc5: bool
        """
        self._by_lte_pc5 = by_lte_pc5

    @property
    def by_lte_uu(self):
        """Gets the by_lte_uu of this Channel.

        **参数说明**：LTE-Uu的传输通道。若通过LTE-Uu的传输通道下发事件，该字段为true。

        :return: The by_lte_uu of this Channel.
        :rtype: bool
        """
        return self._by_lte_uu

    @by_lte_uu.setter
    def by_lte_uu(self, by_lte_uu):
        """Sets the by_lte_uu of this Channel.

        **参数说明**：LTE-Uu的传输通道。若通过LTE-Uu的传输通道下发事件，该字段为true。

        :param by_lte_uu: The by_lte_uu of this Channel.
        :type by_lte_uu: bool
        """
        self._by_lte_uu = by_lte_uu

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
        if not isinstance(other, Channel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
