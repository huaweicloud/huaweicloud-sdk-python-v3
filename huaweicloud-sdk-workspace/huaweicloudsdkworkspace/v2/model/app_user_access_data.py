# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppUserAccessData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'access_failed_count': 'int',
        'last_access_failed_time': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'username': 'username',
        'access_failed_count': 'access_failed_count',
        'last_access_failed_time': 'last_access_failed_time',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, username=None, access_failed_count=None, last_access_failed_time=None, error_code=None, error_msg=None):
        r"""AppUserAccessData

        The model defined in huaweicloud sdk

        :param username: 用户名称。
        :type username: str
        :param access_failed_count: 接入失败数。
        :type access_failed_count: int
        :param last_access_failed_time: 最近一次接入失败时间，UTC时间，格式为：2022-05-11T11:45:42Z。
        :type last_access_failed_time: str
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误信息。
        :type error_msg: str
        """
        
        

        self._username = None
        self._access_failed_count = None
        self._last_access_failed_time = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if access_failed_count is not None:
            self.access_failed_count = access_failed_count
        if last_access_failed_time is not None:
            self.last_access_failed_time = last_access_failed_time
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def username(self):
        r"""Gets the username of this AppUserAccessData.

        用户名称。

        :return: The username of this AppUserAccessData.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this AppUserAccessData.

        用户名称。

        :param username: The username of this AppUserAccessData.
        :type username: str
        """
        self._username = username

    @property
    def access_failed_count(self):
        r"""Gets the access_failed_count of this AppUserAccessData.

        接入失败数。

        :return: The access_failed_count of this AppUserAccessData.
        :rtype: int
        """
        return self._access_failed_count

    @access_failed_count.setter
    def access_failed_count(self, access_failed_count):
        r"""Sets the access_failed_count of this AppUserAccessData.

        接入失败数。

        :param access_failed_count: The access_failed_count of this AppUserAccessData.
        :type access_failed_count: int
        """
        self._access_failed_count = access_failed_count

    @property
    def last_access_failed_time(self):
        r"""Gets the last_access_failed_time of this AppUserAccessData.

        最近一次接入失败时间，UTC时间，格式为：2022-05-11T11:45:42Z。

        :return: The last_access_failed_time of this AppUserAccessData.
        :rtype: str
        """
        return self._last_access_failed_time

    @last_access_failed_time.setter
    def last_access_failed_time(self, last_access_failed_time):
        r"""Sets the last_access_failed_time of this AppUserAccessData.

        最近一次接入失败时间，UTC时间，格式为：2022-05-11T11:45:42Z。

        :param last_access_failed_time: The last_access_failed_time of this AppUserAccessData.
        :type last_access_failed_time: str
        """
        self._last_access_failed_time = last_access_failed_time

    @property
    def error_code(self):
        r"""Gets the error_code of this AppUserAccessData.

        错误码。

        :return: The error_code of this AppUserAccessData.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this AppUserAccessData.

        错误码。

        :param error_code: The error_code of this AppUserAccessData.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this AppUserAccessData.

        错误信息。

        :return: The error_msg of this AppUserAccessData.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this AppUserAccessData.

        错误信息。

        :param error_msg: The error_msg of this AppUserAccessData.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, AppUserAccessData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
