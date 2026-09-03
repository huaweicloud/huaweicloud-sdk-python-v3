# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlTemplateTrendRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'interval_millis': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'interval_millis': 'interval_millis'
    }

    def __init__(self, instance_id=None, node_id=None, start_at=None, end_at=None, interval_millis=None):
        r"""ShowSqlTemplateTrendRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，实例的唯一标识
        :type instance_id: str
        :param node_id: 节点ID，实例节点的唯一标识
        :type node_id: str
        :param start_at: 开始时间，Unix timestamp，单位：毫秒
        :type start_at: int
        :param end_at: 结束时间，Unix timestamp，单位：毫秒
        :type end_at: int
        :param interval_millis: 聚合毫秒数
        :type interval_millis: int
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._start_at = None
        self._end_at = None
        self._interval_millis = None
        self.discriminator = None

        self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        self.start_at = start_at
        self.end_at = end_at
        if interval_millis is not None:
            self.interval_millis = interval_millis

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowSqlTemplateTrendRequest.

        实例ID，实例的唯一标识

        :return: The instance_id of this ShowSqlTemplateTrendRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowSqlTemplateTrendRequest.

        实例ID，实例的唯一标识

        :param instance_id: The instance_id of this ShowSqlTemplateTrendRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowSqlTemplateTrendRequest.

        节点ID，实例节点的唯一标识

        :return: The node_id of this ShowSqlTemplateTrendRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowSqlTemplateTrendRequest.

        节点ID，实例节点的唯一标识

        :param node_id: The node_id of this ShowSqlTemplateTrendRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def start_at(self):
        r"""Gets the start_at of this ShowSqlTemplateTrendRequest.

        开始时间，Unix timestamp，单位：毫秒

        :return: The start_at of this ShowSqlTemplateTrendRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ShowSqlTemplateTrendRequest.

        开始时间，Unix timestamp，单位：毫秒

        :param start_at: The start_at of this ShowSqlTemplateTrendRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ShowSqlTemplateTrendRequest.

        结束时间，Unix timestamp，单位：毫秒

        :return: The end_at of this ShowSqlTemplateTrendRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ShowSqlTemplateTrendRequest.

        结束时间，Unix timestamp，单位：毫秒

        :param end_at: The end_at of this ShowSqlTemplateTrendRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def interval_millis(self):
        r"""Gets the interval_millis of this ShowSqlTemplateTrendRequest.

        聚合毫秒数

        :return: The interval_millis of this ShowSqlTemplateTrendRequest.
        :rtype: int
        """
        return self._interval_millis

    @interval_millis.setter
    def interval_millis(self, interval_millis):
        r"""Sets the interval_millis of this ShowSqlTemplateTrendRequest.

        聚合毫秒数

        :param interval_millis: The interval_millis of this ShowSqlTemplateTrendRequest.
        :type interval_millis: int
        """
        self._interval_millis = interval_millis

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
        if not isinstance(other, ShowSqlTemplateTrendRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
