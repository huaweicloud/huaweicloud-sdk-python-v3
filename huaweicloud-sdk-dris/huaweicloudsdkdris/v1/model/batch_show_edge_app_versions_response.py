# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowEdgeAppVersionsResponse(SdkResponse):

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
        'versions': 'list[QueryEdgeAppVersionBriefResponseDTO]'
    }

    attribute_map = {
        'count': 'count',
        'versions': 'versions'
    }

    def __init__(self, count=None, versions=None):
        r"""BatchShowEdgeAppVersionsResponse

        The model defined in huaweicloud sdk

        :param count: **参数说明**：总记录数。
        :type count: int
        :param versions: **参数说明**：列举每条记录。
        :type versions: list[:class:`huaweicloudsdkdris.v1.QueryEdgeAppVersionBriefResponseDTO`]
        """
        
        super(BatchShowEdgeAppVersionsResponse, self).__init__()

        self._count = None
        self._versions = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if versions is not None:
            self.versions = versions

    @property
    def count(self):
        r"""Gets the count of this BatchShowEdgeAppVersionsResponse.

        **参数说明**：总记录数。

        :return: The count of this BatchShowEdgeAppVersionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this BatchShowEdgeAppVersionsResponse.

        **参数说明**：总记录数。

        :param count: The count of this BatchShowEdgeAppVersionsResponse.
        :type count: int
        """
        self._count = count

    @property
    def versions(self):
        r"""Gets the versions of this BatchShowEdgeAppVersionsResponse.

        **参数说明**：列举每条记录。

        :return: The versions of this BatchShowEdgeAppVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.QueryEdgeAppVersionBriefResponseDTO`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this BatchShowEdgeAppVersionsResponse.

        **参数说明**：列举每条记录。

        :param versions: The versions of this BatchShowEdgeAppVersionsResponse.
        :type versions: list[:class:`huaweicloudsdkdris.v1.QueryEdgeAppVersionBriefResponseDTO`]
        """
        self._versions = versions

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
        if not isinstance(other, BatchShowEdgeAppVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
