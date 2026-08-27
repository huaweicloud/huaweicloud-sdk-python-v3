# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModelGroupResponse(SdkResponse):

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
        'providers': 'list[ModelGroupProviderItemResp]',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'priority': 'priority',
        'default_model_id': 'default_model_id',
        'providers': 'providers',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, priority=None, default_model_id=None, providers=None, create_time=None, update_time=None):
        r"""CreateModelGroupResponse

        The model defined in huaweicloud sdk

        :param id: 分组id。
        :type id: str
        :param name: 分组名称。
        :type name: str
        :param description: 分组描述。
        :type description: str
        :param priority: 分组优先级。
        :type priority: int
        :param default_model_id: 默认模型ID。
        :type default_model_id: str
        :param providers: 关联的供应商关联记录列表。
        :type providers: list[:class:`huaweicloudsdkworkspace.v2.ModelGroupProviderItemResp`]
        :param create_time: 创建时间（ISO8601格式，UTC时区）。
        :type create_time: str
        :param update_time: 更新时间（ISO8601格式，UTC时区）。
        :type update_time: str
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._priority = None
        self._default_model_id = None
        self._providers = None
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
        if providers is not None:
            self.providers = providers
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this CreateModelGroupResponse.

        分组id。

        :return: The id of this CreateModelGroupResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateModelGroupResponse.

        分组id。

        :param id: The id of this CreateModelGroupResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateModelGroupResponse.

        分组名称。

        :return: The name of this CreateModelGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateModelGroupResponse.

        分组名称。

        :param name: The name of this CreateModelGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateModelGroupResponse.

        分组描述。

        :return: The description of this CreateModelGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateModelGroupResponse.

        分组描述。

        :param description: The description of this CreateModelGroupResponse.
        :type description: str
        """
        self._description = description

    @property
    def priority(self):
        r"""Gets the priority of this CreateModelGroupResponse.

        分组优先级。

        :return: The priority of this CreateModelGroupResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CreateModelGroupResponse.

        分组优先级。

        :param priority: The priority of this CreateModelGroupResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def default_model_id(self):
        r"""Gets the default_model_id of this CreateModelGroupResponse.

        默认模型ID。

        :return: The default_model_id of this CreateModelGroupResponse.
        :rtype: str
        """
        return self._default_model_id

    @default_model_id.setter
    def default_model_id(self, default_model_id):
        r"""Sets the default_model_id of this CreateModelGroupResponse.

        默认模型ID。

        :param default_model_id: The default_model_id of this CreateModelGroupResponse.
        :type default_model_id: str
        """
        self._default_model_id = default_model_id

    @property
    def providers(self):
        r"""Gets the providers of this CreateModelGroupResponse.

        关联的供应商关联记录列表。

        :return: The providers of this CreateModelGroupResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ModelGroupProviderItemResp`]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        r"""Sets the providers of this CreateModelGroupResponse.

        关联的供应商关联记录列表。

        :param providers: The providers of this CreateModelGroupResponse.
        :type providers: list[:class:`huaweicloudsdkworkspace.v2.ModelGroupProviderItemResp`]
        """
        self._providers = providers

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateModelGroupResponse.

        创建时间（ISO8601格式，UTC时区）。

        :return: The create_time of this CreateModelGroupResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateModelGroupResponse.

        创建时间（ISO8601格式，UTC时区）。

        :param create_time: The create_time of this CreateModelGroupResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateModelGroupResponse.

        更新时间（ISO8601格式，UTC时区）。

        :return: The update_time of this CreateModelGroupResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateModelGroupResponse.

        更新时间（ISO8601格式，UTC时区）。

        :param update_time: The update_time of this CreateModelGroupResponse.
        :type update_time: str
        """
        self._update_time = update_time

    def to_dict(self):
        import warnings
        warnings.warn("CreateModelGroupResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateModelGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
