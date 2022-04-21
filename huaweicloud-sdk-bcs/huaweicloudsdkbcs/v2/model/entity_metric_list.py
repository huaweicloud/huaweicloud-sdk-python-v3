# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EntityMetricList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[Dimension]',
        'values': 'list[EntityMetricListItem]'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'values': 'values'
    }

    def __init__(self, dimensions=None, values=None):
        """EntityMetricList

        The model defined in huaweicloud sdk

        :param dimensions: 指标对象列表。
        :type dimensions: list[:class:`huaweicloudsdkbcs.v2.Dimension`]
        :param values: 监控数据列表项目。
        :type values: list[:class:`huaweicloudsdkbcs.v2.EntityMetricListItem`]
        """
        
        

        self._dimensions = None
        self._values = None
        self.discriminator = None

        if dimensions is not None:
            self.dimensions = dimensions
        if values is not None:
            self.values = values

    @property
    def dimensions(self):
        """Gets the dimensions of this EntityMetricList.

        指标对象列表。

        :return: The dimensions of this EntityMetricList.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.Dimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this EntityMetricList.

        指标对象列表。

        :param dimensions: The dimensions of this EntityMetricList.
        :type dimensions: list[:class:`huaweicloudsdkbcs.v2.Dimension`]
        """
        self._dimensions = dimensions

    @property
    def values(self):
        """Gets the values of this EntityMetricList.

        监控数据列表项目。

        :return: The values of this EntityMetricList.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.EntityMetricListItem`]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this EntityMetricList.

        监控数据列表项目。

        :param values: The values of this EntityMetricList.
        :type values: list[:class:`huaweicloudsdkbcs.v2.EntityMetricListItem`]
        """
        self._values = values

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
        if not isinstance(other, EntityMetricList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
