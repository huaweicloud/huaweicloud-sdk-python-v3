# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'priority': 'int',
        'description': 'str',
        'targets': 'list[Target]',
        'policies': 'Policies',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'priority': 'priority',
        'description': 'description',
        'targets': 'targets',
        'policies': 'policies',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, priority=None, description=None, targets=None, policies=None, create_time=None, update_time=None):
        """PolicyGroup

        The model defined in huaweicloud sdk

        :param id: 策略组的唯一标识
        :type id: str
        :param name: 策略组名称
        :type name: str
        :param priority: 优先级
        :type priority: int
        :param description: 服务器组描述
        :type description: str
        :param targets: 应用对象列表。
        :type targets: list[:class:`huaweicloudsdkworkspaceapp.v1.Target`]
        :param policies: 
        :type policies: :class:`huaweicloudsdkworkspaceapp.v1.Policies`
        :param create_time: 策略组创建时间
        :type create_time: datetime
        :param update_time: 策略组更新时间
        :type update_time: datetime
        """
        
        

        self._id = None
        self._name = None
        self._priority = None
        self._description = None
        self._targets = None
        self._policies = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority
        if description is not None:
            self.description = description
        if targets is not None:
            self.targets = targets
        if policies is not None:
            self.policies = policies
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this PolicyGroup.

        策略组的唯一标识

        :return: The id of this PolicyGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyGroup.

        策略组的唯一标识

        :param id: The id of this PolicyGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PolicyGroup.

        策略组名称

        :return: The name of this PolicyGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyGroup.

        策略组名称

        :param name: The name of this PolicyGroup.
        :type name: str
        """
        self._name = name

    @property
    def priority(self):
        """Gets the priority of this PolicyGroup.

        优先级

        :return: The priority of this PolicyGroup.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PolicyGroup.

        优先级

        :param priority: The priority of this PolicyGroup.
        :type priority: int
        """
        self._priority = priority

    @property
    def description(self):
        """Gets the description of this PolicyGroup.

        服务器组描述

        :return: The description of this PolicyGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyGroup.

        服务器组描述

        :param description: The description of this PolicyGroup.
        :type description: str
        """
        self._description = description

    @property
    def targets(self):
        """Gets the targets of this PolicyGroup.

        应用对象列表。

        :return: The targets of this PolicyGroup.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.Target`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this PolicyGroup.

        应用对象列表。

        :param targets: The targets of this PolicyGroup.
        :type targets: list[:class:`huaweicloudsdkworkspaceapp.v1.Target`]
        """
        self._targets = targets

    @property
    def policies(self):
        """Gets the policies of this PolicyGroup.

        :return: The policies of this PolicyGroup.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Policies`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PolicyGroup.

        :param policies: The policies of this PolicyGroup.
        :type policies: :class:`huaweicloudsdkworkspaceapp.v1.Policies`
        """
        self._policies = policies

    @property
    def create_time(self):
        """Gets the create_time of this PolicyGroup.

        策略组创建时间

        :return: The create_time of this PolicyGroup.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PolicyGroup.

        策略组创建时间

        :param create_time: The create_time of this PolicyGroup.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this PolicyGroup.

        策略组更新时间

        :return: The update_time of this PolicyGroup.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this PolicyGroup.

        策略组更新时间

        :param update_time: The update_time of this PolicyGroup.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, PolicyGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
