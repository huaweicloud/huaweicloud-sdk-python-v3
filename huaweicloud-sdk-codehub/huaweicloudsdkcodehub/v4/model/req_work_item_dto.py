# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqWorkItemDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'subject': 'str',
        'sequence': 'str',
        'tracker': 'ReqWorkItemBasicDto',
        'status': 'ReqWorkItemBasicDto',
        'priority': 'ReqWorkItemBasicDto'
    }

    attribute_map = {
        'id': 'id',
        'subject': 'subject',
        'sequence': 'sequence',
        'tracker': 'tracker',
        'status': 'status',
        'priority': 'priority'
    }

    def __init__(self, id=None, subject=None, sequence=None, tracker=None, status=None, priority=None):
        r"""ReqWorkItemDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 工作项ID。
        :type id: str
        :param subject: **参数解释：** 工作项标题。
        :type subject: str
        :param sequence: **参数解释：** 工作项编号， scrum类型项目该值为空。
        :type sequence: str
        :param tracker: 
        :type tracker: :class:`huaweicloudsdkcodehub.v4.ReqWorkItemBasicDto`
        :param status: 
        :type status: :class:`huaweicloudsdkcodehub.v4.ReqWorkItemBasicDto`
        :param priority: 
        :type priority: :class:`huaweicloudsdkcodehub.v4.ReqWorkItemBasicDto`
        """
        
        

        self._id = None
        self._subject = None
        self._sequence = None
        self._tracker = None
        self._status = None
        self._priority = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if subject is not None:
            self.subject = subject
        if sequence is not None:
            self.sequence = sequence
        if tracker is not None:
            self.tracker = tracker
        if status is not None:
            self.status = status
        if priority is not None:
            self.priority = priority

    @property
    def id(self):
        r"""Gets the id of this ReqWorkItemDto.

        **参数解释：** 工作项ID。

        :return: The id of this ReqWorkItemDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ReqWorkItemDto.

        **参数解释：** 工作项ID。

        :param id: The id of this ReqWorkItemDto.
        :type id: str
        """
        self._id = id

    @property
    def subject(self):
        r"""Gets the subject of this ReqWorkItemDto.

        **参数解释：** 工作项标题。

        :return: The subject of this ReqWorkItemDto.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this ReqWorkItemDto.

        **参数解释：** 工作项标题。

        :param subject: The subject of this ReqWorkItemDto.
        :type subject: str
        """
        self._subject = subject

    @property
    def sequence(self):
        r"""Gets the sequence of this ReqWorkItemDto.

        **参数解释：** 工作项编号， scrum类型项目该值为空。

        :return: The sequence of this ReqWorkItemDto.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this ReqWorkItemDto.

        **参数解释：** 工作项编号， scrum类型项目该值为空。

        :param sequence: The sequence of this ReqWorkItemDto.
        :type sequence: str
        """
        self._sequence = sequence

    @property
    def tracker(self):
        r"""Gets the tracker of this ReqWorkItemDto.

        :return: The tracker of this ReqWorkItemDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ReqWorkItemBasicDto`
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        r"""Sets the tracker of this ReqWorkItemDto.

        :param tracker: The tracker of this ReqWorkItemDto.
        :type tracker: :class:`huaweicloudsdkcodehub.v4.ReqWorkItemBasicDto`
        """
        self._tracker = tracker

    @property
    def status(self):
        r"""Gets the status of this ReqWorkItemDto.

        :return: The status of this ReqWorkItemDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ReqWorkItemBasicDto`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ReqWorkItemDto.

        :param status: The status of this ReqWorkItemDto.
        :type status: :class:`huaweicloudsdkcodehub.v4.ReqWorkItemBasicDto`
        """
        self._status = status

    @property
    def priority(self):
        r"""Gets the priority of this ReqWorkItemDto.

        :return: The priority of this ReqWorkItemDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ReqWorkItemBasicDto`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ReqWorkItemDto.

        :param priority: The priority of this ReqWorkItemDto.
        :type priority: :class:`huaweicloudsdkcodehub.v4.ReqWorkItemBasicDto`
        """
        self._priority = priority

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
        if not isinstance(other, ReqWorkItemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
