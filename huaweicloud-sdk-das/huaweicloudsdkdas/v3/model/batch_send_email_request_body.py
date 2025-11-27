# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSendEmailRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id_list': 'list[str]',
        'email': 'str',
        'topic': 'str',
        'topic_urn': 'str',
        'obs_bucket_name': 'str',
        'service_uri': 'str'
    }

    attribute_map = {
        'task_id_list': 'task_id_list',
        'email': 'email',
        'topic': 'topic',
        'topic_urn': 'topic_urn',
        'obs_bucket_name': 'obs_bucket_name',
        'service_uri': 'service_uri'
    }

    def __init__(self, task_id_list=None, email=None, topic=None, topic_urn=None, obs_bucket_name=None, service_uri=None):
        r"""BatchSendEmailRequestBody

        The model defined in huaweicloud sdk

        :param task_id_list: 报告ID列表
        :type task_id_list: list[str]
        :param email: 邮箱地址
        :type email: str
        :param topic: 主题名称
        :type topic: str
        :param topic_urn: 主题标识符
        :type topic_urn: str
        :param obs_bucket_name: OBS桶名
        :type obs_bucket_name: str
        :param service_uri: 服务地址
        :type service_uri: str
        """
        
        

        self._task_id_list = None
        self._email = None
        self._topic = None
        self._topic_urn = None
        self._obs_bucket_name = None
        self._service_uri = None
        self.discriminator = None

        self.task_id_list = task_id_list
        if email is not None:
            self.email = email
        if topic is not None:
            self.topic = topic
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if service_uri is not None:
            self.service_uri = service_uri

    @property
    def task_id_list(self):
        r"""Gets the task_id_list of this BatchSendEmailRequestBody.

        报告ID列表

        :return: The task_id_list of this BatchSendEmailRequestBody.
        :rtype: list[str]
        """
        return self._task_id_list

    @task_id_list.setter
    def task_id_list(self, task_id_list):
        r"""Sets the task_id_list of this BatchSendEmailRequestBody.

        报告ID列表

        :param task_id_list: The task_id_list of this BatchSendEmailRequestBody.
        :type task_id_list: list[str]
        """
        self._task_id_list = task_id_list

    @property
    def email(self):
        r"""Gets the email of this BatchSendEmailRequestBody.

        邮箱地址

        :return: The email of this BatchSendEmailRequestBody.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this BatchSendEmailRequestBody.

        邮箱地址

        :param email: The email of this BatchSendEmailRequestBody.
        :type email: str
        """
        self._email = email

    @property
    def topic(self):
        r"""Gets the topic of this BatchSendEmailRequestBody.

        主题名称

        :return: The topic of this BatchSendEmailRequestBody.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this BatchSendEmailRequestBody.

        主题名称

        :param topic: The topic of this BatchSendEmailRequestBody.
        :type topic: str
        """
        self._topic = topic

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this BatchSendEmailRequestBody.

        主题标识符

        :return: The topic_urn of this BatchSendEmailRequestBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this BatchSendEmailRequestBody.

        主题标识符

        :param topic_urn: The topic_urn of this BatchSendEmailRequestBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this BatchSendEmailRequestBody.

        OBS桶名

        :return: The obs_bucket_name of this BatchSendEmailRequestBody.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this BatchSendEmailRequestBody.

        OBS桶名

        :param obs_bucket_name: The obs_bucket_name of this BatchSendEmailRequestBody.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def service_uri(self):
        r"""Gets the service_uri of this BatchSendEmailRequestBody.

        服务地址

        :return: The service_uri of this BatchSendEmailRequestBody.
        :rtype: str
        """
        return self._service_uri

    @service_uri.setter
    def service_uri(self, service_uri):
        r"""Sets the service_uri of this BatchSendEmailRequestBody.

        服务地址

        :param service_uri: The service_uri of this BatchSendEmailRequestBody.
        :type service_uri: str
        """
        self._service_uri = service_uri

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchSendEmailRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
