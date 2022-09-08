# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IefFlinkJobStatusReportReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'jobs': 'list[Jobs]',
        'message_id': 'str',
        'msg_confirm_topic': 'str'
    }

    attribute_map = {
        'jobs': 'jobs',
        'message_id': 'message_id',
        'msg_confirm_topic': 'msg_confirm_topic'
    }

    def __init__(self, jobs=None, message_id=None, msg_confirm_topic=None):
        """IefFlinkJobStatusReportReq

        The model defined in huaweicloud sdk

        :param jobs: 作业信息列表
        :type jobs: list[:class:`huaweicloudsdkdli.v1.Jobs`]
        :param message_id: 消息id
        :type message_id: str
        :param msg_confirm_topic: 消息确认topic
        :type msg_confirm_topic: str
        """
        
        

        self._jobs = None
        self._message_id = None
        self._msg_confirm_topic = None
        self.discriminator = None

        self.jobs = jobs
        self.message_id = message_id
        if msg_confirm_topic is not None:
            self.msg_confirm_topic = msg_confirm_topic

    @property
    def jobs(self):
        """Gets the jobs of this IefFlinkJobStatusReportReq.

        作业信息列表

        :return: The jobs of this IefFlinkJobStatusReportReq.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Jobs`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this IefFlinkJobStatusReportReq.

        作业信息列表

        :param jobs: The jobs of this IefFlinkJobStatusReportReq.
        :type jobs: list[:class:`huaweicloudsdkdli.v1.Jobs`]
        """
        self._jobs = jobs

    @property
    def message_id(self):
        """Gets the message_id of this IefFlinkJobStatusReportReq.

        消息id

        :return: The message_id of this IefFlinkJobStatusReportReq.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this IefFlinkJobStatusReportReq.

        消息id

        :param message_id: The message_id of this IefFlinkJobStatusReportReq.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def msg_confirm_topic(self):
        """Gets the msg_confirm_topic of this IefFlinkJobStatusReportReq.

        消息确认topic

        :return: The msg_confirm_topic of this IefFlinkJobStatusReportReq.
        :rtype: str
        """
        return self._msg_confirm_topic

    @msg_confirm_topic.setter
    def msg_confirm_topic(self, msg_confirm_topic):
        """Sets the msg_confirm_topic of this IefFlinkJobStatusReportReq.

        消息确认topic

        :param msg_confirm_topic: The msg_confirm_topic of this IefFlinkJobStatusReportReq.
        :type msg_confirm_topic: str
        """
        self._msg_confirm_topic = msg_confirm_topic

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
        if not isinstance(other, IefFlinkJobStatusReportReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
