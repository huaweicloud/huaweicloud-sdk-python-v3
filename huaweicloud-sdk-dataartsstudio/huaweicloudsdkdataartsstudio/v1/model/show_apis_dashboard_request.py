# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApisDashboardRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dlm_type': 'str',
        'instance_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'time_unit': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'time_unit': 'time_unit',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, dlm_type=None, instance_id=None, start_time=None, end_time=None, time_unit=None, limit=None, offset=None):
        r"""ShowApisDashboardRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param dlm_type: 数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。
        :type dlm_type: str
        :param instance_id: 集群编号。
        :type instance_id: str
        :param start_time: 开始时间（13位时间戳）。
        :type start_time: int
        :param end_time: 结束时间（13位时间戳）。
        :type end_time: int
        :param time_unit: 时间单位。
        :type time_unit: str
        :param limit: limit。
        :type limit: int
        :param offset: offset。
        :type offset: int
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._time_unit = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if dlm_type is not None:
            self.dlm_type = dlm_type
        if instance_id is not None:
            self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.time_unit = time_unit
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowApisDashboardRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ShowApisDashboardRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowApisDashboardRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ShowApisDashboardRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        r"""Gets the dlm_type of this ShowApisDashboardRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :return: The dlm_type of this ShowApisDashboardRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        r"""Sets the dlm_type of this ShowApisDashboardRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :param dlm_type: The dlm_type of this ShowApisDashboardRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowApisDashboardRequest.

        集群编号。

        :return: The instance_id of this ShowApisDashboardRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowApisDashboardRequest.

        集群编号。

        :param instance_id: The instance_id of this ShowApisDashboardRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowApisDashboardRequest.

        开始时间（13位时间戳）。

        :return: The start_time of this ShowApisDashboardRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowApisDashboardRequest.

        开始时间（13位时间戳）。

        :param start_time: The start_time of this ShowApisDashboardRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowApisDashboardRequest.

        结束时间（13位时间戳）。

        :return: The end_time of this ShowApisDashboardRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowApisDashboardRequest.

        结束时间（13位时间戳）。

        :param end_time: The end_time of this ShowApisDashboardRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def time_unit(self):
        r"""Gets the time_unit of this ShowApisDashboardRequest.

        时间单位。

        :return: The time_unit of this ShowApisDashboardRequest.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        r"""Sets the time_unit of this ShowApisDashboardRequest.

        时间单位。

        :param time_unit: The time_unit of this ShowApisDashboardRequest.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def limit(self):
        r"""Gets the limit of this ShowApisDashboardRequest.

        limit。

        :return: The limit of this ShowApisDashboardRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowApisDashboardRequest.

        limit。

        :param limit: The limit of this ShowApisDashboardRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowApisDashboardRequest.

        offset。

        :return: The offset of this ShowApisDashboardRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowApisDashboardRequest.

        offset。

        :param offset: The offset of this ShowApisDashboardRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowApisDashboardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
