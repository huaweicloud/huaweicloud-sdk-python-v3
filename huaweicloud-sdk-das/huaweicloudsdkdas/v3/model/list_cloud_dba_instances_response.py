# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudDbaInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_list': 'list[DASInstanceInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'instance_list': 'instance_list',
        'total_count': 'total_count'
    }

    def __init__(self, instance_list=None, total_count=None):
        r"""ListCloudDbaInstancesResponse

        The model defined in huaweicloud sdk

        :param instance_list: 实例列表。
        :type instance_list: list[:class:`huaweicloudsdkdas.v3.DASInstanceInfo`]
        :param total_count: 总数。
        :type total_count: int
        """
        
        super(ListCloudDbaInstancesResponse, self).__init__()

        self._instance_list = None
        self._total_count = None
        self.discriminator = None

        if instance_list is not None:
            self.instance_list = instance_list
        if total_count is not None:
            self.total_count = total_count

    @property
    def instance_list(self):
        r"""Gets the instance_list of this ListCloudDbaInstancesResponse.

        实例列表。

        :return: The instance_list of this ListCloudDbaInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DASInstanceInfo`]
        """
        return self._instance_list

    @instance_list.setter
    def instance_list(self, instance_list):
        r"""Sets the instance_list of this ListCloudDbaInstancesResponse.

        实例列表。

        :param instance_list: The instance_list of this ListCloudDbaInstancesResponse.
        :type instance_list: list[:class:`huaweicloudsdkdas.v3.DASInstanceInfo`]
        """
        self._instance_list = instance_list

    @property
    def total_count(self):
        r"""Gets the total_count of this ListCloudDbaInstancesResponse.

        总数。

        :return: The total_count of this ListCloudDbaInstancesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListCloudDbaInstancesResponse.

        总数。

        :param total_count: The total_count of this ListCloudDbaInstancesResponse.
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
        if not isinstance(other, ListCloudDbaInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
