# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TwinUpdateDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'twin': 'dict(str, ValueInTwin)',
        'property_visitors': 'dict(str, ValueInPropertyVisitors)'
    }

    attribute_map = {
        'twin': 'twin',
        'property_visitors': 'property_visitors'
    }

    def __init__(self, twin=None, property_visitors=None):
        r"""TwinUpdateDetail

        The model defined in huaweicloud sdk

        :param twin: 终端设备动态属性
        :type twin: dict(str, ValueInTwin)
        :param property_visitors: 孪生属性配置，与access_protocol关联。
        :type property_visitors: dict(str, ValueInPropertyVisitors)
        """
        
        

        self._twin = None
        self._property_visitors = None
        self.discriminator = None

        if twin is not None:
            self.twin = twin
        if property_visitors is not None:
            self.property_visitors = property_visitors

    @property
    def twin(self):
        r"""Gets the twin of this TwinUpdateDetail.

        终端设备动态属性

        :return: The twin of this TwinUpdateDetail.
        :rtype: dict(str, ValueInTwin)
        """
        return self._twin

    @twin.setter
    def twin(self, twin):
        r"""Sets the twin of this TwinUpdateDetail.

        终端设备动态属性

        :param twin: The twin of this TwinUpdateDetail.
        :type twin: dict(str, ValueInTwin)
        """
        self._twin = twin

    @property
    def property_visitors(self):
        r"""Gets the property_visitors of this TwinUpdateDetail.

        孪生属性配置，与access_protocol关联。

        :return: The property_visitors of this TwinUpdateDetail.
        :rtype: dict(str, ValueInPropertyVisitors)
        """
        return self._property_visitors

    @property_visitors.setter
    def property_visitors(self, property_visitors):
        r"""Sets the property_visitors of this TwinUpdateDetail.

        孪生属性配置，与access_protocol关联。

        :param property_visitors: The property_visitors of this TwinUpdateDetail.
        :type property_visitors: dict(str, ValueInPropertyVisitors)
        """
        self._property_visitors = property_visitors

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
        if not isinstance(other, TwinUpdateDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
