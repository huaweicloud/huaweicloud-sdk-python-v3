# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DynamicDataMask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'mask_strategies': 'list[MaskStrategies]',
        'data': 'list[dict(str, object)]'
    }

    attribute_map = {
        'mask_strategies': 'mask_strategies',
        'data': 'data'
    }

    def __init__(self, mask_strategies=None, data=None):
        """DynamicDataMask

        The model defined in huaweicloud sdk

        :param mask_strategies: 脱敏策略列表，每一个策略对应一个字段，脱敏策略数最多100个。
        :type mask_strategies: list[:class:`huaweicloudsdkdsc.v1.MaskStrategies`]
        :param data: 数据列表。
        :type data: list[dict(str, object)]
        """
        
        

        self._mask_strategies = None
        self._data = None
        self.discriminator = None

        self.mask_strategies = mask_strategies
        self.data = data

    @property
    def mask_strategies(self):
        """Gets the mask_strategies of this DynamicDataMask.

        脱敏策略列表，每一个策略对应一个字段，脱敏策略数最多100个。

        :return: The mask_strategies of this DynamicDataMask.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.MaskStrategies`]
        """
        return self._mask_strategies

    @mask_strategies.setter
    def mask_strategies(self, mask_strategies):
        """Sets the mask_strategies of this DynamicDataMask.

        脱敏策略列表，每一个策略对应一个字段，脱敏策略数最多100个。

        :param mask_strategies: The mask_strategies of this DynamicDataMask.
        :type mask_strategies: list[:class:`huaweicloudsdkdsc.v1.MaskStrategies`]
        """
        self._mask_strategies = mask_strategies

    @property
    def data(self):
        """Gets the data of this DynamicDataMask.

        数据列表。

        :return: The data of this DynamicDataMask.
        :rtype: list[dict(str, object)]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DynamicDataMask.

        数据列表。

        :param data: The data of this DynamicDataMask.
        :type data: list[dict(str, object)]
        """
        self._data = data

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
        if not isinstance(other, DynamicDataMask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
