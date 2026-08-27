# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelGroupItemVO:

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
        'description': 'str',
        'priority': 'int',
        'default_model_id': 'str',
        'provider_count': 'int',
        'resource_count': 'int',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'priority': 'priority',
        'default_model_id': 'default_model_id',
        'provider_count': 'provider_count',
        'resource_count': 'resource_count',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, priority=None, default_model_id=None, provider_count=None, resource_count=None, create_time=None, update_time=None):
        r"""ModelGroupItemVO

        The model defined in huaweicloud sdk

        :param id: 模型组id。
        :type id: str
        :param name: 分组名称。
        :type name: str
        :param description: 分组描述。
        :type description: str
        :param priority: 分组优先级。
        :type priority: int
        :param default_model_id: 默认模型ID。
        :type default_model_id: str
        :param provider_count: 关联的供应商数量。
        :type provider_count: int
        :param resource_count: 关联的应用对象数量（Agent实例+桌面标签）。
        :type resource_count: int
        :param create_time: 创建时间（ISO8601格式，UTC时区）。
        :type create_time: str
        :param update_time: 更新时间（ISO8601格式，UTC时区）。
        :type update_time: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._priority = None
        self._default_model_id = None
        self._provider_count = None
        self._resource_count = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if priority is not None:
            self.priority = priority
        if default_model_id is not None:
            self.default_model_id = default_model_id
        if provider_count is not None:
            self.provider_count = provider_count
        if resource_count is not None:
            self.resource_count = resource_count
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ModelGroupItemVO.

        模型组id。

        :return: The id of this ModelGroupItemVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelGroupItemVO.

        模型组id。

        :param id: The id of this ModelGroupItemVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ModelGroupItemVO.

        分组名称。

        :return: The name of this ModelGroupItemVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModelGroupItemVO.

        分组名称。

        :param name: The name of this ModelGroupItemVO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ModelGroupItemVO.

        分组描述。

        :return: The description of this ModelGroupItemVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModelGroupItemVO.

        分组描述。

        :param description: The description of this ModelGroupItemVO.
        :type description: str
        """
        self._description = description

    @property
    def priority(self):
        r"""Gets the priority of this ModelGroupItemVO.

        分组优先级。

        :return: The priority of this ModelGroupItemVO.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ModelGroupItemVO.

        分组优先级。

        :param priority: The priority of this ModelGroupItemVO.
        :type priority: int
        """
        self._priority = priority

    @property
    def default_model_id(self):
        r"""Gets the default_model_id of this ModelGroupItemVO.

        默认模型ID。

        :return: The default_model_id of this ModelGroupItemVO.
        :rtype: str
        """
        return self._default_model_id

    @default_model_id.setter
    def default_model_id(self, default_model_id):
        r"""Sets the default_model_id of this ModelGroupItemVO.

        默认模型ID。

        :param default_model_id: The default_model_id of this ModelGroupItemVO.
        :type default_model_id: str
        """
        self._default_model_id = default_model_id

    @property
    def provider_count(self):
        r"""Gets the provider_count of this ModelGroupItemVO.

        关联的供应商数量。

        :return: The provider_count of this ModelGroupItemVO.
        :rtype: int
        """
        return self._provider_count

    @provider_count.setter
    def provider_count(self, provider_count):
        r"""Sets the provider_count of this ModelGroupItemVO.

        关联的供应商数量。

        :param provider_count: The provider_count of this ModelGroupItemVO.
        :type provider_count: int
        """
        self._provider_count = provider_count

    @property
    def resource_count(self):
        r"""Gets the resource_count of this ModelGroupItemVO.

        关联的应用对象数量（Agent实例+桌面标签）。

        :return: The resource_count of this ModelGroupItemVO.
        :rtype: int
        """
        return self._resource_count

    @resource_count.setter
    def resource_count(self, resource_count):
        r"""Sets the resource_count of this ModelGroupItemVO.

        关联的应用对象数量（Agent实例+桌面标签）。

        :param resource_count: The resource_count of this ModelGroupItemVO.
        :type resource_count: int
        """
        self._resource_count = resource_count

    @property
    def create_time(self):
        r"""Gets the create_time of this ModelGroupItemVO.

        创建时间（ISO8601格式，UTC时区）。

        :return: The create_time of this ModelGroupItemVO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ModelGroupItemVO.

        创建时间（ISO8601格式，UTC时区）。

        :param create_time: The create_time of this ModelGroupItemVO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ModelGroupItemVO.

        更新时间（ISO8601格式，UTC时区）。

        :return: The update_time of this ModelGroupItemVO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ModelGroupItemVO.

        更新时间（ISO8601格式，UTC时区）。

        :param update_time: The update_time of this ModelGroupItemVO.
        :type update_time: str
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
        if not isinstance(other, ModelGroupItemVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
