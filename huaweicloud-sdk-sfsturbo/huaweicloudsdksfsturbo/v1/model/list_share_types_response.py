# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShareTypesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_types': 'list[ShareTypeResponseBody]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'share_types': 'share_types',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, share_types=None, x_request_id=None):
        r"""ListShareTypesResponse

        The model defined in huaweicloud sdk

        :param share_types: 文件系统类型和配额列表
        :type share_types: list[:class:`huaweicloudsdksfsturbo.v1.ShareTypeResponseBody`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListShareTypesResponse, self).__init__()

        self._share_types = None
        self._x_request_id = None
        self.discriminator = None

        if share_types is not None:
            self.share_types = share_types
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def share_types(self):
        r"""Gets the share_types of this ListShareTypesResponse.

        文件系统类型和配额列表

        :return: The share_types of this ListShareTypesResponse.
        :rtype: list[:class:`huaweicloudsdksfsturbo.v1.ShareTypeResponseBody`]
        """
        return self._share_types

    @share_types.setter
    def share_types(self, share_types):
        r"""Sets the share_types of this ListShareTypesResponse.

        文件系统类型和配额列表

        :param share_types: The share_types of this ListShareTypesResponse.
        :type share_types: list[:class:`huaweicloudsdksfsturbo.v1.ShareTypeResponseBody`]
        """
        self._share_types = share_types

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListShareTypesResponse.

        :return: The x_request_id of this ListShareTypesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListShareTypesResponse.

        :param x_request_id: The x_request_id of this ListShareTypesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListShareTypesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
