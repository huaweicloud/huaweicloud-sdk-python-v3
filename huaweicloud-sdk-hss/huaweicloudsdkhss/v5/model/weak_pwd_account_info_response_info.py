# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WeakPwdAccountInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'service_type': 'str',
        'duration': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'service_type': 'service_type',
        'duration': 'duration'
    }

    def __init__(self, user_name=None, service_type=None, duration=None):
        """WeakPwdAccountInfoResponseInfo

        The model defined in huaweicloud sdk

        :param user_name: 弱口令账号名称
        :type user_name: str
        :param service_type: 账号类型
        :type service_type: str
        :param duration: 弱口令使用时长，单位天
        :type duration: int
        """
        
        

        self._user_name = None
        self._service_type = None
        self._duration = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if service_type is not None:
            self.service_type = service_type
        if duration is not None:
            self.duration = duration

    @property
    def user_name(self):
        """Gets the user_name of this WeakPwdAccountInfoResponseInfo.

        弱口令账号名称

        :return: The user_name of this WeakPwdAccountInfoResponseInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this WeakPwdAccountInfoResponseInfo.

        弱口令账号名称

        :param user_name: The user_name of this WeakPwdAccountInfoResponseInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def service_type(self):
        """Gets the service_type of this WeakPwdAccountInfoResponseInfo.

        账号类型

        :return: The service_type of this WeakPwdAccountInfoResponseInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this WeakPwdAccountInfoResponseInfo.

        账号类型

        :param service_type: The service_type of this WeakPwdAccountInfoResponseInfo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def duration(self):
        """Gets the duration of this WeakPwdAccountInfoResponseInfo.

        弱口令使用时长，单位天

        :return: The duration of this WeakPwdAccountInfoResponseInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this WeakPwdAccountInfoResponseInfo.

        弱口令使用时长，单位天

        :param duration: The duration of this WeakPwdAccountInfoResponseInfo.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, WeakPwdAccountInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
