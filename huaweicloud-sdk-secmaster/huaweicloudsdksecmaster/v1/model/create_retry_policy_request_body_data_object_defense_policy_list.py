# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRetryPolicyRequestBodyDataObjectDefensePolicyList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'defense_connection_id': 'str',
        'defense_connection_name': 'str',
        'defense_connection_region_id': 'str',
        'defense_connection_region_name': 'str',
        'defense_type': 'str',
        'target_enterprise_id': 'str',
        'target_enterprise_name': 'str',
        'target_project_id': 'str',
        'target_project_name': 'str'
    }

    attribute_map = {
        'defense_connection_id': 'defense_connection_id',
        'defense_connection_name': 'defense_connection_name',
        'defense_connection_region_id': 'defense_connection_region_id',
        'defense_connection_region_name': 'defense_connection_region_name',
        'defense_type': 'defense_type',
        'target_enterprise_id': 'target_enterprise_id',
        'target_enterprise_name': 'target_enterprise_name',
        'target_project_id': 'target_project_id',
        'target_project_name': 'target_project_name'
    }

    def __init__(self, defense_connection_id=None, defense_connection_name=None, defense_connection_region_id=None, defense_connection_region_name=None, defense_type=None, target_enterprise_id=None, target_enterprise_name=None, target_project_id=None, target_project_name=None):
        r"""CreateRetryPolicyRequestBodyDataObjectDefensePolicyList

        The model defined in huaweicloud sdk

        :param defense_connection_id: 操作连接ID
        :type defense_connection_id: str
        :param defense_connection_name: 操作连接名称
        :type defense_connection_name: str
        :param defense_connection_region_id: 防线策略归属区域ID
        :type defense_connection_region_id: str
        :param defense_connection_region_name: 防线策略归属区域名称
        :type defense_connection_region_name: str
        :param defense_type: 防线服务
        :type defense_type: str
        :param target_enterprise_id: 企业项目ID
        :type target_enterprise_id: str
        :param target_enterprise_name: 企业项目名称
        :type target_enterprise_name: str
        :param target_project_id: 防线策略归属项目ID
        :type target_project_id: str
        :param target_project_name: 防线策略归属项目名称
        :type target_project_name: str
        """
        
        

        self._defense_connection_id = None
        self._defense_connection_name = None
        self._defense_connection_region_id = None
        self._defense_connection_region_name = None
        self._defense_type = None
        self._target_enterprise_id = None
        self._target_enterprise_name = None
        self._target_project_id = None
        self._target_project_name = None
        self.discriminator = None

        self.defense_connection_id = defense_connection_id
        self.defense_connection_name = defense_connection_name
        self.defense_connection_region_id = defense_connection_region_id
        self.defense_connection_region_name = defense_connection_region_name
        self.defense_type = defense_type
        self.target_enterprise_id = target_enterprise_id
        self.target_enterprise_name = target_enterprise_name
        self.target_project_id = target_project_id
        self.target_project_name = target_project_name

    @property
    def defense_connection_id(self):
        r"""Gets the defense_connection_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        操作连接ID

        :return: The defense_connection_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :rtype: str
        """
        return self._defense_connection_id

    @defense_connection_id.setter
    def defense_connection_id(self, defense_connection_id):
        r"""Sets the defense_connection_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        操作连接ID

        :param defense_connection_id: The defense_connection_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :type defense_connection_id: str
        """
        self._defense_connection_id = defense_connection_id

    @property
    def defense_connection_name(self):
        r"""Gets the defense_connection_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        操作连接名称

        :return: The defense_connection_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :rtype: str
        """
        return self._defense_connection_name

    @defense_connection_name.setter
    def defense_connection_name(self, defense_connection_name):
        r"""Sets the defense_connection_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        操作连接名称

        :param defense_connection_name: The defense_connection_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :type defense_connection_name: str
        """
        self._defense_connection_name = defense_connection_name

    @property
    def defense_connection_region_id(self):
        r"""Gets the defense_connection_region_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        防线策略归属区域ID

        :return: The defense_connection_region_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :rtype: str
        """
        return self._defense_connection_region_id

    @defense_connection_region_id.setter
    def defense_connection_region_id(self, defense_connection_region_id):
        r"""Sets the defense_connection_region_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        防线策略归属区域ID

        :param defense_connection_region_id: The defense_connection_region_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :type defense_connection_region_id: str
        """
        self._defense_connection_region_id = defense_connection_region_id

    @property
    def defense_connection_region_name(self):
        r"""Gets the defense_connection_region_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        防线策略归属区域名称

        :return: The defense_connection_region_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :rtype: str
        """
        return self._defense_connection_region_name

    @defense_connection_region_name.setter
    def defense_connection_region_name(self, defense_connection_region_name):
        r"""Sets the defense_connection_region_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        防线策略归属区域名称

        :param defense_connection_region_name: The defense_connection_region_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :type defense_connection_region_name: str
        """
        self._defense_connection_region_name = defense_connection_region_name

    @property
    def defense_type(self):
        r"""Gets the defense_type of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        防线服务

        :return: The defense_type of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :rtype: str
        """
        return self._defense_type

    @defense_type.setter
    def defense_type(self, defense_type):
        r"""Sets the defense_type of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        防线服务

        :param defense_type: The defense_type of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :type defense_type: str
        """
        self._defense_type = defense_type

    @property
    def target_enterprise_id(self):
        r"""Gets the target_enterprise_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        企业项目ID

        :return: The target_enterprise_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :rtype: str
        """
        return self._target_enterprise_id

    @target_enterprise_id.setter
    def target_enterprise_id(self, target_enterprise_id):
        r"""Sets the target_enterprise_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        企业项目ID

        :param target_enterprise_id: The target_enterprise_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :type target_enterprise_id: str
        """
        self._target_enterprise_id = target_enterprise_id

    @property
    def target_enterprise_name(self):
        r"""Gets the target_enterprise_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        企业项目名称

        :return: The target_enterprise_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :rtype: str
        """
        return self._target_enterprise_name

    @target_enterprise_name.setter
    def target_enterprise_name(self, target_enterprise_name):
        r"""Sets the target_enterprise_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        企业项目名称

        :param target_enterprise_name: The target_enterprise_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :type target_enterprise_name: str
        """
        self._target_enterprise_name = target_enterprise_name

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        防线策略归属项目ID

        :return: The target_project_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        防线策略归属项目ID

        :param target_project_id: The target_project_id of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

    @property
    def target_project_name(self):
        r"""Gets the target_project_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        防线策略归属项目名称

        :return: The target_project_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :rtype: str
        """
        return self._target_project_name

    @target_project_name.setter
    def target_project_name(self, target_project_name):
        r"""Sets the target_project_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.

        防线策略归属项目名称

        :param target_project_name: The target_project_name of this CreateRetryPolicyRequestBodyDataObjectDefensePolicyList.
        :type target_project_name: str
        """
        self._target_project_name = target_project_name

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
        if not isinstance(other, CreateRetryPolicyRequestBodyDataObjectDefensePolicyList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
