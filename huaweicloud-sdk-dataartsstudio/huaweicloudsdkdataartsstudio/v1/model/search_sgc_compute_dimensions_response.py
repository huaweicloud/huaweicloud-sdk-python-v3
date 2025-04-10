# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchSgcComputeDimensionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'computes': 'list[ComputeDimension]'
    }

    attribute_map = {
        'count': 'count',
        'computes': 'computes'
    }

    def __init__(self, count=None, computes=None):
        r"""SearchSgcComputeDimensionsResponse

        The model defined in huaweicloud sdk

        :param count: 总数
        :type count: int
        :param computes: 计算成本实例列表
        :type computes: list[:class:`huaweicloudsdkdataartsstudio.v1.ComputeDimension`]
        """
        
        super(SearchSgcComputeDimensionsResponse, self).__init__()

        self._count = None
        self._computes = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if computes is not None:
            self.computes = computes

    @property
    def count(self):
        r"""Gets the count of this SearchSgcComputeDimensionsResponse.

        总数

        :return: The count of this SearchSgcComputeDimensionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this SearchSgcComputeDimensionsResponse.

        总数

        :param count: The count of this SearchSgcComputeDimensionsResponse.
        :type count: int
        """
        self._count = count

    @property
    def computes(self):
        r"""Gets the computes of this SearchSgcComputeDimensionsResponse.

        计算成本实例列表

        :return: The computes of this SearchSgcComputeDimensionsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ComputeDimension`]
        """
        return self._computes

    @computes.setter
    def computes(self, computes):
        r"""Sets the computes of this SearchSgcComputeDimensionsResponse.

        计算成本实例列表

        :param computes: The computes of this SearchSgcComputeDimensionsResponse.
        :type computes: list[:class:`huaweicloudsdkdataartsstudio.v1.ComputeDimension`]
        """
        self._computes = computes

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
        if not isinstance(other, SearchSgcComputeDimensionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
