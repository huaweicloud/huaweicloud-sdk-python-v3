# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicBorderGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'str'
    }

    attribute_map = {
        'fields': 'fields'
    }

    def __init__(self, fields=None):
        """ListPublicBorderGroupsRequest

        The model defined in huaweicloud sdk

        :param fields: 显示，形式为\&quot;fields&#x3D;id&amp;fields&#x3D;name&amp;...\&quot;  支持字段：publicip_pools/public_border_group
        :type fields: str
        """
        
        

        self._fields = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields

    @property
    def fields(self):
        """Gets the fields of this ListPublicBorderGroupsRequest.

        显示，形式为\"fields=id&fields=name&...\"  支持字段：publicip_pools/public_border_group

        :return: The fields of this ListPublicBorderGroupsRequest.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListPublicBorderGroupsRequest.

        显示，形式为\"fields=id&fields=name&...\"  支持字段：publicip_pools/public_border_group

        :param fields: The fields of this ListPublicBorderGroupsRequest.
        :type fields: str
        """
        self._fields = fields

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
        if not isinstance(other, ListPublicBorderGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
