# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSkillOrderListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'skill_name': 'str',
        'skill_form': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'skill_name': 'skill_name',
        'skill_form': 'skill_form'
    }

    def __init__(self, limit=None, offset=None, skill_name=None, skill_form=None):
        r"""ShowSkillOrderListRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量, 最大 100，默认值 10
        :type limit: int
        :param offset: 查询的起始位置, 默认值 0
        :type offset: int
        :param skill_name: 技能名称，支持模糊匹配。中英文、数字、下划线、中划线 长度[1-60]
        :type skill_name: str
        :param skill_form: 技能形式，no_termplate不支持Modelbox部署模板，support_template支持Modelbox模板。
        :type skill_form: str
        """
        
        

        self._limit = None
        self._offset = None
        self._skill_name = None
        self._skill_form = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if skill_name is not None:
            self.skill_name = skill_name
        if skill_form is not None:
            self.skill_form = skill_form

    @property
    def limit(self):
        r"""Gets the limit of this ShowSkillOrderListRequest.

        每页显示的条目数量, 最大 100，默认值 10

        :return: The limit of this ShowSkillOrderListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowSkillOrderListRequest.

        每页显示的条目数量, 最大 100，默认值 10

        :param limit: The limit of this ShowSkillOrderListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowSkillOrderListRequest.

        查询的起始位置, 默认值 0

        :return: The offset of this ShowSkillOrderListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowSkillOrderListRequest.

        查询的起始位置, 默认值 0

        :param offset: The offset of this ShowSkillOrderListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def skill_name(self):
        r"""Gets the skill_name of this ShowSkillOrderListRequest.

        技能名称，支持模糊匹配。中英文、数字、下划线、中划线 长度[1-60]

        :return: The skill_name of this ShowSkillOrderListRequest.
        :rtype: str
        """
        return self._skill_name

    @skill_name.setter
    def skill_name(self, skill_name):
        r"""Sets the skill_name of this ShowSkillOrderListRequest.

        技能名称，支持模糊匹配。中英文、数字、下划线、中划线 长度[1-60]

        :param skill_name: The skill_name of this ShowSkillOrderListRequest.
        :type skill_name: str
        """
        self._skill_name = skill_name

    @property
    def skill_form(self):
        r"""Gets the skill_form of this ShowSkillOrderListRequest.

        技能形式，no_termplate不支持Modelbox部署模板，support_template支持Modelbox模板。

        :return: The skill_form of this ShowSkillOrderListRequest.
        :rtype: str
        """
        return self._skill_form

    @skill_form.setter
    def skill_form(self, skill_form):
        r"""Sets the skill_form of this ShowSkillOrderListRequest.

        技能形式，no_termplate不支持Modelbox部署模板，support_template支持Modelbox模板。

        :param skill_form: The skill_form of this ShowSkillOrderListRequest.
        :type skill_form: str
        """
        self._skill_form = skill_form

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
        if not isinstance(other, ShowSkillOrderListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
