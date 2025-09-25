# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upgrade_type': 'str',
        'upgrade_action': 'str',
        'target_version': 'str',
        'upgrade_shard_num': 'int',
        'upgrade_az': 'str'
    }

    attribute_map = {
        'upgrade_type': 'upgrade_type',
        'upgrade_action': 'upgrade_action',
        'target_version': 'target_version',
        'upgrade_shard_num': 'upgrade_shard_num',
        'upgrade_az': 'upgrade_az'
    }

    def __init__(self, upgrade_type=None, upgrade_action=None, target_version=None, upgrade_shard_num=None, upgrade_az=None):
        r"""UpgradeRequestBody

        The model defined in huaweicloud sdk

        :param upgrade_type: **参数解释**: 实例升级类型，区分大小写。包括就地升级，灰度升级，热补丁升级三种，三种升级方式的异同，详见接口描述。 **约束限制**: 不涉及。 **取值范围**: - inplace：就地升级。 - grey：灰度升级。 - hotfix：热补丁升级。  **默认取值**:   不涉及。
        :type upgrade_type: str
        :param upgrade_action: **参数解释**: 实例升级操作，区分大小写。 实例升级类型是就地升级时非必选。 灰度升级包括升级自动提交、升级待观察、提交升级和升级回退四种。 热补丁升级包括升级自动提交，升级回退两种。 **约束限制**: 不涉及。 **取值范围**: - upgradeAutoCommit：升级自动提交。 - upgrade：升级待观察。 - commit：提交升级。 - rollback：升级回退。  **默认取值**:   不涉及。
        :type upgrade_action: str
        :param target_version: **参数解释**: 实例升级目标版本。 **约束限制**: - 热补丁升级场景下支持传入多个热补丁版本。  **取值范围**:   不涉及。 **默认取值**: 不涉及。
        :type target_version: str
        :param upgrade_shard_num: **参数解释**: 分布式实例灰度升级，滚动升级分片数。分布式实例灰度升级，升级待观察必填。该值不能大于实例未升级分片总数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type upgrade_shard_num: int
        :param upgrade_az: **参数解释**: 灰度升级，升级待观察AZ值，升级待观察时必填。可以支持多AZ一起升级，AZ之间以英文逗号分隔。不能填入不属于该实例的AZ值。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type upgrade_az: str
        """
        
        

        self._upgrade_type = None
        self._upgrade_action = None
        self._target_version = None
        self._upgrade_shard_num = None
        self._upgrade_az = None
        self.discriminator = None

        self.upgrade_type = upgrade_type
        if upgrade_action is not None:
            self.upgrade_action = upgrade_action
        if target_version is not None:
            self.target_version = target_version
        if upgrade_shard_num is not None:
            self.upgrade_shard_num = upgrade_shard_num
        if upgrade_az is not None:
            self.upgrade_az = upgrade_az

    @property
    def upgrade_type(self):
        r"""Gets the upgrade_type of this UpgradeRequestBody.

        **参数解释**: 实例升级类型，区分大小写。包括就地升级，灰度升级，热补丁升级三种，三种升级方式的异同，详见接口描述。 **约束限制**: 不涉及。 **取值范围**: - inplace：就地升级。 - grey：灰度升级。 - hotfix：热补丁升级。  **默认取值**:   不涉及。

        :return: The upgrade_type of this UpgradeRequestBody.
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        r"""Sets the upgrade_type of this UpgradeRequestBody.

        **参数解释**: 实例升级类型，区分大小写。包括就地升级，灰度升级，热补丁升级三种，三种升级方式的异同，详见接口描述。 **约束限制**: 不涉及。 **取值范围**: - inplace：就地升级。 - grey：灰度升级。 - hotfix：热补丁升级。  **默认取值**:   不涉及。

        :param upgrade_type: The upgrade_type of this UpgradeRequestBody.
        :type upgrade_type: str
        """
        self._upgrade_type = upgrade_type

    @property
    def upgrade_action(self):
        r"""Gets the upgrade_action of this UpgradeRequestBody.

        **参数解释**: 实例升级操作，区分大小写。 实例升级类型是就地升级时非必选。 灰度升级包括升级自动提交、升级待观察、提交升级和升级回退四种。 热补丁升级包括升级自动提交，升级回退两种。 **约束限制**: 不涉及。 **取值范围**: - upgradeAutoCommit：升级自动提交。 - upgrade：升级待观察。 - commit：提交升级。 - rollback：升级回退。  **默认取值**:   不涉及。

        :return: The upgrade_action of this UpgradeRequestBody.
        :rtype: str
        """
        return self._upgrade_action

    @upgrade_action.setter
    def upgrade_action(self, upgrade_action):
        r"""Sets the upgrade_action of this UpgradeRequestBody.

        **参数解释**: 实例升级操作，区分大小写。 实例升级类型是就地升级时非必选。 灰度升级包括升级自动提交、升级待观察、提交升级和升级回退四种。 热补丁升级包括升级自动提交，升级回退两种。 **约束限制**: 不涉及。 **取值范围**: - upgradeAutoCommit：升级自动提交。 - upgrade：升级待观察。 - commit：提交升级。 - rollback：升级回退。  **默认取值**:   不涉及。

        :param upgrade_action: The upgrade_action of this UpgradeRequestBody.
        :type upgrade_action: str
        """
        self._upgrade_action = upgrade_action

    @property
    def target_version(self):
        r"""Gets the target_version of this UpgradeRequestBody.

        **参数解释**: 实例升级目标版本。 **约束限制**: - 热补丁升级场景下支持传入多个热补丁版本。  **取值范围**:   不涉及。 **默认取值**: 不涉及。

        :return: The target_version of this UpgradeRequestBody.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this UpgradeRequestBody.

        **参数解释**: 实例升级目标版本。 **约束限制**: - 热补丁升级场景下支持传入多个热补丁版本。  **取值范围**:   不涉及。 **默认取值**: 不涉及。

        :param target_version: The target_version of this UpgradeRequestBody.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def upgrade_shard_num(self):
        r"""Gets the upgrade_shard_num of this UpgradeRequestBody.

        **参数解释**: 分布式实例灰度升级，滚动升级分片数。分布式实例灰度升级，升级待观察必填。该值不能大于实例未升级分片总数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The upgrade_shard_num of this UpgradeRequestBody.
        :rtype: int
        """
        return self._upgrade_shard_num

    @upgrade_shard_num.setter
    def upgrade_shard_num(self, upgrade_shard_num):
        r"""Sets the upgrade_shard_num of this UpgradeRequestBody.

        **参数解释**: 分布式实例灰度升级，滚动升级分片数。分布式实例灰度升级，升级待观察必填。该值不能大于实例未升级分片总数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param upgrade_shard_num: The upgrade_shard_num of this UpgradeRequestBody.
        :type upgrade_shard_num: int
        """
        self._upgrade_shard_num = upgrade_shard_num

    @property
    def upgrade_az(self):
        r"""Gets the upgrade_az of this UpgradeRequestBody.

        **参数解释**: 灰度升级，升级待观察AZ值，升级待观察时必填。可以支持多AZ一起升级，AZ之间以英文逗号分隔。不能填入不属于该实例的AZ值。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The upgrade_az of this UpgradeRequestBody.
        :rtype: str
        """
        return self._upgrade_az

    @upgrade_az.setter
    def upgrade_az(self, upgrade_az):
        r"""Sets the upgrade_az of this UpgradeRequestBody.

        **参数解释**: 灰度升级，升级待观察AZ值，升级待观察时必填。可以支持多AZ一起升级，AZ之间以英文逗号分隔。不能填入不属于该实例的AZ值。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param upgrade_az: The upgrade_az of this UpgradeRequestBody.
        :type upgrade_az: str
        """
        self._upgrade_az = upgrade_az

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
        if not isinstance(other, UpgradeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
