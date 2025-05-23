# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'params': 'PipelineSourceParam'
    }

    attribute_map = {
        'type': 'type',
        'params': 'params'
    }

    def __init__(self, type=None, params=None):
        r"""PipelineSource

        The model defined in huaweicloud sdk

        :param type: 流水线源类型
        :type type: str
        :param params: 
        :type params: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineSourceParam`
        """
        
        

        self._type = None
        self._params = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if params is not None:
            self.params = params

    @property
    def type(self):
        r"""Gets the type of this PipelineSource.

        流水线源类型

        :return: The type of this PipelineSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PipelineSource.

        流水线源类型

        :param type: The type of this PipelineSource.
        :type type: str
        """
        self._type = type

    @property
    def params(self):
        r"""Gets the params of this PipelineSource.

        :return: The params of this PipelineSource.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineSourceParam`
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this PipelineSource.

        :param params: The params of this PipelineSource.
        :type params: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineSourceParam`
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
        if not isinstance(other, PipelineSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
