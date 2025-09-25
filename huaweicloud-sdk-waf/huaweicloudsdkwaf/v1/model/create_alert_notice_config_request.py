# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlertNoticeConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'enterprise_project_id': 'str',
        'body': 'AlertNoticeConfig'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'enterprise_project_id': 'enterpriseProjectId',
        'body': 'body'
    }

    def __init__(self, x_language=None, enterprise_project_id=None, body=None):
        r"""CreateAlertNoticeConfigRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释：** 语言，默认值为en-us。zh-cn（中文）/en-us（英文） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** zh-cn
        :type x_language: str
        :param enterprise_project_id: **参数解释：** 企业项目ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type enterprise_project_id: str
        :param body: Body of the CreateAlertNoticeConfigRequest
        :type body: :class:`huaweicloudsdkwaf.v1.AlertNoticeConfig`
        """
        
        

        self._x_language = None
        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.x_language = x_language
        self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this CreateAlertNoticeConfigRequest.

        **参数解释：** 语言，默认值为en-us。zh-cn（中文）/en-us（英文） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** zh-cn

        :return: The x_language of this CreateAlertNoticeConfigRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this CreateAlertNoticeConfigRequest.

        **参数解释：** 语言，默认值为en-us。zh-cn（中文）/en-us（英文） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** zh-cn

        :param x_language: The x_language of this CreateAlertNoticeConfigRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateAlertNoticeConfigRequest.

        **参数解释：** 企业项目ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The enterprise_project_id of this CreateAlertNoticeConfigRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateAlertNoticeConfigRequest.

        **参数解释：** 企业项目ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param enterprise_project_id: The enterprise_project_id of this CreateAlertNoticeConfigRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        r"""Gets the body of this CreateAlertNoticeConfigRequest.

        :return: The body of this CreateAlertNoticeConfigRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.AlertNoticeConfig`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateAlertNoticeConfigRequest.

        :param body: The body of this CreateAlertNoticeConfigRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.AlertNoticeConfig`
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
        if not isinstance(other, CreateAlertNoticeConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
