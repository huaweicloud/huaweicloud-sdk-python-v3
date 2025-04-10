# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScheduleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_node_id': 'str',
        'schedule_id': 'str',
        'body': 'UpdateScheduleReqDTO'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'schedule_id': 'schedule_id',
        'body': 'body'
    }

    def __init__(self, edge_node_id=None, schedule_id=None, body=None):
        r"""UpdateScheduleRequest

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param schedule_id: 调度计划id
        :type schedule_id: str
        :param body: Body of the UpdateScheduleRequest
        :type body: :class:`huaweicloudsdkiotedge.v2.UpdateScheduleReqDTO`
        """
        
        

        self._edge_node_id = None
        self._schedule_id = None
        self._body = None
        self.discriminator = None

        self.edge_node_id = edge_node_id
        self.schedule_id = schedule_id
        if body is not None:
            self.body = body

    @property
    def edge_node_id(self):
        r"""Gets the edge_node_id of this UpdateScheduleRequest.

        边缘节点ID

        :return: The edge_node_id of this UpdateScheduleRequest.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        r"""Sets the edge_node_id of this UpdateScheduleRequest.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this UpdateScheduleRequest.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def schedule_id(self):
        r"""Gets the schedule_id of this UpdateScheduleRequest.

        调度计划id

        :return: The schedule_id of this UpdateScheduleRequest.
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        r"""Sets the schedule_id of this UpdateScheduleRequest.

        调度计划id

        :param schedule_id: The schedule_id of this UpdateScheduleRequest.
        :type schedule_id: str
        """
        self._schedule_id = schedule_id

    @property
    def body(self):
        r"""Gets the body of this UpdateScheduleRequest.

        :return: The body of this UpdateScheduleRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateScheduleReqDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateScheduleRequest.

        :param body: The body of this UpdateScheduleRequest.
        :type body: :class:`huaweicloudsdkiotedge.v2.UpdateScheduleReqDTO`
        """
        self._body = body

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
        if not isinstance(other, UpdateScheduleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
