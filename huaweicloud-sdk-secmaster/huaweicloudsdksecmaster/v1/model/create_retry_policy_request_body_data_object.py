# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRetryPolicyRequestBodyDataObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retry_list': 'list[str]',
        'block_age': 'CreateRetryPolicyRequestBodyDataObjectBlockAge',
        'block_target': 'str',
        'defense_policy_list': 'list[CreateRetryPolicyRequestBodyDataObjectDefensePolicyList]',
        'description': 'str',
        'labels': 'str',
        'policy_category': 'str',
        'policy_type': 'CreateRetryPolicyRequestBodyDataObjectPolicyType',
        'region_id': 'str',
        'policy_direction': 'str',
        'account_scope': 'str',
        'eps_scope': 'str',
        'region_scope': 'str'
    }

    attribute_map = {
        'retry_list': 'retry_list',
        'block_age': 'block_age',
        'block_target': 'block_target',
        'defense_policy_list': 'defense_policy_list',
        'description': 'description',
        'labels': 'labels',
        'policy_category': 'policy_category',
        'policy_type': 'policy_type',
        'region_id': 'region_id',
        'policy_direction': 'policy_direction',
        'account_scope': 'account_scope',
        'eps_scope': 'eps_scope',
        'region_scope': 'region_scope'
    }

    def __init__(self, retry_list=None, block_age=None, block_target=None, defense_policy_list=None, description=None, labels=None, policy_category=None, policy_type=None, region_id=None, policy_direction=None, account_scope=None, eps_scope=None, region_scope=None):
        r"""CreateRetryPolicyRequestBodyDataObject

        The model defined in huaweicloud sdk

        :param retry_list: 重试策略ID
        :type retry_list: list[str]
        :param block_age: 
        :type block_age: :class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyRequestBodyDataObjectBlockAge`
        :param block_target: 策略对象
        :type block_target: str
        :param defense_policy_list: 与操作连接对应的策略列表
        :type defense_policy_list: list[:class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyRequestBodyDataObjectDefensePolicyList`]
        :param description: 描述信息
        :type description: str
        :param labels: 标签
        :type labels: str
        :param policy_category: 类型,WHITE/BLOCK,WHITE代表加白(将ip等对象加入白名单),BLOCK代表阻断(将ip等对象加入黑名单)
        :type policy_category: str
        :param policy_type: 
        :type policy_type: :class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyRequestBodyDataObjectPolicyType`
        :param region_id: 区域ID
        :type region_id: str
        :param policy_direction: 出入方向
        :type policy_direction: str
        :param account_scope: 账号范围
        :type account_scope: str
        :param eps_scope: 企业项目范围
        :type eps_scope: str
        :param region_scope: region范围
        :type region_scope: str
        """
        
        

        self._retry_list = None
        self._block_age = None
        self._block_target = None
        self._defense_policy_list = None
        self._description = None
        self._labels = None
        self._policy_category = None
        self._policy_type = None
        self._region_id = None
        self._policy_direction = None
        self._account_scope = None
        self._eps_scope = None
        self._region_scope = None
        self.discriminator = None

        if retry_list is not None:
            self.retry_list = retry_list
        self.block_age = block_age
        self.block_target = block_target
        self.defense_policy_list = defense_policy_list
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        self.policy_category = policy_category
        self.policy_type = policy_type
        self.region_id = region_id
        if policy_direction is not None:
            self.policy_direction = policy_direction
        if account_scope is not None:
            self.account_scope = account_scope
        if eps_scope is not None:
            self.eps_scope = eps_scope
        if region_scope is not None:
            self.region_scope = region_scope

    @property
    def retry_list(self):
        r"""Gets the retry_list of this CreateRetryPolicyRequestBodyDataObject.

        重试策略ID

        :return: The retry_list of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: list[str]
        """
        return self._retry_list

    @retry_list.setter
    def retry_list(self, retry_list):
        r"""Sets the retry_list of this CreateRetryPolicyRequestBodyDataObject.

        重试策略ID

        :param retry_list: The retry_list of this CreateRetryPolicyRequestBodyDataObject.
        :type retry_list: list[str]
        """
        self._retry_list = retry_list

    @property
    def block_age(self):
        r"""Gets the block_age of this CreateRetryPolicyRequestBodyDataObject.

        :return: The block_age of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyRequestBodyDataObjectBlockAge`
        """
        return self._block_age

    @block_age.setter
    def block_age(self, block_age):
        r"""Sets the block_age of this CreateRetryPolicyRequestBodyDataObject.

        :param block_age: The block_age of this CreateRetryPolicyRequestBodyDataObject.
        :type block_age: :class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyRequestBodyDataObjectBlockAge`
        """
        self._block_age = block_age

    @property
    def block_target(self):
        r"""Gets the block_target of this CreateRetryPolicyRequestBodyDataObject.

        策略对象

        :return: The block_target of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: str
        """
        return self._block_target

    @block_target.setter
    def block_target(self, block_target):
        r"""Sets the block_target of this CreateRetryPolicyRequestBodyDataObject.

        策略对象

        :param block_target: The block_target of this CreateRetryPolicyRequestBodyDataObject.
        :type block_target: str
        """
        self._block_target = block_target

    @property
    def defense_policy_list(self):
        r"""Gets the defense_policy_list of this CreateRetryPolicyRequestBodyDataObject.

        与操作连接对应的策略列表

        :return: The defense_policy_list of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyRequestBodyDataObjectDefensePolicyList`]
        """
        return self._defense_policy_list

    @defense_policy_list.setter
    def defense_policy_list(self, defense_policy_list):
        r"""Sets the defense_policy_list of this CreateRetryPolicyRequestBodyDataObject.

        与操作连接对应的策略列表

        :param defense_policy_list: The defense_policy_list of this CreateRetryPolicyRequestBodyDataObject.
        :type defense_policy_list: list[:class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyRequestBodyDataObjectDefensePolicyList`]
        """
        self._defense_policy_list = defense_policy_list

    @property
    def description(self):
        r"""Gets the description of this CreateRetryPolicyRequestBodyDataObject.

        描述信息

        :return: The description of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateRetryPolicyRequestBodyDataObject.

        描述信息

        :param description: The description of this CreateRetryPolicyRequestBodyDataObject.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        r"""Gets the labels of this CreateRetryPolicyRequestBodyDataObject.

        标签

        :return: The labels of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateRetryPolicyRequestBodyDataObject.

        标签

        :param labels: The labels of this CreateRetryPolicyRequestBodyDataObject.
        :type labels: str
        """
        self._labels = labels

    @property
    def policy_category(self):
        r"""Gets the policy_category of this CreateRetryPolicyRequestBodyDataObject.

        类型,WHITE/BLOCK,WHITE代表加白(将ip等对象加入白名单),BLOCK代表阻断(将ip等对象加入黑名单)

        :return: The policy_category of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: str
        """
        return self._policy_category

    @policy_category.setter
    def policy_category(self, policy_category):
        r"""Sets the policy_category of this CreateRetryPolicyRequestBodyDataObject.

        类型,WHITE/BLOCK,WHITE代表加白(将ip等对象加入白名单),BLOCK代表阻断(将ip等对象加入黑名单)

        :param policy_category: The policy_category of this CreateRetryPolicyRequestBodyDataObject.
        :type policy_category: str
        """
        self._policy_category = policy_category

    @property
    def policy_type(self):
        r"""Gets the policy_type of this CreateRetryPolicyRequestBodyDataObject.

        :return: The policy_type of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyRequestBodyDataObjectPolicyType`
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this CreateRetryPolicyRequestBodyDataObject.

        :param policy_type: The policy_type of this CreateRetryPolicyRequestBodyDataObject.
        :type policy_type: :class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyRequestBodyDataObjectPolicyType`
        """
        self._policy_type = policy_type

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateRetryPolicyRequestBodyDataObject.

        区域ID

        :return: The region_id of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateRetryPolicyRequestBodyDataObject.

        区域ID

        :param region_id: The region_id of this CreateRetryPolicyRequestBodyDataObject.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def policy_direction(self):
        r"""Gets the policy_direction of this CreateRetryPolicyRequestBodyDataObject.

        出入方向

        :return: The policy_direction of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: str
        """
        return self._policy_direction

    @policy_direction.setter
    def policy_direction(self, policy_direction):
        r"""Sets the policy_direction of this CreateRetryPolicyRequestBodyDataObject.

        出入方向

        :param policy_direction: The policy_direction of this CreateRetryPolicyRequestBodyDataObject.
        :type policy_direction: str
        """
        self._policy_direction = policy_direction

    @property
    def account_scope(self):
        r"""Gets the account_scope of this CreateRetryPolicyRequestBodyDataObject.

        账号范围

        :return: The account_scope of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: str
        """
        return self._account_scope

    @account_scope.setter
    def account_scope(self, account_scope):
        r"""Sets the account_scope of this CreateRetryPolicyRequestBodyDataObject.

        账号范围

        :param account_scope: The account_scope of this CreateRetryPolicyRequestBodyDataObject.
        :type account_scope: str
        """
        self._account_scope = account_scope

    @property
    def eps_scope(self):
        r"""Gets the eps_scope of this CreateRetryPolicyRequestBodyDataObject.

        企业项目范围

        :return: The eps_scope of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: str
        """
        return self._eps_scope

    @eps_scope.setter
    def eps_scope(self, eps_scope):
        r"""Sets the eps_scope of this CreateRetryPolicyRequestBodyDataObject.

        企业项目范围

        :param eps_scope: The eps_scope of this CreateRetryPolicyRequestBodyDataObject.
        :type eps_scope: str
        """
        self._eps_scope = eps_scope

    @property
    def region_scope(self):
        r"""Gets the region_scope of this CreateRetryPolicyRequestBodyDataObject.

        region范围

        :return: The region_scope of this CreateRetryPolicyRequestBodyDataObject.
        :rtype: str
        """
        return self._region_scope

    @region_scope.setter
    def region_scope(self, region_scope):
        r"""Sets the region_scope of this CreateRetryPolicyRequestBodyDataObject.

        region范围

        :param region_scope: The region_scope of this CreateRetryPolicyRequestBodyDataObject.
        :type region_scope: str
        """
        self._region_scope = region_scope

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
        if not isinstance(other, CreateRetryPolicyRequestBodyDataObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
