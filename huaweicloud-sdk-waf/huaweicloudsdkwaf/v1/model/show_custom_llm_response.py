# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomLlmResponse(SdkResponse):

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
        'model_name': 'str',
        'protocol': 'str',
        'url': 'str',
        'referenced_policies': 'list[ReferencedPolicy]',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'model_name': 'model_name',
        'protocol': 'protocol',
        'url': 'url',
        'referenced_policies': 'referenced_policies',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, model_name=None, protocol=None, url=None, referenced_policies=None, create_time=None, update_time=None):
        r"""ShowCustomLlmResponse

        The model defined in huaweicloud sdk

        :param id: 自定义大模型ID
        :type id: str
        :param name: 自定义大模型名称
        :type name: str
        :param description: 自定义大模型描述
        :type description: str
        :param model_name: 模型名称
        :type model_name: str
        :param protocol: 协议类型
        :type protocol: str
        :param url: API地址
        :type url: str
        :param referenced_policies: 引用的策略列表
        :type referenced_policies: list[:class:`huaweicloudsdkwaf.v1.ReferencedPolicy`]
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._model_name = None
        self._protocol = None
        self._url = None
        self._referenced_policies = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if model_name is not None:
            self.model_name = model_name
        if protocol is not None:
            self.protocol = protocol
        if url is not None:
            self.url = url
        if referenced_policies is not None:
            self.referenced_policies = referenced_policies
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ShowCustomLlmResponse.

        自定义大模型ID

        :return: The id of this ShowCustomLlmResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowCustomLlmResponse.

        自定义大模型ID

        :param id: The id of this ShowCustomLlmResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowCustomLlmResponse.

        自定义大模型名称

        :return: The name of this ShowCustomLlmResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowCustomLlmResponse.

        自定义大模型名称

        :param name: The name of this ShowCustomLlmResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowCustomLlmResponse.

        自定义大模型描述

        :return: The description of this ShowCustomLlmResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowCustomLlmResponse.

        自定义大模型描述

        :param description: The description of this ShowCustomLlmResponse.
        :type description: str
        """
        self._description = description

    @property
    def model_name(self):
        r"""Gets the model_name of this ShowCustomLlmResponse.

        模型名称

        :return: The model_name of this ShowCustomLlmResponse.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this ShowCustomLlmResponse.

        模型名称

        :param model_name: The model_name of this ShowCustomLlmResponse.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def protocol(self):
        r"""Gets the protocol of this ShowCustomLlmResponse.

        协议类型

        :return: The protocol of this ShowCustomLlmResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ShowCustomLlmResponse.

        协议类型

        :param protocol: The protocol of this ShowCustomLlmResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def url(self):
        r"""Gets the url of this ShowCustomLlmResponse.

        API地址

        :return: The url of this ShowCustomLlmResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowCustomLlmResponse.

        API地址

        :param url: The url of this ShowCustomLlmResponse.
        :type url: str
        """
        self._url = url

    @property
    def referenced_policies(self):
        r"""Gets the referenced_policies of this ShowCustomLlmResponse.

        引用的策略列表

        :return: The referenced_policies of this ShowCustomLlmResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.ReferencedPolicy`]
        """
        return self._referenced_policies

    @referenced_policies.setter
    def referenced_policies(self, referenced_policies):
        r"""Sets the referenced_policies of this ShowCustomLlmResponse.

        引用的策略列表

        :param referenced_policies: The referenced_policies of this ShowCustomLlmResponse.
        :type referenced_policies: list[:class:`huaweicloudsdkwaf.v1.ReferencedPolicy`]
        """
        self._referenced_policies = referenced_policies

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowCustomLlmResponse.

        创建时间

        :return: The create_time of this ShowCustomLlmResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowCustomLlmResponse.

        创建时间

        :param create_time: The create_time of this ShowCustomLlmResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowCustomLlmResponse.

        更新时间

        :return: The update_time of this ShowCustomLlmResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowCustomLlmResponse.

        更新时间

        :param update_time: The update_time of this ShowCustomLlmResponse.
        :type update_time: int
        """
        self._update_time = update_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowCustomLlmResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowCustomLlmResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
