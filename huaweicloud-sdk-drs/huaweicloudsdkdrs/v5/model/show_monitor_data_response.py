# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonitorDataResponse(SdkResponse):

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
        'is_src_normal': 'bool',
        'is_dst_normal': 'bool',
        'src_offset': 'str',
        'node_offset': 'str',
        'dst_offset': 'str',
        'src_delay': 'int',
        'dst_delay': 'int',
        'src_rps': 'str',
        'src_io': 'str',
        'dst_rps': 'str',
        'dst_io': 'str',
        'trans_data': 'str',
        'trans_lines': 'str',
        'used_volumes': 'str',
        'used_memory': 'str',
        'used_cpu_percent': 'str',
        'node_volume_size': 'int',
        'node_memory_size': 'int',
        'update_time': 'str',
        'apply_rate': 'int'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'is_src_normal': 'is_src_normal',
        'is_dst_normal': 'is_dst_normal',
        'src_offset': 'src_offset',
        'node_offset': 'node_offset',
        'dst_offset': 'dst_offset',
        'src_delay': 'src_delay',
        'dst_delay': 'dst_delay',
        'src_rps': 'src_rps',
        'src_io': 'src_io',
        'dst_rps': 'dst_rps',
        'dst_io': 'dst_io',
        'trans_data': 'trans_data',
        'trans_lines': 'trans_lines',
        'used_volumes': 'used_volumes',
        'used_memory': 'used_memory',
        'used_cpu_percent': 'used_cpu_percent',
        'node_volume_size': 'node_volume_size',
        'node_memory_size': 'node_memory_size',
        'update_time': 'update_time',
        'apply_rate': 'apply_rate'
    }

    def __init__(self, bandwidth=None, is_src_normal=None, is_dst_normal=None, src_offset=None, node_offset=None, dst_offset=None, src_delay=None, dst_delay=None, src_rps=None, src_io=None, dst_rps=None, dst_io=None, trans_data=None, trans_lines=None, used_volumes=None, used_memory=None, used_cpu_percent=None, node_volume_size=None, node_memory_size=None, update_time=None, apply_rate=None):
        r"""ShowMonitorDataResponse

        The model defined in huaweicloud sdk

        :param bandwidth: EIP带宽，单位：MB/S
        :type bandwidth: str
        :param is_src_normal: 源库连接状态是否正常。
        :type is_src_normal: bool
        :param is_dst_normal: 目标库连接状态是否正常。
        :type is_dst_normal: bool
        :param src_offset: 源库offSet位点。
        :type src_offset: str
        :param node_offset: 迁移实例offSet位点。
        :type node_offset: str
        :param dst_offset: 目标库offSet位点。
        :type dst_offset: str
        :param src_delay: 源库时延。
        :type src_delay: int
        :param dst_delay: 目标库时延。
        :type dst_delay: int
        :param src_rps: 源库RPS。
        :type src_rps: str
        :param src_io: 源库IO。
        :type src_io: str
        :param dst_rps: 目标库RPS。
        :type dst_rps: str
        :param dst_io: 目标库IO。
        :type dst_io: str
        :param trans_data: 迁移数据量。单位：MB
        :type trans_data: str
        :param trans_lines: 迁移数据行数。
        :type trans_lines: str
        :param used_volumes: 磁盘使用量。单位：GB
        :type used_volumes: str
        :param used_memory: 内存使用量。单位：MB
        :type used_memory: str
        :param used_cpu_percent: CPU使用百分比。
        :type used_cpu_percent: str
        :param node_volume_size: node磁盘总大小。单位：GB
        :type node_volume_size: int
        :param node_memory_size: node内存总大小。单位：MB
        :type node_memory_size: int
        :param update_time: 更新时间。
        :type update_time: str
        :param apply_rate: 同步速度。单位：byte/s
        :type apply_rate: int
        """
        
        super(ShowMonitorDataResponse, self).__init__()

        self._bandwidth = None
        self._is_src_normal = None
        self._is_dst_normal = None
        self._src_offset = None
        self._node_offset = None
        self._dst_offset = None
        self._src_delay = None
        self._dst_delay = None
        self._src_rps = None
        self._src_io = None
        self._dst_rps = None
        self._dst_io = None
        self._trans_data = None
        self._trans_lines = None
        self._used_volumes = None
        self._used_memory = None
        self._used_cpu_percent = None
        self._node_volume_size = None
        self._node_memory_size = None
        self._update_time = None
        self._apply_rate = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if is_src_normal is not None:
            self.is_src_normal = is_src_normal
        if is_dst_normal is not None:
            self.is_dst_normal = is_dst_normal
        if src_offset is not None:
            self.src_offset = src_offset
        if node_offset is not None:
            self.node_offset = node_offset
        if dst_offset is not None:
            self.dst_offset = dst_offset
        if src_delay is not None:
            self.src_delay = src_delay
        if dst_delay is not None:
            self.dst_delay = dst_delay
        if src_rps is not None:
            self.src_rps = src_rps
        if src_io is not None:
            self.src_io = src_io
        if dst_rps is not None:
            self.dst_rps = dst_rps
        if dst_io is not None:
            self.dst_io = dst_io
        if trans_data is not None:
            self.trans_data = trans_data
        if trans_lines is not None:
            self.trans_lines = trans_lines
        if used_volumes is not None:
            self.used_volumes = used_volumes
        if used_memory is not None:
            self.used_memory = used_memory
        if used_cpu_percent is not None:
            self.used_cpu_percent = used_cpu_percent
        if node_volume_size is not None:
            self.node_volume_size = node_volume_size
        if node_memory_size is not None:
            self.node_memory_size = node_memory_size
        if update_time is not None:
            self.update_time = update_time
        if apply_rate is not None:
            self.apply_rate = apply_rate

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this ShowMonitorDataResponse.

        EIP带宽，单位：MB/S

        :return: The bandwidth of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this ShowMonitorDataResponse.

        EIP带宽，单位：MB/S

        :param bandwidth: The bandwidth of this ShowMonitorDataResponse.
        :type bandwidth: str
        """
        self._bandwidth = bandwidth

    @property
    def is_src_normal(self):
        r"""Gets the is_src_normal of this ShowMonitorDataResponse.

        源库连接状态是否正常。

        :return: The is_src_normal of this ShowMonitorDataResponse.
        :rtype: bool
        """
        return self._is_src_normal

    @is_src_normal.setter
    def is_src_normal(self, is_src_normal):
        r"""Sets the is_src_normal of this ShowMonitorDataResponse.

        源库连接状态是否正常。

        :param is_src_normal: The is_src_normal of this ShowMonitorDataResponse.
        :type is_src_normal: bool
        """
        self._is_src_normal = is_src_normal

    @property
    def is_dst_normal(self):
        r"""Gets the is_dst_normal of this ShowMonitorDataResponse.

        目标库连接状态是否正常。

        :return: The is_dst_normal of this ShowMonitorDataResponse.
        :rtype: bool
        """
        return self._is_dst_normal

    @is_dst_normal.setter
    def is_dst_normal(self, is_dst_normal):
        r"""Sets the is_dst_normal of this ShowMonitorDataResponse.

        目标库连接状态是否正常。

        :param is_dst_normal: The is_dst_normal of this ShowMonitorDataResponse.
        :type is_dst_normal: bool
        """
        self._is_dst_normal = is_dst_normal

    @property
    def src_offset(self):
        r"""Gets the src_offset of this ShowMonitorDataResponse.

        源库offSet位点。

        :return: The src_offset of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._src_offset

    @src_offset.setter
    def src_offset(self, src_offset):
        r"""Sets the src_offset of this ShowMonitorDataResponse.

        源库offSet位点。

        :param src_offset: The src_offset of this ShowMonitorDataResponse.
        :type src_offset: str
        """
        self._src_offset = src_offset

    @property
    def node_offset(self):
        r"""Gets the node_offset of this ShowMonitorDataResponse.

        迁移实例offSet位点。

        :return: The node_offset of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._node_offset

    @node_offset.setter
    def node_offset(self, node_offset):
        r"""Sets the node_offset of this ShowMonitorDataResponse.

        迁移实例offSet位点。

        :param node_offset: The node_offset of this ShowMonitorDataResponse.
        :type node_offset: str
        """
        self._node_offset = node_offset

    @property
    def dst_offset(self):
        r"""Gets the dst_offset of this ShowMonitorDataResponse.

        目标库offSet位点。

        :return: The dst_offset of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._dst_offset

    @dst_offset.setter
    def dst_offset(self, dst_offset):
        r"""Sets the dst_offset of this ShowMonitorDataResponse.

        目标库offSet位点。

        :param dst_offset: The dst_offset of this ShowMonitorDataResponse.
        :type dst_offset: str
        """
        self._dst_offset = dst_offset

    @property
    def src_delay(self):
        r"""Gets the src_delay of this ShowMonitorDataResponse.

        源库时延。

        :return: The src_delay of this ShowMonitorDataResponse.
        :rtype: int
        """
        return self._src_delay

    @src_delay.setter
    def src_delay(self, src_delay):
        r"""Sets the src_delay of this ShowMonitorDataResponse.

        源库时延。

        :param src_delay: The src_delay of this ShowMonitorDataResponse.
        :type src_delay: int
        """
        self._src_delay = src_delay

    @property
    def dst_delay(self):
        r"""Gets the dst_delay of this ShowMonitorDataResponse.

        目标库时延。

        :return: The dst_delay of this ShowMonitorDataResponse.
        :rtype: int
        """
        return self._dst_delay

    @dst_delay.setter
    def dst_delay(self, dst_delay):
        r"""Sets the dst_delay of this ShowMonitorDataResponse.

        目标库时延。

        :param dst_delay: The dst_delay of this ShowMonitorDataResponse.
        :type dst_delay: int
        """
        self._dst_delay = dst_delay

    @property
    def src_rps(self):
        r"""Gets the src_rps of this ShowMonitorDataResponse.

        源库RPS。

        :return: The src_rps of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._src_rps

    @src_rps.setter
    def src_rps(self, src_rps):
        r"""Sets the src_rps of this ShowMonitorDataResponse.

        源库RPS。

        :param src_rps: The src_rps of this ShowMonitorDataResponse.
        :type src_rps: str
        """
        self._src_rps = src_rps

    @property
    def src_io(self):
        r"""Gets the src_io of this ShowMonitorDataResponse.

        源库IO。

        :return: The src_io of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._src_io

    @src_io.setter
    def src_io(self, src_io):
        r"""Sets the src_io of this ShowMonitorDataResponse.

        源库IO。

        :param src_io: The src_io of this ShowMonitorDataResponse.
        :type src_io: str
        """
        self._src_io = src_io

    @property
    def dst_rps(self):
        r"""Gets the dst_rps of this ShowMonitorDataResponse.

        目标库RPS。

        :return: The dst_rps of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._dst_rps

    @dst_rps.setter
    def dst_rps(self, dst_rps):
        r"""Sets the dst_rps of this ShowMonitorDataResponse.

        目标库RPS。

        :param dst_rps: The dst_rps of this ShowMonitorDataResponse.
        :type dst_rps: str
        """
        self._dst_rps = dst_rps

    @property
    def dst_io(self):
        r"""Gets the dst_io of this ShowMonitorDataResponse.

        目标库IO。

        :return: The dst_io of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._dst_io

    @dst_io.setter
    def dst_io(self, dst_io):
        r"""Sets the dst_io of this ShowMonitorDataResponse.

        目标库IO。

        :param dst_io: The dst_io of this ShowMonitorDataResponse.
        :type dst_io: str
        """
        self._dst_io = dst_io

    @property
    def trans_data(self):
        r"""Gets the trans_data of this ShowMonitorDataResponse.

        迁移数据量。单位：MB

        :return: The trans_data of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._trans_data

    @trans_data.setter
    def trans_data(self, trans_data):
        r"""Sets the trans_data of this ShowMonitorDataResponse.

        迁移数据量。单位：MB

        :param trans_data: The trans_data of this ShowMonitorDataResponse.
        :type trans_data: str
        """
        self._trans_data = trans_data

    @property
    def trans_lines(self):
        r"""Gets the trans_lines of this ShowMonitorDataResponse.

        迁移数据行数。

        :return: The trans_lines of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._trans_lines

    @trans_lines.setter
    def trans_lines(self, trans_lines):
        r"""Sets the trans_lines of this ShowMonitorDataResponse.

        迁移数据行数。

        :param trans_lines: The trans_lines of this ShowMonitorDataResponse.
        :type trans_lines: str
        """
        self._trans_lines = trans_lines

    @property
    def used_volumes(self):
        r"""Gets the used_volumes of this ShowMonitorDataResponse.

        磁盘使用量。单位：GB

        :return: The used_volumes of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._used_volumes

    @used_volumes.setter
    def used_volumes(self, used_volumes):
        r"""Sets the used_volumes of this ShowMonitorDataResponse.

        磁盘使用量。单位：GB

        :param used_volumes: The used_volumes of this ShowMonitorDataResponse.
        :type used_volumes: str
        """
        self._used_volumes = used_volumes

    @property
    def used_memory(self):
        r"""Gets the used_memory of this ShowMonitorDataResponse.

        内存使用量。单位：MB

        :return: The used_memory of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._used_memory

    @used_memory.setter
    def used_memory(self, used_memory):
        r"""Sets the used_memory of this ShowMonitorDataResponse.

        内存使用量。单位：MB

        :param used_memory: The used_memory of this ShowMonitorDataResponse.
        :type used_memory: str
        """
        self._used_memory = used_memory

    @property
    def used_cpu_percent(self):
        r"""Gets the used_cpu_percent of this ShowMonitorDataResponse.

        CPU使用百分比。

        :return: The used_cpu_percent of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._used_cpu_percent

    @used_cpu_percent.setter
    def used_cpu_percent(self, used_cpu_percent):
        r"""Sets the used_cpu_percent of this ShowMonitorDataResponse.

        CPU使用百分比。

        :param used_cpu_percent: The used_cpu_percent of this ShowMonitorDataResponse.
        :type used_cpu_percent: str
        """
        self._used_cpu_percent = used_cpu_percent

    @property
    def node_volume_size(self):
        r"""Gets the node_volume_size of this ShowMonitorDataResponse.

        node磁盘总大小。单位：GB

        :return: The node_volume_size of this ShowMonitorDataResponse.
        :rtype: int
        """
        return self._node_volume_size

    @node_volume_size.setter
    def node_volume_size(self, node_volume_size):
        r"""Sets the node_volume_size of this ShowMonitorDataResponse.

        node磁盘总大小。单位：GB

        :param node_volume_size: The node_volume_size of this ShowMonitorDataResponse.
        :type node_volume_size: int
        """
        self._node_volume_size = node_volume_size

    @property
    def node_memory_size(self):
        r"""Gets the node_memory_size of this ShowMonitorDataResponse.

        node内存总大小。单位：MB

        :return: The node_memory_size of this ShowMonitorDataResponse.
        :rtype: int
        """
        return self._node_memory_size

    @node_memory_size.setter
    def node_memory_size(self, node_memory_size):
        r"""Sets the node_memory_size of this ShowMonitorDataResponse.

        node内存总大小。单位：MB

        :param node_memory_size: The node_memory_size of this ShowMonitorDataResponse.
        :type node_memory_size: int
        """
        self._node_memory_size = node_memory_size

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowMonitorDataResponse.

        更新时间。

        :return: The update_time of this ShowMonitorDataResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowMonitorDataResponse.

        更新时间。

        :param update_time: The update_time of this ShowMonitorDataResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def apply_rate(self):
        r"""Gets the apply_rate of this ShowMonitorDataResponse.

        同步速度。单位：byte/s

        :return: The apply_rate of this ShowMonitorDataResponse.
        :rtype: int
        """
        return self._apply_rate

    @apply_rate.setter
    def apply_rate(self, apply_rate):
        r"""Sets the apply_rate of this ShowMonitorDataResponse.

        同步速度。单位：byte/s

        :param apply_rate: The apply_rate of this ShowMonitorDataResponse.
        :type apply_rate: int
        """
        self._apply_rate = apply_rate

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
        if not isinstance(other, ShowMonitorDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
