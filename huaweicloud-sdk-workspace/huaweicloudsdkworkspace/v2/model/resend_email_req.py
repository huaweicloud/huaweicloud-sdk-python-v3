# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResendEmailReq:

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
        'phone_template_id': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'phone_template_id': 'phone_template_id'
    }

    def __init__(self, template_id=None, phone_template_id=None):
        r"""ResendEmailReq

        The model defined in huaweicloud sdk

        :param template_id: 邮件模板ID。
        :type template_id: str
        :param phone_template_id: 短信模板ID。
        :type phone_template_id: str
        """
        
        

        self._template_id = None
        self._phone_template_id = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if phone_template_id is not None:
            self.phone_template_id = phone_template_id

    @property
    def template_id(self):
        r"""Gets the template_id of this ResendEmailReq.

        邮件模板ID。

        :return: The template_id of this ResendEmailReq.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ResendEmailReq.

        邮件模板ID。

        :param template_id: The template_id of this ResendEmailReq.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def phone_template_id(self):
        r"""Gets the phone_template_id of this ResendEmailReq.

        短信模板ID。

        :return: The phone_template_id of this ResendEmailReq.
        :rtype: str
        """
        return self._phone_template_id

    @phone_template_id.setter
    def phone_template_id(self, phone_template_id):
        r"""Sets the phone_template_id of this ResendEmailReq.

        短信模板ID。

        :param phone_template_id: The phone_template_id of this ResendEmailReq.
        :type phone_template_id: str
        """
        self._phone_template_id = phone_template_id

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
        if not isinstance(other, ResendEmailReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
