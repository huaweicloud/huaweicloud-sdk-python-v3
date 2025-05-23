# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSharedReposDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'list[ShowReposResp]',
        'content_range': 'str'
    }

    attribute_map = {
        'body': 'body',
        'content_range': 'Content-Range'
    }

    def __init__(self, body=None, content_range=None):
        r"""ListSharedReposDetailsResponse

        The model defined in huaweicloud sdk

        :param body: 
        :type body: list[:class:`huaweicloudsdkswr.v2.ShowReposResp`]
        :param content_range: 
        :type content_range: str
        """
        
        super(ListSharedReposDetailsResponse, self).__init__()

        self._body = None
        self._content_range = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if content_range is not None:
            self.content_range = content_range

    @property
    def body(self):
        r"""Gets the body of this ListSharedReposDetailsResponse.

        :return: The body of this ListSharedReposDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.ShowReposResp`]
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListSharedReposDetailsResponse.

        :param body: The body of this ListSharedReposDetailsResponse.
        :type body: list[:class:`huaweicloudsdkswr.v2.ShowReposResp`]
        """
        self._body = body

    @property
    def content_range(self):
        r"""Gets the content_range of this ListSharedReposDetailsResponse.

        :return: The content_range of this ListSharedReposDetailsResponse.
        :rtype: str
        """
        return self._content_range

    @content_range.setter
    def content_range(self, content_range):
        r"""Sets the content_range of this ListSharedReposDetailsResponse.

        :param content_range: The content_range of this ListSharedReposDetailsResponse.
        :type content_range: str
        """
        self._content_range = content_range

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
        if not isinstance(other, ListSharedReposDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
