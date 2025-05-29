# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Parameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'params': 'list[CreateBuildJobParameterParam]'
    }

    attribute_map = {
        'name': 'name',
        'params': 'params'
    }

    def __init__(self, name=None, params=None):
        r"""Parameter

        The model defined in huaweicloud sdk

        :param name: 参数定义名，默认为hudson.model.StringParameterDefinition
        :type name: str
        :param params: 构建执行参数子参数
        :type params: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameterParam`]
        """
        
        

        self._name = None
        self._params = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if params is not None:
            self.params = params

    @property
    def name(self):
        r"""Gets the name of this Parameter.

        参数定义名，默认为hudson.model.StringParameterDefinition

        :return: The name of this Parameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Parameter.

        参数定义名，默认为hudson.model.StringParameterDefinition

        :param name: The name of this Parameter.
        :type name: str
        """
        self._name = name

    @property
    def params(self):
        r"""Gets the params of this Parameter.

        构建执行参数子参数

        :return: The params of this Parameter.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameterParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this Parameter.

        构建执行参数子参数

        :param params: The params of this Parameter.
        :type params: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameterParam`]
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
        if not isinstance(other, Parameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
