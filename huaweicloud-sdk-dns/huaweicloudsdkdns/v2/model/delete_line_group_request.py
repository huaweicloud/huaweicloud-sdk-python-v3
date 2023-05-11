# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLineGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'linegroup_id': 'str'
    }

    attribute_map = {
        'linegroup_id': 'linegroup_id'
    }

    def __init__(self, linegroup_id=None):
        """DeleteLineGroupRequest

        The model defined in huaweicloud sdk

        :param linegroup_id: 线路分组ID。
        :type linegroup_id: str
        """
        
        

        self._linegroup_id = None
        self.discriminator = None

        self.linegroup_id = linegroup_id

    @property
    def linegroup_id(self):
        """Gets the linegroup_id of this DeleteLineGroupRequest.

        线路分组ID。

        :return: The linegroup_id of this DeleteLineGroupRequest.
        :rtype: str
        """
        return self._linegroup_id

    @linegroup_id.setter
    def linegroup_id(self, linegroup_id):
        """Sets the linegroup_id of this DeleteLineGroupRequest.

        线路分组ID。

        :param linegroup_id: The linegroup_id of this DeleteLineGroupRequest.
        :type linegroup_id: str
        """
        self._linegroup_id = linegroup_id

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
        if not isinstance(other, DeleteLineGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
