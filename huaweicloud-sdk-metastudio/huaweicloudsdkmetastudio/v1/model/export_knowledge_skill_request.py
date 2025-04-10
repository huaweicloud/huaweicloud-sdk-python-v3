# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportKnowledgeSkillRequest:

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
        'export_type': 'int'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'skill_id': 'skill_id',
        'export_type': 'export_type'
    }

    def __init__(self, x_app_user_id=None, skill_id=None, export_type=None):
        r"""ExportKnowledgeSkillRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param skill_id: 技能ID。
        :type skill_id: str
        :param export_type: 导出格式类型。0：科大讯飞
        :type export_type: int
        """
        
        

        self._x_app_user_id = None
        self._skill_id = None
        self._export_type = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.skill_id = skill_id
        self.export_type = export_type

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ExportKnowledgeSkillRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ExportKnowledgeSkillRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ExportKnowledgeSkillRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ExportKnowledgeSkillRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def skill_id(self):
        r"""Gets the skill_id of this ExportKnowledgeSkillRequest.

        技能ID。

        :return: The skill_id of this ExportKnowledgeSkillRequest.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        r"""Sets the skill_id of this ExportKnowledgeSkillRequest.

        技能ID。

        :param skill_id: The skill_id of this ExportKnowledgeSkillRequest.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def export_type(self):
        r"""Gets the export_type of this ExportKnowledgeSkillRequest.

        导出格式类型。0：科大讯飞

        :return: The export_type of this ExportKnowledgeSkillRequest.
        :rtype: int
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        r"""Sets the export_type of this ExportKnowledgeSkillRequest.

        导出格式类型。0：科大讯飞

        :param export_type: The export_type of this ExportKnowledgeSkillRequest.
        :type export_type: int
        """
        self._export_type = export_type

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
        if not isinstance(other, ExportKnowledgeSkillRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
