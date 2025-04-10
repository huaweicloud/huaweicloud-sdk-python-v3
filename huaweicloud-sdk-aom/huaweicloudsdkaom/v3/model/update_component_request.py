# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateComponentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'body': 'ComponentUpdateParam'
    }

    attribute_map = {
        'component_id': 'component_id',
        'body': 'body'
    }

    def __init__(self, component_id=None, body=None):
        r"""UpdateComponentRequest

        The model defined in huaweicloud sdk

        :param component_id: 组件id
        :type component_id: str
        :param body: Body of the UpdateComponentRequest
        :type body: :class:`huaweicloudsdkaom.v3.ComponentUpdateParam`
        """
        
        

        self._component_id = None
        self._body = None
        self.discriminator = None

        self.component_id = component_id
        if body is not None:
            self.body = body

    @property
    def component_id(self):
        r"""Gets the component_id of this UpdateComponentRequest.

        组件id

        :return: The component_id of this UpdateComponentRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this UpdateComponentRequest.

        组件id

        :param component_id: The component_id of this UpdateComponentRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def body(self):
        r"""Gets the body of this UpdateComponentRequest.

        :return: The body of this UpdateComponentRequest.
        :rtype: :class:`huaweicloudsdkaom.v3.ComponentUpdateParam`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateComponentRequest.

        :param body: The body of this UpdateComponentRequest.
        :type body: :class:`huaweicloudsdkaom.v3.ComponentUpdateParam`
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
        if not isinstance(other, UpdateComponentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
