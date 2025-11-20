# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteAlertNoticeConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'x_language': 'str',
        'body': 'BatchDeleteAlertNoticeConfigBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterpriseProjectId',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, x_language=None, body=None):
        r"""BatchDeleteAlertNoticeConfigRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释：** 企业项目ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type enterprise_project_id: str
        :param x_language: 语言，默认值为en-us。zh-cn（中文）/en-us（英文）
        :type x_language: str
        :param body: Body of the BatchDeleteAlertNoticeConfigRequest
        :type body: :class:`huaweicloudsdkwaf.v1.BatchDeleteAlertNoticeConfigBody`
        """
        
        

        self._enterprise_project_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this BatchDeleteAlertNoticeConfigRequest.

        **参数解释：** 企业项目ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The enterprise_project_id of this BatchDeleteAlertNoticeConfigRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this BatchDeleteAlertNoticeConfigRequest.

        **参数解释：** 企业项目ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param enterprise_project_id: The enterprise_project_id of this BatchDeleteAlertNoticeConfigRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def x_language(self):
        r"""Gets the x_language of this BatchDeleteAlertNoticeConfigRequest.

        语言，默认值为en-us。zh-cn（中文）/en-us（英文）

        :return: The x_language of this BatchDeleteAlertNoticeConfigRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this BatchDeleteAlertNoticeConfigRequest.

        语言，默认值为en-us。zh-cn（中文）/en-us（英文）

        :param x_language: The x_language of this BatchDeleteAlertNoticeConfigRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this BatchDeleteAlertNoticeConfigRequest.

        :return: The body of this BatchDeleteAlertNoticeConfigRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.BatchDeleteAlertNoticeConfigBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchDeleteAlertNoticeConfigRequest.

        :param body: The body of this BatchDeleteAlertNoticeConfigRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.BatchDeleteAlertNoticeConfigBody`
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
        if not isinstance(other, BatchDeleteAlertNoticeConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
