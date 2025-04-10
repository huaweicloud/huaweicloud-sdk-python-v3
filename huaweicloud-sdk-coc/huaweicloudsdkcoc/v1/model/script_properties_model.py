# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptPropertiesModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_level': 'str',
        'version': 'str',
        'reviewers': 'list[ReviewerInfo]',
        'protocol': 'str'
    }

    attribute_map = {
        'risk_level': 'risk_level',
        'version': 'version',
        'reviewers': 'reviewers',
        'protocol': 'protocol'
    }

    def __init__(self, risk_level=None, version=None, reviewers=None, protocol=None):
        r"""ScriptPropertiesModel

        The model defined in huaweicloud sdk

        :param risk_level: 风险等级 LOW:低风险 MEDIUM:中风险 HIGH:高风险
        :type risk_level: str
        :param version: 脚本版本号
        :type version: str
        :param reviewers: 审批人，不填写不需要审批
        :type reviewers: list[:class:`huaweicloudsdkcoc.v1.ReviewerInfo`]
        :param protocol: 审批消息通知协议，用于通知审批人 DEFAULT：默认 SMS：短信 EMAIL：邮件 DING_TALK：钉钉 WE_LINK：welink WECHAT:微信 CALLNOTIFY：语言 NOT_TO_NOTIFY：不通知
        :type protocol: str
        """
        
        

        self._risk_level = None
        self._version = None
        self._reviewers = None
        self._protocol = None
        self.discriminator = None

        self.risk_level = risk_level
        self.version = version
        if reviewers is not None:
            self.reviewers = reviewers
        if protocol is not None:
            self.protocol = protocol

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ScriptPropertiesModel.

        风险等级 LOW:低风险 MEDIUM:中风险 HIGH:高风险

        :return: The risk_level of this ScriptPropertiesModel.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ScriptPropertiesModel.

        风险等级 LOW:低风险 MEDIUM:中风险 HIGH:高风险

        :param risk_level: The risk_level of this ScriptPropertiesModel.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def version(self):
        r"""Gets the version of this ScriptPropertiesModel.

        脚本版本号

        :return: The version of this ScriptPropertiesModel.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ScriptPropertiesModel.

        脚本版本号

        :param version: The version of this ScriptPropertiesModel.
        :type version: str
        """
        self._version = version

    @property
    def reviewers(self):
        r"""Gets the reviewers of this ScriptPropertiesModel.

        审批人，不填写不需要审批

        :return: The reviewers of this ScriptPropertiesModel.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ReviewerInfo`]
        """
        return self._reviewers

    @reviewers.setter
    def reviewers(self, reviewers):
        r"""Sets the reviewers of this ScriptPropertiesModel.

        审批人，不填写不需要审批

        :param reviewers: The reviewers of this ScriptPropertiesModel.
        :type reviewers: list[:class:`huaweicloudsdkcoc.v1.ReviewerInfo`]
        """
        self._reviewers = reviewers

    @property
    def protocol(self):
        r"""Gets the protocol of this ScriptPropertiesModel.

        审批消息通知协议，用于通知审批人 DEFAULT：默认 SMS：短信 EMAIL：邮件 DING_TALK：钉钉 WE_LINK：welink WECHAT:微信 CALLNOTIFY：语言 NOT_TO_NOTIFY：不通知

        :return: The protocol of this ScriptPropertiesModel.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ScriptPropertiesModel.

        审批消息通知协议，用于通知审批人 DEFAULT：默认 SMS：短信 EMAIL：邮件 DING_TALK：钉钉 WE_LINK：welink WECHAT:微信 CALLNOTIFY：语言 NOT_TO_NOTIFY：不通知

        :param protocol: The protocol of this ScriptPropertiesModel.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, ScriptPropertiesModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
