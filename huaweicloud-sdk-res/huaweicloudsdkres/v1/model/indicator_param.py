# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndicatorParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customize_parameter': 'CustomizeParameter',
        'customize_formula': 'CustomizeFormula'
    }

    attribute_map = {
        'customize_parameter': 'customize_parameter',
        'customize_formula': 'customize_formula'
    }

    def __init__(self, customize_parameter=None, customize_formula=None):
        """IndicatorParam

        The model defined in huaweicloud sdk

        :param customize_parameter: 
        :type customize_parameter: :class:`huaweicloudsdkres.v1.CustomizeParameter`
        :param customize_formula: 
        :type customize_formula: :class:`huaweicloudsdkres.v1.CustomizeFormula`
        """
        
        

        self._customize_parameter = None
        self._customize_formula = None
        self.discriminator = None

        if customize_parameter is not None:
            self.customize_parameter = customize_parameter
        if customize_formula is not None:
            self.customize_formula = customize_formula

    @property
    def customize_parameter(self):
        """Gets the customize_parameter of this IndicatorParam.


        :return: The customize_parameter of this IndicatorParam.
        :rtype: :class:`huaweicloudsdkres.v1.CustomizeParameter`
        """
        return self._customize_parameter

    @customize_parameter.setter
    def customize_parameter(self, customize_parameter):
        """Sets the customize_parameter of this IndicatorParam.


        :param customize_parameter: The customize_parameter of this IndicatorParam.
        :type customize_parameter: :class:`huaweicloudsdkres.v1.CustomizeParameter`
        """
        self._customize_parameter = customize_parameter

    @property
    def customize_formula(self):
        """Gets the customize_formula of this IndicatorParam.


        :return: The customize_formula of this IndicatorParam.
        :rtype: :class:`huaweicloudsdkres.v1.CustomizeFormula`
        """
        return self._customize_formula

    @customize_formula.setter
    def customize_formula(self, customize_formula):
        """Sets the customize_formula of this IndicatorParam.


        :param customize_formula: The customize_formula of this IndicatorParam.
        :type customize_formula: :class:`huaweicloudsdkres.v1.CustomizeFormula`
        """
        self._customize_formula = customize_formula

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
        if not isinstance(other, IndicatorParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
