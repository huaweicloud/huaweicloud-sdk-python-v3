# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaurusDbAdvancedBackupPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'instance_id': 'str',
        'instance_name': 'str'
    }

    attribute_map = {
        'status': 'status',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name'
    }

    def __init__(self, status=None, instance_id=None, instance_name=None):
        r"""UpdateTaurusDbAdvancedBackupPolicyResponse

        The model defined in huaweicloud sdk

        :param status: **参数解释**：  状态信息。  **取值范围**：  COMPLETED：设置备份策略成功。
        :type status: str
        :param instance_id: **参数解释**： 实例ID，严格匹配UUID规则。 **取值范围**： 与请求的实例ID相同。 
        :type instance_id: str
        :param instance_name: **参数解释**： 实例名称。 **取值范围**： 实例ID对应的实例名称。 
        :type instance_name: str
        """
        
        super().__init__()

        self._status = None
        self._instance_id = None
        self._instance_name = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name

    @property
    def status(self):
        r"""Gets the status of this UpdateTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**：  状态信息。  **取值范围**：  COMPLETED：设置备份策略成功。

        :return: The status of this UpdateTaurusDbAdvancedBackupPolicyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**：  状态信息。  **取值范围**：  COMPLETED：设置备份策略成功。

        :param status: The status of this UpdateTaurusDbAdvancedBackupPolicyResponse.
        :type status: str
        """
        self._status = status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**： 实例ID，严格匹配UUID规则。 **取值范围**： 与请求的实例ID相同。 

        :return: The instance_id of this UpdateTaurusDbAdvancedBackupPolicyResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**： 实例ID，严格匹配UUID规则。 **取值范围**： 与请求的实例ID相同。 

        :param instance_id: The instance_id of this UpdateTaurusDbAdvancedBackupPolicyResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this UpdateTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**： 实例名称。 **取值范围**： 实例ID对应的实例名称。 

        :return: The instance_name of this UpdateTaurusDbAdvancedBackupPolicyResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this UpdateTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**： 实例名称。 **取值范围**： 实例ID对应的实例名称。 

        :param instance_name: The instance_name of this UpdateTaurusDbAdvancedBackupPolicyResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    def to_dict(self):
        import warnings
        warnings.warn("UpdateTaurusDbAdvancedBackupPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateTaurusDbAdvancedBackupPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
