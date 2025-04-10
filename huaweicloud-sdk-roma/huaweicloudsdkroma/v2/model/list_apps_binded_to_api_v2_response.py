# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppsBindedToApiV2Response(SdkResponse):

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
        'auths': 'list[ApiAuthInfo]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'auths': 'auths'
    }

    def __init__(self, size=None, total=None, auths=None):
        r"""ListAppsBindedToApiV2Response

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param auths: 本次返回的API列表
        :type auths: list[:class:`huaweicloudsdkroma.v2.ApiAuthInfo`]
        """
        
        super(ListAppsBindedToApiV2Response, self).__init__()

        self._size = None
        self._total = None
        self._auths = None
        self.discriminator = None

        self.size = size
        self.total = total
        if auths is not None:
            self.auths = auths

    @property
    def size(self):
        r"""Gets the size of this ListAppsBindedToApiV2Response.

        本次返回的列表长度

        :return: The size of this ListAppsBindedToApiV2Response.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListAppsBindedToApiV2Response.

        本次返回的列表长度

        :param size: The size of this ListAppsBindedToApiV2Response.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListAppsBindedToApiV2Response.

        满足条件的记录数

        :return: The total of this ListAppsBindedToApiV2Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAppsBindedToApiV2Response.

        满足条件的记录数

        :param total: The total of this ListAppsBindedToApiV2Response.
        :type total: int
        """
        self._total = total

    @property
    def auths(self):
        r"""Gets the auths of this ListAppsBindedToApiV2Response.

        本次返回的API列表

        :return: The auths of this ListAppsBindedToApiV2Response.
        :rtype: list[:class:`huaweicloudsdkroma.v2.ApiAuthInfo`]
        """
        return self._auths

    @auths.setter
    def auths(self, auths):
        r"""Sets the auths of this ListAppsBindedToApiV2Response.

        本次返回的API列表

        :param auths: The auths of this ListAppsBindedToApiV2Response.
        :type auths: list[:class:`huaweicloudsdkroma.v2.ApiAuthInfo`]
        """
        self._auths = auths

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
        if not isinstance(other, ListAppsBindedToApiV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
