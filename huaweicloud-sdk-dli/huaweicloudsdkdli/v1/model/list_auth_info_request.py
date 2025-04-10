# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuthInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_info_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'auth_info_name': 'auth_info_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, auth_info_name=None, offset=None, limit=None):
        r"""ListAuthInfoRequest

        The model defined in huaweicloud sdk

        :param auth_info_name: 认证信息名称
        :type auth_info_name: str
        :param offset: 默认为0
        :type offset: int
        :param limit: 默认为100
        :type limit: int
        """
        
        

        self._auth_info_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if auth_info_name is not None:
            self.auth_info_name = auth_info_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def auth_info_name(self):
        r"""Gets the auth_info_name of this ListAuthInfoRequest.

        认证信息名称

        :return: The auth_info_name of this ListAuthInfoRequest.
        :rtype: str
        """
        return self._auth_info_name

    @auth_info_name.setter
    def auth_info_name(self, auth_info_name):
        r"""Sets the auth_info_name of this ListAuthInfoRequest.

        认证信息名称

        :param auth_info_name: The auth_info_name of this ListAuthInfoRequest.
        :type auth_info_name: str
        """
        self._auth_info_name = auth_info_name

    @property
    def offset(self):
        r"""Gets the offset of this ListAuthInfoRequest.

        默认为0

        :return: The offset of this ListAuthInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAuthInfoRequest.

        默认为0

        :param offset: The offset of this ListAuthInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAuthInfoRequest.

        默认为100

        :return: The limit of this ListAuthInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAuthInfoRequest.

        默认为100

        :param limit: The limit of this ListAuthInfoRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAuthInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
