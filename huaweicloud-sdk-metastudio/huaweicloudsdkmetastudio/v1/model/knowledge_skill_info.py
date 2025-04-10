# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KnowledgeSkillInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'skill_id': 'str',
        'name': 'str',
        'identify': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'skill_id': 'skill_id',
        'name': 'name',
        'identify': 'identify',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, skill_id=None, name=None, identify=None, create_time=None, update_time=None):
        r"""KnowledgeSkillInfo

        The model defined in huaweicloud sdk

        :param skill_id: 技能ID。
        :type skill_id: str
        :param name: 技能名称。
        :type name: str
        :param identify: 技能标识。
        :type identify: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._skill_id = None
        self._name = None
        self._identify = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if skill_id is not None:
            self.skill_id = skill_id
        if name is not None:
            self.name = name
        if identify is not None:
            self.identify = identify
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def skill_id(self):
        r"""Gets the skill_id of this KnowledgeSkillInfo.

        技能ID。

        :return: The skill_id of this KnowledgeSkillInfo.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        r"""Sets the skill_id of this KnowledgeSkillInfo.

        技能ID。

        :param skill_id: The skill_id of this KnowledgeSkillInfo.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def name(self):
        r"""Gets the name of this KnowledgeSkillInfo.

        技能名称。

        :return: The name of this KnowledgeSkillInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KnowledgeSkillInfo.

        技能名称。

        :param name: The name of this KnowledgeSkillInfo.
        :type name: str
        """
        self._name = name

    @property
    def identify(self):
        r"""Gets the identify of this KnowledgeSkillInfo.

        技能标识。

        :return: The identify of this KnowledgeSkillInfo.
        :rtype: str
        """
        return self._identify

    @identify.setter
    def identify(self, identify):
        r"""Sets the identify of this KnowledgeSkillInfo.

        技能标识。

        :param identify: The identify of this KnowledgeSkillInfo.
        :type identify: str
        """
        self._identify = identify

    @property
    def create_time(self):
        r"""Gets the create_time of this KnowledgeSkillInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this KnowledgeSkillInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this KnowledgeSkillInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this KnowledgeSkillInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this KnowledgeSkillInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this KnowledgeSkillInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this KnowledgeSkillInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this KnowledgeSkillInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, KnowledgeSkillInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
