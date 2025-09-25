# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LlmRuleInfoRespDetectOpts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'content_idx': 'str',
        'action': 'LlmRuleInfoRespDetectOptsAction'
    }

    attribute_map = {
        'enable': 'enable',
        'content_idx': 'content_idx',
        'action': 'action'
    }

    def __init__(self, enable=None, content_idx=None, action=None):
        r"""LlmRuleInfoRespDetectOpts

        The model defined in huaweicloud sdk

        :param enable: 检测开关
        :type enable: bool
        :param content_idx: 响应内容索引
        :type content_idx: str
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoRespDetectOptsAction`
        """
        
        

        self._enable = None
        self._content_idx = None
        self._action = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if content_idx is not None:
            self.content_idx = content_idx
        if action is not None:
            self.action = action

    @property
    def enable(self):
        r"""Gets the enable of this LlmRuleInfoRespDetectOpts.

        检测开关

        :return: The enable of this LlmRuleInfoRespDetectOpts.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this LlmRuleInfoRespDetectOpts.

        检测开关

        :param enable: The enable of this LlmRuleInfoRespDetectOpts.
        :type enable: bool
        """
        self._enable = enable

    @property
    def content_idx(self):
        r"""Gets the content_idx of this LlmRuleInfoRespDetectOpts.

        响应内容索引

        :return: The content_idx of this LlmRuleInfoRespDetectOpts.
        :rtype: str
        """
        return self._content_idx

    @content_idx.setter
    def content_idx(self, content_idx):
        r"""Sets the content_idx of this LlmRuleInfoRespDetectOpts.

        响应内容索引

        :param content_idx: The content_idx of this LlmRuleInfoRespDetectOpts.
        :type content_idx: str
        """
        self._content_idx = content_idx

    @property
    def action(self):
        r"""Gets the action of this LlmRuleInfoRespDetectOpts.

        :return: The action of this LlmRuleInfoRespDetectOpts.
        :rtype: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoRespDetectOptsAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this LlmRuleInfoRespDetectOpts.

        :param action: The action of this LlmRuleInfoRespDetectOpts.
        :type action: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoRespDetectOptsAction`
        """
        self._action = action

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
        if not isinstance(other, LlmRuleInfoRespDetectOpts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
