# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_name': 'str',
        'database_name': 'str',
        'owner': 'str',
        'owner_type': 'str',
        'owner_auth_source_type': 'str',
        'description': 'str',
        'location': 'str',
        'parameters': 'dict(str, str)',
        'table_location_list': 'list[str]',
        'function_location_list': 'list[str]',
        'access_policy_source': 'str',
        'catalog_id': 'str',
        'connection_name': 'str',
        'data_statistic_enable': 'bool',
        'database_id': 'str',
        'database_status': 'int',
        'database_type': 'str',
        'external_database_id': 'str',
        'permission_connection_name': 'str',
        'update_time': 'datetime',
        'version_id': 'str'
    }

    attribute_map = {
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'owner': 'owner',
        'owner_type': 'owner_type',
        'owner_auth_source_type': 'owner_auth_source_type',
        'description': 'description',
        'location': 'location',
        'parameters': 'parameters',
        'table_location_list': 'table_location_list',
        'function_location_list': 'function_location_list',
        'access_policy_source': 'access_policy_source',
        'catalog_id': 'catalog_id',
        'connection_name': 'connection_name',
        'data_statistic_enable': 'data_statistic_enable',
        'database_id': 'database_id',
        'database_status': 'database_status',
        'database_type': 'database_type',
        'external_database_id': 'external_database_id',
        'permission_connection_name': 'permission_connection_name',
        'update_time': 'update_time',
        'version_id': 'version_id'
    }

    def __init__(self, catalog_name=None, database_name=None, owner=None, owner_type=None, owner_auth_source_type=None, description=None, location=None, parameters=None, table_location_list=None, function_location_list=None, access_policy_source=None, catalog_id=None, connection_name=None, data_statistic_enable=None, database_id=None, database_status=None, database_type=None, external_database_id=None, permission_connection_name=None, update_time=None, version_id=None):
        r"""ShowDatabaseResponse

        The model defined in huaweicloud sdk

        :param catalog_name: catalog名称
        :type catalog_name: str
        :param database_name: 数据库名称
        :type database_name: str
        :param owner: 数据库所有者
        :type owner: str
        :param owner_type: 所有者类型,USER-用户,GROUP-组,ROLE-角色
        :type owner_type: str
        :param owner_auth_source_type: 所有者授权来源类型,IAM-云用户,SAML-联邦,LDAP-ld用户,LOCAL-本地用户,AGENTTENANT-委托,OTHER-其它。LakeFormation服务分为一期和二期，一期响应Body无该参数。
        :type owner_auth_source_type: str
        :param description: 数据库描述信息
        :type description: str
        :param location: 数据库路径地址。例如obs://location/uri/
        :type location: str
        :param parameters: 参数信息
        :type parameters: dict(str, str)
        :param table_location_list: 表路径列表。LakeFormation服务分为一期和二期，一期响应Body无该参数，二期默认为null。当值为null时，响应Body无该参数。
        :type table_location_list: list[str]
        :param function_location_list: 函数路径列表。默认为null，当值为null时，响应Body无该参数。
        :type function_location_list: list[str]
        :param access_policy_source: 权限策略来源。可选值为：lakeformation、ranger、hive。
        :type access_policy_source: str
        :param catalog_id: catalogID。
        :type catalog_id: str
        :param connection_name: 连接名称。
        :type connection_name: str
        :param data_statistic_enable: 数据概况统计开关。默认状态为关，若要开启database下table的数据概况统计，需要先打开database的数据概况开关。database此开关开启后，database下所有table都会默认开启此开关
        :type data_statistic_enable: bool
        :param database_id: 数据库ID。
        :type database_id: str
        :param database_status: 数据库状态：0表示正常，1表示删除中，2表示已删除，3表示恢复中，4表示清除中。
        :type database_status: int
        :param database_type: 数据库类型：MANAGED_DATABASE内置数据库、FOREIGN_DATABASE外置数据库。
        :type database_type: str
        :param external_database_id: 用户端数据库id，创建时指定，不可修改。
        :type external_database_id: str
        :param permission_connection_name: 权限连接名称。绑定后由该权限连接代理鉴权。为空时保留原权限连接。
        :type permission_connection_name: str
        :param update_time: 数据库元数据最后一次修改时间。
        :type update_time: datetime
        :param version_id: 版本ID
        :type version_id: str
        """
        
        super().__init__()

        self._catalog_name = None
        self._database_name = None
        self._owner = None
        self._owner_type = None
        self._owner_auth_source_type = None
        self._description = None
        self._location = None
        self._parameters = None
        self._table_location_list = None
        self._function_location_list = None
        self._access_policy_source = None
        self._catalog_id = None
        self._connection_name = None
        self._data_statistic_enable = None
        self._database_id = None
        self._database_status = None
        self._database_type = None
        self._external_database_id = None
        self._permission_connection_name = None
        self._update_time = None
        self._version_id = None
        self.discriminator = None

        if catalog_name is not None:
            self.catalog_name = catalog_name
        if database_name is not None:
            self.database_name = database_name
        if owner is not None:
            self.owner = owner
        if owner_type is not None:
            self.owner_type = owner_type
        if owner_auth_source_type is not None:
            self.owner_auth_source_type = owner_auth_source_type
        if description is not None:
            self.description = description
        if location is not None:
            self.location = location
        if parameters is not None:
            self.parameters = parameters
        if table_location_list is not None:
            self.table_location_list = table_location_list
        if function_location_list is not None:
            self.function_location_list = function_location_list
        if access_policy_source is not None:
            self.access_policy_source = access_policy_source
        if catalog_id is not None:
            self.catalog_id = catalog_id
        if connection_name is not None:
            self.connection_name = connection_name
        if data_statistic_enable is not None:
            self.data_statistic_enable = data_statistic_enable
        if database_id is not None:
            self.database_id = database_id
        if database_status is not None:
            self.database_status = database_status
        if database_type is not None:
            self.database_type = database_type
        if external_database_id is not None:
            self.external_database_id = external_database_id
        if permission_connection_name is not None:
            self.permission_connection_name = permission_connection_name
        if update_time is not None:
            self.update_time = update_time
        if version_id is not None:
            self.version_id = version_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this ShowDatabaseResponse.

        catalog名称

        :return: The catalog_name of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this ShowDatabaseResponse.

        catalog名称

        :param catalog_name: The catalog_name of this ShowDatabaseResponse.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowDatabaseResponse.

        数据库名称

        :return: The database_name of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowDatabaseResponse.

        数据库名称

        :param database_name: The database_name of this ShowDatabaseResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def owner(self):
        r"""Gets the owner of this ShowDatabaseResponse.

        数据库所有者

        :return: The owner of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ShowDatabaseResponse.

        数据库所有者

        :param owner: The owner of this ShowDatabaseResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_type(self):
        r"""Gets the owner_type of this ShowDatabaseResponse.

        所有者类型,USER-用户,GROUP-组,ROLE-角色

        :return: The owner_type of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this ShowDatabaseResponse.

        所有者类型,USER-用户,GROUP-组,ROLE-角色

        :param owner_type: The owner_type of this ShowDatabaseResponse.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def owner_auth_source_type(self):
        r"""Gets the owner_auth_source_type of this ShowDatabaseResponse.

        所有者授权来源类型,IAM-云用户,SAML-联邦,LDAP-ld用户,LOCAL-本地用户,AGENTTENANT-委托,OTHER-其它。LakeFormation服务分为一期和二期，一期响应Body无该参数。

        :return: The owner_auth_source_type of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._owner_auth_source_type

    @owner_auth_source_type.setter
    def owner_auth_source_type(self, owner_auth_source_type):
        r"""Sets the owner_auth_source_type of this ShowDatabaseResponse.

        所有者授权来源类型,IAM-云用户,SAML-联邦,LDAP-ld用户,LOCAL-本地用户,AGENTTENANT-委托,OTHER-其它。LakeFormation服务分为一期和二期，一期响应Body无该参数。

        :param owner_auth_source_type: The owner_auth_source_type of this ShowDatabaseResponse.
        :type owner_auth_source_type: str
        """
        self._owner_auth_source_type = owner_auth_source_type

    @property
    def description(self):
        r"""Gets the description of this ShowDatabaseResponse.

        数据库描述信息

        :return: The description of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowDatabaseResponse.

        数据库描述信息

        :param description: The description of this ShowDatabaseResponse.
        :type description: str
        """
        self._description = description

    @property
    def location(self):
        r"""Gets the location of this ShowDatabaseResponse.

        数据库路径地址。例如obs://location/uri/

        :return: The location of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ShowDatabaseResponse.

        数据库路径地址。例如obs://location/uri/

        :param location: The location of this ShowDatabaseResponse.
        :type location: str
        """
        self._location = location

    @property
    def parameters(self):
        r"""Gets the parameters of this ShowDatabaseResponse.

        参数信息

        :return: The parameters of this ShowDatabaseResponse.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ShowDatabaseResponse.

        参数信息

        :param parameters: The parameters of this ShowDatabaseResponse.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def table_location_list(self):
        r"""Gets the table_location_list of this ShowDatabaseResponse.

        表路径列表。LakeFormation服务分为一期和二期，一期响应Body无该参数，二期默认为null。当值为null时，响应Body无该参数。

        :return: The table_location_list of this ShowDatabaseResponse.
        :rtype: list[str]
        """
        return self._table_location_list

    @table_location_list.setter
    def table_location_list(self, table_location_list):
        r"""Sets the table_location_list of this ShowDatabaseResponse.

        表路径列表。LakeFormation服务分为一期和二期，一期响应Body无该参数，二期默认为null。当值为null时，响应Body无该参数。

        :param table_location_list: The table_location_list of this ShowDatabaseResponse.
        :type table_location_list: list[str]
        """
        self._table_location_list = table_location_list

    @property
    def function_location_list(self):
        r"""Gets the function_location_list of this ShowDatabaseResponse.

        函数路径列表。默认为null，当值为null时，响应Body无该参数。

        :return: The function_location_list of this ShowDatabaseResponse.
        :rtype: list[str]
        """
        return self._function_location_list

    @function_location_list.setter
    def function_location_list(self, function_location_list):
        r"""Sets the function_location_list of this ShowDatabaseResponse.

        函数路径列表。默认为null，当值为null时，响应Body无该参数。

        :param function_location_list: The function_location_list of this ShowDatabaseResponse.
        :type function_location_list: list[str]
        """
        self._function_location_list = function_location_list

    @property
    def access_policy_source(self):
        r"""Gets the access_policy_source of this ShowDatabaseResponse.

        权限策略来源。可选值为：lakeformation、ranger、hive。

        :return: The access_policy_source of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._access_policy_source

    @access_policy_source.setter
    def access_policy_source(self, access_policy_source):
        r"""Sets the access_policy_source of this ShowDatabaseResponse.

        权限策略来源。可选值为：lakeformation、ranger、hive。

        :param access_policy_source: The access_policy_source of this ShowDatabaseResponse.
        :type access_policy_source: str
        """
        self._access_policy_source = access_policy_source

    @property
    def catalog_id(self):
        r"""Gets the catalog_id of this ShowDatabaseResponse.

        catalogID。

        :return: The catalog_id of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        r"""Sets the catalog_id of this ShowDatabaseResponse.

        catalogID。

        :param catalog_id: The catalog_id of this ShowDatabaseResponse.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def connection_name(self):
        r"""Gets the connection_name of this ShowDatabaseResponse.

        连接名称。

        :return: The connection_name of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        r"""Sets the connection_name of this ShowDatabaseResponse.

        连接名称。

        :param connection_name: The connection_name of this ShowDatabaseResponse.
        :type connection_name: str
        """
        self._connection_name = connection_name

    @property
    def data_statistic_enable(self):
        r"""Gets the data_statistic_enable of this ShowDatabaseResponse.

        数据概况统计开关。默认状态为关，若要开启database下table的数据概况统计，需要先打开database的数据概况开关。database此开关开启后，database下所有table都会默认开启此开关

        :return: The data_statistic_enable of this ShowDatabaseResponse.
        :rtype: bool
        """
        return self._data_statistic_enable

    @data_statistic_enable.setter
    def data_statistic_enable(self, data_statistic_enable):
        r"""Sets the data_statistic_enable of this ShowDatabaseResponse.

        数据概况统计开关。默认状态为关，若要开启database下table的数据概况统计，需要先打开database的数据概况开关。database此开关开启后，database下所有table都会默认开启此开关

        :param data_statistic_enable: The data_statistic_enable of this ShowDatabaseResponse.
        :type data_statistic_enable: bool
        """
        self._data_statistic_enable = data_statistic_enable

    @property
    def database_id(self):
        r"""Gets the database_id of this ShowDatabaseResponse.

        数据库ID。

        :return: The database_id of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        r"""Sets the database_id of this ShowDatabaseResponse.

        数据库ID。

        :param database_id: The database_id of this ShowDatabaseResponse.
        :type database_id: str
        """
        self._database_id = database_id

    @property
    def database_status(self):
        r"""Gets the database_status of this ShowDatabaseResponse.

        数据库状态：0表示正常，1表示删除中，2表示已删除，3表示恢复中，4表示清除中。

        :return: The database_status of this ShowDatabaseResponse.
        :rtype: int
        """
        return self._database_status

    @database_status.setter
    def database_status(self, database_status):
        r"""Sets the database_status of this ShowDatabaseResponse.

        数据库状态：0表示正常，1表示删除中，2表示已删除，3表示恢复中，4表示清除中。

        :param database_status: The database_status of this ShowDatabaseResponse.
        :type database_status: int
        """
        self._database_status = database_status

    @property
    def database_type(self):
        r"""Gets the database_type of this ShowDatabaseResponse.

        数据库类型：MANAGED_DATABASE内置数据库、FOREIGN_DATABASE外置数据库。

        :return: The database_type of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        r"""Sets the database_type of this ShowDatabaseResponse.

        数据库类型：MANAGED_DATABASE内置数据库、FOREIGN_DATABASE外置数据库。

        :param database_type: The database_type of this ShowDatabaseResponse.
        :type database_type: str
        """
        self._database_type = database_type

    @property
    def external_database_id(self):
        r"""Gets the external_database_id of this ShowDatabaseResponse.

        用户端数据库id，创建时指定，不可修改。

        :return: The external_database_id of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._external_database_id

    @external_database_id.setter
    def external_database_id(self, external_database_id):
        r"""Sets the external_database_id of this ShowDatabaseResponse.

        用户端数据库id，创建时指定，不可修改。

        :param external_database_id: The external_database_id of this ShowDatabaseResponse.
        :type external_database_id: str
        """
        self._external_database_id = external_database_id

    @property
    def permission_connection_name(self):
        r"""Gets the permission_connection_name of this ShowDatabaseResponse.

        权限连接名称。绑定后由该权限连接代理鉴权。为空时保留原权限连接。

        :return: The permission_connection_name of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._permission_connection_name

    @permission_connection_name.setter
    def permission_connection_name(self, permission_connection_name):
        r"""Sets the permission_connection_name of this ShowDatabaseResponse.

        权限连接名称。绑定后由该权限连接代理鉴权。为空时保留原权限连接。

        :param permission_connection_name: The permission_connection_name of this ShowDatabaseResponse.
        :type permission_connection_name: str
        """
        self._permission_connection_name = permission_connection_name

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowDatabaseResponse.

        数据库元数据最后一次修改时间。

        :return: The update_time of this ShowDatabaseResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowDatabaseResponse.

        数据库元数据最后一次修改时间。

        :param update_time: The update_time of this ShowDatabaseResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def version_id(self):
        r"""Gets the version_id of this ShowDatabaseResponse.

        版本ID

        :return: The version_id of this ShowDatabaseResponse.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this ShowDatabaseResponse.

        版本ID

        :param version_id: The version_id of this ShowDatabaseResponse.
        :type version_id: str
        """
        self._version_id = version_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowDatabaseResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
