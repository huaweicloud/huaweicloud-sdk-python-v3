# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScalingActivityV2LogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'log_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'start_number': 'int',
        'limit': 'int',
        'type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'log_id': 'log_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'start_number': 'start_number',
        'limit': 'limit',
        'type': 'type',
        'status': 'status'
    }

    def __init__(self, scaling_group_id=None, log_id=None, start_time=None, end_time=None, start_number=None, limit=None, type=None, status=None):
        """ListScalingActivityV2LogsRequest

        The model defined in huaweicloud sdk

        :param scaling_group_id: 伸缩组ID。
        :type scaling_group_id: str
        :param log_id: 伸缩活动日志ID
        :type log_id: str
        :param start_time: 查询的起始时间，格式是“yyyy-MM-ddThh:mm:ssZ”。
        :type start_time: str
        :param end_time: 查询的截止时间，格式是“yyyy-MM-ddThh:mm:ssZ”。
        :type end_time: str
        :param start_number: 查询的起始行号，默认为0。
        :type start_number: int
        :param limit: 查询记录数，默认20，最大100。
        :type limit: int
        :param type: 查询的伸缩活动类型（查询多类型使用逗号分隔）： - NORMAL：普通伸缩活动 - MANNUAL_REMOVE：从伸缩组手动移除实例 - MANNUAL_DELETE：从伸缩组手动移除并删除实例 - MANNUAL_ADD：实例手动加入伸缩组。 - ELB_CHECK_DELETE：ELB检查移除并删除实例。 - AUDIT_CHECK_DELETE：通过审计openstack移除并删除实例。 - DIFF：期望实例数与实际实例数不一致。 - MODIFY_ELB：LB迁移。 - ENTER_STANDBY：实例转入备用。 - EXIT_STANDBY：实例移出备用。
        :type type: str
        :param status: 查询的伸缩活动状态：SUCCESS：成功；FAIL：失败；DOING：伸缩中
        :type status: str
        """
        
        

        self._scaling_group_id = None
        self._log_id = None
        self._start_time = None
        self._end_time = None
        self._start_number = None
        self._limit = None
        self._type = None
        self._status = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        if log_id is not None:
            self.log_id = log_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ListScalingActivityV2LogsRequest.

        伸缩组ID。

        :return: The scaling_group_id of this ListScalingActivityV2LogsRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ListScalingActivityV2LogsRequest.

        伸缩组ID。

        :param scaling_group_id: The scaling_group_id of this ListScalingActivityV2LogsRequest.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def log_id(self):
        """Gets the log_id of this ListScalingActivityV2LogsRequest.

        伸缩活动日志ID

        :return: The log_id of this ListScalingActivityV2LogsRequest.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this ListScalingActivityV2LogsRequest.

        伸缩活动日志ID

        :param log_id: The log_id of this ListScalingActivityV2LogsRequest.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def start_time(self):
        """Gets the start_time of this ListScalingActivityV2LogsRequest.

        查询的起始时间，格式是“yyyy-MM-ddThh:mm:ssZ”。

        :return: The start_time of this ListScalingActivityV2LogsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListScalingActivityV2LogsRequest.

        查询的起始时间，格式是“yyyy-MM-ddThh:mm:ssZ”。

        :param start_time: The start_time of this ListScalingActivityV2LogsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListScalingActivityV2LogsRequest.

        查询的截止时间，格式是“yyyy-MM-ddThh:mm:ssZ”。

        :return: The end_time of this ListScalingActivityV2LogsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListScalingActivityV2LogsRequest.

        查询的截止时间，格式是“yyyy-MM-ddThh:mm:ssZ”。

        :param end_time: The end_time of this ListScalingActivityV2LogsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingActivityV2LogsRequest.

        查询的起始行号，默认为0。

        :return: The start_number of this ListScalingActivityV2LogsRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingActivityV2LogsRequest.

        查询的起始行号，默认为0。

        :param start_number: The start_number of this ListScalingActivityV2LogsRequest.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingActivityV2LogsRequest.

        查询记录数，默认20，最大100。

        :return: The limit of this ListScalingActivityV2LogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingActivityV2LogsRequest.

        查询记录数，默认20，最大100。

        :param limit: The limit of this ListScalingActivityV2LogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        """Gets the type of this ListScalingActivityV2LogsRequest.

        查询的伸缩活动类型（查询多类型使用逗号分隔）： - NORMAL：普通伸缩活动 - MANNUAL_REMOVE：从伸缩组手动移除实例 - MANNUAL_DELETE：从伸缩组手动移除并删除实例 - MANNUAL_ADD：实例手动加入伸缩组。 - ELB_CHECK_DELETE：ELB检查移除并删除实例。 - AUDIT_CHECK_DELETE：通过审计openstack移除并删除实例。 - DIFF：期望实例数与实际实例数不一致。 - MODIFY_ELB：LB迁移。 - ENTER_STANDBY：实例转入备用。 - EXIT_STANDBY：实例移出备用。

        :return: The type of this ListScalingActivityV2LogsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListScalingActivityV2LogsRequest.

        查询的伸缩活动类型（查询多类型使用逗号分隔）： - NORMAL：普通伸缩活动 - MANNUAL_REMOVE：从伸缩组手动移除实例 - MANNUAL_DELETE：从伸缩组手动移除并删除实例 - MANNUAL_ADD：实例手动加入伸缩组。 - ELB_CHECK_DELETE：ELB检查移除并删除实例。 - AUDIT_CHECK_DELETE：通过审计openstack移除并删除实例。 - DIFF：期望实例数与实际实例数不一致。 - MODIFY_ELB：LB迁移。 - ENTER_STANDBY：实例转入备用。 - EXIT_STANDBY：实例移出备用。

        :param type: The type of this ListScalingActivityV2LogsRequest.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this ListScalingActivityV2LogsRequest.

        查询的伸缩活动状态：SUCCESS：成功；FAIL：失败；DOING：伸缩中

        :return: The status of this ListScalingActivityV2LogsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListScalingActivityV2LogsRequest.

        查询的伸缩活动状态：SUCCESS：成功；FAIL：失败；DOING：伸缩中

        :param status: The status of this ListScalingActivityV2LogsRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListScalingActivityV2LogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
