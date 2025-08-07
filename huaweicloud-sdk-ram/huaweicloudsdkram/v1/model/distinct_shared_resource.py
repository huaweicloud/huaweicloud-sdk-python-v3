# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DistinctSharedResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_urn': 'str',
        'resource_type': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'resource_urn': 'resource_urn',
        'resource_type': 'resource_type',
        'updated_at': 'updated_at'
    }

    def __init__(self, resource_urn=None, resource_type=None, updated_at=None):
        r"""DistinctSharedResource

        The model defined in huaweicloud sdk

        :param resource_urn: 资源的统一资源名称。
        :type resource_urn: str
        :param resource_type: 资源的类型。
        :type resource_type: str
        :param updated_at: 最后一次更新资源共享实例的时间。
        :type updated_at: datetime
        """
        
        

        self._resource_urn = None
        self._resource_type = None
        self._updated_at = None
        self.discriminator = None

        if resource_urn is not None:
            self.resource_urn = resource_urn
        if resource_type is not None:
            self.resource_type = resource_type
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def resource_urn(self):
        r"""Gets the resource_urn of this DistinctSharedResource.

        资源的统一资源名称。

        :return: The resource_urn of this DistinctSharedResource.
        :rtype: str
        """
        return self._resource_urn

    @resource_urn.setter
    def resource_urn(self, resource_urn):
        r"""Sets the resource_urn of this DistinctSharedResource.

        资源的统一资源名称。

        :param resource_urn: The resource_urn of this DistinctSharedResource.
        :type resource_urn: str
        """
        self._resource_urn = resource_urn

    @property
    def resource_type(self):
        r"""Gets the resource_type of this DistinctSharedResource.

        资源的类型。

        :return: The resource_type of this DistinctSharedResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this DistinctSharedResource.

        资源的类型。

        :param resource_type: The resource_type of this DistinctSharedResource.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def updated_at(self):
        r"""Gets the updated_at of this DistinctSharedResource.

        最后一次更新资源共享实例的时间。

        :return: The updated_at of this DistinctSharedResource.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this DistinctSharedResource.

        最后一次更新资源共享实例的时间。

        :param updated_at: The updated_at of this DistinctSharedResource.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, DistinctSharedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
