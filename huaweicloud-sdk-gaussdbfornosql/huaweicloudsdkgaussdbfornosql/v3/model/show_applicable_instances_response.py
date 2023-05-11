# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApplicableInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instances': 'list[ApplicableInstanceRsp]',
        'count': 'int'
    }

    attribute_map = {
        'instances': 'instances',
        'count': 'count'
    }

    def __init__(self, instances=None, count=None):
        """ShowApplicableInstancesResponse

        The model defined in huaweicloud sdk

        :param instances: 实例列表
        :type instances: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ApplicableInstanceRsp`]
        :param count: 应用参数的实例数量限制。
        :type count: int
        """
        
        super(ShowApplicableInstancesResponse, self).__init__()

        self._instances = None
        self._count = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if count is not None:
            self.count = count

    @property
    def instances(self):
        """Gets the instances of this ShowApplicableInstancesResponse.

        实例列表

        :return: The instances of this ShowApplicableInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ApplicableInstanceRsp`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ShowApplicableInstancesResponse.

        实例列表

        :param instances: The instances of this ShowApplicableInstancesResponse.
        :type instances: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ApplicableInstanceRsp`]
        """
        self._instances = instances

    @property
    def count(self):
        """Gets the count of this ShowApplicableInstancesResponse.

        应用参数的实例数量限制。

        :return: The count of this ShowApplicableInstancesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowApplicableInstancesResponse.

        应用参数的实例数量限制。

        :param count: The count of this ShowApplicableInstancesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ShowApplicableInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
