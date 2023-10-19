# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatabaseResponse(SdkResponse):

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
        'function_location_list': 'list[str]'
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
        'function_location_list': 'function_location_list'
    }

    def __init__(self, catalog_name=None, database_name=None, owner=None, owner_type=None, owner_auth_source_type=None, description=None, location=None, parameters=None, table_location_list=None, function_location_list=None):
        """UpdateDatabaseResponse

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
        """
        
        super(UpdateDatabaseResponse, self).__init__()

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

    @property
    def catalog_name(self):
        """Gets the catalog_name of this UpdateDatabaseResponse.

        catalog名称

        :return: The catalog_name of this UpdateDatabaseResponse.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this UpdateDatabaseResponse.

        catalog名称

        :param catalog_name: The catalog_name of this UpdateDatabaseResponse.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        """Gets the database_name of this UpdateDatabaseResponse.

        数据库名称

        :return: The database_name of this UpdateDatabaseResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this UpdateDatabaseResponse.

        数据库名称

        :param database_name: The database_name of this UpdateDatabaseResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def owner(self):
        """Gets the owner of this UpdateDatabaseResponse.

        数据库所有者

        :return: The owner of this UpdateDatabaseResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UpdateDatabaseResponse.

        数据库所有者

        :param owner: The owner of this UpdateDatabaseResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_type(self):
        """Gets the owner_type of this UpdateDatabaseResponse.

        所有者类型,USER-用户,GROUP-组,ROLE-角色

        :return: The owner_type of this UpdateDatabaseResponse.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this UpdateDatabaseResponse.

        所有者类型,USER-用户,GROUP-组,ROLE-角色

        :param owner_type: The owner_type of this UpdateDatabaseResponse.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def owner_auth_source_type(self):
        """Gets the owner_auth_source_type of this UpdateDatabaseResponse.

        所有者授权来源类型,IAM-云用户,SAML-联邦,LDAP-ld用户,LOCAL-本地用户,AGENTTENANT-委托,OTHER-其它。LakeFormation服务分为一期和二期，一期响应Body无该参数。

        :return: The owner_auth_source_type of this UpdateDatabaseResponse.
        :rtype: str
        """
        return self._owner_auth_source_type

    @owner_auth_source_type.setter
    def owner_auth_source_type(self, owner_auth_source_type):
        """Sets the owner_auth_source_type of this UpdateDatabaseResponse.

        所有者授权来源类型,IAM-云用户,SAML-联邦,LDAP-ld用户,LOCAL-本地用户,AGENTTENANT-委托,OTHER-其它。LakeFormation服务分为一期和二期，一期响应Body无该参数。

        :param owner_auth_source_type: The owner_auth_source_type of this UpdateDatabaseResponse.
        :type owner_auth_source_type: str
        """
        self._owner_auth_source_type = owner_auth_source_type

    @property
    def description(self):
        """Gets the description of this UpdateDatabaseResponse.

        数据库描述信息

        :return: The description of this UpdateDatabaseResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDatabaseResponse.

        数据库描述信息

        :param description: The description of this UpdateDatabaseResponse.
        :type description: str
        """
        self._description = description

    @property
    def location(self):
        """Gets the location of this UpdateDatabaseResponse.

        数据库路径地址。例如obs://location/uri/

        :return: The location of this UpdateDatabaseResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this UpdateDatabaseResponse.

        数据库路径地址。例如obs://location/uri/

        :param location: The location of this UpdateDatabaseResponse.
        :type location: str
        """
        self._location = location

    @property
    def parameters(self):
        """Gets the parameters of this UpdateDatabaseResponse.

        参数信息

        :return: The parameters of this UpdateDatabaseResponse.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this UpdateDatabaseResponse.

        参数信息

        :param parameters: The parameters of this UpdateDatabaseResponse.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def table_location_list(self):
        """Gets the table_location_list of this UpdateDatabaseResponse.

        表路径列表。LakeFormation服务分为一期和二期，一期响应Body无该参数，二期默认为null。当值为null时，响应Body无该参数。

        :return: The table_location_list of this UpdateDatabaseResponse.
        :rtype: list[str]
        """
        return self._table_location_list

    @table_location_list.setter
    def table_location_list(self, table_location_list):
        """Sets the table_location_list of this UpdateDatabaseResponse.

        表路径列表。LakeFormation服务分为一期和二期，一期响应Body无该参数，二期默认为null。当值为null时，响应Body无该参数。

        :param table_location_list: The table_location_list of this UpdateDatabaseResponse.
        :type table_location_list: list[str]
        """
        self._table_location_list = table_location_list

    @property
    def function_location_list(self):
        """Gets the function_location_list of this UpdateDatabaseResponse.

        函数路径列表。默认为null，当值为null时，响应Body无该参数。

        :return: The function_location_list of this UpdateDatabaseResponse.
        :rtype: list[str]
        """
        return self._function_location_list

    @function_location_list.setter
    def function_location_list(self, function_location_list):
        """Sets the function_location_list of this UpdateDatabaseResponse.

        函数路径列表。默认为null，当值为null时，响应Body无该参数。

        :param function_location_list: The function_location_list of this UpdateDatabaseResponse.
        :type function_location_list: list[str]
        """
        self._function_location_list = function_location_list

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
        if not isinstance(other, UpdateDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
