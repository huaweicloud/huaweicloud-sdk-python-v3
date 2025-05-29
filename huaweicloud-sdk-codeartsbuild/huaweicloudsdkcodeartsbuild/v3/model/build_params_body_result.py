# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildParamsBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_parameters': 'list[BuildParams]'
    }

    attribute_map = {
        'build_parameters': 'build_parameters'
    }

    def __init__(self, build_parameters=None):
        r"""BuildParamsBodyResult

        The model defined in huaweicloud sdk

        :param build_parameters: 构建参数约束列表
        :type build_parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.BuildParams`]
        """
        
        

        self._build_parameters = None
        self.discriminator = None

        if build_parameters is not None:
            self.build_parameters = build_parameters

    @property
    def build_parameters(self):
        r"""Gets the build_parameters of this BuildParamsBodyResult.

        构建参数约束列表

        :return: The build_parameters of this BuildParamsBodyResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.BuildParams`]
        """
        return self._build_parameters

    @build_parameters.setter
    def build_parameters(self, build_parameters):
        r"""Sets the build_parameters of this BuildParamsBodyResult.

        构建参数约束列表

        :param build_parameters: The build_parameters of this BuildParamsBodyResult.
        :type build_parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.BuildParams`]
        """
        self._build_parameters = build_parameters

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
        if not isinstance(other, BuildParamsBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
