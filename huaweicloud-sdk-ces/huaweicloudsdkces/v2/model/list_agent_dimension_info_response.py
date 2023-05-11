# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentDimensionInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[AgentDimension]',
        'count': 'int'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'count': 'count'
    }

    def __init__(self, dimensions=None, count=None):
        """ListAgentDimensionInfoResponse

        The model defined in huaweicloud sdk

        :param dimensions: 维度信息
        :type dimensions: list[:class:`huaweicloudsdkces.v2.AgentDimension`]
        :param count: 维度信息总数
        :type count: int
        """
        
        super(ListAgentDimensionInfoResponse, self).__init__()

        self._dimensions = None
        self._count = None
        self.discriminator = None

        if dimensions is not None:
            self.dimensions = dimensions
        if count is not None:
            self.count = count

    @property
    def dimensions(self):
        """Gets the dimensions of this ListAgentDimensionInfoResponse.

        维度信息

        :return: The dimensions of this ListAgentDimensionInfoResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.AgentDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ListAgentDimensionInfoResponse.

        维度信息

        :param dimensions: The dimensions of this ListAgentDimensionInfoResponse.
        :type dimensions: list[:class:`huaweicloudsdkces.v2.AgentDimension`]
        """
        self._dimensions = dimensions

    @property
    def count(self):
        """Gets the count of this ListAgentDimensionInfoResponse.

        维度信息总数

        :return: The count of this ListAgentDimensionInfoResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAgentDimensionInfoResponse.

        维度信息总数

        :param count: The count of this ListAgentDimensionInfoResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListAgentDimensionInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
