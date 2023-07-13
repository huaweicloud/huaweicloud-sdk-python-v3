# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicIpsResponse(SdkResponse):

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
        'publicips': 'list[PublicIp]'
    }

    attribute_map = {
        'count': 'count',
        'publicips': 'publicips'
    }

    def __init__(self, count=None, publicips=None):
        """ListPublicIpsResponse

        The model defined in huaweicloud sdk

        :param count: 弹性公网IP数目。
        :type count: int
        :param publicips: 弹性公网IP数组对象。
        :type publicips: list[:class:`huaweicloudsdkiec.v1.PublicIp`]
        """
        
        super(ListPublicIpsResponse, self).__init__()

        self._count = None
        self._publicips = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if publicips is not None:
            self.publicips = publicips

    @property
    def count(self):
        """Gets the count of this ListPublicIpsResponse.

        弹性公网IP数目。

        :return: The count of this ListPublicIpsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListPublicIpsResponse.

        弹性公网IP数目。

        :param count: The count of this ListPublicIpsResponse.
        :type count: int
        """
        self._count = count

    @property
    def publicips(self):
        """Gets the publicips of this ListPublicIpsResponse.

        弹性公网IP数组对象。

        :return: The publicips of this ListPublicIpsResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.PublicIp`]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        """Sets the publicips of this ListPublicIpsResponse.

        弹性公网IP数组对象。

        :param publicips: The publicips of this ListPublicIpsResponse.
        :type publicips: list[:class:`huaweicloudsdkiec.v1.PublicIp`]
        """
        self._publicips = publicips

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
        if not isinstance(other, ListPublicIpsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
