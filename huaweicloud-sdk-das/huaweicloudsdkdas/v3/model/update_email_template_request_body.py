# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEmailTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'int',
        'template_name': 'str',
        'group_id': 'list[int]',
        'health_rank': 'list[str]',
        'email': 'str',
        'topic': 'str',
        'topic_urn': 'str',
        'obs_bucket_name': 'str',
        'inspection_time': 'str',
        'send_time': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'group_id': 'group_id',
        'health_rank': 'health_rank',
        'email': 'email',
        'topic': 'topic',
        'topic_urn': 'topic_urn',
        'obs_bucket_name': 'obs_bucket_name',
        'inspection_time': 'inspection_time',
        'send_time': 'send_time',
        'time_zone': 'time_zone'
    }

    def __init__(self, template_id=None, template_name=None, group_id=None, health_rank=None, email=None, topic=None, topic_urn=None, obs_bucket_name=None, inspection_time=None, send_time=None, time_zone=None):
        r"""UpdateEmailTemplateRequestBody

        The model defined in huaweicloud sdk

        :param template_id: 邮件模板ID
        :type template_id: int
        :param template_name: 邮件模板名称
        :type template_name: str
        :param group_id: 实例组ID列表
        :type group_id: list[int]
        :param health_rank: 健康等级列表
        :type health_rank: list[str]
        :param email: 邮箱地址
        :type email: str
        :param topic: 主题名称
        :type topic: str
        :param topic_urn: 主题标识符
        :type topic_urn: str
        :param obs_bucket_name: OBS桶名
        :type obs_bucket_name: str
        :param inspection_time: 诊断时间，12:00-12:00（默认）或00:00-00:00
        :type inspection_time: str
        :param send_time: 发送时间
        :type send_time: str
        :param time_zone: 时区
        :type time_zone: str
        """
        
        

        self._template_id = None
        self._template_name = None
        self._group_id = None
        self._health_rank = None
        self._email = None
        self._topic = None
        self._topic_urn = None
        self._obs_bucket_name = None
        self._inspection_time = None
        self._send_time = None
        self._time_zone = None
        self.discriminator = None

        self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if group_id is not None:
            self.group_id = group_id
        if health_rank is not None:
            self.health_rank = health_rank
        if email is not None:
            self.email = email
        if topic is not None:
            self.topic = topic
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if inspection_time is not None:
            self.inspection_time = inspection_time
        if send_time is not None:
            self.send_time = send_time
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateEmailTemplateRequestBody.

        邮件模板ID

        :return: The template_id of this UpdateEmailTemplateRequestBody.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateEmailTemplateRequestBody.

        邮件模板ID

        :param template_id: The template_id of this UpdateEmailTemplateRequestBody.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this UpdateEmailTemplateRequestBody.

        邮件模板名称

        :return: The template_name of this UpdateEmailTemplateRequestBody.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this UpdateEmailTemplateRequestBody.

        邮件模板名称

        :param template_name: The template_name of this UpdateEmailTemplateRequestBody.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateEmailTemplateRequestBody.

        实例组ID列表

        :return: The group_id of this UpdateEmailTemplateRequestBody.
        :rtype: list[int]
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateEmailTemplateRequestBody.

        实例组ID列表

        :param group_id: The group_id of this UpdateEmailTemplateRequestBody.
        :type group_id: list[int]
        """
        self._group_id = group_id

    @property
    def health_rank(self):
        r"""Gets the health_rank of this UpdateEmailTemplateRequestBody.

        健康等级列表

        :return: The health_rank of this UpdateEmailTemplateRequestBody.
        :rtype: list[str]
        """
        return self._health_rank

    @health_rank.setter
    def health_rank(self, health_rank):
        r"""Sets the health_rank of this UpdateEmailTemplateRequestBody.

        健康等级列表

        :param health_rank: The health_rank of this UpdateEmailTemplateRequestBody.
        :type health_rank: list[str]
        """
        self._health_rank = health_rank

    @property
    def email(self):
        r"""Gets the email of this UpdateEmailTemplateRequestBody.

        邮箱地址

        :return: The email of this UpdateEmailTemplateRequestBody.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this UpdateEmailTemplateRequestBody.

        邮箱地址

        :param email: The email of this UpdateEmailTemplateRequestBody.
        :type email: str
        """
        self._email = email

    @property
    def topic(self):
        r"""Gets the topic of this UpdateEmailTemplateRequestBody.

        主题名称

        :return: The topic of this UpdateEmailTemplateRequestBody.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this UpdateEmailTemplateRequestBody.

        主题名称

        :param topic: The topic of this UpdateEmailTemplateRequestBody.
        :type topic: str
        """
        self._topic = topic

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this UpdateEmailTemplateRequestBody.

        主题标识符

        :return: The topic_urn of this UpdateEmailTemplateRequestBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this UpdateEmailTemplateRequestBody.

        主题标识符

        :param topic_urn: The topic_urn of this UpdateEmailTemplateRequestBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this UpdateEmailTemplateRequestBody.

        OBS桶名

        :return: The obs_bucket_name of this UpdateEmailTemplateRequestBody.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this UpdateEmailTemplateRequestBody.

        OBS桶名

        :param obs_bucket_name: The obs_bucket_name of this UpdateEmailTemplateRequestBody.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def inspection_time(self):
        r"""Gets the inspection_time of this UpdateEmailTemplateRequestBody.

        诊断时间，12:00-12:00（默认）或00:00-00:00

        :return: The inspection_time of this UpdateEmailTemplateRequestBody.
        :rtype: str
        """
        return self._inspection_time

    @inspection_time.setter
    def inspection_time(self, inspection_time):
        r"""Sets the inspection_time of this UpdateEmailTemplateRequestBody.

        诊断时间，12:00-12:00（默认）或00:00-00:00

        :param inspection_time: The inspection_time of this UpdateEmailTemplateRequestBody.
        :type inspection_time: str
        """
        self._inspection_time = inspection_time

    @property
    def send_time(self):
        r"""Gets the send_time of this UpdateEmailTemplateRequestBody.

        发送时间

        :return: The send_time of this UpdateEmailTemplateRequestBody.
        :rtype: str
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        r"""Sets the send_time of this UpdateEmailTemplateRequestBody.

        发送时间

        :param send_time: The send_time of this UpdateEmailTemplateRequestBody.
        :type send_time: str
        """
        self._send_time = send_time

    @property
    def time_zone(self):
        r"""Gets the time_zone of this UpdateEmailTemplateRequestBody.

        时区

        :return: The time_zone of this UpdateEmailTemplateRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this UpdateEmailTemplateRequestBody.

        时区

        :param time_zone: The time_zone of this UpdateEmailTemplateRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, UpdateEmailTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
