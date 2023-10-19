# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigurationsInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instances': 'list[ApplicableInstances]',
        'total_count': 'int'
    }

    attribute_map = {
        'instances': 'instances',
        'total_count': 'total_count'
    }

    def __init__(self, instances=None, total_count=None):
        """ListConfigurationsInstancesResponse

        The model defined in huaweicloud sdk

        :param instances: 可以应用的实例列表。
        :type instances: list[:class:`huaweicloudsdkgaussdb.v3.ApplicableInstances`]
        :param total_count: 可应用的实例列表数量。
        :type total_count: int
        """
        
        super(ListConfigurationsInstancesResponse, self).__init__()

        self._instances = None
        self._total_count = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if total_count is not None:
            self.total_count = total_count

    @property
    def instances(self):
        """Gets the instances of this ListConfigurationsInstancesResponse.

        可以应用的实例列表。

        :return: The instances of this ListConfigurationsInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ApplicableInstances`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListConfigurationsInstancesResponse.

        可以应用的实例列表。

        :param instances: The instances of this ListConfigurationsInstancesResponse.
        :type instances: list[:class:`huaweicloudsdkgaussdb.v3.ApplicableInstances`]
        """
        self._instances = instances

    @property
    def total_count(self):
        """Gets the total_count of this ListConfigurationsInstancesResponse.

        可应用的实例列表数量。

        :return: The total_count of this ListConfigurationsInstancesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListConfigurationsInstancesResponse.

        可应用的实例列表数量。

        :param total_count: The total_count of this ListConfigurationsInstancesResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListConfigurationsInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
