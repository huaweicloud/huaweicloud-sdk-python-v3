# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTransitIpTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'key': 'key',
        'resource_id': 'resource_id'
    }

    def __init__(self, key=None, resource_id=None):
        """DeleteTransitIpTagRequest

        The model defined in huaweicloud sdk

        :param key: 标签key。
        :type key: str
        :param resource_id: 中转IP的ID。
        :type resource_id: str
        """
        
        

        self._key = None
        self._resource_id = None
        self.discriminator = None

        self.key = key
        self.resource_id = resource_id

    @property
    def key(self):
        """Gets the key of this DeleteTransitIpTagRequest.

        标签key。

        :return: The key of this DeleteTransitIpTagRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeleteTransitIpTagRequest.

        标签key。

        :param key: The key of this DeleteTransitIpTagRequest.
        :type key: str
        """
        self._key = key

    @property
    def resource_id(self):
        """Gets the resource_id of this DeleteTransitIpTagRequest.

        中转IP的ID。

        :return: The resource_id of this DeleteTransitIpTagRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this DeleteTransitIpTagRequest.

        中转IP的ID。

        :param resource_id: The resource_id of this DeleteTransitIpTagRequest.
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
        if not isinstance(other, DeleteTransitIpTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
