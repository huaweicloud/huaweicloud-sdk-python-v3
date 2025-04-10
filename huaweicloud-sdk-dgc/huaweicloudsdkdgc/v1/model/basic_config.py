# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner': 'str',
        'agency': 'str',
        'is_ignore_waiting': 'int',
        'priority': 'int',
        'execute_user': 'str',
        'instance_timeout': 'int',
        'custom_fields': 'object',
        'tags': 'list[str]'
    }

    attribute_map = {
        'owner': 'owner',
        'agency': 'agency',
        'is_ignore_waiting': 'isIgnoreWaiting',
        'priority': 'priority',
        'execute_user': 'executeUser',
        'instance_timeout': 'instanceTimeout',
        'custom_fields': 'customFields',
        'tags': 'tags'
    }

    def __init__(self, owner=None, agency=None, is_ignore_waiting=None, priority=None, execute_user=None, instance_timeout=None, custom_fields=None, tags=None):
        r"""BasicConfig

        The model defined in huaweicloud sdk

        :param owner: 作业责任人
        :type owner: str
        :param agency: 作业委托的名称
        :type agency: str
        :param is_ignore_waiting: 实例超时是否忽略等待时间, 取值范围为0和1, 0：表示实例超时不忽略等待时间1：表示实例超时忽略等待时间
        :type is_ignore_waiting: int
        :param priority: 作业优先级
        :type priority: int
        :param execute_user: 作业执行用户
        :type execute_user: str
        :param instance_timeout: 实例超时时间
        :type instance_timeout: int
        :param custom_fields: 用户自定义属性字段
        :type custom_fields: object
        :param tags: 作业标签列表
        :type tags: list[str]
        """
        
        

        self._owner = None
        self._agency = None
        self._is_ignore_waiting = None
        self._priority = None
        self._execute_user = None
        self._instance_timeout = None
        self._custom_fields = None
        self._tags = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if agency is not None:
            self.agency = agency
        if is_ignore_waiting is not None:
            self.is_ignore_waiting = is_ignore_waiting
        if priority is not None:
            self.priority = priority
        if execute_user is not None:
            self.execute_user = execute_user
        if instance_timeout is not None:
            self.instance_timeout = instance_timeout
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if tags is not None:
            self.tags = tags

    @property
    def owner(self):
        r"""Gets the owner of this BasicConfig.

        作业责任人

        :return: The owner of this BasicConfig.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this BasicConfig.

        作业责任人

        :param owner: The owner of this BasicConfig.
        :type owner: str
        """
        self._owner = owner

    @property
    def agency(self):
        r"""Gets the agency of this BasicConfig.

        作业委托的名称

        :return: The agency of this BasicConfig.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this BasicConfig.

        作业委托的名称

        :param agency: The agency of this BasicConfig.
        :type agency: str
        """
        self._agency = agency

    @property
    def is_ignore_waiting(self):
        r"""Gets the is_ignore_waiting of this BasicConfig.

        实例超时是否忽略等待时间, 取值范围为0和1, 0：表示实例超时不忽略等待时间1：表示实例超时忽略等待时间

        :return: The is_ignore_waiting of this BasicConfig.
        :rtype: int
        """
        return self._is_ignore_waiting

    @is_ignore_waiting.setter
    def is_ignore_waiting(self, is_ignore_waiting):
        r"""Sets the is_ignore_waiting of this BasicConfig.

        实例超时是否忽略等待时间, 取值范围为0和1, 0：表示实例超时不忽略等待时间1：表示实例超时忽略等待时间

        :param is_ignore_waiting: The is_ignore_waiting of this BasicConfig.
        :type is_ignore_waiting: int
        """
        self._is_ignore_waiting = is_ignore_waiting

    @property
    def priority(self):
        r"""Gets the priority of this BasicConfig.

        作业优先级

        :return: The priority of this BasicConfig.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this BasicConfig.

        作业优先级

        :param priority: The priority of this BasicConfig.
        :type priority: int
        """
        self._priority = priority

    @property
    def execute_user(self):
        r"""Gets the execute_user of this BasicConfig.

        作业执行用户

        :return: The execute_user of this BasicConfig.
        :rtype: str
        """
        return self._execute_user

    @execute_user.setter
    def execute_user(self, execute_user):
        r"""Sets the execute_user of this BasicConfig.

        作业执行用户

        :param execute_user: The execute_user of this BasicConfig.
        :type execute_user: str
        """
        self._execute_user = execute_user

    @property
    def instance_timeout(self):
        r"""Gets the instance_timeout of this BasicConfig.

        实例超时时间

        :return: The instance_timeout of this BasicConfig.
        :rtype: int
        """
        return self._instance_timeout

    @instance_timeout.setter
    def instance_timeout(self, instance_timeout):
        r"""Sets the instance_timeout of this BasicConfig.

        实例超时时间

        :param instance_timeout: The instance_timeout of this BasicConfig.
        :type instance_timeout: int
        """
        self._instance_timeout = instance_timeout

    @property
    def custom_fields(self):
        r"""Gets the custom_fields of this BasicConfig.

        用户自定义属性字段

        :return: The custom_fields of this BasicConfig.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        r"""Sets the custom_fields of this BasicConfig.

        用户自定义属性字段

        :param custom_fields: The custom_fields of this BasicConfig.
        :type custom_fields: object
        """
        self._custom_fields = custom_fields

    @property
    def tags(self):
        r"""Gets the tags of this BasicConfig.

        作业标签列表

        :return: The tags of this BasicConfig.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BasicConfig.

        作业标签列表

        :param tags: The tags of this BasicConfig.
        :type tags: list[str]
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
        if not isinstance(other, BasicConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
