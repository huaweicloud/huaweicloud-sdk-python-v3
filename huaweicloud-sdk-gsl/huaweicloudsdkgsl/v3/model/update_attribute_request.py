# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAttributeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attribute_id': 'int',
        'body': 'AddOrModifyAttributeReq'
    }

    attribute_map = {
        'attribute_id': 'attribute_id',
        'body': 'body'
    }

    def __init__(self, attribute_id=None, body=None):
        r"""UpdateAttributeRequest

        The model defined in huaweicloud sdk

        :param attribute_id: 自定义属性标识
        :type attribute_id: int
        :param body: Body of the UpdateAttributeRequest
        :type body: :class:`huaweicloudsdkgsl.v3.AddOrModifyAttributeReq`
        """
        
        

        self._attribute_id = None
        self._body = None
        self.discriminator = None

        self.attribute_id = attribute_id
        if body is not None:
            self.body = body

    @property
    def attribute_id(self):
        r"""Gets the attribute_id of this UpdateAttributeRequest.

        自定义属性标识

        :return: The attribute_id of this UpdateAttributeRequest.
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        r"""Sets the attribute_id of this UpdateAttributeRequest.

        自定义属性标识

        :param attribute_id: The attribute_id of this UpdateAttributeRequest.
        :type attribute_id: int
        """
        self._attribute_id = attribute_id

    @property
    def body(self):
        r"""Gets the body of this UpdateAttributeRequest.

        :return: The body of this UpdateAttributeRequest.
        :rtype: :class:`huaweicloudsdkgsl.v3.AddOrModifyAttributeReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAttributeRequest.

        :param body: The body of this UpdateAttributeRequest.
        :type body: :class:`huaweicloudsdkgsl.v3.AddOrModifyAttributeReq`
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
        if not isinstance(other, UpdateAttributeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
