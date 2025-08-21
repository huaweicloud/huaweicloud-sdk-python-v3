# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateReportProfileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'report_profile_id': 'str',
        'body': 'UpdateReportProfileDto'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'report_profile_id': 'report_profile_id',
        'body': 'body'
    }

    def __init__(self, fw_instance_id=None, report_profile_id=None, body=None):
        r"""UpdateReportProfileRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        :param report_profile_id: **参数解释**： 安全报告模板ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type report_profile_id: str
        :param body: Body of the UpdateReportProfileRequest
        :type body: :class:`huaweicloudsdkcfw.v1.UpdateReportProfileDto`
        """
        
        

        self._fw_instance_id = None
        self._report_profile_id = None
        self._body = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        self.report_profile_id = report_profile_id
        if body is not None:
            self.body = body

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this UpdateReportProfileRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this UpdateReportProfileRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this UpdateReportProfileRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this UpdateReportProfileRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def report_profile_id(self):
        r"""Gets the report_profile_id of this UpdateReportProfileRequest.

        **参数解释**： 安全报告模板ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The report_profile_id of this UpdateReportProfileRequest.
        :rtype: str
        """
        return self._report_profile_id

    @report_profile_id.setter
    def report_profile_id(self, report_profile_id):
        r"""Sets the report_profile_id of this UpdateReportProfileRequest.

        **参数解释**： 安全报告模板ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param report_profile_id: The report_profile_id of this UpdateReportProfileRequest.
        :type report_profile_id: str
        """
        self._report_profile_id = report_profile_id

    @property
    def body(self):
        r"""Gets the body of this UpdateReportProfileRequest.

        :return: The body of this UpdateReportProfileRequest.
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateReportProfileDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateReportProfileRequest.

        :param body: The body of this UpdateReportProfileRequest.
        :type body: :class:`huaweicloudsdkcfw.v1.UpdateReportProfileDto`
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
        if not isinstance(other, UpdateReportProfileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
