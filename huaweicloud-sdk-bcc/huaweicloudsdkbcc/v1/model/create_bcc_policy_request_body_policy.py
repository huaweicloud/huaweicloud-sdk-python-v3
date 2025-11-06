# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBccPolicyRequestBodyPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protection_type': 'str',
        'enabled': 'bool',
        'name': 'str',
        'region_id': 'str',
        'cyber': 'bool',
        'storage_type': 'str',
        'policy_type': 'str',
        'service_type': 'str',
        'cbr_policy_detail': 'CreateBccPolicyRequestBodyPolicyCbrPolicyDetail'
    }

    attribute_map = {
        'protection_type': 'protection_type',
        'enabled': 'enabled',
        'name': 'name',
        'region_id': 'region_id',
        'cyber': 'cyber',
        'storage_type': 'storage_type',
        'policy_type': 'policy_type',
        'service_type': 'service_type',
        'cbr_policy_detail': 'cbr_policy_detail'
    }

    def __init__(self, protection_type=None, enabled=None, name=None, region_id=None, cyber=None, storage_type=None, policy_type=None, service_type=None, cbr_policy_detail=None):
        r"""CreateBccPolicyRequestBodyPolicy

        The model defined in huaweicloud sdk

        :param protection_type: protection_type
        :type protection_type: str
        :param enabled: enabled
        :type enabled: bool
        :param name: 策略名称，取值长度范围[2,64]。
        :type name: str
        :param region_id: 区域ID
        :type region_id: str
        :param cyber: 是否启用加密
        :type cyber: bool
        :param storage_type: 存储类型，obs,evs,sfs，默认obs
        :type storage_type: str
        :param policy_type: 策略类型,cbr_local_policy,cbr_remote_policy,rds_local_policy,rds_remote_policy
        :type policy_type: str
        :param service_type: 保护服务类型，如:ecs, evs, rds
        :type service_type: str
        :param cbr_policy_detail: 
        :type cbr_policy_detail: :class:`huaweicloudsdkbcc.v1.CreateBccPolicyRequestBodyPolicyCbrPolicyDetail`
        """
        
        

        self._protection_type = None
        self._enabled = None
        self._name = None
        self._region_id = None
        self._cyber = None
        self._storage_type = None
        self._policy_type = None
        self._service_type = None
        self._cbr_policy_detail = None
        self.discriminator = None

        self.protection_type = protection_type
        self.enabled = enabled
        self.name = name
        self.region_id = region_id
        self.cyber = cyber
        self.storage_type = storage_type
        self.policy_type = policy_type
        self.service_type = service_type
        self.cbr_policy_detail = cbr_policy_detail

    @property
    def protection_type(self):
        r"""Gets the protection_type of this CreateBccPolicyRequestBodyPolicy.

        protection_type

        :return: The protection_type of this CreateBccPolicyRequestBodyPolicy.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        r"""Sets the protection_type of this CreateBccPolicyRequestBodyPolicy.

        protection_type

        :param protection_type: The protection_type of this CreateBccPolicyRequestBodyPolicy.
        :type protection_type: str
        """
        self._protection_type = protection_type

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateBccPolicyRequestBodyPolicy.

        enabled

        :return: The enabled of this CreateBccPolicyRequestBodyPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateBccPolicyRequestBodyPolicy.

        enabled

        :param enabled: The enabled of this CreateBccPolicyRequestBodyPolicy.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def name(self):
        r"""Gets the name of this CreateBccPolicyRequestBodyPolicy.

        策略名称，取值长度范围[2,64]。

        :return: The name of this CreateBccPolicyRequestBodyPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateBccPolicyRequestBodyPolicy.

        策略名称，取值长度范围[2,64]。

        :param name: The name of this CreateBccPolicyRequestBodyPolicy.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateBccPolicyRequestBodyPolicy.

        区域ID

        :return: The region_id of this CreateBccPolicyRequestBodyPolicy.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateBccPolicyRequestBodyPolicy.

        区域ID

        :param region_id: The region_id of this CreateBccPolicyRequestBodyPolicy.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def cyber(self):
        r"""Gets the cyber of this CreateBccPolicyRequestBodyPolicy.

        是否启用加密

        :return: The cyber of this CreateBccPolicyRequestBodyPolicy.
        :rtype: bool
        """
        return self._cyber

    @cyber.setter
    def cyber(self, cyber):
        r"""Sets the cyber of this CreateBccPolicyRequestBodyPolicy.

        是否启用加密

        :param cyber: The cyber of this CreateBccPolicyRequestBodyPolicy.
        :type cyber: bool
        """
        self._cyber = cyber

    @property
    def storage_type(self):
        r"""Gets the storage_type of this CreateBccPolicyRequestBodyPolicy.

        存储类型，obs,evs,sfs，默认obs

        :return: The storage_type of this CreateBccPolicyRequestBodyPolicy.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this CreateBccPolicyRequestBodyPolicy.

        存储类型，obs,evs,sfs，默认obs

        :param storage_type: The storage_type of this CreateBccPolicyRequestBodyPolicy.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def policy_type(self):
        r"""Gets the policy_type of this CreateBccPolicyRequestBodyPolicy.

        策略类型,cbr_local_policy,cbr_remote_policy,rds_local_policy,rds_remote_policy

        :return: The policy_type of this CreateBccPolicyRequestBodyPolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this CreateBccPolicyRequestBodyPolicy.

        策略类型,cbr_local_policy,cbr_remote_policy,rds_local_policy,rds_remote_policy

        :param policy_type: The policy_type of this CreateBccPolicyRequestBodyPolicy.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def service_type(self):
        r"""Gets the service_type of this CreateBccPolicyRequestBodyPolicy.

        保护服务类型，如:ecs, evs, rds

        :return: The service_type of this CreateBccPolicyRequestBodyPolicy.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this CreateBccPolicyRequestBodyPolicy.

        保护服务类型，如:ecs, evs, rds

        :param service_type: The service_type of this CreateBccPolicyRequestBodyPolicy.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def cbr_policy_detail(self):
        r"""Gets the cbr_policy_detail of this CreateBccPolicyRequestBodyPolicy.

        :return: The cbr_policy_detail of this CreateBccPolicyRequestBodyPolicy.
        :rtype: :class:`huaweicloudsdkbcc.v1.CreateBccPolicyRequestBodyPolicyCbrPolicyDetail`
        """
        return self._cbr_policy_detail

    @cbr_policy_detail.setter
    def cbr_policy_detail(self, cbr_policy_detail):
        r"""Sets the cbr_policy_detail of this CreateBccPolicyRequestBodyPolicy.

        :param cbr_policy_detail: The cbr_policy_detail of this CreateBccPolicyRequestBodyPolicy.
        :type cbr_policy_detail: :class:`huaweicloudsdkbcc.v1.CreateBccPolicyRequestBodyPolicyCbrPolicyDetail`
        """
        self._cbr_policy_detail = cbr_policy_detail

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
        if not isinstance(other, CreateBccPolicyRequestBodyPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
