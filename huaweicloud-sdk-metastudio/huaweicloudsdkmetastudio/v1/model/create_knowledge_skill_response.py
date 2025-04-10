# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKnowledgeSkillResponse(SdkResponse):

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
        'identify': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'skill_id': 'skill_id',
        'identify': 'identify',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, skill_id=None, identify=None, x_request_id=None):
        r"""CreateKnowledgeSkillResponse

        The model defined in huaweicloud sdk

        :param skill_id: 技能ID。
        :type skill_id: str
        :param identify: 技能标识。
        :type identify: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateKnowledgeSkillResponse, self).__init__()

        self._skill_id = None
        self._identify = None
        self._x_request_id = None
        self.discriminator = None

        if skill_id is not None:
            self.skill_id = skill_id
        if identify is not None:
            self.identify = identify
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def skill_id(self):
        r"""Gets the skill_id of this CreateKnowledgeSkillResponse.

        技能ID。

        :return: The skill_id of this CreateKnowledgeSkillResponse.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        r"""Sets the skill_id of this CreateKnowledgeSkillResponse.

        技能ID。

        :param skill_id: The skill_id of this CreateKnowledgeSkillResponse.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def identify(self):
        r"""Gets the identify of this CreateKnowledgeSkillResponse.

        技能标识。

        :return: The identify of this CreateKnowledgeSkillResponse.
        :rtype: str
        """
        return self._identify

    @identify.setter
    def identify(self, identify):
        r"""Sets the identify of this CreateKnowledgeSkillResponse.

        技能标识。

        :param identify: The identify of this CreateKnowledgeSkillResponse.
        :type identify: str
        """
        self._identify = identify

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateKnowledgeSkillResponse.

        :return: The x_request_id of this CreateKnowledgeSkillResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateKnowledgeSkillResponse.

        :param x_request_id: The x_request_id of this CreateKnowledgeSkillResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CreateKnowledgeSkillResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
