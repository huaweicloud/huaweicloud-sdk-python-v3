# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDrInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'failed_message': 'str',
        'replica_state': 'str',
        'wal_write_receive_delay_in_mb': 'str',
        'wal_write_replay_delay_in_mb': 'str',
        'wal_receive_replay_delay_in_ms': 'str',
        'master_instance_id': 'str',
        'master_region': 'str',
        'slave_instance_id': 'str',
        'slave_region': 'str',
        'build_process': 'str',
        'time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'failed_message': 'failed_message',
        'replica_state': 'replica_state',
        'wal_write_receive_delay_in_mb': 'wal_write_receive_delay_in_mb',
        'wal_write_replay_delay_in_mb': 'wal_write_replay_delay_in_mb',
        'wal_receive_replay_delay_in_ms': 'wal_receive_replay_delay_in_ms',
        'master_instance_id': 'master_instance_id',
        'master_region': 'master_region',
        'slave_instance_id': 'slave_instance_id',
        'slave_region': 'slave_region',
        'build_process': 'build_process',
        'time': 'time'
    }

    def __init__(self, id=None, status=None, failed_message=None, replica_state=None, wal_write_receive_delay_in_mb=None, wal_write_replay_delay_in_mb=None, wal_receive_replay_delay_in_ms=None, master_instance_id=None, master_region=None, slave_instance_id=None, slave_region=None, build_process=None, time=None):
        r"""InstanceDrInfo

        The model defined in huaweicloud sdk

        :param id: 容灾关系id
        :type id: str
        :param status: 容灾搭建状态
        :type status: str
        :param failed_message: 失败消息
        :type failed_message: str
        :param replica_state: 同步状态，取值范围是0或-1，0表示正常，-1表示异常。
        :type replica_state: str
        :param wal_write_receive_delay_in_mb: 发送延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前接收wal日志位点的差值。
        :type wal_write_receive_delay_in_mb: str
        :param wal_write_replay_delay_in_mb: 端到端延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前回放wal日志位点的差值。
        :type wal_write_replay_delay_in_mb: str
        :param wal_receive_replay_delay_in_ms: 回放延迟时间（ms），即数据在灾备上回放的延迟时间。
        :type wal_receive_replay_delay_in_ms: str
        :param master_instance_id: 主实例ID
        :type master_instance_id: str
        :param master_region: 主实例所在region
        :type master_region: str
        :param slave_instance_id: 灾备实例ID
        :type slave_instance_id: str
        :param slave_region: 灾备实例所在region
        :type slave_region: str
        :param build_process: 搭建流程。master表示配置主实例容灾能力流程。slave表示配置灾备实例容灾能力流程。
        :type build_process: str
        :param time: 灾备搭建时间
        :type time: int
        """
        
        

        self._id = None
        self._status = None
        self._failed_message = None
        self._replica_state = None
        self._wal_write_receive_delay_in_mb = None
        self._wal_write_replay_delay_in_mb = None
        self._wal_receive_replay_delay_in_ms = None
        self._master_instance_id = None
        self._master_region = None
        self._slave_instance_id = None
        self._slave_region = None
        self._build_process = None
        self._time = None
        self.discriminator = None

        self.id = id
        self.status = status
        if failed_message is not None:
            self.failed_message = failed_message
        if replica_state is not None:
            self.replica_state = replica_state
        if wal_write_receive_delay_in_mb is not None:
            self.wal_write_receive_delay_in_mb = wal_write_receive_delay_in_mb
        if wal_write_replay_delay_in_mb is not None:
            self.wal_write_replay_delay_in_mb = wal_write_replay_delay_in_mb
        if wal_receive_replay_delay_in_ms is not None:
            self.wal_receive_replay_delay_in_ms = wal_receive_replay_delay_in_ms
        self.master_instance_id = master_instance_id
        self.master_region = master_region
        self.slave_instance_id = slave_instance_id
        self.slave_region = slave_region
        if build_process is not None:
            self.build_process = build_process
        self.time = time

    @property
    def id(self):
        r"""Gets the id of this InstanceDrInfo.

        容灾关系id

        :return: The id of this InstanceDrInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstanceDrInfo.

        容灾关系id

        :param id: The id of this InstanceDrInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this InstanceDrInfo.

        容灾搭建状态

        :return: The status of this InstanceDrInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceDrInfo.

        容灾搭建状态

        :param status: The status of this InstanceDrInfo.
        :type status: str
        """
        self._status = status

    @property
    def failed_message(self):
        r"""Gets the failed_message of this InstanceDrInfo.

        失败消息

        :return: The failed_message of this InstanceDrInfo.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        r"""Sets the failed_message of this InstanceDrInfo.

        失败消息

        :param failed_message: The failed_message of this InstanceDrInfo.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def replica_state(self):
        r"""Gets the replica_state of this InstanceDrInfo.

        同步状态，取值范围是0或-1，0表示正常，-1表示异常。

        :return: The replica_state of this InstanceDrInfo.
        :rtype: str
        """
        return self._replica_state

    @replica_state.setter
    def replica_state(self, replica_state):
        r"""Sets the replica_state of this InstanceDrInfo.

        同步状态，取值范围是0或-1，0表示正常，-1表示异常。

        :param replica_state: The replica_state of this InstanceDrInfo.
        :type replica_state: str
        """
        self._replica_state = replica_state

    @property
    def wal_write_receive_delay_in_mb(self):
        r"""Gets the wal_write_receive_delay_in_mb of this InstanceDrInfo.

        发送延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前接收wal日志位点的差值。

        :return: The wal_write_receive_delay_in_mb of this InstanceDrInfo.
        :rtype: str
        """
        return self._wal_write_receive_delay_in_mb

    @wal_write_receive_delay_in_mb.setter
    def wal_write_receive_delay_in_mb(self, wal_write_receive_delay_in_mb):
        r"""Sets the wal_write_receive_delay_in_mb of this InstanceDrInfo.

        发送延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前接收wal日志位点的差值。

        :param wal_write_receive_delay_in_mb: The wal_write_receive_delay_in_mb of this InstanceDrInfo.
        :type wal_write_receive_delay_in_mb: str
        """
        self._wal_write_receive_delay_in_mb = wal_write_receive_delay_in_mb

    @property
    def wal_write_replay_delay_in_mb(self):
        r"""Gets the wal_write_replay_delay_in_mb of this InstanceDrInfo.

        端到端延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前回放wal日志位点的差值。

        :return: The wal_write_replay_delay_in_mb of this InstanceDrInfo.
        :rtype: str
        """
        return self._wal_write_replay_delay_in_mb

    @wal_write_replay_delay_in_mb.setter
    def wal_write_replay_delay_in_mb(self, wal_write_replay_delay_in_mb):
        r"""Sets the wal_write_replay_delay_in_mb of this InstanceDrInfo.

        端到端延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前回放wal日志位点的差值。

        :param wal_write_replay_delay_in_mb: The wal_write_replay_delay_in_mb of this InstanceDrInfo.
        :type wal_write_replay_delay_in_mb: str
        """
        self._wal_write_replay_delay_in_mb = wal_write_replay_delay_in_mb

    @property
    def wal_receive_replay_delay_in_ms(self):
        r"""Gets the wal_receive_replay_delay_in_ms of this InstanceDrInfo.

        回放延迟时间（ms），即数据在灾备上回放的延迟时间。

        :return: The wal_receive_replay_delay_in_ms of this InstanceDrInfo.
        :rtype: str
        """
        return self._wal_receive_replay_delay_in_ms

    @wal_receive_replay_delay_in_ms.setter
    def wal_receive_replay_delay_in_ms(self, wal_receive_replay_delay_in_ms):
        r"""Sets the wal_receive_replay_delay_in_ms of this InstanceDrInfo.

        回放延迟时间（ms），即数据在灾备上回放的延迟时间。

        :param wal_receive_replay_delay_in_ms: The wal_receive_replay_delay_in_ms of this InstanceDrInfo.
        :type wal_receive_replay_delay_in_ms: str
        """
        self._wal_receive_replay_delay_in_ms = wal_receive_replay_delay_in_ms

    @property
    def master_instance_id(self):
        r"""Gets the master_instance_id of this InstanceDrInfo.

        主实例ID

        :return: The master_instance_id of this InstanceDrInfo.
        :rtype: str
        """
        return self._master_instance_id

    @master_instance_id.setter
    def master_instance_id(self, master_instance_id):
        r"""Sets the master_instance_id of this InstanceDrInfo.

        主实例ID

        :param master_instance_id: The master_instance_id of this InstanceDrInfo.
        :type master_instance_id: str
        """
        self._master_instance_id = master_instance_id

    @property
    def master_region(self):
        r"""Gets the master_region of this InstanceDrInfo.

        主实例所在region

        :return: The master_region of this InstanceDrInfo.
        :rtype: str
        """
        return self._master_region

    @master_region.setter
    def master_region(self, master_region):
        r"""Sets the master_region of this InstanceDrInfo.

        主实例所在region

        :param master_region: The master_region of this InstanceDrInfo.
        :type master_region: str
        """
        self._master_region = master_region

    @property
    def slave_instance_id(self):
        r"""Gets the slave_instance_id of this InstanceDrInfo.

        灾备实例ID

        :return: The slave_instance_id of this InstanceDrInfo.
        :rtype: str
        """
        return self._slave_instance_id

    @slave_instance_id.setter
    def slave_instance_id(self, slave_instance_id):
        r"""Sets the slave_instance_id of this InstanceDrInfo.

        灾备实例ID

        :param slave_instance_id: The slave_instance_id of this InstanceDrInfo.
        :type slave_instance_id: str
        """
        self._slave_instance_id = slave_instance_id

    @property
    def slave_region(self):
        r"""Gets the slave_region of this InstanceDrInfo.

        灾备实例所在region

        :return: The slave_region of this InstanceDrInfo.
        :rtype: str
        """
        return self._slave_region

    @slave_region.setter
    def slave_region(self, slave_region):
        r"""Sets the slave_region of this InstanceDrInfo.

        灾备实例所在region

        :param slave_region: The slave_region of this InstanceDrInfo.
        :type slave_region: str
        """
        self._slave_region = slave_region

    @property
    def build_process(self):
        r"""Gets the build_process of this InstanceDrInfo.

        搭建流程。master表示配置主实例容灾能力流程。slave表示配置灾备实例容灾能力流程。

        :return: The build_process of this InstanceDrInfo.
        :rtype: str
        """
        return self._build_process

    @build_process.setter
    def build_process(self, build_process):
        r"""Sets the build_process of this InstanceDrInfo.

        搭建流程。master表示配置主实例容灾能力流程。slave表示配置灾备实例容灾能力流程。

        :param build_process: The build_process of this InstanceDrInfo.
        :type build_process: str
        """
        self._build_process = build_process

    @property
    def time(self):
        r"""Gets the time of this InstanceDrInfo.

        灾备搭建时间

        :return: The time of this InstanceDrInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this InstanceDrInfo.

        灾备搭建时间

        :param time: The time of this InstanceDrInfo.
        :type time: int
        """
        self._time = time

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
        if not isinstance(other, InstanceDrInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
