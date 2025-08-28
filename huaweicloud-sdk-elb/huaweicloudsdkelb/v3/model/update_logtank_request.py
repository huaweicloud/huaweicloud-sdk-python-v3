# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLogtankRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logtank_id': 'str',
        'body': 'UpdateLogtankRequestBody'
    }

    attribute_map = {
        'logtank_id': 'logtank_id',
        'body': 'body'
    }

    def __init__(self, logtank_id=None, body=None):
        r"""UpdateLogtankRequest

        The model defined in huaweicloud sdk

        :param logtank_id: **参数解释**：云日志ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type logtank_id: str
        :param body: Body of the UpdateLogtankRequest
        :type body: :class:`huaweicloudsdkelb.v3.UpdateLogtankRequestBody`
        """
        
        

        self._logtank_id = None
        self._body = None
        self.discriminator = None

        self.logtank_id = logtank_id
        if body is not None:
            self.body = body

    @property
    def logtank_id(self):
        r"""Gets the logtank_id of this UpdateLogtankRequest.

        **参数解释**：云日志ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The logtank_id of this UpdateLogtankRequest.
        :rtype: str
        """
        return self._logtank_id

    @logtank_id.setter
    def logtank_id(self, logtank_id):
        r"""Sets the logtank_id of this UpdateLogtankRequest.

        **参数解释**：云日志ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param logtank_id: The logtank_id of this UpdateLogtankRequest.
        :type logtank_id: str
        """
        self._logtank_id = logtank_id

    @property
    def body(self):
        r"""Gets the body of this UpdateLogtankRequest.

        :return: The body of this UpdateLogtankRequest.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateLogtankRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateLogtankRequest.

        :param body: The body of this UpdateLogtankRequest.
        :type body: :class:`huaweicloudsdkelb.v3.UpdateLogtankRequestBody`
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
        if not isinstance(other, UpdateLogtankRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
