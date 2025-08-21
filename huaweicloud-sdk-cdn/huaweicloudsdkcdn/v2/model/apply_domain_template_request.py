# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyDomainTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tml_id': 'str',
        'body': 'TemplateApplyRequestBody'
    }

    attribute_map = {
        'tml_id': 'tml_id',
        'body': 'body'
    }

    def __init__(self, tml_id=None, body=None):
        r"""ApplyDomainTemplateRequest

        The model defined in huaweicloud sdk

        :param tml_id: **参数解释：** 域名模板ID，可以通过查询域名模板列表接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tml_id: str
        :param body: Body of the ApplyDomainTemplateRequest
        :type body: :class:`huaweicloudsdkcdn.v2.TemplateApplyRequestBody`
        """
        
        

        self._tml_id = None
        self._body = None
        self.discriminator = None

        self.tml_id = tml_id
        if body is not None:
            self.body = body

    @property
    def tml_id(self):
        r"""Gets the tml_id of this ApplyDomainTemplateRequest.

        **参数解释：** 域名模板ID，可以通过查询域名模板列表接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tml_id of this ApplyDomainTemplateRequest.
        :rtype: str
        """
        return self._tml_id

    @tml_id.setter
    def tml_id(self, tml_id):
        r"""Sets the tml_id of this ApplyDomainTemplateRequest.

        **参数解释：** 域名模板ID，可以通过查询域名模板列表接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tml_id: The tml_id of this ApplyDomainTemplateRequest.
        :type tml_id: str
        """
        self._tml_id = tml_id

    @property
    def body(self):
        r"""Gets the body of this ApplyDomainTemplateRequest.

        :return: The body of this ApplyDomainTemplateRequest.
        :rtype: :class:`huaweicloudsdkcdn.v2.TemplateApplyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ApplyDomainTemplateRequest.

        :param body: The body of this ApplyDomainTemplateRequest.
        :type body: :class:`huaweicloudsdkcdn.v2.TemplateApplyRequestBody`
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
        if not isinstance(other, ApplyDomainTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
