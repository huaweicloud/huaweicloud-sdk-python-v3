# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyGroupForTemplate:

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
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'priority': 'priority',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, priority=None, description=None, create_time=None, update_time=None):
        r"""PolicyGroupForTemplate

        The model defined in huaweicloud sdk

        :param id: 策略组的唯一标识。
        :type id: str
        :param name: 策略组名称。
        :type name: str
        :param priority: 优先级。
        :type priority: int
        :param description: 服务器组描述。
        :type description: str
        :param create_time: 策略组创建时间。
        :type create_time: datetime
        :param update_time: 策略组更新时间。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._name = None
        self._priority = None
        self._description = None
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
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this PolicyGroupForTemplate.

        策略组的唯一标识。

        :return: The id of this PolicyGroupForTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PolicyGroupForTemplate.

        策略组的唯一标识。

        :param id: The id of this PolicyGroupForTemplate.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PolicyGroupForTemplate.

        策略组名称。

        :return: The name of this PolicyGroupForTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PolicyGroupForTemplate.

        策略组名称。

        :param name: The name of this PolicyGroupForTemplate.
        :type name: str
        """
        self._name = name

    @property
    def priority(self):
        r"""Gets the priority of this PolicyGroupForTemplate.

        优先级。

        :return: The priority of this PolicyGroupForTemplate.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this PolicyGroupForTemplate.

        优先级。

        :param priority: The priority of this PolicyGroupForTemplate.
        :type priority: int
        """
        self._priority = priority

    @property
    def description(self):
        r"""Gets the description of this PolicyGroupForTemplate.

        服务器组描述。

        :return: The description of this PolicyGroupForTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PolicyGroupForTemplate.

        服务器组描述。

        :param description: The description of this PolicyGroupForTemplate.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this PolicyGroupForTemplate.

        策略组创建时间。

        :return: The create_time of this PolicyGroupForTemplate.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PolicyGroupForTemplate.

        策略组创建时间。

        :param create_time: The create_time of this PolicyGroupForTemplate.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this PolicyGroupForTemplate.

        策略组更新时间。

        :return: The update_time of this PolicyGroupForTemplate.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PolicyGroupForTemplate.

        策略组更新时间。

        :param update_time: The update_time of this PolicyGroupForTemplate.
        :type update_time: datetime
        """
        self._update_time = update_time

    def to_dict(self):
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
        if not isinstance(other, PolicyGroupForTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
