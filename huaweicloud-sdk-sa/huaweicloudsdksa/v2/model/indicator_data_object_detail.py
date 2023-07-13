# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndicatorDataObjectDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'indicator_type': 'CreateIndicatorDetailIndicatorType',
        'value': 'str'
    }

    attribute_map = {
        'indicator_type': 'indicator_type',
        'value': 'value'
    }

    def __init__(self, indicator_type=None, value=None):
        """IndicatorDataObjectDetail

        The model defined in huaweicloud sdk

        :param indicator_type: 
        :type indicator_type: :class:`huaweicloudsdksa.v2.CreateIndicatorDetailIndicatorType`
        :param value: 值，如：ip url domain等
        :type value: str
        """
        
        

        self._indicator_type = None
        self._value = None
        self.discriminator = None

        if indicator_type is not None:
            self.indicator_type = indicator_type
        if value is not None:
            self.value = value

    @property
    def indicator_type(self):
        """Gets the indicator_type of this IndicatorDataObjectDetail.

        :return: The indicator_type of this IndicatorDataObjectDetail.
        :rtype: :class:`huaweicloudsdksa.v2.CreateIndicatorDetailIndicatorType`
        """
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, indicator_type):
        """Sets the indicator_type of this IndicatorDataObjectDetail.

        :param indicator_type: The indicator_type of this IndicatorDataObjectDetail.
        :type indicator_type: :class:`huaweicloudsdksa.v2.CreateIndicatorDetailIndicatorType`
        """
        self._indicator_type = indicator_type

    @property
    def value(self):
        """Gets the value of this IndicatorDataObjectDetail.

        值，如：ip url domain等

        :return: The value of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IndicatorDataObjectDetail.

        值，如：ip url domain等

        :param value: The value of this IndicatorDataObjectDetail.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, IndicatorDataObjectDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
