# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicBorderGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_border_groups': 'list[CommonPoolsWithBorderGroupDict]',
        'request_id': 'str'
    }

    attribute_map = {
        'public_border_groups': 'public_border_groups',
        'request_id': 'request_id'
    }

    def __init__(self, public_border_groups=None, request_id=None):
        r"""ListPublicBorderGroupsResponse

        The model defined in huaweicloud sdk

        :param public_border_groups: 功能说明：公共池分组对象
        :type public_border_groups: list[:class:`huaweicloudsdkeip.v3.CommonPoolsWithBorderGroupDict`]
        :param request_id: 本次请求的编号
        :type request_id: str
        """
        
        super(ListPublicBorderGroupsResponse, self).__init__()

        self._public_border_groups = None
        self._request_id = None
        self.discriminator = None

        if public_border_groups is not None:
            self.public_border_groups = public_border_groups
        if request_id is not None:
            self.request_id = request_id

    @property
    def public_border_groups(self):
        r"""Gets the public_border_groups of this ListPublicBorderGroupsResponse.

        功能说明：公共池分组对象

        :return: The public_border_groups of this ListPublicBorderGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v3.CommonPoolsWithBorderGroupDict`]
        """
        return self._public_border_groups

    @public_border_groups.setter
    def public_border_groups(self, public_border_groups):
        r"""Sets the public_border_groups of this ListPublicBorderGroupsResponse.

        功能说明：公共池分组对象

        :param public_border_groups: The public_border_groups of this ListPublicBorderGroupsResponse.
        :type public_border_groups: list[:class:`huaweicloudsdkeip.v3.CommonPoolsWithBorderGroupDict`]
        """
        self._public_border_groups = public_border_groups

    @property
    def request_id(self):
        r"""Gets the request_id of this ListPublicBorderGroupsResponse.

        本次请求的编号

        :return: The request_id of this ListPublicBorderGroupsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListPublicBorderGroupsResponse.

        本次请求的编号

        :param request_id: The request_id of this ListPublicBorderGroupsResponse.
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
        if not isinstance(other, ListPublicBorderGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
