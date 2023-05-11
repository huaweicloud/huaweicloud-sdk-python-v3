# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDataGuardMonitorResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth': 'str',
        'cpu_used_percent': 'str',
        'dst_delay': 'int',
        'dst_io': 'str',
        'dst_normal': 'bool',
        'dst_offset': 'str',
        'dst_rps': 'str',
        'mem_used_in_mb': 'str',
        'node_mem_in_mb': 'int',
        'node_offset': 'str',
        'node_volume_in_gb': 'int',
        'sr_delay': 'int',
        'sr_offset': 'str',
        'src_io': 'str',
        'src_normal': 'bool',
        'src_rps': 'str',
        'trans_in_mb': 'str',
        'trans_lines': 'str',
        'volume_used_in_gb': 'str',
        'migration_bytes_per_second': 'int'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'cpu_used_percent': 'cpuUsed_percent',
        'dst_delay': 'dst_delay',
        'dst_io': 'dst_io',
        'dst_normal': 'dst_normal',
        'dst_offset': 'dst_offset',
        'dst_rps': 'dst_rps',
        'mem_used_in_mb': 'mem_used_inMB',
        'node_mem_in_mb': 'node_mem_inMB',
        'node_offset': 'node_offset',
        'node_volume_in_gb': 'node_volume_inGB',
        'sr_delay': 'sr_delay',
        'sr_offset': 'sr_offset',
        'src_io': 'src_io',
        'src_normal': 'src_normal',
        'src_rps': 'src_rps',
        'trans_in_mb': 'trans_inMB',
        'trans_lines': 'trans_lines',
        'volume_used_in_gb': 'volume_used_inGB',
        'migration_bytes_per_second': 'migration_bytes_per_second'
    }

    def __init__(self, bandwidth=None, cpu_used_percent=None, dst_delay=None, dst_io=None, dst_normal=None, dst_offset=None, dst_rps=None, mem_used_in_mb=None, node_mem_in_mb=None, node_offset=None, node_volume_in_gb=None, sr_delay=None, sr_offset=None, src_io=None, src_normal=None, src_rps=None, trans_in_mb=None, trans_lines=None, volume_used_in_gb=None, migration_bytes_per_second=None):
        """QueryDataGuardMonitorResponse

        The model defined in huaweicloud sdk

        :param bandwidth: 带宽。
        :type bandwidth: str
        :param cpu_used_percent: cpu百分比。
        :type cpu_used_percent: str
        :param dst_delay: 目标库时延。
        :type dst_delay: int
        :param dst_io: 目标io。
        :type dst_io: str
        :param dst_normal: 目标库连接状态。
        :type dst_normal: bool
        :param dst_offset: 目标库offSet位点。
        :type dst_offset: str
        :param dst_rps: 目标rps。
        :type dst_rps: str
        :param mem_used_in_mb: 内存使用。
        :type mem_used_in_mb: str
        :param node_mem_in_mb: node内存总大小。
        :type node_mem_in_mb: int
        :param node_offset: 迁移实例offSet位点。
        :type node_offset: str
        :param node_volume_in_gb: node磁盘总大小。
        :type node_volume_in_gb: int
        :param sr_delay: 源库时延。
        :type sr_delay: int
        :param sr_offset: 源库offSet位点。
        :type sr_offset: str
        :param src_io: 源io。
        :type src_io: str
        :param src_normal: 源库连接状态。
        :type src_normal: bool
        :param src_rps: 源rps。
        :type src_rps: str
        :param trans_in_mb: 迁移数据量。
        :type trans_in_mb: str
        :param trans_lines: 迁移数据行数。
        :type trans_lines: str
        :param volume_used_in_gb: 磁盘使用。
        :type volume_used_in_gb: str
        :param migration_bytes_per_second: 每秒迁移字节大小。
        :type migration_bytes_per_second: int
        """
        
        

        self._bandwidth = None
        self._cpu_used_percent = None
        self._dst_delay = None
        self._dst_io = None
        self._dst_normal = None
        self._dst_offset = None
        self._dst_rps = None
        self._mem_used_in_mb = None
        self._node_mem_in_mb = None
        self._node_offset = None
        self._node_volume_in_gb = None
        self._sr_delay = None
        self._sr_offset = None
        self._src_io = None
        self._src_normal = None
        self._src_rps = None
        self._trans_in_mb = None
        self._trans_lines = None
        self._volume_used_in_gb = None
        self._migration_bytes_per_second = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if cpu_used_percent is not None:
            self.cpu_used_percent = cpu_used_percent
        if dst_delay is not None:
            self.dst_delay = dst_delay
        if dst_io is not None:
            self.dst_io = dst_io
        if dst_normal is not None:
            self.dst_normal = dst_normal
        if dst_offset is not None:
            self.dst_offset = dst_offset
        if dst_rps is not None:
            self.dst_rps = dst_rps
        if mem_used_in_mb is not None:
            self.mem_used_in_mb = mem_used_in_mb
        if node_mem_in_mb is not None:
            self.node_mem_in_mb = node_mem_in_mb
        if node_offset is not None:
            self.node_offset = node_offset
        if node_volume_in_gb is not None:
            self.node_volume_in_gb = node_volume_in_gb
        if sr_delay is not None:
            self.sr_delay = sr_delay
        if sr_offset is not None:
            self.sr_offset = sr_offset
        if src_io is not None:
            self.src_io = src_io
        if src_normal is not None:
            self.src_normal = src_normal
        if src_rps is not None:
            self.src_rps = src_rps
        if trans_in_mb is not None:
            self.trans_in_mb = trans_in_mb
        if trans_lines is not None:
            self.trans_lines = trans_lines
        if volume_used_in_gb is not None:
            self.volume_used_in_gb = volume_used_in_gb
        if migration_bytes_per_second is not None:
            self.migration_bytes_per_second = migration_bytes_per_second

    @property
    def bandwidth(self):
        """Gets the bandwidth of this QueryDataGuardMonitorResponse.

        带宽。

        :return: The bandwidth of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this QueryDataGuardMonitorResponse.

        带宽。

        :param bandwidth: The bandwidth of this QueryDataGuardMonitorResponse.
        :type bandwidth: str
        """
        self._bandwidth = bandwidth

    @property
    def cpu_used_percent(self):
        """Gets the cpu_used_percent of this QueryDataGuardMonitorResponse.

        cpu百分比。

        :return: The cpu_used_percent of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._cpu_used_percent

    @cpu_used_percent.setter
    def cpu_used_percent(self, cpu_used_percent):
        """Sets the cpu_used_percent of this QueryDataGuardMonitorResponse.

        cpu百分比。

        :param cpu_used_percent: The cpu_used_percent of this QueryDataGuardMonitorResponse.
        :type cpu_used_percent: str
        """
        self._cpu_used_percent = cpu_used_percent

    @property
    def dst_delay(self):
        """Gets the dst_delay of this QueryDataGuardMonitorResponse.

        目标库时延。

        :return: The dst_delay of this QueryDataGuardMonitorResponse.
        :rtype: int
        """
        return self._dst_delay

    @dst_delay.setter
    def dst_delay(self, dst_delay):
        """Sets the dst_delay of this QueryDataGuardMonitorResponse.

        目标库时延。

        :param dst_delay: The dst_delay of this QueryDataGuardMonitorResponse.
        :type dst_delay: int
        """
        self._dst_delay = dst_delay

    @property
    def dst_io(self):
        """Gets the dst_io of this QueryDataGuardMonitorResponse.

        目标io。

        :return: The dst_io of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._dst_io

    @dst_io.setter
    def dst_io(self, dst_io):
        """Sets the dst_io of this QueryDataGuardMonitorResponse.

        目标io。

        :param dst_io: The dst_io of this QueryDataGuardMonitorResponse.
        :type dst_io: str
        """
        self._dst_io = dst_io

    @property
    def dst_normal(self):
        """Gets the dst_normal of this QueryDataGuardMonitorResponse.

        目标库连接状态。

        :return: The dst_normal of this QueryDataGuardMonitorResponse.
        :rtype: bool
        """
        return self._dst_normal

    @dst_normal.setter
    def dst_normal(self, dst_normal):
        """Sets the dst_normal of this QueryDataGuardMonitorResponse.

        目标库连接状态。

        :param dst_normal: The dst_normal of this QueryDataGuardMonitorResponse.
        :type dst_normal: bool
        """
        self._dst_normal = dst_normal

    @property
    def dst_offset(self):
        """Gets the dst_offset of this QueryDataGuardMonitorResponse.

        目标库offSet位点。

        :return: The dst_offset of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._dst_offset

    @dst_offset.setter
    def dst_offset(self, dst_offset):
        """Sets the dst_offset of this QueryDataGuardMonitorResponse.

        目标库offSet位点。

        :param dst_offset: The dst_offset of this QueryDataGuardMonitorResponse.
        :type dst_offset: str
        """
        self._dst_offset = dst_offset

    @property
    def dst_rps(self):
        """Gets the dst_rps of this QueryDataGuardMonitorResponse.

        目标rps。

        :return: The dst_rps of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._dst_rps

    @dst_rps.setter
    def dst_rps(self, dst_rps):
        """Sets the dst_rps of this QueryDataGuardMonitorResponse.

        目标rps。

        :param dst_rps: The dst_rps of this QueryDataGuardMonitorResponse.
        :type dst_rps: str
        """
        self._dst_rps = dst_rps

    @property
    def mem_used_in_mb(self):
        """Gets the mem_used_in_mb of this QueryDataGuardMonitorResponse.

        内存使用。

        :return: The mem_used_in_mb of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._mem_used_in_mb

    @mem_used_in_mb.setter
    def mem_used_in_mb(self, mem_used_in_mb):
        """Sets the mem_used_in_mb of this QueryDataGuardMonitorResponse.

        内存使用。

        :param mem_used_in_mb: The mem_used_in_mb of this QueryDataGuardMonitorResponse.
        :type mem_used_in_mb: str
        """
        self._mem_used_in_mb = mem_used_in_mb

    @property
    def node_mem_in_mb(self):
        """Gets the node_mem_in_mb of this QueryDataGuardMonitorResponse.

        node内存总大小。

        :return: The node_mem_in_mb of this QueryDataGuardMonitorResponse.
        :rtype: int
        """
        return self._node_mem_in_mb

    @node_mem_in_mb.setter
    def node_mem_in_mb(self, node_mem_in_mb):
        """Sets the node_mem_in_mb of this QueryDataGuardMonitorResponse.

        node内存总大小。

        :param node_mem_in_mb: The node_mem_in_mb of this QueryDataGuardMonitorResponse.
        :type node_mem_in_mb: int
        """
        self._node_mem_in_mb = node_mem_in_mb

    @property
    def node_offset(self):
        """Gets the node_offset of this QueryDataGuardMonitorResponse.

        迁移实例offSet位点。

        :return: The node_offset of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._node_offset

    @node_offset.setter
    def node_offset(self, node_offset):
        """Sets the node_offset of this QueryDataGuardMonitorResponse.

        迁移实例offSet位点。

        :param node_offset: The node_offset of this QueryDataGuardMonitorResponse.
        :type node_offset: str
        """
        self._node_offset = node_offset

    @property
    def node_volume_in_gb(self):
        """Gets the node_volume_in_gb of this QueryDataGuardMonitorResponse.

        node磁盘总大小。

        :return: The node_volume_in_gb of this QueryDataGuardMonitorResponse.
        :rtype: int
        """
        return self._node_volume_in_gb

    @node_volume_in_gb.setter
    def node_volume_in_gb(self, node_volume_in_gb):
        """Sets the node_volume_in_gb of this QueryDataGuardMonitorResponse.

        node磁盘总大小。

        :param node_volume_in_gb: The node_volume_in_gb of this QueryDataGuardMonitorResponse.
        :type node_volume_in_gb: int
        """
        self._node_volume_in_gb = node_volume_in_gb

    @property
    def sr_delay(self):
        """Gets the sr_delay of this QueryDataGuardMonitorResponse.

        源库时延。

        :return: The sr_delay of this QueryDataGuardMonitorResponse.
        :rtype: int
        """
        return self._sr_delay

    @sr_delay.setter
    def sr_delay(self, sr_delay):
        """Sets the sr_delay of this QueryDataGuardMonitorResponse.

        源库时延。

        :param sr_delay: The sr_delay of this QueryDataGuardMonitorResponse.
        :type sr_delay: int
        """
        self._sr_delay = sr_delay

    @property
    def sr_offset(self):
        """Gets the sr_offset of this QueryDataGuardMonitorResponse.

        源库offSet位点。

        :return: The sr_offset of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._sr_offset

    @sr_offset.setter
    def sr_offset(self, sr_offset):
        """Sets the sr_offset of this QueryDataGuardMonitorResponse.

        源库offSet位点。

        :param sr_offset: The sr_offset of this QueryDataGuardMonitorResponse.
        :type sr_offset: str
        """
        self._sr_offset = sr_offset

    @property
    def src_io(self):
        """Gets the src_io of this QueryDataGuardMonitorResponse.

        源io。

        :return: The src_io of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._src_io

    @src_io.setter
    def src_io(self, src_io):
        """Sets the src_io of this QueryDataGuardMonitorResponse.

        源io。

        :param src_io: The src_io of this QueryDataGuardMonitorResponse.
        :type src_io: str
        """
        self._src_io = src_io

    @property
    def src_normal(self):
        """Gets the src_normal of this QueryDataGuardMonitorResponse.

        源库连接状态。

        :return: The src_normal of this QueryDataGuardMonitorResponse.
        :rtype: bool
        """
        return self._src_normal

    @src_normal.setter
    def src_normal(self, src_normal):
        """Sets the src_normal of this QueryDataGuardMonitorResponse.

        源库连接状态。

        :param src_normal: The src_normal of this QueryDataGuardMonitorResponse.
        :type src_normal: bool
        """
        self._src_normal = src_normal

    @property
    def src_rps(self):
        """Gets the src_rps of this QueryDataGuardMonitorResponse.

        源rps。

        :return: The src_rps of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._src_rps

    @src_rps.setter
    def src_rps(self, src_rps):
        """Sets the src_rps of this QueryDataGuardMonitorResponse.

        源rps。

        :param src_rps: The src_rps of this QueryDataGuardMonitorResponse.
        :type src_rps: str
        """
        self._src_rps = src_rps

    @property
    def trans_in_mb(self):
        """Gets the trans_in_mb of this QueryDataGuardMonitorResponse.

        迁移数据量。

        :return: The trans_in_mb of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._trans_in_mb

    @trans_in_mb.setter
    def trans_in_mb(self, trans_in_mb):
        """Sets the trans_in_mb of this QueryDataGuardMonitorResponse.

        迁移数据量。

        :param trans_in_mb: The trans_in_mb of this QueryDataGuardMonitorResponse.
        :type trans_in_mb: str
        """
        self._trans_in_mb = trans_in_mb

    @property
    def trans_lines(self):
        """Gets the trans_lines of this QueryDataGuardMonitorResponse.

        迁移数据行数。

        :return: The trans_lines of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._trans_lines

    @trans_lines.setter
    def trans_lines(self, trans_lines):
        """Sets the trans_lines of this QueryDataGuardMonitorResponse.

        迁移数据行数。

        :param trans_lines: The trans_lines of this QueryDataGuardMonitorResponse.
        :type trans_lines: str
        """
        self._trans_lines = trans_lines

    @property
    def volume_used_in_gb(self):
        """Gets the volume_used_in_gb of this QueryDataGuardMonitorResponse.

        磁盘使用。

        :return: The volume_used_in_gb of this QueryDataGuardMonitorResponse.
        :rtype: str
        """
        return self._volume_used_in_gb

    @volume_used_in_gb.setter
    def volume_used_in_gb(self, volume_used_in_gb):
        """Sets the volume_used_in_gb of this QueryDataGuardMonitorResponse.

        磁盘使用。

        :param volume_used_in_gb: The volume_used_in_gb of this QueryDataGuardMonitorResponse.
        :type volume_used_in_gb: str
        """
        self._volume_used_in_gb = volume_used_in_gb

    @property
    def migration_bytes_per_second(self):
        """Gets the migration_bytes_per_second of this QueryDataGuardMonitorResponse.

        每秒迁移字节大小。

        :return: The migration_bytes_per_second of this QueryDataGuardMonitorResponse.
        :rtype: int
        """
        return self._migration_bytes_per_second

    @migration_bytes_per_second.setter
    def migration_bytes_per_second(self, migration_bytes_per_second):
        """Sets the migration_bytes_per_second of this QueryDataGuardMonitorResponse.

        每秒迁移字节大小。

        :param migration_bytes_per_second: The migration_bytes_per_second of this QueryDataGuardMonitorResponse.
        :type migration_bytes_per_second: int
        """
        self._migration_bytes_per_second = migration_bytes_per_second

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
        if not isinstance(other, QueryDataGuardMonitorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
