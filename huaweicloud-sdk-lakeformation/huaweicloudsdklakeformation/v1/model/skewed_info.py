# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SkewedInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'skewed_column_names': 'list[str]',
        'skewed_column_value_location_maps': 'dict(str, str)',
        'skewed_column_values': 'list[list[str]]'
    }

    attribute_map = {
        'skewed_column_names': 'skewed_column_names',
        'skewed_column_value_location_maps': 'skewed_column_value_location_maps',
        'skewed_column_values': 'skewed_column_values'
    }

    def __init__(self, skewed_column_names=None, skewed_column_value_location_maps=None, skewed_column_values=None):
        """SkewedInfo

        The model defined in huaweicloud sdk

        :param skewed_column_names: 数据偏移列的列表
        :type skewed_column_names: list[str]
        :param skewed_column_value_location_maps: 偏斜值和地址的映射关系.
        :type skewed_column_value_location_maps: dict(str, str)
        :param skewed_column_values: 偏斜值的列表.
        :type skewed_column_values: list[list[str]]
        """
        
        

        self._skewed_column_names = None
        self._skewed_column_value_location_maps = None
        self._skewed_column_values = None
        self.discriminator = None

        self.skewed_column_names = skewed_column_names
        self.skewed_column_value_location_maps = skewed_column_value_location_maps
        self.skewed_column_values = skewed_column_values

    @property
    def skewed_column_names(self):
        """Gets the skewed_column_names of this SkewedInfo.

        数据偏移列的列表

        :return: The skewed_column_names of this SkewedInfo.
        :rtype: list[str]
        """
        return self._skewed_column_names

    @skewed_column_names.setter
    def skewed_column_names(self, skewed_column_names):
        """Sets the skewed_column_names of this SkewedInfo.

        数据偏移列的列表

        :param skewed_column_names: The skewed_column_names of this SkewedInfo.
        :type skewed_column_names: list[str]
        """
        self._skewed_column_names = skewed_column_names

    @property
    def skewed_column_value_location_maps(self):
        """Gets the skewed_column_value_location_maps of this SkewedInfo.

        偏斜值和地址的映射关系.

        :return: The skewed_column_value_location_maps of this SkewedInfo.
        :rtype: dict(str, str)
        """
        return self._skewed_column_value_location_maps

    @skewed_column_value_location_maps.setter
    def skewed_column_value_location_maps(self, skewed_column_value_location_maps):
        """Sets the skewed_column_value_location_maps of this SkewedInfo.

        偏斜值和地址的映射关系.

        :param skewed_column_value_location_maps: The skewed_column_value_location_maps of this SkewedInfo.
        :type skewed_column_value_location_maps: dict(str, str)
        """
        self._skewed_column_value_location_maps = skewed_column_value_location_maps

    @property
    def skewed_column_values(self):
        """Gets the skewed_column_values of this SkewedInfo.

        偏斜值的列表.

        :return: The skewed_column_values of this SkewedInfo.
        :rtype: list[list[str]]
        """
        return self._skewed_column_values

    @skewed_column_values.setter
    def skewed_column_values(self, skewed_column_values):
        """Sets the skewed_column_values of this SkewedInfo.

        偏斜值的列表.

        :param skewed_column_values: The skewed_column_values of this SkewedInfo.
        :type skewed_column_values: list[list[str]]
        """
        self._skewed_column_values = skewed_column_values

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
        if not isinstance(other, SkewedInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
