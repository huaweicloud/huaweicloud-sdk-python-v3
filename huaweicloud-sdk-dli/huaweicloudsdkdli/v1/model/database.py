# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Database:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'owner': 'str',
        'table_number': 'int',
        'description': 'str',
        'enterprise_project_id': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'database_name': 'database_name',
        'owner': 'owner',
        'table_number': 'table_number',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'resource_id': 'resource_id'
    }

    def __init__(self, database_name=None, owner=None, table_number=None, description=None, enterprise_project_id=None, resource_id=None):
        """Database

        The model defined in huaweicloud sdk

        :param database_name: 数据库名称。
        :type database_name: str
        :param owner: 数据库的创建者。
        :type owner: str
        :param table_number: 数据库中表的个数。
        :type table_number: int
        :param description: 数据库相关的描述信息。
        :type description: str
        :param enterprise_project_id: 企业项目ID，“0”表示default，即默认的企业项目。关于如何设置企业项目请参考《企业管理用户指南》。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。
        :type enterprise_project_id: str
        :param resource_id: 资源ID。
        :type resource_id: str
        """
        
        

        self._database_name = None
        self._owner = None
        self._table_number = None
        self._description = None
        self._enterprise_project_id = None
        self._resource_id = None
        self.discriminator = None

        if database_name is not None:
            self.database_name = database_name
        if owner is not None:
            self.owner = owner
        if table_number is not None:
            self.table_number = table_number
        if description is not None:
            self.description = description
        self.enterprise_project_id = enterprise_project_id
        self.resource_id = resource_id

    @property
    def database_name(self):
        """Gets the database_name of this Database.

        数据库名称。

        :return: The database_name of this Database.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this Database.

        数据库名称。

        :param database_name: The database_name of this Database.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def owner(self):
        """Gets the owner of this Database.

        数据库的创建者。

        :return: The owner of this Database.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Database.

        数据库的创建者。

        :param owner: The owner of this Database.
        :type owner: str
        """
        self._owner = owner

    @property
    def table_number(self):
        """Gets the table_number of this Database.

        数据库中表的个数。

        :return: The table_number of this Database.
        :rtype: int
        """
        return self._table_number

    @table_number.setter
    def table_number(self, table_number):
        """Sets the table_number of this Database.

        数据库中表的个数。

        :param table_number: The table_number of this Database.
        :type table_number: int
        """
        self._table_number = table_number

    @property
    def description(self):
        """Gets the description of this Database.

        数据库相关的描述信息。

        :return: The description of this Database.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Database.

        数据库相关的描述信息。

        :param description: The description of this Database.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Database.

        企业项目ID，“0”表示default，即默认的企业项目。关于如何设置企业项目请参考《企业管理用户指南》。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。

        :return: The enterprise_project_id of this Database.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Database.

        企业项目ID，“0”表示default，即默认的企业项目。关于如何设置企业项目请参考《企业管理用户指南》。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。

        :param enterprise_project_id: The enterprise_project_id of this Database.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def resource_id(self):
        """Gets the resource_id of this Database.

        资源ID。

        :return: The resource_id of this Database.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Database.

        资源ID。

        :param resource_id: The resource_id of this Database.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, Database):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
