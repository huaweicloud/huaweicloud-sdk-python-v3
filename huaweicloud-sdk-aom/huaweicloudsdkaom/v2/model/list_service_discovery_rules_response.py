# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceDiscoveryRulesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_rules': 'list[AppRules]',
        'error_code': 'str',
        'error_message': 'str',
        'response_status': 'int'
    }

    attribute_map = {
        'app_rules': 'appRules',
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'response_status': 'responseStatus'
    }

    def __init__(self, app_rules=None, error_code=None, error_message=None, response_status=None):
        """ListServiceDiscoveryRulesResponse - a model defined in huaweicloud sdk"""
        
        super(ListServiceDiscoveryRulesResponse, self).__init__()

        self._app_rules = None
        self._error_code = None
        self._error_message = None
        self._response_status = None
        self.discriminator = None

        if app_rules is not None:
            self.app_rules = app_rules
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if response_status is not None:
            self.response_status = response_status

    @property
    def app_rules(self):
        """Gets the app_rules of this ListServiceDiscoveryRulesResponse.

        查询结果规则信息。

        :return: The app_rules of this ListServiceDiscoveryRulesResponse.
        :rtype: list[AppRules]
        """
        return self._app_rules

    @app_rules.setter
    def app_rules(self, app_rules):
        """Sets the app_rules of this ListServiceDiscoveryRulesResponse.

        查询结果规则信息。

        :param app_rules: The app_rules of this ListServiceDiscoveryRulesResponse.
        :type: list[AppRules]
        """
        self._app_rules = app_rules

    @property
    def error_code(self):
        """Gets the error_code of this ListServiceDiscoveryRulesResponse.

        响应码,AOM_INVENTORY_2000000代表正常返回。

        :return: The error_code of this ListServiceDiscoveryRulesResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ListServiceDiscoveryRulesResponse.

        响应码,AOM_INVENTORY_2000000代表正常返回。

        :param error_code: The error_code of this ListServiceDiscoveryRulesResponse.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this ListServiceDiscoveryRulesResponse.

        响应信息描述。

        :return: The error_message of this ListServiceDiscoveryRulesResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ListServiceDiscoveryRulesResponse.

        响应信息描述。

        :param error_message: The error_message of this ListServiceDiscoveryRulesResponse.
        :type: str
        """
        self._error_message = error_message

    @property
    def response_status(self):
        """Gets the response_status of this ListServiceDiscoveryRulesResponse.

        响应状态码。

        :return: The response_status of this ListServiceDiscoveryRulesResponse.
        :rtype: int
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        """Sets the response_status of this ListServiceDiscoveryRulesResponse.

        响应状态码。

        :param response_status: The response_status of this ListServiceDiscoveryRulesResponse.
        :type: int
        """
        self._response_status = response_status

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
        if not isinstance(other, ListServiceDiscoveryRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
