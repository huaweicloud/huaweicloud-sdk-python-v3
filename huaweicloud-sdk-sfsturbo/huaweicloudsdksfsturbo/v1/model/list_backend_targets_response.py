# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackendTargetsResponse(SdkResponse):

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
        'targets': 'list[ShowBackendTargetInfoResponseBody]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'targets': 'targets',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, count=None, targets=None, x_request_id=None):
        r"""ListBackendTargetsResponse

        The model defined in huaweicloud sdk

        :param count: 后端存储列表个数
        :type count: int
        :param targets: 后端存储列表
        :type targets: list[:class:`huaweicloudsdksfsturbo.v1.ShowBackendTargetInfoResponseBody`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListBackendTargetsResponse, self).__init__()

        self._count = None
        self._targets = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if targets is not None:
            self.targets = targets
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        r"""Gets the count of this ListBackendTargetsResponse.

        后端存储列表个数

        :return: The count of this ListBackendTargetsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListBackendTargetsResponse.

        后端存储列表个数

        :param count: The count of this ListBackendTargetsResponse.
        :type count: int
        """
        self._count = count

    @property
    def targets(self):
        r"""Gets the targets of this ListBackendTargetsResponse.

        后端存储列表

        :return: The targets of this ListBackendTargetsResponse.
        :rtype: list[:class:`huaweicloudsdksfsturbo.v1.ShowBackendTargetInfoResponseBody`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this ListBackendTargetsResponse.

        后端存储列表

        :param targets: The targets of this ListBackendTargetsResponse.
        :type targets: list[:class:`huaweicloudsdksfsturbo.v1.ShowBackendTargetInfoResponseBody`]
        """
        self._targets = targets

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListBackendTargetsResponse.

        :return: The x_request_id of this ListBackendTargetsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListBackendTargetsResponse.

        :param x_request_id: The x_request_id of this ListBackendTargetsResponse.
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
        if not isinstance(other, ListBackendTargetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
