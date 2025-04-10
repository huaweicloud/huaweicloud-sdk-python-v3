# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DefaultTopicRequest:

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
        'project_id': 'str',
        'status': 'int',
        'topic_urn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'status': 'status',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, id=None, project_id=None, status=None, topic_urn=None):
        r"""DefaultTopicRequest

        The model defined in huaweicloud sdk

        :param id: DSC告警主题ID（非消息通知服务主题ID）
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param status: 告警通知状态
        :type status: int
        :param topic_urn: 消息通知主题的唯一资源标识符
        :type topic_urn: str
        """
        
        

        self._id = None
        self._project_id = None
        self._status = None
        self._topic_urn = None
        self.discriminator = None

        self.id = id
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        self.topic_urn = topic_urn

    @property
    def id(self):
        r"""Gets the id of this DefaultTopicRequest.

        DSC告警主题ID（非消息通知服务主题ID）

        :return: The id of this DefaultTopicRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DefaultTopicRequest.

        DSC告警主题ID（非消息通知服务主题ID）

        :param id: The id of this DefaultTopicRequest.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this DefaultTopicRequest.

        项目ID

        :return: The project_id of this DefaultTopicRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DefaultTopicRequest.

        项目ID

        :param project_id: The project_id of this DefaultTopicRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this DefaultTopicRequest.

        告警通知状态

        :return: The status of this DefaultTopicRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DefaultTopicRequest.

        告警通知状态

        :param status: The status of this DefaultTopicRequest.
        :type status: int
        """
        self._status = status

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this DefaultTopicRequest.

        消息通知主题的唯一资源标识符

        :return: The topic_urn of this DefaultTopicRequest.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this DefaultTopicRequest.

        消息通知主题的唯一资源标识符

        :param topic_urn: The topic_urn of this DefaultTopicRequest.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

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
        if not isinstance(other, DefaultTopicRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
