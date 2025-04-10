# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateNatTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'tags': 'list[Tags]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'tags': 'tags'
    }

    def __init__(self, request_id=None, tags=None):
        r"""ListPrivateNatTagsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求id。
        :type request_id: str
        :param tags: 标签。
        :type tags: list[:class:`huaweicloudsdknat.v2.Tags`]
        """
        
        super(ListPrivateNatTagsResponse, self).__init__()

        self._request_id = None
        self._tags = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if tags is not None:
            self.tags = tags

    @property
    def request_id(self):
        r"""Gets the request_id of this ListPrivateNatTagsResponse.

        请求id。

        :return: The request_id of this ListPrivateNatTagsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListPrivateNatTagsResponse.

        请求id。

        :param request_id: The request_id of this ListPrivateNatTagsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def tags(self):
        r"""Gets the tags of this ListPrivateNatTagsResponse.

        标签。

        :return: The tags of this ListPrivateNatTagsResponse.
        :rtype: list[:class:`huaweicloudsdknat.v2.Tags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListPrivateNatTagsResponse.

        标签。

        :param tags: The tags of this ListPrivateNatTagsResponse.
        :type tags: list[:class:`huaweicloudsdknat.v2.Tags`]
        """
        self._tags = tags

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
        if not isinstance(other, ListPrivateNatTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
