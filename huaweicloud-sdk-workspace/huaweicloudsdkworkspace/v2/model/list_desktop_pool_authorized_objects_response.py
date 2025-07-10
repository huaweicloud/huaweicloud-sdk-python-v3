# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopPoolAuthorizedObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'objects': 'list[AuthorizedObjects]',
        'total_count': 'int'
    }

    attribute_map = {
        'objects': 'objects',
        'total_count': 'total_count'
    }

    def __init__(self, objects=None, total_count=None):
        r"""ListDesktopPoolAuthorizedObjectsResponse

        The model defined in huaweicloud sdk

        :param objects: 授权对象。
        :type objects: list[:class:`huaweicloudsdkworkspace.v2.AuthorizedObjects`]
        :param total_count: 满足条件的用户、用户组总数。
        :type total_count: int
        """
        
        super(ListDesktopPoolAuthorizedObjectsResponse, self).__init__()

        self._objects = None
        self._total_count = None
        self.discriminator = None

        if objects is not None:
            self.objects = objects
        if total_count is not None:
            self.total_count = total_count

    @property
    def objects(self):
        r"""Gets the objects of this ListDesktopPoolAuthorizedObjectsResponse.

        授权对象。

        :return: The objects of this ListDesktopPoolAuthorizedObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AuthorizedObjects`]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        r"""Sets the objects of this ListDesktopPoolAuthorizedObjectsResponse.

        授权对象。

        :param objects: The objects of this ListDesktopPoolAuthorizedObjectsResponse.
        :type objects: list[:class:`huaweicloudsdkworkspace.v2.AuthorizedObjects`]
        """
        self._objects = objects

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDesktopPoolAuthorizedObjectsResponse.

        满足条件的用户、用户组总数。

        :return: The total_count of this ListDesktopPoolAuthorizedObjectsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDesktopPoolAuthorizedObjectsResponse.

        满足条件的用户、用户组总数。

        :param total_count: The total_count of this ListDesktopPoolAuthorizedObjectsResponse.
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
        if not isinstance(other, ListDesktopPoolAuthorizedObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
