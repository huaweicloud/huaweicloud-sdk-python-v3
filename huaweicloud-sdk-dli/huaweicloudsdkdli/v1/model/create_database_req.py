# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatabaseReq:

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
        'description': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[TmsTagEntity]'
    }

    attribute_map = {
        'database_name': 'database_name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, database_name=None, description=None, enterprise_project_id=None, tags=None):
        """CreateDatabaseReq

        The model defined in huaweicloud sdk

        :param database_name: 新增数据库名称。 说明： “default”为内置数据库，不能创建名为“default”的数据库。
        :type database_name: str
        :param description: 新增数据库的描述信息。
        :type description: str
        :param enterprise_project_id: 企业项目ID，“0”表示default，即默认的企业项目。关于如何设置企业项目请参考《企业管理用户指南》。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。
        :type enterprise_project_id: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        
        

        self._database_name = None
        self._description = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        self.database_name = database_name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def database_name(self):
        """Gets the database_name of this CreateDatabaseReq.

        新增数据库名称。 说明： “default”为内置数据库，不能创建名为“default”的数据库。

        :return: The database_name of this CreateDatabaseReq.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this CreateDatabaseReq.

        新增数据库名称。 说明： “default”为内置数据库，不能创建名为“default”的数据库。

        :param database_name: The database_name of this CreateDatabaseReq.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def description(self):
        """Gets the description of this CreateDatabaseReq.

        新增数据库的描述信息。

        :return: The description of this CreateDatabaseReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDatabaseReq.

        新增数据库的描述信息。

        :param description: The description of this CreateDatabaseReq.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateDatabaseReq.

        企业项目ID，“0”表示default，即默认的企业项目。关于如何设置企业项目请参考《企业管理用户指南》。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。

        :return: The enterprise_project_id of this CreateDatabaseReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateDatabaseReq.

        企业项目ID，“0”表示default，即默认的企业项目。关于如何设置企业项目请参考《企业管理用户指南》。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateDatabaseReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateDatabaseReq.

        标签

        :return: The tags of this CreateDatabaseReq.
        :rtype: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDatabaseReq.

        标签

        :param tags: The tags of this CreateDatabaseReq.
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateDatabaseReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
