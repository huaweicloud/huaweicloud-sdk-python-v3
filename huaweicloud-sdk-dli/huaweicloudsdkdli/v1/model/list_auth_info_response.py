# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuthInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'count': 'int',
        'auth_infos': 'list[AuthInfo]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'count': 'count',
        'auth_infos': 'auth_infos'
    }

    def __init__(self, is_success=None, message=None, count=None, auth_infos=None):
        """ListAuthInfoResponse

        The model defined in huaweicloud sdk

        :param is_success: 是否成功
        :type is_success: bool
        :param message: 请求消息
        :type message: str
        :param count: 认证信息个数
        :type count: int
        :param auth_infos: 认证信息列表
        :type auth_infos: list[:class:`huaweicloudsdkdli.v1.AuthInfo`]
        """
        
        super(ListAuthInfoResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._count = None
        self._auth_infos = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if count is not None:
            self.count = count
        if auth_infos is not None:
            self.auth_infos = auth_infos

    @property
    def is_success(self):
        """Gets the is_success of this ListAuthInfoResponse.

        是否成功

        :return: The is_success of this ListAuthInfoResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListAuthInfoResponse.

        是否成功

        :param is_success: The is_success of this ListAuthInfoResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListAuthInfoResponse.

        请求消息

        :return: The message of this ListAuthInfoResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListAuthInfoResponse.

        请求消息

        :param message: The message of this ListAuthInfoResponse.
        :type message: str
        """
        self._message = message

    @property
    def count(self):
        """Gets the count of this ListAuthInfoResponse.

        认证信息个数

        :return: The count of this ListAuthInfoResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAuthInfoResponse.

        认证信息个数

        :param count: The count of this ListAuthInfoResponse.
        :type count: int
        """
        self._count = count

    @property
    def auth_infos(self):
        """Gets the auth_infos of this ListAuthInfoResponse.

        认证信息列表

        :return: The auth_infos of this ListAuthInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.AuthInfo`]
        """
        return self._auth_infos

    @auth_infos.setter
    def auth_infos(self, auth_infos):
        """Sets the auth_infos of this ListAuthInfoResponse.

        认证信息列表

        :param auth_infos: The auth_infos of this ListAuthInfoResponse.
        :type auth_infos: list[:class:`huaweicloudsdkdli.v1.AuthInfo`]
        """
        self._auth_infos = auth_infos

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
        if not isinstance(other, ListAuthInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
