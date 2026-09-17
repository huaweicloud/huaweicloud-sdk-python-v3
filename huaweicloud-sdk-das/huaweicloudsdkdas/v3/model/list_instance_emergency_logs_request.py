# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceEmergencyLogsRequest:

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
        'start_time': 'int',
        'end_time': 'int',
        'cur_page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'cur_page': 'cur_page',
        'per_page': 'per_page'
    }

    def __init__(self, instance_id=None, node_id=None, start_time=None, end_time=None, cur_page=None, per_page=None):
        r"""ListInstanceEmergencyLogsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param node_id: 节点ID
        :type node_id: str
        :param start_time: 开始时间（Unix时间戳，毫秒）
        :type start_time: int
        :param end_time: 结束时间（Unix时间戳，毫秒）
        :type end_time: int
        :param cur_page: 当前页码
        :type cur_page: int
        :param per_page: 每页记录数
        :type per_page: int
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._start_time = None
        self._end_time = None
        self._cur_page = None
        self._per_page = None
        self.discriminator = None

        self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceEmergencyLogsRequest.

        实例ID

        :return: The instance_id of this ListInstanceEmergencyLogsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceEmergencyLogsRequest.

        实例ID

        :param instance_id: The instance_id of this ListInstanceEmergencyLogsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ListInstanceEmergencyLogsRequest.

        节点ID

        :return: The node_id of this ListInstanceEmergencyLogsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListInstanceEmergencyLogsRequest.

        节点ID

        :param node_id: The node_id of this ListInstanceEmergencyLogsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListInstanceEmergencyLogsRequest.

        开始时间（Unix时间戳，毫秒）

        :return: The start_time of this ListInstanceEmergencyLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListInstanceEmergencyLogsRequest.

        开始时间（Unix时间戳，毫秒）

        :param start_time: The start_time of this ListInstanceEmergencyLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListInstanceEmergencyLogsRequest.

        结束时间（Unix时间戳，毫秒）

        :return: The end_time of this ListInstanceEmergencyLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListInstanceEmergencyLogsRequest.

        结束时间（Unix时间戳，毫秒）

        :param end_time: The end_time of this ListInstanceEmergencyLogsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListInstanceEmergencyLogsRequest.

        当前页码

        :return: The cur_page of this ListInstanceEmergencyLogsRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListInstanceEmergencyLogsRequest.

        当前页码

        :param cur_page: The cur_page of this ListInstanceEmergencyLogsRequest.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListInstanceEmergencyLogsRequest.

        每页记录数

        :return: The per_page of this ListInstanceEmergencyLogsRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListInstanceEmergencyLogsRequest.

        每页记录数

        :param per_page: The per_page of this ListInstanceEmergencyLogsRequest.
        :type per_page: int
        """
        self._per_page = per_page

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
        if not isinstance(other, ListInstanceEmergencyLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
