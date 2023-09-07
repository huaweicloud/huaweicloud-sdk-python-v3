# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthConfigA:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_config': 'object',
        'auth_dynamic': 'object',
        'auth_info': 'dict(str, str)',
        'auth_prop': 'object',
        'auth_type': 'str',
        'cdm_params_config': 'object',
        'host_config': 'object'
    }

    attribute_map = {
        'auth_config': 'auth_config',
        'auth_dynamic': 'auth_dynamic',
        'auth_info': 'auth_info',
        'auth_prop': 'auth_prop',
        'auth_type': 'auth_type',
        'cdm_params_config': 'cdm_params_config',
        'host_config': 'host_config'
    }

    def __init__(self, auth_config=None, auth_dynamic=None, auth_info=None, auth_prop=None, auth_type=None, cdm_params_config=None, host_config=None):
        """AuthConfigA

        The model defined in huaweicloud sdk

        :param auth_config: 
        :type auth_config: object
        :param auth_dynamic: 
        :type auth_dynamic: object
        :param auth_info: 
        :type auth_info: dict(str, str)
        :param auth_prop: 
        :type auth_prop: object
        :param auth_type: 
        :type auth_type: str
        :param cdm_params_config: 
        :type cdm_params_config: object
        :param host_config: 
        :type host_config: object
        """
        
        

        self._auth_config = None
        self._auth_dynamic = None
        self._auth_info = None
        self._auth_prop = None
        self._auth_type = None
        self._cdm_params_config = None
        self._host_config = None
        self.discriminator = None

        if auth_config is not None:
            self.auth_config = auth_config
        if auth_dynamic is not None:
            self.auth_dynamic = auth_dynamic
        if auth_info is not None:
            self.auth_info = auth_info
        if auth_prop is not None:
            self.auth_prop = auth_prop
        if auth_type is not None:
            self.auth_type = auth_type
        if cdm_params_config is not None:
            self.cdm_params_config = cdm_params_config
        if host_config is not None:
            self.host_config = host_config

    @property
    def auth_config(self):
        """Gets the auth_config of this AuthConfigA.

        :return: The auth_config of this AuthConfigA.
        :rtype: object
        """
        return self._auth_config

    @auth_config.setter
    def auth_config(self, auth_config):
        """Sets the auth_config of this AuthConfigA.

        :param auth_config: The auth_config of this AuthConfigA.
        :type auth_config: object
        """
        self._auth_config = auth_config

    @property
    def auth_dynamic(self):
        """Gets the auth_dynamic of this AuthConfigA.

        :return: The auth_dynamic of this AuthConfigA.
        :rtype: object
        """
        return self._auth_dynamic

    @auth_dynamic.setter
    def auth_dynamic(self, auth_dynamic):
        """Sets the auth_dynamic of this AuthConfigA.

        :param auth_dynamic: The auth_dynamic of this AuthConfigA.
        :type auth_dynamic: object
        """
        self._auth_dynamic = auth_dynamic

    @property
    def auth_info(self):
        """Gets the auth_info of this AuthConfigA.

        :return: The auth_info of this AuthConfigA.
        :rtype: dict(str, str)
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        """Sets the auth_info of this AuthConfigA.

        :param auth_info: The auth_info of this AuthConfigA.
        :type auth_info: dict(str, str)
        """
        self._auth_info = auth_info

    @property
    def auth_prop(self):
        """Gets the auth_prop of this AuthConfigA.

        :return: The auth_prop of this AuthConfigA.
        :rtype: object
        """
        return self._auth_prop

    @auth_prop.setter
    def auth_prop(self, auth_prop):
        """Sets the auth_prop of this AuthConfigA.

        :param auth_prop: The auth_prop of this AuthConfigA.
        :type auth_prop: object
        """
        self._auth_prop = auth_prop

    @property
    def auth_type(self):
        """Gets the auth_type of this AuthConfigA.

        :return: The auth_type of this AuthConfigA.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this AuthConfigA.

        :param auth_type: The auth_type of this AuthConfigA.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def cdm_params_config(self):
        """Gets the cdm_params_config of this AuthConfigA.

        :return: The cdm_params_config of this AuthConfigA.
        :rtype: object
        """
        return self._cdm_params_config

    @cdm_params_config.setter
    def cdm_params_config(self, cdm_params_config):
        """Sets the cdm_params_config of this AuthConfigA.

        :param cdm_params_config: The cdm_params_config of this AuthConfigA.
        :type cdm_params_config: object
        """
        self._cdm_params_config = cdm_params_config

    @property
    def host_config(self):
        """Gets the host_config of this AuthConfigA.

        :return: The host_config of this AuthConfigA.
        :rtype: object
        """
        return self._host_config

    @host_config.setter
    def host_config(self, host_config):
        """Sets the host_config of this AuthConfigA.

        :param host_config: The host_config of this AuthConfigA.
        :type host_config: object
        """
        self._host_config = host_config

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
        if not isinstance(other, AuthConfigA):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
