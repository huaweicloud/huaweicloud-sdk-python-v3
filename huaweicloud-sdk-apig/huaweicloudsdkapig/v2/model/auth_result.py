# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'error_msg': 'str',
        'error_code': 'str',
        'api_name': 'str',
        'app_name': 'str'
    }

    attribute_map = {
        'status': 'status',
        'error_msg': 'error_msg',
        'error_code': 'error_code',
        'api_name': 'api_name',
        'app_name': 'app_name'
    }

    def __init__(self, status=None, error_msg=None, error_code=None, api_name=None, app_name=None):
        """AuthResult

        The model defined in huaweicloud sdk

        :param status: 授权结果 - SUCCESS：授权成功 - SKIPPED：跳过 - FAILED：授权失败
        :type status: str
        :param error_msg: 授权失败错误信息
        :type error_msg: str
        :param error_code: 授权失败错误码
        :type error_code: str
        :param api_name: 授权失败的API名称
        :type api_name: str
        :param app_name: 授权失败的APP名称
        :type app_name: str
        """
        
        

        self._status = None
        self._error_msg = None
        self._error_code = None
        self._api_name = None
        self._app_name = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if error_msg is not None:
            self.error_msg = error_msg
        if error_code is not None:
            self.error_code = error_code
        if api_name is not None:
            self.api_name = api_name
        if app_name is not None:
            self.app_name = app_name

    @property
    def status(self):
        """Gets the status of this AuthResult.

        授权结果 - SUCCESS：授权成功 - SKIPPED：跳过 - FAILED：授权失败

        :return: The status of this AuthResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuthResult.

        授权结果 - SUCCESS：授权成功 - SKIPPED：跳过 - FAILED：授权失败

        :param status: The status of this AuthResult.
        :type status: str
        """
        self._status = status

    @property
    def error_msg(self):
        """Gets the error_msg of this AuthResult.

        授权失败错误信息

        :return: The error_msg of this AuthResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this AuthResult.

        授权失败错误信息

        :param error_msg: The error_msg of this AuthResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_code(self):
        """Gets the error_code of this AuthResult.

        授权失败错误码

        :return: The error_code of this AuthResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AuthResult.

        授权失败错误码

        :param error_code: The error_code of this AuthResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def api_name(self):
        """Gets the api_name of this AuthResult.

        授权失败的API名称

        :return: The api_name of this AuthResult.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this AuthResult.

        授权失败的API名称

        :param api_name: The api_name of this AuthResult.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def app_name(self):
        """Gets the app_name of this AuthResult.

        授权失败的APP名称

        :return: The app_name of this AuthResult.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AuthResult.

        授权失败的APP名称

        :param app_name: The app_name of this AuthResult.
        :type app_name: str
        """
        self._app_name = app_name

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
        if not isinstance(other, AuthResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
