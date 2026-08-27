# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceModelGroupItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'default_model_id': 'str',
        'priority': 'int',
        'update_time': 'str',
        'providers': 'list[InstanceModelProviderConfig]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'default_model_id': 'default_model_id',
        'priority': 'priority',
        'update_time': 'update_time',
        'providers': 'providers'
    }

    def __init__(self, group_id=None, group_name=None, default_model_id=None, priority=None, update_time=None, providers=None):
        r"""InstanceModelGroupItem

        The model defined in huaweicloud sdk

        :param group_id: 模型分组 ID
        :type group_id: str
        :param group_name: 模型分组名称
        :type group_name: str
        :param default_model_id: 分组内默认模型 ID，未设置时为空
        :type default_model_id: str
        :param priority: 分组优先级（数值越小优先级越高）
        :type priority: int
        :param update_time: 模型分组更新时间
        :type update_time: str
        :param providers: 供应商配置列表（不含 API Key）
        :type providers: list[:class:`huaweicloudsdkworkspace.v2.InstanceModelProviderConfig`]
        """
        
        

        self._group_id = None
        self._group_name = None
        self._default_model_id = None
        self._priority = None
        self._update_time = None
        self._providers = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if default_model_id is not None:
            self.default_model_id = default_model_id
        if priority is not None:
            self.priority = priority
        if update_time is not None:
            self.update_time = update_time
        if providers is not None:
            self.providers = providers

    @property
    def group_id(self):
        r"""Gets the group_id of this InstanceModelGroupItem.

        模型分组 ID

        :return: The group_id of this InstanceModelGroupItem.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this InstanceModelGroupItem.

        模型分组 ID

        :param group_id: The group_id of this InstanceModelGroupItem.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this InstanceModelGroupItem.

        模型分组名称

        :return: The group_name of this InstanceModelGroupItem.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this InstanceModelGroupItem.

        模型分组名称

        :param group_name: The group_name of this InstanceModelGroupItem.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def default_model_id(self):
        r"""Gets the default_model_id of this InstanceModelGroupItem.

        分组内默认模型 ID，未设置时为空

        :return: The default_model_id of this InstanceModelGroupItem.
        :rtype: str
        """
        return self._default_model_id

    @default_model_id.setter
    def default_model_id(self, default_model_id):
        r"""Sets the default_model_id of this InstanceModelGroupItem.

        分组内默认模型 ID，未设置时为空

        :param default_model_id: The default_model_id of this InstanceModelGroupItem.
        :type default_model_id: str
        """
        self._default_model_id = default_model_id

    @property
    def priority(self):
        r"""Gets the priority of this InstanceModelGroupItem.

        分组优先级（数值越小优先级越高）

        :return: The priority of this InstanceModelGroupItem.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this InstanceModelGroupItem.

        分组优先级（数值越小优先级越高）

        :param priority: The priority of this InstanceModelGroupItem.
        :type priority: int
        """
        self._priority = priority

    @property
    def update_time(self):
        r"""Gets the update_time of this InstanceModelGroupItem.

        模型分组更新时间

        :return: The update_time of this InstanceModelGroupItem.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this InstanceModelGroupItem.

        模型分组更新时间

        :param update_time: The update_time of this InstanceModelGroupItem.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def providers(self):
        r"""Gets the providers of this InstanceModelGroupItem.

        供应商配置列表（不含 API Key）

        :return: The providers of this InstanceModelGroupItem.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.InstanceModelProviderConfig`]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        r"""Sets the providers of this InstanceModelGroupItem.

        供应商配置列表（不含 API Key）

        :param providers: The providers of this InstanceModelGroupItem.
        :type providers: list[:class:`huaweicloudsdkworkspace.v2.InstanceModelProviderConfig`]
        """
        self._providers = providers

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
        if not isinstance(other, InstanceModelGroupItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
