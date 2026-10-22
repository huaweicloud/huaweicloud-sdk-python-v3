# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAiAppResponse(SdkResponse):

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
        'create_time': 'int',
        'protect_status': 'int',
        'policy': 'Policy'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'create_time': 'createTime',
        'protect_status': 'protectStatus',
        'policy': 'policy'
    }

    def __init__(self, id=None, name=None, description=None, create_time=None, protect_status=None, policy=None):
        r"""ShowAiAppResponse

        The model defined in huaweicloud sdk

        :param id: AI应用ID
        :type id: str
        :param name: AI应用名称
        :type name: str
        :param description: 应用描述
        :type description: str
        :param create_time: 创建时间戳（毫秒Unix时间戳）
        :type create_time: int
        :param protect_status: 防护状态（0：禁用，1：启用）
        :type protect_status: int
        :param policy: 
        :type policy: :class:`huaweicloudsdkwaf.v1.Policy`
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._create_time = None
        self._protect_status = None
        self._policy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if protect_status is not None:
            self.protect_status = protect_status
        if policy is not None:
            self.policy = policy

    @property
    def id(self):
        r"""Gets the id of this ShowAiAppResponse.

        AI应用ID

        :return: The id of this ShowAiAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAiAppResponse.

        AI应用ID

        :param id: The id of this ShowAiAppResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowAiAppResponse.

        AI应用名称

        :return: The name of this ShowAiAppResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAiAppResponse.

        AI应用名称

        :param name: The name of this ShowAiAppResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowAiAppResponse.

        应用描述

        :return: The description of this ShowAiAppResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowAiAppResponse.

        应用描述

        :param description: The description of this ShowAiAppResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowAiAppResponse.

        创建时间戳（毫秒Unix时间戳）

        :return: The create_time of this ShowAiAppResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowAiAppResponse.

        创建时间戳（毫秒Unix时间戳）

        :param create_time: The create_time of this ShowAiAppResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ShowAiAppResponse.

        防护状态（0：禁用，1：启用）

        :return: The protect_status of this ShowAiAppResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ShowAiAppResponse.

        防护状态（0：禁用，1：启用）

        :param protect_status: The protect_status of this ShowAiAppResponse.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def policy(self):
        r"""Gets the policy of this ShowAiAppResponse.

        :return: The policy of this ShowAiAppResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.Policy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ShowAiAppResponse.

        :param policy: The policy of this ShowAiAppResponse.
        :type policy: :class:`huaweicloudsdkwaf.v1.Policy`
        """
        self._policy = policy

    def to_dict(self):
        import warnings
        warnings.warn("ShowAiAppResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAiAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
