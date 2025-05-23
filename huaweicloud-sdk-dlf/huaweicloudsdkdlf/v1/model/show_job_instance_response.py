# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'plan_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'execute_time': 'int',
        'instances_id': 'str',
        'total': 'int',
        'nodes': 'list[NodeInstance]'
    }

    attribute_map = {
        'status': 'status',
        'plan_time': 'planTime',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'execute_time': 'executeTime',
        'instances_id': 'instancesId',
        'total': 'total',
        'nodes': 'nodes'
    }

    def __init__(self, status=None, plan_time=None, start_time=None, end_time=None, execute_time=None, instances_id=None, total=None, nodes=None):
        r"""ShowJobInstanceResponse

        The model defined in huaweicloud sdk

        :param status: 
        :type status: str
        :param plan_time: 
        :type plan_time: int
        :param start_time: 
        :type start_time: int
        :param end_time: 
        :type end_time: int
        :param execute_time: 
        :type execute_time: int
        :param instances_id: 
        :type instances_id: str
        :param total: 
        :type total: int
        :param nodes: 
        :type nodes: list[:class:`huaweicloudsdkdlf.v1.NodeInstance`]
        """
        
        super(ShowJobInstanceResponse, self).__init__()

        self._status = None
        self._plan_time = None
        self._start_time = None
        self._end_time = None
        self._execute_time = None
        self._instances_id = None
        self._total = None
        self._nodes = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if plan_time is not None:
            self.plan_time = plan_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if execute_time is not None:
            self.execute_time = execute_time
        if instances_id is not None:
            self.instances_id = instances_id
        if total is not None:
            self.total = total
        if nodes is not None:
            self.nodes = nodes

    @property
    def status(self):
        r"""Gets the status of this ShowJobInstanceResponse.

        :return: The status of this ShowJobInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowJobInstanceResponse.

        :param status: The status of this ShowJobInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def plan_time(self):
        r"""Gets the plan_time of this ShowJobInstanceResponse.

        :return: The plan_time of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        r"""Sets the plan_time of this ShowJobInstanceResponse.

        :param plan_time: The plan_time of this ShowJobInstanceResponse.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowJobInstanceResponse.

        :return: The start_time of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowJobInstanceResponse.

        :param start_time: The start_time of this ShowJobInstanceResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowJobInstanceResponse.

        :return: The end_time of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowJobInstanceResponse.

        :param end_time: The end_time of this ShowJobInstanceResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def execute_time(self):
        r"""Gets the execute_time of this ShowJobInstanceResponse.

        :return: The execute_time of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this ShowJobInstanceResponse.

        :param execute_time: The execute_time of this ShowJobInstanceResponse.
        :type execute_time: int
        """
        self._execute_time = execute_time

    @property
    def instances_id(self):
        r"""Gets the instances_id of this ShowJobInstanceResponse.

        :return: The instances_id of this ShowJobInstanceResponse.
        :rtype: str
        """
        return self._instances_id

    @instances_id.setter
    def instances_id(self, instances_id):
        r"""Sets the instances_id of this ShowJobInstanceResponse.

        :param instances_id: The instances_id of this ShowJobInstanceResponse.
        :type instances_id: str
        """
        self._instances_id = instances_id

    @property
    def total(self):
        r"""Gets the total of this ShowJobInstanceResponse.

        :return: The total of this ShowJobInstanceResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowJobInstanceResponse.

        :param total: The total of this ShowJobInstanceResponse.
        :type total: int
        """
        self._total = total

    @property
    def nodes(self):
        r"""Gets the nodes of this ShowJobInstanceResponse.

        :return: The nodes of this ShowJobInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdlf.v1.NodeInstance`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ShowJobInstanceResponse.

        :param nodes: The nodes of this ShowJobInstanceResponse.
        :type nodes: list[:class:`huaweicloudsdkdlf.v1.NodeInstance`]
        """
        self._nodes = nodes

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
        if not isinstance(other, ShowJobInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
