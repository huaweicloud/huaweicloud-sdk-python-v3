# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddOrUpdateMetricOrEventAlarmRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_id': 'str',
        'enterprise_project_id': 'str',
        'body': 'AddOrUpdateAlarmRuleV4RequestBody'
    }

    attribute_map = {
        'action_id': 'action_id',
        'enterprise_project_id': 'Enterprise-Project-Id',
        'body': 'body'
    }

    def __init__(self, action_id=None, enterprise_project_id=None, body=None):
        r"""AddOrUpdateMetricOrEventAlarmRuleRequest

        The model defined in huaweicloud sdk

        :param action_id: 告警规则id。 - 新增告警时，填写\&quot;add-alarm-action\&quot; - 更新告警时，填写“update-alarm-action”
        :type action_id: str
        :param enterprise_project_id: 企业项目id。 - 查询单个企业项目下实例，填写企业项目id。  - 查询所有企业项目下实例，填写“all_granted_eps”。
        :type enterprise_project_id: str
        :param body: Body of the AddOrUpdateMetricOrEventAlarmRuleRequest
        :type body: :class:`huaweicloudsdkaom.v2.AddOrUpdateAlarmRuleV4RequestBody`
        """
        
        

        self._action_id = None
        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.action_id = action_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def action_id(self):
        r"""Gets the action_id of this AddOrUpdateMetricOrEventAlarmRuleRequest.

        告警规则id。 - 新增告警时，填写\"add-alarm-action\" - 更新告警时，填写“update-alarm-action”

        :return: The action_id of this AddOrUpdateMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this AddOrUpdateMetricOrEventAlarmRuleRequest.

        告警规则id。 - 新增告警时，填写\"add-alarm-action\" - 更新告警时，填写“update-alarm-action”

        :param action_id: The action_id of this AddOrUpdateMetricOrEventAlarmRuleRequest.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AddOrUpdateMetricOrEventAlarmRuleRequest.

        企业项目id。 - 查询单个企业项目下实例，填写企业项目id。  - 查询所有企业项目下实例，填写“all_granted_eps”。

        :return: The enterprise_project_id of this AddOrUpdateMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AddOrUpdateMetricOrEventAlarmRuleRequest.

        企业项目id。 - 查询单个企业项目下实例，填写企业项目id。  - 查询所有企业项目下实例，填写“all_granted_eps”。

        :param enterprise_project_id: The enterprise_project_id of this AddOrUpdateMetricOrEventAlarmRuleRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        r"""Gets the body of this AddOrUpdateMetricOrEventAlarmRuleRequest.

        :return: The body of this AddOrUpdateMetricOrEventAlarmRuleRequest.
        :rtype: :class:`huaweicloudsdkaom.v2.AddOrUpdateAlarmRuleV4RequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AddOrUpdateMetricOrEventAlarmRuleRequest.

        :param body: The body of this AddOrUpdateMetricOrEventAlarmRuleRequest.
        :type body: :class:`huaweicloudsdkaom.v2.AddOrUpdateAlarmRuleV4RequestBody`
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
        if not isinstance(other, AddOrUpdateMetricOrEventAlarmRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
