# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbsFlowEntry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'qa_flow_id': 'str',
        'start_node_id': 'str'
    }

    attribute_map = {
        'qa_flow_id': 'qa_flow_id',
        'start_node_id': 'start_node_id'
    }

    def __init__(self, qa_flow_id=None, start_node_id=None):
        """CbsFlowEntry

        The model defined in huaweicloud sdk

        :param qa_flow_id: 问题流程id
        :type qa_flow_id: str
        :param start_node_id: 开始节点id
        :type start_node_id: str
        """
        
        

        self._qa_flow_id = None
        self._start_node_id = None
        self.discriminator = None

        if qa_flow_id is not None:
            self.qa_flow_id = qa_flow_id
        if start_node_id is not None:
            self.start_node_id = start_node_id

    @property
    def qa_flow_id(self):
        """Gets the qa_flow_id of this CbsFlowEntry.

        问题流程id

        :return: The qa_flow_id of this CbsFlowEntry.
        :rtype: str
        """
        return self._qa_flow_id

    @qa_flow_id.setter
    def qa_flow_id(self, qa_flow_id):
        """Sets the qa_flow_id of this CbsFlowEntry.

        问题流程id

        :param qa_flow_id: The qa_flow_id of this CbsFlowEntry.
        :type qa_flow_id: str
        """
        self._qa_flow_id = qa_flow_id

    @property
    def start_node_id(self):
        """Gets the start_node_id of this CbsFlowEntry.

        开始节点id

        :return: The start_node_id of this CbsFlowEntry.
        :rtype: str
        """
        return self._start_node_id

    @start_node_id.setter
    def start_node_id(self, start_node_id):
        """Sets the start_node_id of this CbsFlowEntry.

        开始节点id

        :param start_node_id: The start_node_id of this CbsFlowEntry.
        :type start_node_id: str
        """
        self._start_node_id = start_node_id

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
        if not isinstance(other, CbsFlowEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
