# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Selector:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_selector': 'FieldSelector'
    }

    attribute_map = {
        'field_selector': 'fieldSelector'
    }

    def __init__(self, field_selector=None):
        r"""Selector

        The model defined in huaweicloud sdk

        :param field_selector: 
        :type field_selector: :class:`huaweicloudsdkasm.v1.FieldSelector`
        """
        
        

        self._field_selector = None
        self.discriminator = None

        if field_selector is not None:
            self.field_selector = field_selector

    @property
    def field_selector(self):
        r"""Gets the field_selector of this Selector.

        :return: The field_selector of this Selector.
        :rtype: :class:`huaweicloudsdkasm.v1.FieldSelector`
        """
        return self._field_selector

    @field_selector.setter
    def field_selector(self, field_selector):
        r"""Sets the field_selector of this Selector.

        :param field_selector: The field_selector of this Selector.
        :type field_selector: :class:`huaweicloudsdkasm.v1.FieldSelector`
        """
        self._field_selector = field_selector

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
        if not isinstance(other, Selector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
