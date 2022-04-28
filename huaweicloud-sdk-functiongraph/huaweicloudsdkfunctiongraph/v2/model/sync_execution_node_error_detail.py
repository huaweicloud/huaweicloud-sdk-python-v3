# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncExecutionNodeErrorDetail:

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
        'error_message': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'error_message': 'error_message',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, node_id=None, error_message=None, begin_time=None, end_time=None):
        """SyncExecutionNodeErrorDetail

        The model defined in huaweicloud sdk

        :param node_id: 流程节点ID
        :type node_id: str
        :param error_message: 错误详细信息
        :type error_message: str
        :param begin_time: 流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type begin_time: str
        :param end_time: 流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type end_time: str
        """
        
        

        self._node_id = None
        self._error_message = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if error_message is not None:
            self.error_message = error_message
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def node_id(self):
        """Gets the node_id of this SyncExecutionNodeErrorDetail.

        流程节点ID

        :return: The node_id of this SyncExecutionNodeErrorDetail.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this SyncExecutionNodeErrorDetail.

        流程节点ID

        :param node_id: The node_id of this SyncExecutionNodeErrorDetail.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def error_message(self):
        """Gets the error_message of this SyncExecutionNodeErrorDetail.

        错误详细信息

        :return: The error_message of this SyncExecutionNodeErrorDetail.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this SyncExecutionNodeErrorDetail.

        错误详细信息

        :param error_message: The error_message of this SyncExecutionNodeErrorDetail.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def begin_time(self):
        """Gets the begin_time of this SyncExecutionNodeErrorDetail.

        流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The begin_time of this SyncExecutionNodeErrorDetail.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this SyncExecutionNodeErrorDetail.

        流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param begin_time: The begin_time of this SyncExecutionNodeErrorDetail.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this SyncExecutionNodeErrorDetail.

        流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The end_time of this SyncExecutionNodeErrorDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SyncExecutionNodeErrorDetail.

        流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param end_time: The end_time of this SyncExecutionNodeErrorDetail.
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
        if not isinstance(other, SyncExecutionNodeErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
