# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthOpt:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_code_auth_type': 'str'
    }

    attribute_map = {
        'app_code_auth_type': 'app_code_auth_type'
    }

    def __init__(self, app_code_auth_type=None):
        """AuthOpt

        The model defined in huaweicloud sdk

        :param app_code_auth_type: AppCode简易认证类型，仅在auth_type为APP时生效，默认为DISABLE： - DISABLE：不开启简易认证 - HEADER：开启简易认证且AppCode位置在HEADER
        :type app_code_auth_type: str
        """
        
        

        self._app_code_auth_type = None
        self.discriminator = None

        if app_code_auth_type is not None:
            self.app_code_auth_type = app_code_auth_type

    @property
    def app_code_auth_type(self):
        """Gets the app_code_auth_type of this AuthOpt.

        AppCode简易认证类型，仅在auth_type为APP时生效，默认为DISABLE： - DISABLE：不开启简易认证 - HEADER：开启简易认证且AppCode位置在HEADER

        :return: The app_code_auth_type of this AuthOpt.
        :rtype: str
        """
        return self._app_code_auth_type

    @app_code_auth_type.setter
    def app_code_auth_type(self, app_code_auth_type):
        """Sets the app_code_auth_type of this AuthOpt.

        AppCode简易认证类型，仅在auth_type为APP时生效，默认为DISABLE： - DISABLE：不开启简易认证 - HEADER：开启简易认证且AppCode位置在HEADER

        :param app_code_auth_type: The app_code_auth_type of this AuthOpt.
        :type app_code_auth_type: str
        """
        self._app_code_auth_type = app_code_auth_type

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
        if not isinstance(other, AuthOpt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
