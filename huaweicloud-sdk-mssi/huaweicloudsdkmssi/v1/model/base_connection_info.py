# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseConnectionInfo:

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
        'auth_config_id': 'str',
        'auth_dynamic': 'object',
        'auth_info': 'object',
        'auth_prop': 'object',
        'auth_type': 'str',
        'cdm_params_config': 'object',
        'connection_name': 'str',
        'connector_id': 'str',
        'description': 'str',
        'host_config': 'object'
    }

    attribute_map = {
        'auth_config': 'auth_config',
        'auth_config_id': 'auth_config_id',
        'auth_dynamic': 'auth_dynamic',
        'auth_info': 'auth_info',
        'auth_prop': 'auth_prop',
        'auth_type': 'auth_type',
        'cdm_params_config': 'cdm_params_config',
        'connection_name': 'connection_name',
        'connector_id': 'connector_id',
        'description': 'description',
        'host_config': 'host_config'
    }

    def __init__(self, auth_config=None, auth_config_id=None, auth_dynamic=None, auth_info=None, auth_prop=None, auth_type=None, cdm_params_config=None, connection_name=None, connector_id=None, description=None, host_config=None):
        """BaseConnectionInfo

        The model defined in huaweicloud sdk

        :param auth_config: 
        :type auth_config: object
        :param auth_config_id: 
        :type auth_config_id: str
        :param auth_dynamic: 
        :type auth_dynamic: object
        :param auth_info: 
        :type auth_info: object
        :param auth_prop: 
        :type auth_prop: object
        :param auth_type: 
        :type auth_type: str
        :param cdm_params_config: 
        :type cdm_params_config: object
        :param connection_name: 
        :type connection_name: str
        :param connector_id: 
        :type connector_id: str
        :param description: 
        :type description: str
        :param host_config: 
        :type host_config: object
        """
        
        

        self._auth_config = None
        self._auth_config_id = None
        self._auth_dynamic = None
        self._auth_info = None
        self._auth_prop = None
        self._auth_type = None
        self._cdm_params_config = None
        self._connection_name = None
        self._connector_id = None
        self._description = None
        self._host_config = None
        self.discriminator = None

        if auth_config is not None:
            self.auth_config = auth_config
        if auth_config_id is not None:
            self.auth_config_id = auth_config_id
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
        if connection_name is not None:
            self.connection_name = connection_name
        if connector_id is not None:
            self.connector_id = connector_id
        if description is not None:
            self.description = description
        if host_config is not None:
            self.host_config = host_config

    @property
    def auth_config(self):
        """Gets the auth_config of this BaseConnectionInfo.

        :return: The auth_config of this BaseConnectionInfo.
        :rtype: object
        """
        return self._auth_config

    @auth_config.setter
    def auth_config(self, auth_config):
        """Sets the auth_config of this BaseConnectionInfo.

        :param auth_config: The auth_config of this BaseConnectionInfo.
        :type auth_config: object
        """
        self._auth_config = auth_config

    @property
    def auth_config_id(self):
        """Gets the auth_config_id of this BaseConnectionInfo.

        :return: The auth_config_id of this BaseConnectionInfo.
        :rtype: str
        """
        return self._auth_config_id

    @auth_config_id.setter
    def auth_config_id(self, auth_config_id):
        """Sets the auth_config_id of this BaseConnectionInfo.

        :param auth_config_id: The auth_config_id of this BaseConnectionInfo.
        :type auth_config_id: str
        """
        self._auth_config_id = auth_config_id

    @property
    def auth_dynamic(self):
        """Gets the auth_dynamic of this BaseConnectionInfo.

        :return: The auth_dynamic of this BaseConnectionInfo.
        :rtype: object
        """
        return self._auth_dynamic

    @auth_dynamic.setter
    def auth_dynamic(self, auth_dynamic):
        """Sets the auth_dynamic of this BaseConnectionInfo.

        :param auth_dynamic: The auth_dynamic of this BaseConnectionInfo.
        :type auth_dynamic: object
        """
        self._auth_dynamic = auth_dynamic

    @property
    def auth_info(self):
        """Gets the auth_info of this BaseConnectionInfo.

        :return: The auth_info of this BaseConnectionInfo.
        :rtype: object
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        """Sets the auth_info of this BaseConnectionInfo.

        :param auth_info: The auth_info of this BaseConnectionInfo.
        :type auth_info: object
        """
        self._auth_info = auth_info

    @property
    def auth_prop(self):
        """Gets the auth_prop of this BaseConnectionInfo.

        :return: The auth_prop of this BaseConnectionInfo.
        :rtype: object
        """
        return self._auth_prop

    @auth_prop.setter
    def auth_prop(self, auth_prop):
        """Sets the auth_prop of this BaseConnectionInfo.

        :param auth_prop: The auth_prop of this BaseConnectionInfo.
        :type auth_prop: object
        """
        self._auth_prop = auth_prop

    @property
    def auth_type(self):
        """Gets the auth_type of this BaseConnectionInfo.

        :return: The auth_type of this BaseConnectionInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this BaseConnectionInfo.

        :param auth_type: The auth_type of this BaseConnectionInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def cdm_params_config(self):
        """Gets the cdm_params_config of this BaseConnectionInfo.

        :return: The cdm_params_config of this BaseConnectionInfo.
        :rtype: object
        """
        return self._cdm_params_config

    @cdm_params_config.setter
    def cdm_params_config(self, cdm_params_config):
        """Sets the cdm_params_config of this BaseConnectionInfo.

        :param cdm_params_config: The cdm_params_config of this BaseConnectionInfo.
        :type cdm_params_config: object
        """
        self._cdm_params_config = cdm_params_config

    @property
    def connection_name(self):
        """Gets the connection_name of this BaseConnectionInfo.

        :return: The connection_name of this BaseConnectionInfo.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        """Sets the connection_name of this BaseConnectionInfo.

        :param connection_name: The connection_name of this BaseConnectionInfo.
        :type connection_name: str
        """
        self._connection_name = connection_name

    @property
    def connector_id(self):
        """Gets the connector_id of this BaseConnectionInfo.

        :return: The connector_id of this BaseConnectionInfo.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this BaseConnectionInfo.

        :param connector_id: The connector_id of this BaseConnectionInfo.
        :type connector_id: str
        """
        self._connector_id = connector_id

    @property
    def description(self):
        """Gets the description of this BaseConnectionInfo.

        :return: The description of this BaseConnectionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BaseConnectionInfo.

        :param description: The description of this BaseConnectionInfo.
        :type description: str
        """
        self._description = description

    @property
    def host_config(self):
        """Gets the host_config of this BaseConnectionInfo.

        :return: The host_config of this BaseConnectionInfo.
        :rtype: object
        """
        return self._host_config

    @host_config.setter
    def host_config(self, host_config):
        """Sets the host_config of this BaseConnectionInfo.

        :param host_config: The host_config of this BaseConnectionInfo.
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
        if not isinstance(other, BaseConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
