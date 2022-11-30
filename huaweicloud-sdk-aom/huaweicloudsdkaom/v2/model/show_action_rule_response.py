# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowActionRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_name': 'str',
        'project_id': 'str',
        'user_name': 'str',
        'desc': 'str',
        'type': 'str',
        'notification_template': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'time_zone': 'str',
        'smn_topics': 'list[SmnTopics]'
    }

    attribute_map = {
        'rule_name': 'rule_name',
        'project_id': 'project_id',
        'user_name': 'user_name',
        'desc': 'desc',
        'type': 'type',
        'notification_template': 'notification_template',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'time_zone': 'time_zone',
        'smn_topics': 'smn_topics'
    }

    def __init__(self, rule_name=None, project_id=None, user_name=None, desc=None, type=None, notification_template=None, create_time=None, update_time=None, time_zone=None, smn_topics=None):
        """ShowActionRuleResponse

        The model defined in huaweicloud sdk

        :param rule_name: 规则名称
        :type rule_name: str
        :param project_id: 项目ID
        :type project_id: str
        :param user_name: 子账号名称
        :type user_name: str
        :param desc: 规则描述
        :type desc: str
        :param type: 规则类型。1：通知，2：用户
        :type type: str
        :param notification_template: 消息模板
        :type notification_template: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 修改时间
        :type update_time: int
        :param time_zone: 时区
        :type time_zone: str
        :param smn_topics: SMN主题信息，不能大于5
        :type smn_topics: list[:class:`huaweicloudsdkaom.v2.SmnTopics`]
        """
        
        super(ShowActionRuleResponse, self).__init__()

        self._rule_name = None
        self._project_id = None
        self._user_name = None
        self._desc = None
        self._type = None
        self._notification_template = None
        self._create_time = None
        self._update_time = None
        self._time_zone = None
        self._smn_topics = None
        self.discriminator = None

        if rule_name is not None:
            self.rule_name = rule_name
        if project_id is not None:
            self.project_id = project_id
        if user_name is not None:
            self.user_name = user_name
        if desc is not None:
            self.desc = desc
        if type is not None:
            self.type = type
        if notification_template is not None:
            self.notification_template = notification_template
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if time_zone is not None:
            self.time_zone = time_zone
        if smn_topics is not None:
            self.smn_topics = smn_topics

    @property
    def rule_name(self):
        """Gets the rule_name of this ShowActionRuleResponse.

        规则名称

        :return: The rule_name of this ShowActionRuleResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ShowActionRuleResponse.

        规则名称

        :param rule_name: The rule_name of this ShowActionRuleResponse.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def project_id(self):
        """Gets the project_id of this ShowActionRuleResponse.

        项目ID

        :return: The project_id of this ShowActionRuleResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowActionRuleResponse.

        项目ID

        :param project_id: The project_id of this ShowActionRuleResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def user_name(self):
        """Gets the user_name of this ShowActionRuleResponse.

        子账号名称

        :return: The user_name of this ShowActionRuleResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowActionRuleResponse.

        子账号名称

        :param user_name: The user_name of this ShowActionRuleResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def desc(self):
        """Gets the desc of this ShowActionRuleResponse.

        规则描述

        :return: The desc of this ShowActionRuleResponse.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ShowActionRuleResponse.

        规则描述

        :param desc: The desc of this ShowActionRuleResponse.
        :type desc: str
        """
        self._desc = desc

    @property
    def type(self):
        """Gets the type of this ShowActionRuleResponse.

        规则类型。1：通知，2：用户

        :return: The type of this ShowActionRuleResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowActionRuleResponse.

        规则类型。1：通知，2：用户

        :param type: The type of this ShowActionRuleResponse.
        :type type: str
        """
        self._type = type

    @property
    def notification_template(self):
        """Gets the notification_template of this ShowActionRuleResponse.

        消息模板

        :return: The notification_template of this ShowActionRuleResponse.
        :rtype: str
        """
        return self._notification_template

    @notification_template.setter
    def notification_template(self, notification_template):
        """Sets the notification_template of this ShowActionRuleResponse.

        消息模板

        :param notification_template: The notification_template of this ShowActionRuleResponse.
        :type notification_template: str
        """
        self._notification_template = notification_template

    @property
    def create_time(self):
        """Gets the create_time of this ShowActionRuleResponse.

        创建时间

        :return: The create_time of this ShowActionRuleResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowActionRuleResponse.

        创建时间

        :param create_time: The create_time of this ShowActionRuleResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowActionRuleResponse.

        修改时间

        :return: The update_time of this ShowActionRuleResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowActionRuleResponse.

        修改时间

        :param update_time: The update_time of this ShowActionRuleResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def time_zone(self):
        """Gets the time_zone of this ShowActionRuleResponse.

        时区

        :return: The time_zone of this ShowActionRuleResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ShowActionRuleResponse.

        时区

        :param time_zone: The time_zone of this ShowActionRuleResponse.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def smn_topics(self):
        """Gets the smn_topics of this ShowActionRuleResponse.

        SMN主题信息，不能大于5

        :return: The smn_topics of this ShowActionRuleResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.SmnTopics`]
        """
        return self._smn_topics

    @smn_topics.setter
    def smn_topics(self, smn_topics):
        """Sets the smn_topics of this ShowActionRuleResponse.

        SMN主题信息，不能大于5

        :param smn_topics: The smn_topics of this ShowActionRuleResponse.
        :type smn_topics: list[:class:`huaweicloudsdkaom.v2.SmnTopics`]
        """
        self._smn_topics = smn_topics

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
        if not isinstance(other, ShowActionRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
