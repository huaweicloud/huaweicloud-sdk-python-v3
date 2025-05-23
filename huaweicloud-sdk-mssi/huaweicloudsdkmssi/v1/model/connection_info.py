# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionInfo:

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
        'auth_id': 'str',
        'auth_info': 'object',
        'auth_key': 'str',
        'auth_name': 'str',
        'auth_prop': 'object',
        'auth_type': 'str',
        'cdm_params_config': 'object',
        'connection_name': 'str',
        'connector_id': 'str',
        'connector_name': 'str',
        'create_time': 'datetime',
        'created_by': 'str',
        'description': 'str',
        'domain_id': 'str',
        'host_config': 'object',
        'id': 'str',
        'is_open': 'int',
        'logo': 'str',
        'project_id': 'str',
        'status': 'str',
        'type': 'str',
        'updated_by': 'str',
        'updated_time': 'datetime',
        'user_id': 'str'
    }

    attribute_map = {
        'auth_config': 'auth_config',
        'auth_config_id': 'auth_config_id',
        'auth_dynamic': 'auth_dynamic',
        'auth_id': 'auth_id',
        'auth_info': 'auth_info',
        'auth_key': 'auth_key',
        'auth_name': 'auth_name',
        'auth_prop': 'auth_prop',
        'auth_type': 'auth_type',
        'cdm_params_config': 'cdm_params_config',
        'connection_name': 'connection_name',
        'connector_id': 'connector_id',
        'connector_name': 'connector_name',
        'create_time': 'create_time',
        'created_by': 'created_by',
        'description': 'description',
        'domain_id': 'domain_id',
        'host_config': 'host_config',
        'id': 'id',
        'is_open': 'is_open',
        'logo': 'logo',
        'project_id': 'project_id',
        'status': 'status',
        'type': 'type',
        'updated_by': 'updated_by',
        'updated_time': 'updated_time',
        'user_id': 'user_id'
    }

    def __init__(self, auth_config=None, auth_config_id=None, auth_dynamic=None, auth_id=None, auth_info=None, auth_key=None, auth_name=None, auth_prop=None, auth_type=None, cdm_params_config=None, connection_name=None, connector_id=None, connector_name=None, create_time=None, created_by=None, description=None, domain_id=None, host_config=None, id=None, is_open=None, logo=None, project_id=None, status=None, type=None, updated_by=None, updated_time=None, user_id=None):
        r"""ConnectionInfo

        The model defined in huaweicloud sdk

        :param auth_config: 
        :type auth_config: object
        :param auth_config_id: 
        :type auth_config_id: str
        :param auth_dynamic: 
        :type auth_dynamic: object
        :param auth_id: 
        :type auth_id: str
        :param auth_info: 
        :type auth_info: object
        :param auth_key: 
        :type auth_key: str
        :param auth_name: 
        :type auth_name: str
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
        :param connector_name: 
        :type connector_name: str
        :param create_time: 
        :type create_time: datetime
        :param created_by: 
        :type created_by: str
        :param description: 
        :type description: str
        :param domain_id: 
        :type domain_id: str
        :param host_config: 
        :type host_config: object
        :param id: 
        :type id: str
        :param is_open: 
        :type is_open: int
        :param logo: 
        :type logo: str
        :param project_id: 
        :type project_id: str
        :param status: 
        :type status: str
        :param type: 
        :type type: str
        :param updated_by: 
        :type updated_by: str
        :param updated_time: 
        :type updated_time: datetime
        :param user_id: 
        :type user_id: str
        """
        
        

        self._auth_config = None
        self._auth_config_id = None
        self._auth_dynamic = None
        self._auth_id = None
        self._auth_info = None
        self._auth_key = None
        self._auth_name = None
        self._auth_prop = None
        self._auth_type = None
        self._cdm_params_config = None
        self._connection_name = None
        self._connector_id = None
        self._connector_name = None
        self._create_time = None
        self._created_by = None
        self._description = None
        self._domain_id = None
        self._host_config = None
        self._id = None
        self._is_open = None
        self._logo = None
        self._project_id = None
        self._status = None
        self._type = None
        self._updated_by = None
        self._updated_time = None
        self._user_id = None
        self.discriminator = None

        if auth_config is not None:
            self.auth_config = auth_config
        if auth_config_id is not None:
            self.auth_config_id = auth_config_id
        if auth_dynamic is not None:
            self.auth_dynamic = auth_dynamic
        if auth_id is not None:
            self.auth_id = auth_id
        if auth_info is not None:
            self.auth_info = auth_info
        if auth_key is not None:
            self.auth_key = auth_key
        if auth_name is not None:
            self.auth_name = auth_name
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
        if connector_name is not None:
            self.connector_name = connector_name
        if create_time is not None:
            self.create_time = create_time
        if created_by is not None:
            self.created_by = created_by
        if description is not None:
            self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        if host_config is not None:
            self.host_config = host_config
        if id is not None:
            self.id = id
        if is_open is not None:
            self.is_open = is_open
        if logo is not None:
            self.logo = logo
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_time is not None:
            self.updated_time = updated_time
        if user_id is not None:
            self.user_id = user_id

    @property
    def auth_config(self):
        r"""Gets the auth_config of this ConnectionInfo.

        :return: The auth_config of this ConnectionInfo.
        :rtype: object
        """
        return self._auth_config

    @auth_config.setter
    def auth_config(self, auth_config):
        r"""Sets the auth_config of this ConnectionInfo.

        :param auth_config: The auth_config of this ConnectionInfo.
        :type auth_config: object
        """
        self._auth_config = auth_config

    @property
    def auth_config_id(self):
        r"""Gets the auth_config_id of this ConnectionInfo.

        :return: The auth_config_id of this ConnectionInfo.
        :rtype: str
        """
        return self._auth_config_id

    @auth_config_id.setter
    def auth_config_id(self, auth_config_id):
        r"""Sets the auth_config_id of this ConnectionInfo.

        :param auth_config_id: The auth_config_id of this ConnectionInfo.
        :type auth_config_id: str
        """
        self._auth_config_id = auth_config_id

    @property
    def auth_dynamic(self):
        r"""Gets the auth_dynamic of this ConnectionInfo.

        :return: The auth_dynamic of this ConnectionInfo.
        :rtype: object
        """
        return self._auth_dynamic

    @auth_dynamic.setter
    def auth_dynamic(self, auth_dynamic):
        r"""Sets the auth_dynamic of this ConnectionInfo.

        :param auth_dynamic: The auth_dynamic of this ConnectionInfo.
        :type auth_dynamic: object
        """
        self._auth_dynamic = auth_dynamic

    @property
    def auth_id(self):
        r"""Gets the auth_id of this ConnectionInfo.

        :return: The auth_id of this ConnectionInfo.
        :rtype: str
        """
        return self._auth_id

    @auth_id.setter
    def auth_id(self, auth_id):
        r"""Sets the auth_id of this ConnectionInfo.

        :param auth_id: The auth_id of this ConnectionInfo.
        :type auth_id: str
        """
        self._auth_id = auth_id

    @property
    def auth_info(self):
        r"""Gets the auth_info of this ConnectionInfo.

        :return: The auth_info of this ConnectionInfo.
        :rtype: object
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        r"""Sets the auth_info of this ConnectionInfo.

        :param auth_info: The auth_info of this ConnectionInfo.
        :type auth_info: object
        """
        self._auth_info = auth_info

    @property
    def auth_key(self):
        r"""Gets the auth_key of this ConnectionInfo.

        :return: The auth_key of this ConnectionInfo.
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        r"""Sets the auth_key of this ConnectionInfo.

        :param auth_key: The auth_key of this ConnectionInfo.
        :type auth_key: str
        """
        self._auth_key = auth_key

    @property
    def auth_name(self):
        r"""Gets the auth_name of this ConnectionInfo.

        :return: The auth_name of this ConnectionInfo.
        :rtype: str
        """
        return self._auth_name

    @auth_name.setter
    def auth_name(self, auth_name):
        r"""Sets the auth_name of this ConnectionInfo.

        :param auth_name: The auth_name of this ConnectionInfo.
        :type auth_name: str
        """
        self._auth_name = auth_name

    @property
    def auth_prop(self):
        r"""Gets the auth_prop of this ConnectionInfo.

        :return: The auth_prop of this ConnectionInfo.
        :rtype: object
        """
        return self._auth_prop

    @auth_prop.setter
    def auth_prop(self, auth_prop):
        r"""Sets the auth_prop of this ConnectionInfo.

        :param auth_prop: The auth_prop of this ConnectionInfo.
        :type auth_prop: object
        """
        self._auth_prop = auth_prop

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ConnectionInfo.

        :return: The auth_type of this ConnectionInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ConnectionInfo.

        :param auth_type: The auth_type of this ConnectionInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def cdm_params_config(self):
        r"""Gets the cdm_params_config of this ConnectionInfo.

        :return: The cdm_params_config of this ConnectionInfo.
        :rtype: object
        """
        return self._cdm_params_config

    @cdm_params_config.setter
    def cdm_params_config(self, cdm_params_config):
        r"""Sets the cdm_params_config of this ConnectionInfo.

        :param cdm_params_config: The cdm_params_config of this ConnectionInfo.
        :type cdm_params_config: object
        """
        self._cdm_params_config = cdm_params_config

    @property
    def connection_name(self):
        r"""Gets the connection_name of this ConnectionInfo.

        :return: The connection_name of this ConnectionInfo.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        r"""Sets the connection_name of this ConnectionInfo.

        :param connection_name: The connection_name of this ConnectionInfo.
        :type connection_name: str
        """
        self._connection_name = connection_name

    @property
    def connector_id(self):
        r"""Gets the connector_id of this ConnectionInfo.

        :return: The connector_id of this ConnectionInfo.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        r"""Sets the connector_id of this ConnectionInfo.

        :param connector_id: The connector_id of this ConnectionInfo.
        :type connector_id: str
        """
        self._connector_id = connector_id

    @property
    def connector_name(self):
        r"""Gets the connector_name of this ConnectionInfo.

        :return: The connector_name of this ConnectionInfo.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        r"""Sets the connector_name of this ConnectionInfo.

        :param connector_name: The connector_name of this ConnectionInfo.
        :type connector_name: str
        """
        self._connector_name = connector_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ConnectionInfo.

        :return: The create_time of this ConnectionInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ConnectionInfo.

        :param create_time: The create_time of this ConnectionInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def created_by(self):
        r"""Gets the created_by of this ConnectionInfo.

        :return: The created_by of this ConnectionInfo.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ConnectionInfo.

        :param created_by: The created_by of this ConnectionInfo.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def description(self):
        r"""Gets the description of this ConnectionInfo.

        :return: The description of this ConnectionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConnectionInfo.

        :param description: The description of this ConnectionInfo.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ConnectionInfo.

        :return: The domain_id of this ConnectionInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ConnectionInfo.

        :param domain_id: The domain_id of this ConnectionInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def host_config(self):
        r"""Gets the host_config of this ConnectionInfo.

        :return: The host_config of this ConnectionInfo.
        :rtype: object
        """
        return self._host_config

    @host_config.setter
    def host_config(self, host_config):
        r"""Sets the host_config of this ConnectionInfo.

        :param host_config: The host_config of this ConnectionInfo.
        :type host_config: object
        """
        self._host_config = host_config

    @property
    def id(self):
        r"""Gets the id of this ConnectionInfo.

        :return: The id of this ConnectionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConnectionInfo.

        :param id: The id of this ConnectionInfo.
        :type id: str
        """
        self._id = id

    @property
    def is_open(self):
        r"""Gets the is_open of this ConnectionInfo.

        :return: The is_open of this ConnectionInfo.
        :rtype: int
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        r"""Sets the is_open of this ConnectionInfo.

        :param is_open: The is_open of this ConnectionInfo.
        :type is_open: int
        """
        self._is_open = is_open

    @property
    def logo(self):
        r"""Gets the logo of this ConnectionInfo.

        :return: The logo of this ConnectionInfo.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        r"""Sets the logo of this ConnectionInfo.

        :param logo: The logo of this ConnectionInfo.
        :type logo: str
        """
        self._logo = logo

    @property
    def project_id(self):
        r"""Gets the project_id of this ConnectionInfo.

        :return: The project_id of this ConnectionInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ConnectionInfo.

        :param project_id: The project_id of this ConnectionInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this ConnectionInfo.

        :return: The status of this ConnectionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ConnectionInfo.

        :param status: The status of this ConnectionInfo.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ConnectionInfo.

        :return: The type of this ConnectionInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConnectionInfo.

        :param type: The type of this ConnectionInfo.
        :type type: str
        """
        self._type = type

    @property
    def updated_by(self):
        r"""Gets the updated_by of this ConnectionInfo.

        :return: The updated_by of this ConnectionInfo.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this ConnectionInfo.

        :param updated_by: The updated_by of this ConnectionInfo.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def updated_time(self):
        r"""Gets the updated_time of this ConnectionInfo.

        :return: The updated_time of this ConnectionInfo.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this ConnectionInfo.

        :param updated_time: The updated_time of this ConnectionInfo.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

    @property
    def user_id(self):
        r"""Gets the user_id of this ConnectionInfo.

        :return: The user_id of this ConnectionInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ConnectionInfo.

        :param user_id: The user_id of this ConnectionInfo.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, ConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
