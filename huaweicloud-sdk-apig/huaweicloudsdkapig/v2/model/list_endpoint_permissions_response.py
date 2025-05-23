# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointPermissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'permissions': 'list[EndpointPermission]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'permissions': 'permissions',
        'x_request_id': 'x-request-id'
    }

    def __init__(self, size=None, total=None, permissions=None, x_request_id=None):
        r"""ListEndpointPermissionsResponse

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param permissions: 白名单记录列表
        :type permissions: list[:class:`huaweicloudsdkapig.v2.EndpointPermission`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListEndpointPermissionsResponse, self).__init__()

        self._size = None
        self._total = None
        self._permissions = None
        self._x_request_id = None
        self.discriminator = None

        self.size = size
        self.total = total
        if permissions is not None:
            self.permissions = permissions
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def size(self):
        r"""Gets the size of this ListEndpointPermissionsResponse.

        本次返回的列表长度

        :return: The size of this ListEndpointPermissionsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListEndpointPermissionsResponse.

        本次返回的列表长度

        :param size: The size of this ListEndpointPermissionsResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListEndpointPermissionsResponse.

        满足条件的记录数

        :return: The total of this ListEndpointPermissionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListEndpointPermissionsResponse.

        满足条件的记录数

        :param total: The total of this ListEndpointPermissionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def permissions(self):
        r"""Gets the permissions of this ListEndpointPermissionsResponse.

        白名单记录列表

        :return: The permissions of this ListEndpointPermissionsResponse.
        :rtype: list[:class:`huaweicloudsdkapig.v2.EndpointPermission`]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this ListEndpointPermissionsResponse.

        白名单记录列表

        :param permissions: The permissions of this ListEndpointPermissionsResponse.
        :type permissions: list[:class:`huaweicloudsdkapig.v2.EndpointPermission`]
        """
        self._permissions = permissions

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListEndpointPermissionsResponse.

        :return: The x_request_id of this ListEndpointPermissionsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListEndpointPermissionsResponse.

        :param x_request_id: The x_request_id of this ListEndpointPermissionsResponse.
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
        if not isinstance(other, ListEndpointPermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
