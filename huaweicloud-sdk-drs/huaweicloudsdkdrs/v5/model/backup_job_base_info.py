# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupJobBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'engine_type': 'str',
        'description': 'str',
        'tags': 'list[ResourceTag]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'engine_type': 'engine_type',
        'description': 'description',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, engine_type=None, description=None, tags=None, enterprise_project_id=None):
        r"""BackupJobBaseInfo

        The model defined in huaweicloud sdk

        :param name: 任务名称。 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。   - 最小长度：4     - 最大长度：50
        :type name: str
        :param engine_type: 数据库引擎。  - sqlserver：RDS for SQL Server引擎
        :type engine_type: str
        :param description: 任务描述。
        :type description: str
        :param tags: 标签信息。 标签的值可以包含任意语种字母、数字、空格和_ . : / &#x3D; + - @。
        :type tags: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._engine_type = None
        self._description = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        self.engine_type = engine_type
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this BackupJobBaseInfo.

        任务名称。 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。   - 最小长度：4     - 最大长度：50

        :return: The name of this BackupJobBaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackupJobBaseInfo.

        任务名称。 约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。   - 最小长度：4     - 最大长度：50

        :param name: The name of this BackupJobBaseInfo.
        :type name: str
        """
        self._name = name

    @property
    def engine_type(self):
        r"""Gets the engine_type of this BackupJobBaseInfo.

        数据库引擎。  - sqlserver：RDS for SQL Server引擎

        :return: The engine_type of this BackupJobBaseInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this BackupJobBaseInfo.

        数据库引擎。  - sqlserver：RDS for SQL Server引擎

        :param engine_type: The engine_type of this BackupJobBaseInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def description(self):
        r"""Gets the description of this BackupJobBaseInfo.

        任务描述。

        :return: The description of this BackupJobBaseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BackupJobBaseInfo.

        任务描述。

        :param description: The description of this BackupJobBaseInfo.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this BackupJobBaseInfo.

        标签信息。 标签的值可以包含任意语种字母、数字、空格和_ . : / = + - @。

        :return: The tags of this BackupJobBaseInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BackupJobBaseInfo.

        标签信息。 标签的值可以包含任意语种字母、数字、空格和_ . : / = + - @。

        :param tags: The tags of this BackupJobBaseInfo.
        :type tags: list[:class:`huaweicloudsdkdrs.v5.ResourceTag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this BackupJobBaseInfo.

        企业项目ID。

        :return: The enterprise_project_id of this BackupJobBaseInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this BackupJobBaseInfo.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this BackupJobBaseInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, BackupJobBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
