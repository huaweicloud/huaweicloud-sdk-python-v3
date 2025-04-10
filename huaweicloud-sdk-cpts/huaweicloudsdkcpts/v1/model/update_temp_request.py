# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTempRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'int',
        'body': 'UpdateTempRequestBody'
    }

    attribute_map = {
        'template_id': 'template_id',
        'body': 'body'
    }

    def __init__(self, template_id=None, body=None):
        r"""UpdateTempRequest

        The model defined in huaweicloud sdk

        :param template_id: 事务id
        :type template_id: int
        :param body: Body of the UpdateTempRequest
        :type body: :class:`huaweicloudsdkcpts.v1.UpdateTempRequestBody`
        """
        
        

        self._template_id = None
        self._body = None
        self.discriminator = None

        self.template_id = template_id
        if body is not None:
            self.body = body

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateTempRequest.

        事务id

        :return: The template_id of this UpdateTempRequest.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateTempRequest.

        事务id

        :param template_id: The template_id of this UpdateTempRequest.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def body(self):
        r"""Gets the body of this UpdateTempRequest.

        :return: The body of this UpdateTempRequest.
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateTempRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTempRequest.

        :param body: The body of this UpdateTempRequest.
        :type body: :class:`huaweicloudsdkcpts.v1.UpdateTempRequestBody`
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
        if not isinstance(other, UpdateTempRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
