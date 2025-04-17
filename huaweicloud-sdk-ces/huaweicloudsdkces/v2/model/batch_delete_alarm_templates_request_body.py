# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteAlarmTemplatesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_ids': 'list[str]',
        'delete_associate_alarm': 'bool'
    }

    attribute_map = {
        'template_ids': 'template_ids',
        'delete_associate_alarm': 'delete_associate_alarm'
    }

    def __init__(self, template_ids=None, delete_associate_alarm=None):
        r"""BatchDeleteAlarmTemplatesRequestBody

        The model defined in huaweicloud sdk

        :param template_ids: 需要批量删除的告警模板的ID列表。未关联告警规则的模板可以批量删除多个；已关联告警规则的告警模板，单次只允许删除一个，若同时删除多个已关联告警规则的告警模板，将返回异常
        :type template_ids: list[str]
        :param delete_associate_alarm: 如果告警模板关联了告警规则，是否级联删除告警规则，true代表级联删除，false代表只删除告警模板
        :type delete_associate_alarm: bool
        """
        
        

        self._template_ids = None
        self._delete_associate_alarm = None
        self.discriminator = None

        self.template_ids = template_ids
        self.delete_associate_alarm = delete_associate_alarm

    @property
    def template_ids(self):
        r"""Gets the template_ids of this BatchDeleteAlarmTemplatesRequestBody.

        需要批量删除的告警模板的ID列表。未关联告警规则的模板可以批量删除多个；已关联告警规则的告警模板，单次只允许删除一个，若同时删除多个已关联告警规则的告警模板，将返回异常

        :return: The template_ids of this BatchDeleteAlarmTemplatesRequestBody.
        :rtype: list[str]
        """
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        r"""Sets the template_ids of this BatchDeleteAlarmTemplatesRequestBody.

        需要批量删除的告警模板的ID列表。未关联告警规则的模板可以批量删除多个；已关联告警规则的告警模板，单次只允许删除一个，若同时删除多个已关联告警规则的告警模板，将返回异常

        :param template_ids: The template_ids of this BatchDeleteAlarmTemplatesRequestBody.
        :type template_ids: list[str]
        """
        self._template_ids = template_ids

    @property
    def delete_associate_alarm(self):
        r"""Gets the delete_associate_alarm of this BatchDeleteAlarmTemplatesRequestBody.

        如果告警模板关联了告警规则，是否级联删除告警规则，true代表级联删除，false代表只删除告警模板

        :return: The delete_associate_alarm of this BatchDeleteAlarmTemplatesRequestBody.
        :rtype: bool
        """
        return self._delete_associate_alarm

    @delete_associate_alarm.setter
    def delete_associate_alarm(self, delete_associate_alarm):
        r"""Sets the delete_associate_alarm of this BatchDeleteAlarmTemplatesRequestBody.

        如果告警模板关联了告警规则，是否级联删除告警规则，true代表级联删除，false代表只删除告警模板

        :param delete_associate_alarm: The delete_associate_alarm of this BatchDeleteAlarmTemplatesRequestBody.
        :type delete_associate_alarm: bool
        """
        self._delete_associate_alarm = delete_associate_alarm

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
        if not isinstance(other, BatchDeleteAlarmTemplatesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
