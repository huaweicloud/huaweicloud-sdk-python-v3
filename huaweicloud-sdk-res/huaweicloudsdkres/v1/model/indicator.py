# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Indicator:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'indicator_name': 'str',
        'indicator_params': 'IndicatorParam'
    }

    attribute_map = {
        'indicator_name': 'indicator_name',
        'indicator_params': 'indicator_params'
    }

    def __init__(self, indicator_name=None, indicator_params=None):
        """Indicator

        The model defined in huaweicloud sdk

        :param indicator_name: 指标名称： - clickPVRate，点击PV率 - clickUVRate，点击UV率 - customize，自定义
        :type indicator_name: str
        :param indicator_params: 
        :type indicator_params: :class:`huaweicloudsdkres.v1.IndicatorParam`
        """
        
        

        self._indicator_name = None
        self._indicator_params = None
        self.discriminator = None

        if indicator_name is not None:
            self.indicator_name = indicator_name
        if indicator_params is not None:
            self.indicator_params = indicator_params

    @property
    def indicator_name(self):
        """Gets the indicator_name of this Indicator.

        指标名称： - clickPVRate，点击PV率 - clickUVRate，点击UV率 - customize，自定义

        :return: The indicator_name of this Indicator.
        :rtype: str
        """
        return self._indicator_name

    @indicator_name.setter
    def indicator_name(self, indicator_name):
        """Sets the indicator_name of this Indicator.

        指标名称： - clickPVRate，点击PV率 - clickUVRate，点击UV率 - customize，自定义

        :param indicator_name: The indicator_name of this Indicator.
        :type indicator_name: str
        """
        self._indicator_name = indicator_name

    @property
    def indicator_params(self):
        """Gets the indicator_params of this Indicator.


        :return: The indicator_params of this Indicator.
        :rtype: :class:`huaweicloudsdkres.v1.IndicatorParam`
        """
        return self._indicator_params

    @indicator_params.setter
    def indicator_params(self, indicator_params):
        """Sets the indicator_params of this Indicator.


        :param indicator_params: The indicator_params of this Indicator.
        :type indicator_params: :class:`huaweicloudsdkres.v1.IndicatorParam`
        """
        self._indicator_params = indicator_params

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
        if not isinstance(other, Indicator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
