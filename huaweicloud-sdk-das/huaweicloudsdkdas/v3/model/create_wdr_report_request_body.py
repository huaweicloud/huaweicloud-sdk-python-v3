# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWdrReportRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'start_snapshot_id': 'int',
        'end_snapshot_id': 'int',
        'time_zone': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'start_snapshot_id': 'start_snapshot_id',
        'end_snapshot_id': 'end_snapshot_id',
        'time_zone': 'time_zone'
    }

    def __init__(self, node_id=None, start_snapshot_id=None, end_snapshot_id=None, time_zone=None):
        r"""CreateWdrReportRequestBody

        The model defined in huaweicloud sdk

        :param node_id: 实例节点ID，实例节点的唯一标识。仅支持GaussDB实例节点
        :type node_id: str
        :param start_snapshot_id: WDR快照开始ID
        :type start_snapshot_id: int
        :param end_snapshot_id: WDR快照结束ID
        :type end_snapshot_id: int
        :param time_zone: 时区。格式：Asia/Shanghai
        :type time_zone: str
        """
        
        

        self._node_id = None
        self._start_snapshot_id = None
        self._end_snapshot_id = None
        self._time_zone = None
        self.discriminator = None

        self.node_id = node_id
        self.start_snapshot_id = start_snapshot_id
        self.end_snapshot_id = end_snapshot_id
        self.time_zone = time_zone

    @property
    def node_id(self):
        r"""Gets the node_id of this CreateWdrReportRequestBody.

        实例节点ID，实例节点的唯一标识。仅支持GaussDB实例节点

        :return: The node_id of this CreateWdrReportRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CreateWdrReportRequestBody.

        实例节点ID，实例节点的唯一标识。仅支持GaussDB实例节点

        :param node_id: The node_id of this CreateWdrReportRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def start_snapshot_id(self):
        r"""Gets the start_snapshot_id of this CreateWdrReportRequestBody.

        WDR快照开始ID

        :return: The start_snapshot_id of this CreateWdrReportRequestBody.
        :rtype: int
        """
        return self._start_snapshot_id

    @start_snapshot_id.setter
    def start_snapshot_id(self, start_snapshot_id):
        r"""Sets the start_snapshot_id of this CreateWdrReportRequestBody.

        WDR快照开始ID

        :param start_snapshot_id: The start_snapshot_id of this CreateWdrReportRequestBody.
        :type start_snapshot_id: int
        """
        self._start_snapshot_id = start_snapshot_id

    @property
    def end_snapshot_id(self):
        r"""Gets the end_snapshot_id of this CreateWdrReportRequestBody.

        WDR快照结束ID

        :return: The end_snapshot_id of this CreateWdrReportRequestBody.
        :rtype: int
        """
        return self._end_snapshot_id

    @end_snapshot_id.setter
    def end_snapshot_id(self, end_snapshot_id):
        r"""Sets the end_snapshot_id of this CreateWdrReportRequestBody.

        WDR快照结束ID

        :param end_snapshot_id: The end_snapshot_id of this CreateWdrReportRequestBody.
        :type end_snapshot_id: int
        """
        self._end_snapshot_id = end_snapshot_id

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CreateWdrReportRequestBody.

        时区。格式：Asia/Shanghai

        :return: The time_zone of this CreateWdrReportRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CreateWdrReportRequestBody.

        时区。格式：Asia/Shanghai

        :param time_zone: The time_zone of this CreateWdrReportRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateWdrReportRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
