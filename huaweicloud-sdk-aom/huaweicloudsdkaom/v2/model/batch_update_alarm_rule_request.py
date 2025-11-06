# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateAlarmRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'enterprise_project_id': 'str',
        'body': 'BatchUpdateRequest'
    }

    attribute_map = {
        'action': 'action',
        'enterprise_project_id': 'Enterprise-Project-Id',
        'body': 'body'
    }

    def __init__(self, action=None, enterprise_project_id=None, body=None):
        r"""BatchUpdateAlarmRuleRequest

        The model defined in huaweicloud sdk

        :param action: 批量操作action：  - enable：批量启动Prometheus监控告警规则 - disable：批量停止Prometheus监控告警规则 - BATCH_UPDATE_ACTION_RULE：批量修改Prometheus监控告警规则的告警行动规则
        :type action: str
        :param enterprise_project_id: 企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml) 。 - 批量启停或批量修改单个企业项目下实例，填写企业项目id。  - 不填 则批量启停或批量修改默认企业项目下实例，默认企业项目id为0。
        :type enterprise_project_id: str
        :param body: Body of the BatchUpdateAlarmRuleRequest
        :type body: :class:`huaweicloudsdkaom.v2.BatchUpdateRequest`
        """
        
        

        self._action = None
        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.action = action
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def action(self):
        r"""Gets the action of this BatchUpdateAlarmRuleRequest.

        批量操作action：  - enable：批量启动Prometheus监控告警规则 - disable：批量停止Prometheus监控告警规则 - BATCH_UPDATE_ACTION_RULE：批量修改Prometheus监控告警规则的告警行动规则

        :return: The action of this BatchUpdateAlarmRuleRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchUpdateAlarmRuleRequest.

        批量操作action：  - enable：批量启动Prometheus监控告警规则 - disable：批量停止Prometheus监控告警规则 - BATCH_UPDATE_ACTION_RULE：批量修改Prometheus监控告警规则的告警行动规则

        :param action: The action of this BatchUpdateAlarmRuleRequest.
        :type action: str
        """
        self._action = action

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this BatchUpdateAlarmRuleRequest.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml) 。 - 批量启停或批量修改单个企业项目下实例，填写企业项目id。  - 不填 则批量启停或批量修改默认企业项目下实例，默认企业项目id为0。

        :return: The enterprise_project_id of this BatchUpdateAlarmRuleRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this BatchUpdateAlarmRuleRequest.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml) 。 - 批量启停或批量修改单个企业项目下实例，填写企业项目id。  - 不填 则批量启停或批量修改默认企业项目下实例，默认企业项目id为0。

        :param enterprise_project_id: The enterprise_project_id of this BatchUpdateAlarmRuleRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        r"""Gets the body of this BatchUpdateAlarmRuleRequest.

        :return: The body of this BatchUpdateAlarmRuleRequest.
        :rtype: :class:`huaweicloudsdkaom.v2.BatchUpdateRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchUpdateAlarmRuleRequest.

        :param body: The body of this BatchUpdateAlarmRuleRequest.
        :type body: :class:`huaweicloudsdkaom.v2.BatchUpdateRequest`
        """
        self._body = body

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
        if not isinstance(other, BatchUpdateAlarmRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
