# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateApplicationViewRequestBodySyncRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ep_id': 'str',
        'rule_tags': 'str'
    }

    attribute_map = {
        'ep_id': 'ep_id',
        'rule_tags': 'rule_tags'
    }

    def __init__(self, ep_id=None, rule_tags=None):
        r"""BatchCreateApplicationViewRequestBodySyncRules

        The model defined in huaweicloud sdk

        :param ep_id: **参数解释：** 企业项目id。 **约束限制：** 不涉及。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。 **默认取值：** 不涉及。
        :type ep_id: str
        :param rule_tags: **参数解释：** 关联标签。 **约束限制：** 不涉及。 **取值范围：** 可自定义。 **默认取值：** 不涉及。
        :type rule_tags: str
        """
        
        

        self._ep_id = None
        self._rule_tags = None
        self.discriminator = None

        if ep_id is not None:
            self.ep_id = ep_id
        if rule_tags is not None:
            self.rule_tags = rule_tags

    @property
    def ep_id(self):
        r"""Gets the ep_id of this BatchCreateApplicationViewRequestBodySyncRules.

        **参数解释：** 企业项目id。 **约束限制：** 不涉及。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。 **默认取值：** 不涉及。

        :return: The ep_id of this BatchCreateApplicationViewRequestBodySyncRules.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this BatchCreateApplicationViewRequestBodySyncRules.

        **参数解释：** 企业项目id。 **约束限制：** 不涉及。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。 **默认取值：** 不涉及。

        :param ep_id: The ep_id of this BatchCreateApplicationViewRequestBodySyncRules.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def rule_tags(self):
        r"""Gets the rule_tags of this BatchCreateApplicationViewRequestBodySyncRules.

        **参数解释：** 关联标签。 **约束限制：** 不涉及。 **取值范围：** 可自定义。 **默认取值：** 不涉及。

        :return: The rule_tags of this BatchCreateApplicationViewRequestBodySyncRules.
        :rtype: str
        """
        return self._rule_tags

    @rule_tags.setter
    def rule_tags(self, rule_tags):
        r"""Sets the rule_tags of this BatchCreateApplicationViewRequestBodySyncRules.

        **参数解释：** 关联标签。 **约束限制：** 不涉及。 **取值范围：** 可自定义。 **默认取值：** 不涉及。

        :param rule_tags: The rule_tags of this BatchCreateApplicationViewRequestBodySyncRules.
        :type rule_tags: str
        """
        self._rule_tags = rule_tags

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
        if not isinstance(other, BatchCreateApplicationViewRequestBodySyncRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
