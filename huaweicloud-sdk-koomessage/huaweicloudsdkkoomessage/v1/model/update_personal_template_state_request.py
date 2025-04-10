# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePersonalTemplateStateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tpl_id': 'str',
        'body': 'UpdatePersonalTemplateStateDataRequest'
    }

    attribute_map = {
        'tpl_id': 'tpl_id',
        'body': 'body'
    }

    def __init__(self, tpl_id=None, body=None):
        r"""UpdatePersonalTemplateStateRequest

        The model defined in huaweicloud sdk

        :param tpl_id: 智能信息模板ID。
        :type tpl_id: str
        :param body: Body of the UpdatePersonalTemplateStateRequest
        :type body: :class:`huaweicloudsdkkoomessage.v1.UpdatePersonalTemplateStateDataRequest`
        """
        
        

        self._tpl_id = None
        self._body = None
        self.discriminator = None

        self.tpl_id = tpl_id
        if body is not None:
            self.body = body

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this UpdatePersonalTemplateStateRequest.

        智能信息模板ID。

        :return: The tpl_id of this UpdatePersonalTemplateStateRequest.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this UpdatePersonalTemplateStateRequest.

        智能信息模板ID。

        :param tpl_id: The tpl_id of this UpdatePersonalTemplateStateRequest.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def body(self):
        r"""Gets the body of this UpdatePersonalTemplateStateRequest.

        :return: The body of this UpdatePersonalTemplateStateRequest.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.UpdatePersonalTemplateStateDataRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePersonalTemplateStateRequest.

        :param body: The body of this UpdatePersonalTemplateStateRequest.
        :type body: :class:`huaweicloudsdkkoomessage.v1.UpdatePersonalTemplateStateDataRequest`
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
        if not isinstance(other, UpdatePersonalTemplateStateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
