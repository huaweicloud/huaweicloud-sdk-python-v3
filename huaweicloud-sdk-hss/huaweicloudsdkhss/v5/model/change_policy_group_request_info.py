# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangePolicyGroupRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'protect_mode': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'protect_mode': 'protect_mode'
    }

    def __init__(self, group_id=None, protect_mode=None):
        r"""ChangePolicyGroupRequestInfo

        The model defined in huaweicloud sdk

        :param group_id: **参数解释**: 需要修改的的策略组的策略组ID **约束限制**: 需要使用 ListPolicyGroup 接口查询策略组ID，在 ListPolicyGroup 接口的响应体中返回的 group_id 是可以被修改的策略组ID **取值范围**: 字符长度36-64 **默认取值**: 不涉及
        :type group_id: str
        :param protect_mode: **参数解释**: 防护模式 **约束限制**: 不涉及 **取值范围**: - high_detection: 高检出模式。 - equalization: 均衡模式。  **默认取值**: 不涉及 
        :type protect_mode: str
        """
        
        

        self._group_id = None
        self._protect_mode = None
        self.discriminator = None

        self.group_id = group_id
        if protect_mode is not None:
            self.protect_mode = protect_mode

    @property
    def group_id(self):
        r"""Gets the group_id of this ChangePolicyGroupRequestInfo.

        **参数解释**: 需要修改的的策略组的策略组ID **约束限制**: 需要使用 ListPolicyGroup 接口查询策略组ID，在 ListPolicyGroup 接口的响应体中返回的 group_id 是可以被修改的策略组ID **取值范围**: 字符长度36-64 **默认取值**: 不涉及

        :return: The group_id of this ChangePolicyGroupRequestInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ChangePolicyGroupRequestInfo.

        **参数解释**: 需要修改的的策略组的策略组ID **约束限制**: 需要使用 ListPolicyGroup 接口查询策略组ID，在 ListPolicyGroup 接口的响应体中返回的 group_id 是可以被修改的策略组ID **取值范围**: 字符长度36-64 **默认取值**: 不涉及

        :param group_id: The group_id of this ChangePolicyGroupRequestInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def protect_mode(self):
        r"""Gets the protect_mode of this ChangePolicyGroupRequestInfo.

        **参数解释**: 防护模式 **约束限制**: 不涉及 **取值范围**: - high_detection: 高检出模式。 - equalization: 均衡模式。  **默认取值**: 不涉及 

        :return: The protect_mode of this ChangePolicyGroupRequestInfo.
        :rtype: str
        """
        return self._protect_mode

    @protect_mode.setter
    def protect_mode(self, protect_mode):
        r"""Sets the protect_mode of this ChangePolicyGroupRequestInfo.

        **参数解释**: 防护模式 **约束限制**: 不涉及 **取值范围**: - high_detection: 高检出模式。 - equalization: 均衡模式。  **默认取值**: 不涉及 

        :param protect_mode: The protect_mode of this ChangePolicyGroupRequestInfo.
        :type protect_mode: str
        """
        self._protect_mode = protect_mode

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
        if not isinstance(other, ChangePolicyGroupRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
