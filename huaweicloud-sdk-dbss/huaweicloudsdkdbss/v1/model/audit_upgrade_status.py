# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditUpgradeStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_version': 'str',
        'instance_id': 'str',
        'status': 'int',
        'steps': 'list[AuditUpgradeStep]',
        'total': 'int',
        'upgrade_version': 'str'
    }

    attribute_map = {
        'current_version': 'current_version',
        'instance_id': 'instance_id',
        'status': 'status',
        'steps': 'steps',
        'total': 'total',
        'upgrade_version': 'upgrade_version'
    }

    def __init__(self, current_version=None, instance_id=None, status=None, steps=None, total=None, upgrade_version=None):
        r"""AuditUpgradeStatus

        The model defined in huaweicloud sdk

        :param current_version: 当前版本
        :type current_version: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param status: 状态  - 0：正在升级  - 1：满足条件未升级  - 2：不满足升级条件
        :type status: int
        :param steps: 升级步骤
        :type steps: list[:class:`huaweicloudsdkdbss.v1.AuditUpgradeStep`]
        :param total: 总量
        :type total: int
        :param upgrade_version: 升级版本
        :type upgrade_version: str
        """
        
        

        self._current_version = None
        self._instance_id = None
        self._status = None
        self._steps = None
        self._total = None
        self._upgrade_version = None
        self.discriminator = None

        if current_version is not None:
            self.current_version = current_version
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if steps is not None:
            self.steps = steps
        if total is not None:
            self.total = total
        if upgrade_version is not None:
            self.upgrade_version = upgrade_version

    @property
    def current_version(self):
        r"""Gets the current_version of this AuditUpgradeStatus.

        当前版本

        :return: The current_version of this AuditUpgradeStatus.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this AuditUpgradeStatus.

        当前版本

        :param current_version: The current_version of this AuditUpgradeStatus.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AuditUpgradeStatus.

        实例ID

        :return: The instance_id of this AuditUpgradeStatus.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AuditUpgradeStatus.

        实例ID

        :param instance_id: The instance_id of this AuditUpgradeStatus.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this AuditUpgradeStatus.

        状态  - 0：正在升级  - 1：满足条件未升级  - 2：不满足升级条件

        :return: The status of this AuditUpgradeStatus.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AuditUpgradeStatus.

        状态  - 0：正在升级  - 1：满足条件未升级  - 2：不满足升级条件

        :param status: The status of this AuditUpgradeStatus.
        :type status: int
        """
        self._status = status

    @property
    def steps(self):
        r"""Gets the steps of this AuditUpgradeStatus.

        升级步骤

        :return: The steps of this AuditUpgradeStatus.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.AuditUpgradeStep`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this AuditUpgradeStatus.

        升级步骤

        :param steps: The steps of this AuditUpgradeStatus.
        :type steps: list[:class:`huaweicloudsdkdbss.v1.AuditUpgradeStep`]
        """
        self._steps = steps

    @property
    def total(self):
        r"""Gets the total of this AuditUpgradeStatus.

        总量

        :return: The total of this AuditUpgradeStatus.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this AuditUpgradeStatus.

        总量

        :param total: The total of this AuditUpgradeStatus.
        :type total: int
        """
        self._total = total

    @property
    def upgrade_version(self):
        r"""Gets the upgrade_version of this AuditUpgradeStatus.

        升级版本

        :return: The upgrade_version of this AuditUpgradeStatus.
        :rtype: str
        """
        return self._upgrade_version

    @upgrade_version.setter
    def upgrade_version(self, upgrade_version):
        r"""Sets the upgrade_version of this AuditUpgradeStatus.

        升级版本

        :param upgrade_version: The upgrade_version of this AuditUpgradeStatus.
        :type upgrade_version: str
        """
        self._upgrade_version = upgrade_version

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
        if not isinstance(other, AuditUpgradeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
