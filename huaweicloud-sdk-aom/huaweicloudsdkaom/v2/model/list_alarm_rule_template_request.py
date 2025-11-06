# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmRuleTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'Enterprise-Project-Id',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, enterprise_project_id=None, id=None, type=None):
        r"""ListAlarmRuleTemplateRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。 - 查询单个企业项目下实例，填写企业项目id。  - 查询所有企业项目下实例，填写“all_granted_eps”。
        :type enterprise_project_id: str
        :param id: 告警模板id。
        :type id: str
        :param type: 告警模板类型。默认值为“template”
        :type type: str
        """
        
        

        self._enterprise_project_id = None
        self._id = None
        self._type = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        self.type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAlarmRuleTemplateRequest.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。 - 查询单个企业项目下实例，填写企业项目id。  - 查询所有企业项目下实例，填写“all_granted_eps”。

        :return: The enterprise_project_id of this ListAlarmRuleTemplateRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAlarmRuleTemplateRequest.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。 - 查询单个企业项目下实例，填写企业项目id。  - 查询所有企业项目下实例，填写“all_granted_eps”。

        :param enterprise_project_id: The enterprise_project_id of this ListAlarmRuleTemplateRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this ListAlarmRuleTemplateRequest.

        告警模板id。

        :return: The id of this ListAlarmRuleTemplateRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAlarmRuleTemplateRequest.

        告警模板id。

        :param id: The id of this ListAlarmRuleTemplateRequest.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ListAlarmRuleTemplateRequest.

        告警模板类型。默认值为“template”

        :return: The type of this ListAlarmRuleTemplateRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAlarmRuleTemplateRequest.

        告警模板类型。默认值为“template”

        :param type: The type of this ListAlarmRuleTemplateRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListAlarmRuleTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
