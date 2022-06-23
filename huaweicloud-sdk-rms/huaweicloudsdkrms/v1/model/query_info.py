# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'select_fields': 'list[str]'
    }

    attribute_map = {
        'select_fields': 'select_fields'
    }

    def __init__(self, select_fields=None):
        """QueryInfo

        The model defined in huaweicloud sdk

        :param select_fields: ResourceQL 查询字段
        :type select_fields: list[str]
        """
        
        

        self._select_fields = None
        self.discriminator = None

        if select_fields is not None:
            self.select_fields = select_fields

    @property
    def select_fields(self):
        """Gets the select_fields of this QueryInfo.

        ResourceQL 查询字段

        :return: The select_fields of this QueryInfo.
        :rtype: list[str]
        """
        return self._select_fields

    @select_fields.setter
    def select_fields(self, select_fields):
        """Sets the select_fields of this QueryInfo.

        ResourceQL 查询字段

        :param select_fields: The select_fields of this QueryInfo.
        :type select_fields: list[str]
        """
        self._select_fields = select_fields

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
        if not isinstance(other, QueryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
