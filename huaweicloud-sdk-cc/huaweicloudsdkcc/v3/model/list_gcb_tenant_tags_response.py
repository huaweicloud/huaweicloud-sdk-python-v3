# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGcbTenantTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TmsTagValues]',
        'total_count': 'int',
        'request_id': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'total_count': 'total_count',
        'request_id': 'request_id'
    }

    def __init__(self, tags=None, total_count=None, request_id=None):
        r"""ListGcbTenantTagsResponse

        The model defined in huaweicloud sdk

        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkcc.v3.TmsTagValues`]
        :param total_count: 总记录数。
        :type total_count: int
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ListGcbTenantTagsResponse, self).__init__()

        self._tags = None
        self._total_count = None
        self._request_id = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if total_count is not None:
            self.total_count = total_count
        if request_id is not None:
            self.request_id = request_id

    @property
    def tags(self):
        r"""Gets the tags of this ListGcbTenantTagsResponse.

        标签列表。

        :return: The tags of this ListGcbTenantTagsResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.TmsTagValues`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListGcbTenantTagsResponse.

        标签列表。

        :param tags: The tags of this ListGcbTenantTagsResponse.
        :type tags: list[:class:`huaweicloudsdkcc.v3.TmsTagValues`]
        """
        self._tags = tags

    @property
    def total_count(self):
        r"""Gets the total_count of this ListGcbTenantTagsResponse.

        总记录数。

        :return: The total_count of this ListGcbTenantTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListGcbTenantTagsResponse.

        总记录数。

        :param total_count: The total_count of this ListGcbTenantTagsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def request_id(self):
        r"""Gets the request_id of this ListGcbTenantTagsResponse.

        请求ID。

        :return: The request_id of this ListGcbTenantTagsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListGcbTenantTagsResponse.

        请求ID。

        :param request_id: The request_id of this ListGcbTenantTagsResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListGcbTenantTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
