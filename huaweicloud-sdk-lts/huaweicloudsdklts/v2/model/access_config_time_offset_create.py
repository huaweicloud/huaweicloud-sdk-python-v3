# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigTimeOffsetCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'unit': 'unit'
    }

    def __init__(self, offset=None, unit=None):
        """AccessConfigTimeOffsetCreate

        The model defined in huaweicloud sdk

        :param offset: 偏移时间。 当\&quot;unit\&quot;选择\&quot;day\&quot;时，范围为1~7天。 当\&quot;unit\&quot;选择\&quot;hour\&quot;时，范围为1~168小时。 当\&quot;unit\&quot;选择\&quot;sec\&quot;时，范围为1~604800秒。
        :type offset: int
        :param unit: 偏移时间单位。day ：天，hour：小时，sec：秒
        :type unit: str
        """
        
        

        self._offset = None
        self._unit = None
        self.discriminator = None

        self.offset = offset
        self.unit = unit

    @property
    def offset(self):
        """Gets the offset of this AccessConfigTimeOffsetCreate.

        偏移时间。 当\"unit\"选择\"day\"时，范围为1~7天。 当\"unit\"选择\"hour\"时，范围为1~168小时。 当\"unit\"选择\"sec\"时，范围为1~604800秒。

        :return: The offset of this AccessConfigTimeOffsetCreate.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this AccessConfigTimeOffsetCreate.

        偏移时间。 当\"unit\"选择\"day\"时，范围为1~7天。 当\"unit\"选择\"hour\"时，范围为1~168小时。 当\"unit\"选择\"sec\"时，范围为1~604800秒。

        :param offset: The offset of this AccessConfigTimeOffsetCreate.
        :type offset: int
        """
        self._offset = offset

    @property
    def unit(self):
        """Gets the unit of this AccessConfigTimeOffsetCreate.

        偏移时间单位。day ：天，hour：小时，sec：秒

        :return: The unit of this AccessConfigTimeOffsetCreate.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this AccessConfigTimeOffsetCreate.

        偏移时间单位。day ：天，hour：小时，sec：秒

        :param unit: The unit of this AccessConfigTimeOffsetCreate.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, AccessConfigTimeOffsetCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
