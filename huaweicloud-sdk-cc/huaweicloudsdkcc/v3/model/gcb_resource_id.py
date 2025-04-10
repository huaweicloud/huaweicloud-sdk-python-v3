# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GcbResourceId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id'
    }

    def __init__(self, resource_id=None):
        r"""GcbResourceId

        The model defined in huaweicloud sdk

        :param resource_id: 功能说明：实例ID。 取值范围：1-36个字符，支持数字、字母、_(下划线)、-（中划线）
        :type resource_id: str
        """
        
        

        self._resource_id = None
        self.discriminator = None

        self.resource_id = resource_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this GcbResourceId.

        功能说明：实例ID。 取值范围：1-36个字符，支持数字、字母、_(下划线)、-（中划线）

        :return: The resource_id of this GcbResourceId.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this GcbResourceId.

        功能说明：实例ID。 取值范围：1-36个字符，支持数字、字母、_(下划线)、-（中划线）

        :param resource_id: The resource_id of this GcbResourceId.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, GcbResourceId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
