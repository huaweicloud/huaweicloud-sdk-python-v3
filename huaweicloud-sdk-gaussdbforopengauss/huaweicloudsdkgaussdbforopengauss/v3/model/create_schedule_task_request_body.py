# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateScheduleTaskRequestBody:

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
        'start_time': 'str',
        'upgrade_type': 'str',
        'upgrade_action': 'str',
        'target_version': 'str'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'start_time': 'start_time',
        'upgrade_type': 'upgrade_type',
        'upgrade_action': 'upgrade_action',
        'target_version': 'target_version'
    }

    def __init__(self, instance_ids=None, start_time=None, upgrade_type=None, upgrade_action=None, target_version=None):
        r"""CreateScheduleTaskRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: 实例ID列表。
        :type instance_ids: list[str]
        :param start_time: 任务开始时间。
        :type start_time: str
        :param upgrade_type: 实例升级类型。
        :type upgrade_type: str
        :param upgrade_action: 实例升级操作。
        :type upgrade_action: str
        :param target_version: 实例升级目标版本。
        :type target_version: str
        """
        
        

        self._instance_ids = None
        self._start_time = None
        self._upgrade_type = None
        self._upgrade_action = None
        self._target_version = None
        self.discriminator = None

        self.instance_ids = instance_ids
        self.start_time = start_time
        self.upgrade_type = upgrade_type
        self.upgrade_action = upgrade_action
        self.target_version = target_version

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this CreateScheduleTaskRequestBody.

        实例ID列表。

        :return: The instance_ids of this CreateScheduleTaskRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this CreateScheduleTaskRequestBody.

        实例ID列表。

        :param instance_ids: The instance_ids of this CreateScheduleTaskRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def start_time(self):
        r"""Gets the start_time of this CreateScheduleTaskRequestBody.

        任务开始时间。

        :return: The start_time of this CreateScheduleTaskRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CreateScheduleTaskRequestBody.

        任务开始时间。

        :param start_time: The start_time of this CreateScheduleTaskRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def upgrade_type(self):
        r"""Gets the upgrade_type of this CreateScheduleTaskRequestBody.

        实例升级类型。

        :return: The upgrade_type of this CreateScheduleTaskRequestBody.
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        r"""Sets the upgrade_type of this CreateScheduleTaskRequestBody.

        实例升级类型。

        :param upgrade_type: The upgrade_type of this CreateScheduleTaskRequestBody.
        :type upgrade_type: str
        """
        self._upgrade_type = upgrade_type

    @property
    def upgrade_action(self):
        r"""Gets the upgrade_action of this CreateScheduleTaskRequestBody.

        实例升级操作。

        :return: The upgrade_action of this CreateScheduleTaskRequestBody.
        :rtype: str
        """
        return self._upgrade_action

    @upgrade_action.setter
    def upgrade_action(self, upgrade_action):
        r"""Sets the upgrade_action of this CreateScheduleTaskRequestBody.

        实例升级操作。

        :param upgrade_action: The upgrade_action of this CreateScheduleTaskRequestBody.
        :type upgrade_action: str
        """
        self._upgrade_action = upgrade_action

    @property
    def target_version(self):
        r"""Gets the target_version of this CreateScheduleTaskRequestBody.

        实例升级目标版本。

        :return: The target_version of this CreateScheduleTaskRequestBody.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this CreateScheduleTaskRequestBody.

        实例升级目标版本。

        :param target_version: The target_version of this CreateScheduleTaskRequestBody.
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
        if not isinstance(other, CreateScheduleTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
