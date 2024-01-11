# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionReassignRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reassignments': 'list[PartitionReassignEntity]',
        'throttle': 'int',
        'is_schedule': 'bool',
        'execute_at': 'int'
    }

    attribute_map = {
        'reassignments': 'reassignments',
        'throttle': 'throttle',
        'is_schedule': 'is_schedule',
        'execute_at': 'execute_at'
    }

    def __init__(self, reassignments=None, throttle=None, is_schedule=None, execute_at=None):
        """PartitionReassignRequest

        The model defined in huaweicloud sdk

        :param reassignments: 重平衡分配方案。
        :type reassignments: list[:class:`huaweicloudsdkkafka.v2.PartitionReassignEntity`]
        :param throttle: 重平衡门限值。
        :type throttle: int
        :param is_schedule: 是否作为定时任务执行。若非定时执行，则is_schedule 和execute_at字段可为空；若为定时执行，is_schedule为true，execute_at字段非空。
        :type is_schedule: bool
        :param execute_at: 定时时间，格式为Unix时间戳，单位为毫秒
        :type execute_at: int
        """
        
        

        self._reassignments = None
        self._throttle = None
        self._is_schedule = None
        self._execute_at = None
        self.discriminator = None

        self.reassignments = reassignments
        if throttle is not None:
            self.throttle = throttle
        if is_schedule is not None:
            self.is_schedule = is_schedule
        if execute_at is not None:
            self.execute_at = execute_at

    @property
    def reassignments(self):
        """Gets the reassignments of this PartitionReassignRequest.

        重平衡分配方案。

        :return: The reassignments of this PartitionReassignRequest.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.PartitionReassignEntity`]
        """
        return self._reassignments

    @reassignments.setter
    def reassignments(self, reassignments):
        """Sets the reassignments of this PartitionReassignRequest.

        重平衡分配方案。

        :param reassignments: The reassignments of this PartitionReassignRequest.
        :type reassignments: list[:class:`huaweicloudsdkkafka.v2.PartitionReassignEntity`]
        """
        self._reassignments = reassignments

    @property
    def throttle(self):
        """Gets the throttle of this PartitionReassignRequest.

        重平衡门限值。

        :return: The throttle of this PartitionReassignRequest.
        :rtype: int
        """
        return self._throttle

    @throttle.setter
    def throttle(self, throttle):
        """Sets the throttle of this PartitionReassignRequest.

        重平衡门限值。

        :param throttle: The throttle of this PartitionReassignRequest.
        :type throttle: int
        """
        self._throttle = throttle

    @property
    def is_schedule(self):
        """Gets the is_schedule of this PartitionReassignRequest.

        是否作为定时任务执行。若非定时执行，则is_schedule 和execute_at字段可为空；若为定时执行，is_schedule为true，execute_at字段非空。

        :return: The is_schedule of this PartitionReassignRequest.
        :rtype: bool
        """
        return self._is_schedule

    @is_schedule.setter
    def is_schedule(self, is_schedule):
        """Sets the is_schedule of this PartitionReassignRequest.

        是否作为定时任务执行。若非定时执行，则is_schedule 和execute_at字段可为空；若为定时执行，is_schedule为true，execute_at字段非空。

        :param is_schedule: The is_schedule of this PartitionReassignRequest.
        :type is_schedule: bool
        """
        self._is_schedule = is_schedule

    @property
    def execute_at(self):
        """Gets the execute_at of this PartitionReassignRequest.

        定时时间，格式为Unix时间戳，单位为毫秒

        :return: The execute_at of this PartitionReassignRequest.
        :rtype: int
        """
        return self._execute_at

    @execute_at.setter
    def execute_at(self, execute_at):
        """Sets the execute_at of this PartitionReassignRequest.

        定时时间，格式为Unix时间戳，单位为毫秒

        :param execute_at: The execute_at of this PartitionReassignRequest.
        :type execute_at: int
        """
        self._execute_at = execute_at

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
        if not isinstance(other, PartitionReassignRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
