# coding: utf-8

import pprint
import re

import six





class AuthResultResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'api_name': 'str',
        'app_name': 'str',
        'status': 'str',
        'error_msg': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'api_name': 'api_name',
        'app_name': 'app_name',
        'status': 'status',
        'error_msg': 'error_msg',
        'error_code': 'error_code'
    }

    def __init__(self, api_name=None, app_name=None, status=None, error_msg=None, error_code=None):
        """AuthResultResp - a model defined in huaweicloud sdk"""
        
        

        self._api_name = None
        self._app_name = None
        self._status = None
        self._error_msg = None
        self._error_code = None
        self.discriminator = None

        if api_name is not None:
            self.api_name = api_name
        if app_name is not None:
            self.app_name = app_name
        if status is not None:
            self.status = status
        if error_msg is not None:
            self.error_msg = error_msg
        if error_code is not None:
            self.error_code = error_code

    @property
    def api_name(self):
        """Gets the api_name of this AuthResultResp.

        API名称

        :return: The api_name of this AuthResultResp.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this AuthResultResp.

        API名称

        :param api_name: The api_name of this AuthResultResp.
        :type: str
        """
        self._api_name = api_name

    @property
    def app_name(self):
        """Gets the app_name of this AuthResultResp.

        APP名称

        :return: The app_name of this AuthResultResp.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AuthResultResp.

        APP名称

        :param app_name: The app_name of this AuthResultResp.
        :type: str
        """
        self._app_name = app_name

    @property
    def status(self):
        """Gets the status of this AuthResultResp.

        授权结果 - SUCCESS：授权成功 - SKIPPED：跳过 - FILAED：授权失败

        :return: The status of this AuthResultResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuthResultResp.

        授权结果 - SUCCESS：授权成功 - SKIPPED：跳过 - FILAED：授权失败

        :param status: The status of this AuthResultResp.
        :type: str
        """
        self._status = status

    @property
    def error_msg(self):
        """Gets the error_msg of this AuthResultResp.

        授权失败错误信息

        :return: The error_msg of this AuthResultResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this AuthResultResp.

        授权失败错误信息

        :param error_msg: The error_msg of this AuthResultResp.
        :type: str
        """
        self._error_msg = error_msg

    @property
    def error_code(self):
        """Gets the error_code of this AuthResultResp.

        授权失败错误码

        :return: The error_code of this AuthResultResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AuthResultResp.

        授权失败错误码

        :param error_code: The error_code of this AuthResultResp.
        :type: str
        """
        self._error_code = error_code

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuthResultResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
