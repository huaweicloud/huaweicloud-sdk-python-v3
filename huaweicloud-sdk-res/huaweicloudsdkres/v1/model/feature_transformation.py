# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FeatureTransformation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attr': 'Attribute',
        'discrete_method': 'str',
        'params': 'object'
    }

    attribute_map = {
        'attr': 'attr',
        'discrete_method': 'discrete_method',
        'params': 'params'
    }

    def __init__(self, attr=None, discrete_method=None, params=None):
        r"""FeatureTransformation

        The model defined in huaweicloud sdk

        :param attr: 
        :type attr: :class:`huaweicloudsdkres.v1.Attribute`
        :param discrete_method: 离散方法： - equal_distance_discrete，等距离散 - user_define_discrete，自定义离散 - normalize，归一化 - null，不离散 
        :type discrete_method: str
        :param params: 具体处理参数。
        :type params: object
        """
        
        

        self._attr = None
        self._discrete_method = None
        self._params = None
        self.discriminator = None

        if attr is not None:
            self.attr = attr
        if discrete_method is not None:
            self.discrete_method = discrete_method
        if params is not None:
            self.params = params

    @property
    def attr(self):
        r"""Gets the attr of this FeatureTransformation.

        :return: The attr of this FeatureTransformation.
        :rtype: :class:`huaweicloudsdkres.v1.Attribute`
        """
        return self._attr

    @attr.setter
    def attr(self, attr):
        r"""Sets the attr of this FeatureTransformation.

        :param attr: The attr of this FeatureTransformation.
        :type attr: :class:`huaweicloudsdkres.v1.Attribute`
        """
        self._attr = attr

    @property
    def discrete_method(self):
        r"""Gets the discrete_method of this FeatureTransformation.

        离散方法： - equal_distance_discrete，等距离散 - user_define_discrete，自定义离散 - normalize，归一化 - null，不离散 

        :return: The discrete_method of this FeatureTransformation.
        :rtype: str
        """
        return self._discrete_method

    @discrete_method.setter
    def discrete_method(self, discrete_method):
        r"""Sets the discrete_method of this FeatureTransformation.

        离散方法： - equal_distance_discrete，等距离散 - user_define_discrete，自定义离散 - normalize，归一化 - null，不离散 

        :param discrete_method: The discrete_method of this FeatureTransformation.
        :type discrete_method: str
        """
        self._discrete_method = discrete_method

    @property
    def params(self):
        r"""Gets the params of this FeatureTransformation.

        具体处理参数。

        :return: The params of this FeatureTransformation.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this FeatureTransformation.

        具体处理参数。

        :param params: The params of this FeatureTransformation.
        :type params: object
        """
        self._params = params

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
        if not isinstance(other, FeatureTransformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
