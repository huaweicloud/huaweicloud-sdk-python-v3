# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKeyPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'policy_name': 'str',
        'keyspace_id': 'str',
        'policy': 'ShowKeyPolicyResponseBodyPolicy',
        'description': 'str',
        'created_by': 'str',
        'create_time': 'str',
        'last_modify_time': 'str',
        'last_access_time': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'keyspace_id': 'keyspace_id',
        'policy': 'policy',
        'description': 'description',
        'created_by': 'created_by',
        'create_time': 'create_time',
        'last_modify_time': 'last_modify_time',
        'last_access_time': 'last_access_time'
    }

    def __init__(self, policy_id=None, policy_name=None, keyspace_id=None, policy=None, description=None, created_by=None, create_time=None, last_modify_time=None, last_access_time=None):
        r"""ShowKeyPolicyResponse

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释：** 密钥策略ID **取值范围：** 不涉及
        :type policy_id: str
        :param policy_name: **参数解释：** 密钥策略名称 **取值范围：** 不涉及
        :type policy_name: str
        :param keyspace_id: **参数解释：** 密钥空间ID **取值范围：** 不涉及
        :type keyspace_id: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkkms.v2.ShowKeyPolicyResponseBodyPolicy`
        :param description: **参数解释：** 密钥策略描述信息 **取值范围：** 不涉及
        :type description: str
        :param created_by: **参数解释：** 密钥策略创建人 **取值范围：** 不涉及
        :type created_by: str
        :param create_time: **参数解释：** 密钥策略创建时间 **取值范围：** 不涉及
        :type create_time: str
        :param last_modify_time: **参数解释：** 密钥策略最近修改时间 **取值范围：** 不涉及
        :type last_modify_time: str
        :param last_access_time: **参数解释：** 密钥策略最近访问时间 **取值范围：** 不涉及
        :type last_access_time: str
        """
        
        super().__init__()

        self._policy_id = None
        self._policy_name = None
        self._keyspace_id = None
        self._policy = None
        self._description = None
        self._created_by = None
        self._create_time = None
        self._last_modify_time = None
        self._last_access_time = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if keyspace_id is not None:
            self.keyspace_id = keyspace_id
        if policy is not None:
            self.policy = policy
        if description is not None:
            self.description = description
        if created_by is not None:
            self.created_by = created_by
        if create_time is not None:
            self.create_time = create_time
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time
        if last_access_time is not None:
            self.last_access_time = last_access_time

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略ID **取值范围：** 不涉及

        :return: The policy_id of this ShowKeyPolicyResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略ID **取值范围：** 不涉及

        :param policy_id: The policy_id of this ShowKeyPolicyResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略名称 **取值范围：** 不涉及

        :return: The policy_name of this ShowKeyPolicyResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略名称 **取值范围：** 不涉及

        :param policy_name: The policy_name of this ShowKeyPolicyResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def keyspace_id(self):
        r"""Gets the keyspace_id of this ShowKeyPolicyResponse.

        **参数解释：** 密钥空间ID **取值范围：** 不涉及

        :return: The keyspace_id of this ShowKeyPolicyResponse.
        :rtype: str
        """
        return self._keyspace_id

    @keyspace_id.setter
    def keyspace_id(self, keyspace_id):
        r"""Sets the keyspace_id of this ShowKeyPolicyResponse.

        **参数解释：** 密钥空间ID **取值范围：** 不涉及

        :param keyspace_id: The keyspace_id of this ShowKeyPolicyResponse.
        :type keyspace_id: str
        """
        self._keyspace_id = keyspace_id

    @property
    def policy(self):
        r"""Gets the policy of this ShowKeyPolicyResponse.

        :return: The policy of this ShowKeyPolicyResponse.
        :rtype: :class:`huaweicloudsdkkms.v2.ShowKeyPolicyResponseBodyPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ShowKeyPolicyResponse.

        :param policy: The policy of this ShowKeyPolicyResponse.
        :type policy: :class:`huaweicloudsdkkms.v2.ShowKeyPolicyResponseBodyPolicy`
        """
        self._policy = policy

    @property
    def description(self):
        r"""Gets the description of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略描述信息 **取值范围：** 不涉及

        :return: The description of this ShowKeyPolicyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略描述信息 **取值范围：** 不涉及

        :param description: The description of this ShowKeyPolicyResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_by(self):
        r"""Gets the created_by of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略创建人 **取值范围：** 不涉及

        :return: The created_by of this ShowKeyPolicyResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略创建人 **取值范围：** 不涉及

        :param created_by: The created_by of this ShowKeyPolicyResponse.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略创建时间 **取值范围：** 不涉及

        :return: The create_time of this ShowKeyPolicyResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略创建时间 **取值范围：** 不涉及

        :param create_time: The create_time of this ShowKeyPolicyResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modify_time(self):
        r"""Gets the last_modify_time of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略最近修改时间 **取值范围：** 不涉及

        :return: The last_modify_time of this ShowKeyPolicyResponse.
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        r"""Sets the last_modify_time of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略最近修改时间 **取值范围：** 不涉及

        :param last_modify_time: The last_modify_time of this ShowKeyPolicyResponse.
        :type last_modify_time: str
        """
        self._last_modify_time = last_modify_time

    @property
    def last_access_time(self):
        r"""Gets the last_access_time of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略最近访问时间 **取值范围：** 不涉及

        :return: The last_access_time of this ShowKeyPolicyResponse.
        :rtype: str
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        r"""Sets the last_access_time of this ShowKeyPolicyResponse.

        **参数解释：** 密钥策略最近访问时间 **取值范围：** 不涉及

        :param last_access_time: The last_access_time of this ShowKeyPolicyResponse.
        :type last_access_time: str
        """
        self._last_access_time = last_access_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowKeyPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowKeyPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
