# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDialogReportConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_bucket_name': 'str',
        'obs_endpoint': 'str',
        'enable_dialog_report': 'bool'
    }

    attribute_map = {
        'obs_bucket_name': 'obs_bucket_name',
        'obs_endpoint': 'obs_endpoint',
        'enable_dialog_report': 'enable_dialog_report'
    }

    def __init__(self, obs_bucket_name=None, obs_endpoint=None, enable_dialog_report=None):
        r"""CreateDialogReportConfigReq

        The model defined in huaweicloud sdk

        :param obs_bucket_name: **参数解释**： 接收对话结果上报的obs桶名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64 **默认取值**： 不涉及
        :type obs_bucket_name: str
        :param obs_endpoint: **参数解释**： 接收对话结果上报的obs终端节点。 **约束限制**： 需要为obs合法终端节点。 **取值范围**： 字符长度1-64 **默认取值**： 不涉及
        :type obs_endpoint: str
        :param enable_dialog_report: 对话结果上报开关
        :type enable_dialog_report: bool
        """
        
        

        self._obs_bucket_name = None
        self._obs_endpoint = None
        self._enable_dialog_report = None
        self.discriminator = None

        self.obs_bucket_name = obs_bucket_name
        self.obs_endpoint = obs_endpoint
        self.enable_dialog_report = enable_dialog_report

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this CreateDialogReportConfigReq.

        **参数解释**： 接收对话结果上报的obs桶名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64 **默认取值**： 不涉及

        :return: The obs_bucket_name of this CreateDialogReportConfigReq.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this CreateDialogReportConfigReq.

        **参数解释**： 接收对话结果上报的obs桶名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64 **默认取值**： 不涉及

        :param obs_bucket_name: The obs_bucket_name of this CreateDialogReportConfigReq.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def obs_endpoint(self):
        r"""Gets the obs_endpoint of this CreateDialogReportConfigReq.

        **参数解释**： 接收对话结果上报的obs终端节点。 **约束限制**： 需要为obs合法终端节点。 **取值范围**： 字符长度1-64 **默认取值**： 不涉及

        :return: The obs_endpoint of this CreateDialogReportConfigReq.
        :rtype: str
        """
        return self._obs_endpoint

    @obs_endpoint.setter
    def obs_endpoint(self, obs_endpoint):
        r"""Sets the obs_endpoint of this CreateDialogReportConfigReq.

        **参数解释**： 接收对话结果上报的obs终端节点。 **约束限制**： 需要为obs合法终端节点。 **取值范围**： 字符长度1-64 **默认取值**： 不涉及

        :param obs_endpoint: The obs_endpoint of this CreateDialogReportConfigReq.
        :type obs_endpoint: str
        """
        self._obs_endpoint = obs_endpoint

    @property
    def enable_dialog_report(self):
        r"""Gets the enable_dialog_report of this CreateDialogReportConfigReq.

        对话结果上报开关

        :return: The enable_dialog_report of this CreateDialogReportConfigReq.
        :rtype: bool
        """
        return self._enable_dialog_report

    @enable_dialog_report.setter
    def enable_dialog_report(self, enable_dialog_report):
        r"""Sets the enable_dialog_report of this CreateDialogReportConfigReq.

        对话结果上报开关

        :param enable_dialog_report: The enable_dialog_report of this CreateDialogReportConfigReq.
        :type enable_dialog_report: bool
        """
        self._enable_dialog_report = enable_dialog_report

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
        if not isinstance(other, CreateDialogReportConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
