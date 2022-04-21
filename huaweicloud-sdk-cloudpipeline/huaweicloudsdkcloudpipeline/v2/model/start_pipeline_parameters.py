# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartPipelineParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'build_params': 'list[StartPipelineBuildParams]'
    }

    attribute_map = {
        'build_params': 'build_params'
    }

    def __init__(self, build_params=None):
        """StartPipelineParameters

        The model defined in huaweicloud sdk

        :param build_params: 启动流水线时的构建参数
        :type build_params: list[:class:`huaweicloudsdkcloudpipeline.v2.StartPipelineBuildParams`]
        """
        
        

        self._build_params = None
        self.discriminator = None

        if build_params is not None:
            self.build_params = build_params

    @property
    def build_params(self):
        """Gets the build_params of this StartPipelineParameters.

        启动流水线时的构建参数

        :return: The build_params of this StartPipelineParameters.
        :rtype: list[:class:`huaweicloudsdkcloudpipeline.v2.StartPipelineBuildParams`]
        """
        return self._build_params

    @build_params.setter
    def build_params(self, build_params):
        """Sets the build_params of this StartPipelineParameters.

        启动流水线时的构建参数

        :param build_params: The build_params of this StartPipelineParameters.
        :type build_params: list[:class:`huaweicloudsdkcloudpipeline.v2.StartPipelineBuildParams`]
        """
        self._build_params = build_params

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
        if not isinstance(other, StartPipelineParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
