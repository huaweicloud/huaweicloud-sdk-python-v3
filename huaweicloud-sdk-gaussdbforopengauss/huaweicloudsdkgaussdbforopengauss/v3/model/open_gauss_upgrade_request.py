# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussUpgradeRequest:

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
        'upgrde_action': 'str',
        'target_version': 'str',
        'upgrade_shard_num': 'int',
        'upgrade_az': 'str',
        'is_parallel_upgrade': 'bool'
    }

    attribute_map = {
        'upgrade_type': 'upgrade_type',
        'upgrde_action': 'upgrde_action',
        'target_version': 'target_version',
        'upgrade_shard_num': 'upgrade_shard_num',
        'upgrade_az': 'upgrade_az',
        'is_parallel_upgrade': 'is_parallel_upgrade'
    }

    def __init__(self, upgrade_type=None, upgrde_action=None, target_version=None, upgrade_shard_num=None, upgrade_az=None, is_parallel_upgrade=None):
        """OpenGaussUpgradeRequest

        The model defined in huaweicloud sdk

        :param upgrade_type: 实例升级类型，包括就地升级，灰度升级，热补丁升级三种，三种升级方式的异同，详见接口描述。  inplace 就地升级  grey 灰度升级  hotfix 热补丁升级。
        :type upgrade_type: str
        :param upgrde_action: 实例升级操作，就地升级无需传值。灰度升级包括升级自动提交，升级待观察，提交升级，升级回退四种。热补丁升级包括升级自动提交，升级回退两种。详见接口描述。  upgradeAutoCommit 升级自动提交  upgrade 升级待观察  commit 提交升级  rollback 升级回退。
        :type upgrde_action: str
        :param target_version: 实例升级目标版本，非必填。如果未传值则默认升级到当前实例的优选版本。仅热补丁升级方式下支持传入多个值，升级操作为升级自动提交，则实例版本从小到大批量升级，升级操作为升级回退，则实例版本从大到小批量回退。
        :type target_version: str
        :param upgrade_shard_num: 分布式实例灰度升级，滚动升级分片数。分布式实例灰度升级，升级待观察必填。该值不能大于实例未升级分片总数。
        :type upgrade_shard_num: int
        :param upgrade_az: 主备版实例灰度升级，滚动升级az值，可以支持多az一起升级，az之间以’,’分割。集中式实例灰度升级，升级待观察必填。该值不能填入不属于该实例的az值。
        :type upgrade_az: str
        :param is_parallel_upgrade: 支持AZ内并行升级，升级时先升级所有备DN，再并行升级各分片主DN，最后并行升级CN。仅在灰度升级下有效且需要数据库版本大于等于3.200。
        :type is_parallel_upgrade: bool
        """
        
        

        self._upgrade_type = None
        self._upgrde_action = None
        self._target_version = None
        self._upgrade_shard_num = None
        self._upgrade_az = None
        self._is_parallel_upgrade = None
        self.discriminator = None

        self.upgrade_type = upgrade_type
        if upgrde_action is not None:
            self.upgrde_action = upgrde_action
        if target_version is not None:
            self.target_version = target_version
        if upgrade_shard_num is not None:
            self.upgrade_shard_num = upgrade_shard_num
        if upgrade_az is not None:
            self.upgrade_az = upgrade_az
        if is_parallel_upgrade is not None:
            self.is_parallel_upgrade = is_parallel_upgrade

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this OpenGaussUpgradeRequest.

        实例升级类型，包括就地升级，灰度升级，热补丁升级三种，三种升级方式的异同，详见接口描述。  inplace 就地升级  grey 灰度升级  hotfix 热补丁升级。

        :return: The upgrade_type of this OpenGaussUpgradeRequest.
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this OpenGaussUpgradeRequest.

        实例升级类型，包括就地升级，灰度升级，热补丁升级三种，三种升级方式的异同，详见接口描述。  inplace 就地升级  grey 灰度升级  hotfix 热补丁升级。

        :param upgrade_type: The upgrade_type of this OpenGaussUpgradeRequest.
        :type upgrade_type: str
        """
        self._upgrade_type = upgrade_type

    @property
    def upgrde_action(self):
        """Gets the upgrde_action of this OpenGaussUpgradeRequest.

        实例升级操作，就地升级无需传值。灰度升级包括升级自动提交，升级待观察，提交升级，升级回退四种。热补丁升级包括升级自动提交，升级回退两种。详见接口描述。  upgradeAutoCommit 升级自动提交  upgrade 升级待观察  commit 提交升级  rollback 升级回退。

        :return: The upgrde_action of this OpenGaussUpgradeRequest.
        :rtype: str
        """
        return self._upgrde_action

    @upgrde_action.setter
    def upgrde_action(self, upgrde_action):
        """Sets the upgrde_action of this OpenGaussUpgradeRequest.

        实例升级操作，就地升级无需传值。灰度升级包括升级自动提交，升级待观察，提交升级，升级回退四种。热补丁升级包括升级自动提交，升级回退两种。详见接口描述。  upgradeAutoCommit 升级自动提交  upgrade 升级待观察  commit 提交升级  rollback 升级回退。

        :param upgrde_action: The upgrde_action of this OpenGaussUpgradeRequest.
        :type upgrde_action: str
        """
        self._upgrde_action = upgrde_action

    @property
    def target_version(self):
        """Gets the target_version of this OpenGaussUpgradeRequest.

        实例升级目标版本，非必填。如果未传值则默认升级到当前实例的优选版本。仅热补丁升级方式下支持传入多个值，升级操作为升级自动提交，则实例版本从小到大批量升级，升级操作为升级回退，则实例版本从大到小批量回退。

        :return: The target_version of this OpenGaussUpgradeRequest.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this OpenGaussUpgradeRequest.

        实例升级目标版本，非必填。如果未传值则默认升级到当前实例的优选版本。仅热补丁升级方式下支持传入多个值，升级操作为升级自动提交，则实例版本从小到大批量升级，升级操作为升级回退，则实例版本从大到小批量回退。

        :param target_version: The target_version of this OpenGaussUpgradeRequest.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def upgrade_shard_num(self):
        """Gets the upgrade_shard_num of this OpenGaussUpgradeRequest.

        分布式实例灰度升级，滚动升级分片数。分布式实例灰度升级，升级待观察必填。该值不能大于实例未升级分片总数。

        :return: The upgrade_shard_num of this OpenGaussUpgradeRequest.
        :rtype: int
        """
        return self._upgrade_shard_num

    @upgrade_shard_num.setter
    def upgrade_shard_num(self, upgrade_shard_num):
        """Sets the upgrade_shard_num of this OpenGaussUpgradeRequest.

        分布式实例灰度升级，滚动升级分片数。分布式实例灰度升级，升级待观察必填。该值不能大于实例未升级分片总数。

        :param upgrade_shard_num: The upgrade_shard_num of this OpenGaussUpgradeRequest.
        :type upgrade_shard_num: int
        """
        self._upgrade_shard_num = upgrade_shard_num

    @property
    def upgrade_az(self):
        """Gets the upgrade_az of this OpenGaussUpgradeRequest.

        主备版实例灰度升级，滚动升级az值，可以支持多az一起升级，az之间以’,’分割。集中式实例灰度升级，升级待观察必填。该值不能填入不属于该实例的az值。

        :return: The upgrade_az of this OpenGaussUpgradeRequest.
        :rtype: str
        """
        return self._upgrade_az

    @upgrade_az.setter
    def upgrade_az(self, upgrade_az):
        """Sets the upgrade_az of this OpenGaussUpgradeRequest.

        主备版实例灰度升级，滚动升级az值，可以支持多az一起升级，az之间以’,’分割。集中式实例灰度升级，升级待观察必填。该值不能填入不属于该实例的az值。

        :param upgrade_az: The upgrade_az of this OpenGaussUpgradeRequest.
        :type upgrade_az: str
        """
        self._upgrade_az = upgrade_az

    @property
    def is_parallel_upgrade(self):
        """Gets the is_parallel_upgrade of this OpenGaussUpgradeRequest.

        支持AZ内并行升级，升级时先升级所有备DN，再并行升级各分片主DN，最后并行升级CN。仅在灰度升级下有效且需要数据库版本大于等于3.200。

        :return: The is_parallel_upgrade of this OpenGaussUpgradeRequest.
        :rtype: bool
        """
        return self._is_parallel_upgrade

    @is_parallel_upgrade.setter
    def is_parallel_upgrade(self, is_parallel_upgrade):
        """Sets the is_parallel_upgrade of this OpenGaussUpgradeRequest.

        支持AZ内并行升级，升级时先升级所有备DN，再并行升级各分片主DN，最后并行升级CN。仅在灰度升级下有效且需要数据库版本大于等于3.200。

        :param is_parallel_upgrade: The is_parallel_upgrade of this OpenGaussUpgradeRequest.
        :type is_parallel_upgrade: bool
        """
        self._is_parallel_upgrade = is_parallel_upgrade

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
        if not isinstance(other, OpenGaussUpgradeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
