# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_type': 'object',
        'category': 'str',
        'connector_action_html': 'str',
        'connector_created_type': 'str',
        'connector_id': 'str',
        'connector_version': 'str',
        'created_time': 'datetime',
        'definition': 'object',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'operation_id': 'str',
        'swagger': 'object',
        'test_result': 'str',
        'updated_time': 'datetime',
        'visibility': 'str'
    }

    attribute_map = {
        'action_type': 'action_type',
        'category': 'category',
        'connector_action_html': 'connector_action_html',
        'connector_created_type': 'connector_created_type',
        'connector_id': 'connector_id',
        'connector_version': 'connector_version',
        'created_time': 'created_time',
        'definition': 'definition',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'operation_id': 'operation_id',
        'swagger': 'swagger',
        'test_result': 'test_result',
        'updated_time': 'updated_time',
        'visibility': 'visibility'
    }

    def __init__(self, action_type=None, category=None, connector_action_html=None, connector_created_type=None, connector_id=None, connector_version=None, created_time=None, definition=None, description=None, id=None, name=None, operation_id=None, swagger=None, test_result=None, updated_time=None, visibility=None):
        """ActionBaseInfo

        The model defined in huaweicloud sdk

        :param action_type: 执行动作的类型
        :type action_type: object
        :param category: 分类
        :type category: str
        :param connector_action_html: 
        :type connector_action_html: str
        :param connector_created_type: 
        :type connector_created_type: str
        :param connector_id: 自定义连接器ID
        :type connector_id: str
        :param connector_version: 连接器版本
        :type connector_version: str
        :param created_time: 创建时间
        :type created_time: datetime
        :param definition: 操作or触发器的详细定义
        :type definition: object
        :param description: 描述
        :type description: str
        :param id: 执行动作ID
        :type id: str
        :param name: 执行动作名称
        :type name: str
        :param operation_id: 执行动作ID
        :type operation_id: str
        :param swagger: swagger文档
        :type swagger: object
        :param test_result: 最近一次测试结果
        :type test_result: str
        :param updated_time: 修改时间
        :type updated_time: datetime
        :param visibility: 标记动作在流编排是否可见
        :type visibility: str
        """
        
        

        self._action_type = None
        self._category = None
        self._connector_action_html = None
        self._connector_created_type = None
        self._connector_id = None
        self._connector_version = None
        self._created_time = None
        self._definition = None
        self._description = None
        self._id = None
        self._name = None
        self._operation_id = None
        self._swagger = None
        self._test_result = None
        self._updated_time = None
        self._visibility = None
        self.discriminator = None

        if action_type is not None:
            self.action_type = action_type
        if category is not None:
            self.category = category
        if connector_action_html is not None:
            self.connector_action_html = connector_action_html
        if connector_created_type is not None:
            self.connector_created_type = connector_created_type
        if connector_id is not None:
            self.connector_id = connector_id
        if connector_version is not None:
            self.connector_version = connector_version
        if created_time is not None:
            self.created_time = created_time
        if definition is not None:
            self.definition = definition
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if operation_id is not None:
            self.operation_id = operation_id
        if swagger is not None:
            self.swagger = swagger
        if test_result is not None:
            self.test_result = test_result
        if updated_time is not None:
            self.updated_time = updated_time
        if visibility is not None:
            self.visibility = visibility

    @property
    def action_type(self):
        """Gets the action_type of this ActionBaseInfo.

        执行动作的类型

        :return: The action_type of this ActionBaseInfo.
        :rtype: object
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ActionBaseInfo.

        执行动作的类型

        :param action_type: The action_type of this ActionBaseInfo.
        :type action_type: object
        """
        self._action_type = action_type

    @property
    def category(self):
        """Gets the category of this ActionBaseInfo.

        分类

        :return: The category of this ActionBaseInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ActionBaseInfo.

        分类

        :param category: The category of this ActionBaseInfo.
        :type category: str
        """
        self._category = category

    @property
    def connector_action_html(self):
        """Gets the connector_action_html of this ActionBaseInfo.

        :return: The connector_action_html of this ActionBaseInfo.
        :rtype: str
        """
        return self._connector_action_html

    @connector_action_html.setter
    def connector_action_html(self, connector_action_html):
        """Sets the connector_action_html of this ActionBaseInfo.

        :param connector_action_html: The connector_action_html of this ActionBaseInfo.
        :type connector_action_html: str
        """
        self._connector_action_html = connector_action_html

    @property
    def connector_created_type(self):
        """Gets the connector_created_type of this ActionBaseInfo.

        :return: The connector_created_type of this ActionBaseInfo.
        :rtype: str
        """
        return self._connector_created_type

    @connector_created_type.setter
    def connector_created_type(self, connector_created_type):
        """Sets the connector_created_type of this ActionBaseInfo.

        :param connector_created_type: The connector_created_type of this ActionBaseInfo.
        :type connector_created_type: str
        """
        self._connector_created_type = connector_created_type

    @property
    def connector_id(self):
        """Gets the connector_id of this ActionBaseInfo.

        自定义连接器ID

        :return: The connector_id of this ActionBaseInfo.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this ActionBaseInfo.

        自定义连接器ID

        :param connector_id: The connector_id of this ActionBaseInfo.
        :type connector_id: str
        """
        self._connector_id = connector_id

    @property
    def connector_version(self):
        """Gets the connector_version of this ActionBaseInfo.

        连接器版本

        :return: The connector_version of this ActionBaseInfo.
        :rtype: str
        """
        return self._connector_version

    @connector_version.setter
    def connector_version(self, connector_version):
        """Sets the connector_version of this ActionBaseInfo.

        连接器版本

        :param connector_version: The connector_version of this ActionBaseInfo.
        :type connector_version: str
        """
        self._connector_version = connector_version

    @property
    def created_time(self):
        """Gets the created_time of this ActionBaseInfo.

        创建时间

        :return: The created_time of this ActionBaseInfo.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ActionBaseInfo.

        创建时间

        :param created_time: The created_time of this ActionBaseInfo.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def definition(self):
        """Gets the definition of this ActionBaseInfo.

        操作or触发器的详细定义

        :return: The definition of this ActionBaseInfo.
        :rtype: object
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this ActionBaseInfo.

        操作or触发器的详细定义

        :param definition: The definition of this ActionBaseInfo.
        :type definition: object
        """
        self._definition = definition

    @property
    def description(self):
        """Gets the description of this ActionBaseInfo.

        描述

        :return: The description of this ActionBaseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ActionBaseInfo.

        描述

        :param description: The description of this ActionBaseInfo.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this ActionBaseInfo.

        执行动作ID

        :return: The id of this ActionBaseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActionBaseInfo.

        执行动作ID

        :param id: The id of this ActionBaseInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ActionBaseInfo.

        执行动作名称

        :return: The name of this ActionBaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActionBaseInfo.

        执行动作名称

        :param name: The name of this ActionBaseInfo.
        :type name: str
        """
        self._name = name

    @property
    def operation_id(self):
        """Gets the operation_id of this ActionBaseInfo.

        执行动作ID

        :return: The operation_id of this ActionBaseInfo.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this ActionBaseInfo.

        执行动作ID

        :param operation_id: The operation_id of this ActionBaseInfo.
        :type operation_id: str
        """
        self._operation_id = operation_id

    @property
    def swagger(self):
        """Gets the swagger of this ActionBaseInfo.

        swagger文档

        :return: The swagger of this ActionBaseInfo.
        :rtype: object
        """
        return self._swagger

    @swagger.setter
    def swagger(self, swagger):
        """Sets the swagger of this ActionBaseInfo.

        swagger文档

        :param swagger: The swagger of this ActionBaseInfo.
        :type swagger: object
        """
        self._swagger = swagger

    @property
    def test_result(self):
        """Gets the test_result of this ActionBaseInfo.

        最近一次测试结果

        :return: The test_result of this ActionBaseInfo.
        :rtype: str
        """
        return self._test_result

    @test_result.setter
    def test_result(self, test_result):
        """Sets the test_result of this ActionBaseInfo.

        最近一次测试结果

        :param test_result: The test_result of this ActionBaseInfo.
        :type test_result: str
        """
        self._test_result = test_result

    @property
    def updated_time(self):
        """Gets the updated_time of this ActionBaseInfo.

        修改时间

        :return: The updated_time of this ActionBaseInfo.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ActionBaseInfo.

        修改时间

        :param updated_time: The updated_time of this ActionBaseInfo.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

    @property
    def visibility(self):
        """Gets the visibility of this ActionBaseInfo.

        标记动作在流编排是否可见

        :return: The visibility of this ActionBaseInfo.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this ActionBaseInfo.

        标记动作在流编排是否可见

        :param visibility: The visibility of this ActionBaseInfo.
        :type visibility: str
        """
        self._visibility = visibility

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
        if not isinstance(other, ActionBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
