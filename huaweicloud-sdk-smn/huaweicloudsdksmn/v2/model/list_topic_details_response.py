# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopicDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'update_time': 'str',
        'push_policy': 'int',
        'create_time': 'str',
        'name': 'str',
        'topic_urn': 'str',
        'display_name': 'str',
        'request_id': 'str',
        'enterprise_project_id': 'str',
        'topic_id': 'str'
    }

    attribute_map = {
        'update_time': 'update_time',
        'push_policy': 'push_policy',
        'create_time': 'create_time',
        'name': 'name',
        'topic_urn': 'topic_urn',
        'display_name': 'display_name',
        'request_id': 'request_id',
        'enterprise_project_id': 'enterprise_project_id',
        'topic_id': 'topic_id'
    }

    def __init__(self, update_time=None, push_policy=None, create_time=None, name=None, topic_urn=None, display_name=None, request_id=None, enterprise_project_id=None, topic_id=None):
        r"""ListTopicDetailsResponse

        The model defined in huaweicloud sdk

        :param update_time: 更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type update_time: str
        :param push_policy: 消息推送的策略。0表示发送失败，保留到失败队列，1表示直接丢弃发送失败的消息。
        :type push_policy: int
        :param create_time: 创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type create_time: str
        :param name: 创建Topic的名字。
        :type name: str
        :param topic_urn: Topic的唯一的资源标识。可以通过[查看主题列表获](smn_api_51004.xml)取该标识。
        :type topic_urn: str
        :param display_name: Topic的显示名，推送邮件消息时，作为邮件发件人显示。
        :type display_name: str
        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param topic_id: 主题ID。
        :type topic_id: str
        """
        
        super(ListTopicDetailsResponse, self).__init__()

        self._update_time = None
        self._push_policy = None
        self._create_time = None
        self._name = None
        self._topic_urn = None
        self._display_name = None
        self._request_id = None
        self._enterprise_project_id = None
        self._topic_id = None
        self.discriminator = None

        if update_time is not None:
            self.update_time = update_time
        if push_policy is not None:
            self.push_policy = push_policy
        if create_time is not None:
            self.create_time = create_time
        if name is not None:
            self.name = name
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if display_name is not None:
            self.display_name = display_name
        if request_id is not None:
            self.request_id = request_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if topic_id is not None:
            self.topic_id = topic_id

    @property
    def update_time(self):
        r"""Gets the update_time of this ListTopicDetailsResponse.

        更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The update_time of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListTopicDetailsResponse.

        更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param update_time: The update_time of this ListTopicDetailsResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def push_policy(self):
        r"""Gets the push_policy of this ListTopicDetailsResponse.

        消息推送的策略。0表示发送失败，保留到失败队列，1表示直接丢弃发送失败的消息。

        :return: The push_policy of this ListTopicDetailsResponse.
        :rtype: int
        """
        return self._push_policy

    @push_policy.setter
    def push_policy(self, push_policy):
        r"""Sets the push_policy of this ListTopicDetailsResponse.

        消息推送的策略。0表示发送失败，保留到失败队列，1表示直接丢弃发送失败的消息。

        :param push_policy: The push_policy of this ListTopicDetailsResponse.
        :type push_policy: int
        """
        self._push_policy = push_policy

    @property
    def create_time(self):
        r"""Gets the create_time of this ListTopicDetailsResponse.

        创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The create_time of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListTopicDetailsResponse.

        创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param create_time: The create_time of this ListTopicDetailsResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this ListTopicDetailsResponse.

        创建Topic的名字。

        :return: The name of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTopicDetailsResponse.

        创建Topic的名字。

        :param name: The name of this ListTopicDetailsResponse.
        :type name: str
        """
        self._name = name

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ListTopicDetailsResponse.

        Topic的唯一的资源标识。可以通过[查看主题列表获](smn_api_51004.xml)取该标识。

        :return: The topic_urn of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ListTopicDetailsResponse.

        Topic的唯一的资源标识。可以通过[查看主题列表获](smn_api_51004.xml)取该标识。

        :param topic_urn: The topic_urn of this ListTopicDetailsResponse.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def display_name(self):
        r"""Gets the display_name of this ListTopicDetailsResponse.

        Topic的显示名，推送邮件消息时，作为邮件发件人显示。

        :return: The display_name of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ListTopicDetailsResponse.

        Topic的显示名，推送邮件消息时，作为邮件发件人显示。

        :param display_name: The display_name of this ListTopicDetailsResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def request_id(self):
        r"""Gets the request_id of this ListTopicDetailsResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListTopicDetailsResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListTopicDetailsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListTopicDetailsResponse.

        企业项目ID。

        :return: The enterprise_project_id of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListTopicDetailsResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListTopicDetailsResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def topic_id(self):
        r"""Gets the topic_id of this ListTopicDetailsResponse.

        主题ID。

        :return: The topic_id of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        r"""Sets the topic_id of this ListTopicDetailsResponse.

        主题ID。

        :param topic_id: The topic_id of this ListTopicDetailsResponse.
        :type topic_id: str
        """
        self._topic_id = topic_id

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
        if not isinstance(other, ListTopicDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
