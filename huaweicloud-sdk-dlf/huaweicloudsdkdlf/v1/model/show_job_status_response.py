# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'starttime': 'str',
        'end_time': 'str',
        'last_update_time': 'str',
        'nodes': 'list[RealTimeNodeStatus]'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'starttime': 'starttime',
        'end_time': 'endTime',
        'last_update_time': 'lastUpdateTime',
        'nodes': 'nodes'
    }

    def __init__(self, name=None, status=None, starttime=None, end_time=None, last_update_time=None, nodes=None):
        """ShowJobStatusResponse

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param status: 
        :type status: str
        :param starttime: 
        :type starttime: str
        :param end_time: 
        :type end_time: str
        :param last_update_time: 状态最后更新时间
        :type last_update_time: str
        :param nodes: 
        :type nodes: list[:class:`huaweicloudsdkdlf.v1.RealTimeNodeStatus`]
        """
        
        super(ShowJobStatusResponse, self).__init__()

        self._name = None
        self._status = None
        self._starttime = None
        self._end_time = None
        self._last_update_time = None
        self._nodes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if starttime is not None:
            self.starttime = starttime
        if end_time is not None:
            self.end_time = end_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if nodes is not None:
            self.nodes = nodes

    @property
    def name(self):
        """Gets the name of this ShowJobStatusResponse.

        :return: The name of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowJobStatusResponse.

        :param name: The name of this ShowJobStatusResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ShowJobStatusResponse.

        :return: The status of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJobStatusResponse.

        :param status: The status of this ShowJobStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def starttime(self):
        """Gets the starttime of this ShowJobStatusResponse.

        :return: The starttime of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._starttime

    @starttime.setter
    def starttime(self, starttime):
        """Sets the starttime of this ShowJobStatusResponse.

        :param starttime: The starttime of this ShowJobStatusResponse.
        :type starttime: str
        """
        self._starttime = starttime

    @property
    def end_time(self):
        """Gets the end_time of this ShowJobStatusResponse.

        :return: The end_time of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowJobStatusResponse.

        :param end_time: The end_time of this ShowJobStatusResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this ShowJobStatusResponse.

        状态最后更新时间

        :return: The last_update_time of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this ShowJobStatusResponse.

        状态最后更新时间

        :param last_update_time: The last_update_time of this ShowJobStatusResponse.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def nodes(self):
        """Gets the nodes of this ShowJobStatusResponse.

        :return: The nodes of this ShowJobStatusResponse.
        :rtype: list[:class:`huaweicloudsdkdlf.v1.RealTimeNodeStatus`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ShowJobStatusResponse.

        :param nodes: The nodes of this ShowJobStatusResponse.
        :type nodes: list[:class:`huaweicloudsdkdlf.v1.RealTimeNodeStatus`]
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
        if not isinstance(other, ShowJobStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
