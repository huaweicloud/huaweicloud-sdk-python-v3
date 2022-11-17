# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditlogsResult:

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
        'id': 'str',
        'name': 'str',
        'size': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'id': 'id',
        'name': 'name',
        'size': 'size',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, node_id=None, id=None, name=None, size=None, start_time=None, end_time=None):
        """ListAuditlogsResult

        The model defined in huaweicloud sdk

        :param node_id: 节点ID。
        :type node_id: str
        :param id: 审计日志ID。
        :type id: str
        :param name: 审计日志文件名。
        :type name: str
        :param size: 审计日志大小，单位：byte。
        :type size: int
        :param start_time: 审计日志开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type start_time: str
        :param end_time: 审计日志结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type end_time: str
        """
        
        

        self._node_id = None
        self._id = None
        self._name = None
        self._size = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.node_id = node_id
        self.id = id
        self.name = name
        self.size = size
        self.start_time = start_time
        self.end_time = end_time

    @property
    def node_id(self):
        """Gets the node_id of this ListAuditlogsResult.

        节点ID。

        :return: The node_id of this ListAuditlogsResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ListAuditlogsResult.

        节点ID。

        :param node_id: The node_id of this ListAuditlogsResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def id(self):
        """Gets the id of this ListAuditlogsResult.

        审计日志ID。

        :return: The id of this ListAuditlogsResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAuditlogsResult.

        审计日志ID。

        :param id: The id of this ListAuditlogsResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListAuditlogsResult.

        审计日志文件名。

        :return: The name of this ListAuditlogsResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAuditlogsResult.

        审计日志文件名。

        :param name: The name of this ListAuditlogsResult.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this ListAuditlogsResult.

        审计日志大小，单位：byte。

        :return: The size of this ListAuditlogsResult.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListAuditlogsResult.

        审计日志大小，单位：byte。

        :param size: The size of this ListAuditlogsResult.
        :type size: int
        """
        self._size = size

    @property
    def start_time(self):
        """Gets the start_time of this ListAuditlogsResult.

        审计日志开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The start_time of this ListAuditlogsResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListAuditlogsResult.

        审计日志开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param start_time: The start_time of this ListAuditlogsResult.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAuditlogsResult.

        审计日志结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The end_time of this ListAuditlogsResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAuditlogsResult.

        审计日志结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param end_time: The end_time of this ListAuditlogsResult.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListAuditlogsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
