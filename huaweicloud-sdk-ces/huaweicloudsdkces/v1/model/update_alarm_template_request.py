# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlarmTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'body': 'UpdateAlarmTemplateRequestBody'
    }

    attribute_map = {
        'template_id': 'template_id',
        'body': 'body'
    }

    def __init__(self, template_id=None, body=None):
        r"""UpdateAlarmTemplateRequest

        The model defined in huaweicloud sdk

        :param template_id: 需要更新的自定义告警模板ID。
        :type template_id: str
        :param body: Body of the UpdateAlarmTemplateRequest
        :type body: :class:`huaweicloudsdkces.v1.UpdateAlarmTemplateRequestBody`
        """
        
        

        self._template_id = None
        self._body = None
        self.discriminator = None

        self.template_id = template_id
        if body is not None:
            self.body = body

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateAlarmTemplateRequest.

        需要更新的自定义告警模板ID。

        :return: The template_id of this UpdateAlarmTemplateRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateAlarmTemplateRequest.

        需要更新的自定义告警模板ID。

        :param template_id: The template_id of this UpdateAlarmTemplateRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def body(self):
        r"""Gets the body of this UpdateAlarmTemplateRequest.

        :return: The body of this UpdateAlarmTemplateRequest.
        :rtype: :class:`huaweicloudsdkces.v1.UpdateAlarmTemplateRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAlarmTemplateRequest.

        :param body: The body of this UpdateAlarmTemplateRequest.
        :type body: :class:`huaweicloudsdkces.v1.UpdateAlarmTemplateRequestBody`
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
        if not isinstance(other, UpdateAlarmTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
