# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBUpgradeInstancesVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'upgrade_type': 'str',
        'upgrade_action': 'str',
        'target_version': 'str'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'upgrade_type': 'upgrade_type',
        'upgrade_action': 'upgrade_action',
        'target_version': 'target_version'
    }

    def __init__(self, instance_ids=None, upgrade_type=None, upgrade_action=None, target_version=None):
        """GaussDBUpgradeInstancesVersionRequest

        The model defined in huaweicloud sdk

        :param instance_ids: 批量实例ID
        :type instance_ids: list[str]
        :param upgrade_type: 实例升级类型，包括就地升级，灰度升级、热补丁升级三种
        :type upgrade_type: str
        :param upgrade_action: 实例升级操作，就地升级无需传值。灰度升级包括升级自动提交，升级待观察，提交升级，升级回退四种。
        :type upgrade_action: str
        :param target_version: 批量实例升级目标版本，非必填。如果未传值灰度升级和就地升级默认升级到当前实例的优选版本，热补丁升级无需传该值，默认升级实例所有可升级热补丁。
        :type target_version: str
        """
        
        

        self._instance_ids = None
        self._upgrade_type = None
        self._upgrade_action = None
        self._target_version = None
        self.discriminator = None

        if instance_ids is not None:
            self.instance_ids = instance_ids
        self.upgrade_type = upgrade_type
        if upgrade_action is not None:
            self.upgrade_action = upgrade_action
        if target_version is not None:
            self.target_version = target_version

    @property
    def instance_ids(self):
        """Gets the instance_ids of this GaussDBUpgradeInstancesVersionRequest.

        批量实例ID

        :return: The instance_ids of this GaussDBUpgradeInstancesVersionRequest.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this GaussDBUpgradeInstancesVersionRequest.

        批量实例ID

        :param instance_ids: The instance_ids of this GaussDBUpgradeInstancesVersionRequest.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this GaussDBUpgradeInstancesVersionRequest.

        实例升级类型，包括就地升级，灰度升级、热补丁升级三种

        :return: The upgrade_type of this GaussDBUpgradeInstancesVersionRequest.
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this GaussDBUpgradeInstancesVersionRequest.

        实例升级类型，包括就地升级，灰度升级、热补丁升级三种

        :param upgrade_type: The upgrade_type of this GaussDBUpgradeInstancesVersionRequest.
        :type upgrade_type: str
        """
        self._upgrade_type = upgrade_type

    @property
    def upgrade_action(self):
        """Gets the upgrade_action of this GaussDBUpgradeInstancesVersionRequest.

        实例升级操作，就地升级无需传值。灰度升级包括升级自动提交，升级待观察，提交升级，升级回退四种。

        :return: The upgrade_action of this GaussDBUpgradeInstancesVersionRequest.
        :rtype: str
        """
        return self._upgrade_action

    @upgrade_action.setter
    def upgrade_action(self, upgrade_action):
        """Sets the upgrade_action of this GaussDBUpgradeInstancesVersionRequest.

        实例升级操作，就地升级无需传值。灰度升级包括升级自动提交，升级待观察，提交升级，升级回退四种。

        :param upgrade_action: The upgrade_action of this GaussDBUpgradeInstancesVersionRequest.
        :type upgrade_action: str
        """
        self._upgrade_action = upgrade_action

    @property
    def target_version(self):
        """Gets the target_version of this GaussDBUpgradeInstancesVersionRequest.

        批量实例升级目标版本，非必填。如果未传值灰度升级和就地升级默认升级到当前实例的优选版本，热补丁升级无需传该值，默认升级实例所有可升级热补丁。

        :return: The target_version of this GaussDBUpgradeInstancesVersionRequest.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this GaussDBUpgradeInstancesVersionRequest.

        批量实例升级目标版本，非必填。如果未传值灰度升级和就地升级默认升级到当前实例的优选版本，热补丁升级无需传该值，默认升级实例所有可升级热补丁。

        :param target_version: The target_version of this GaussDBUpgradeInstancesVersionRequest.
        :type target_version: str
        """
        self._target_version = target_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GaussDBUpgradeInstancesVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
