# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[ListTag]',
        'request_id': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'tags': 'tags',
        'request_id': 'request_id',
        'total_count': 'total_count'
    }

    def __init__(self, tags=None, request_id=None, total_count=None):
        r"""ListPortTagsResponse

        The model defined in huaweicloud sdk

        :param tags: tag对象列表
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ListTag`]
        :param request_id: 请求ID
        :type request_id: str
        :param total_count: 资源数量
        :type total_count: int
        """
        
        super(ListPortTagsResponse, self).__init__()

        self._tags = None
        self._request_id = None
        self._total_count = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if request_id is not None:
            self.request_id = request_id
        if total_count is not None:
            self.total_count = total_count

    @property
    def tags(self):
        r"""Gets the tags of this ListPortTagsResponse.

        tag对象列表

        :return: The tags of this ListPortTagsResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.ListTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListPortTagsResponse.

        tag对象列表

        :param tags: The tags of this ListPortTagsResponse.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ListTag`]
        """
        self._tags = tags

    @property
    def request_id(self):
        r"""Gets the request_id of this ListPortTagsResponse.

        请求ID

        :return: The request_id of this ListPortTagsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListPortTagsResponse.

        请求ID

        :param request_id: The request_id of this ListPortTagsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def total_count(self):
        r"""Gets the total_count of this ListPortTagsResponse.

        资源数量

        :return: The total_count of this ListPortTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListPortTagsResponse.

        资源数量

        :param total_count: The total_count of this ListPortTagsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListPortTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
