# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKnowledgeSkillRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'skill_id': 'str',
        'body': 'UpdateKnowledgeSkillReq'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'skill_id': 'skill_id',
        'body': 'body'
    }

    def __init__(self, x_app_user_id=None, skill_id=None, body=None):
        """UpdateKnowledgeSkillRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param skill_id: 技能ID。
        :type skill_id: str
        :param body: Body of the UpdateKnowledgeSkillRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeSkillReq`
        """
        
        

        self._x_app_user_id = None
        self._skill_id = None
        self._body = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.skill_id = skill_id
        if body is not None:
            self.body = body

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this UpdateKnowledgeSkillRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this UpdateKnowledgeSkillRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this UpdateKnowledgeSkillRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this UpdateKnowledgeSkillRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def skill_id(self):
        """Gets the skill_id of this UpdateKnowledgeSkillRequest.

        技能ID。

        :return: The skill_id of this UpdateKnowledgeSkillRequest.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        """Sets the skill_id of this UpdateKnowledgeSkillRequest.

        技能ID。

        :param skill_id: The skill_id of this UpdateKnowledgeSkillRequest.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def body(self):
        """Gets the body of this UpdateKnowledgeSkillRequest.

        :return: The body of this UpdateKnowledgeSkillRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeSkillReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateKnowledgeSkillRequest.

        :param body: The body of this UpdateKnowledgeSkillRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeSkillReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateKnowledgeSkillRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
