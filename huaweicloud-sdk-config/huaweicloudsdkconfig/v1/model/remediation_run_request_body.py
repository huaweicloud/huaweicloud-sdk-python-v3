# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemediationRunRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_supported': 'bool',
        'resource_ids': 'list[str]'
    }

    attribute_map = {
        'all_supported': 'all_supported',
        'resource_ids': 'resource_ids'
    }

    def __init__(self, all_supported=None, resource_ids=None):
        """RemediationRunRequestBody

        The model defined in huaweicloud sdk

        :param all_supported: 是否选择对所有不合规资源执行补救。
        :type all_supported: bool
        :param resource_ids: 
        :type resource_ids: list[str]
        """
        
        

        self._all_supported = None
        self._resource_ids = None
        self.discriminator = None

        self.all_supported = all_supported
        if resource_ids is not None:
            self.resource_ids = resource_ids

    @property
    def all_supported(self):
        """Gets the all_supported of this RemediationRunRequestBody.

        是否选择对所有不合规资源执行补救。

        :return: The all_supported of this RemediationRunRequestBody.
        :rtype: bool
        """
        return self._all_supported

    @all_supported.setter
    def all_supported(self, all_supported):
        """Sets the all_supported of this RemediationRunRequestBody.

        是否选择对所有不合规资源执行补救。

        :param all_supported: The all_supported of this RemediationRunRequestBody.
        :type all_supported: bool
        """
        self._all_supported = all_supported

    @property
    def resource_ids(self):
        """Gets the resource_ids of this RemediationRunRequestBody.

        :return: The resource_ids of this RemediationRunRequestBody.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this RemediationRunRequestBody.

        :param resource_ids: The resource_ids of this RemediationRunRequestBody.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

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
        if not isinstance(other, RemediationRunRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
