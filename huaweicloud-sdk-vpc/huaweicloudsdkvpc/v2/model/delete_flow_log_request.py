# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteFlowLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flowlog_id': 'str'
    }

    attribute_map = {
        'flowlog_id': 'flowlog_id'
    }

    def __init__(self, flowlog_id=None):
        """DeleteFlowLogRequest

        The model defined in huaweicloud sdk

        :param flowlog_id: 流日志资源唯一标识
        :type flowlog_id: str
        """
        
        

        self._flowlog_id = None
        self.discriminator = None

        self.flowlog_id = flowlog_id

    @property
    def flowlog_id(self):
        """Gets the flowlog_id of this DeleteFlowLogRequest.

        流日志资源唯一标识

        :return: The flowlog_id of this DeleteFlowLogRequest.
        :rtype: str
        """
        return self._flowlog_id

    @flowlog_id.setter
    def flowlog_id(self, flowlog_id):
        """Sets the flowlog_id of this DeleteFlowLogRequest.

        流日志资源唯一标识

        :param flowlog_id: The flowlog_id of this DeleteFlowLogRequest.
        :type flowlog_id: str
        """
        self._flowlog_id = flowlog_id

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
        if not isinstance(other, DeleteFlowLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
