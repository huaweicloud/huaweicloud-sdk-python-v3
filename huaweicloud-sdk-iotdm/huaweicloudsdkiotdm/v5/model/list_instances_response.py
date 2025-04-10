# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'marker': 'str',
        'instances': 'list[QueryInstanceSimplify]'
    }

    attribute_map = {
        'count': 'count',
        'marker': 'marker',
        'instances': 'instances'
    }

    def __init__(self, count=None, marker=None, instances=None):
        r"""ListInstancesResponse

        The model defined in huaweicloud sdk

        :param count: 设备接入实例的总数
        :type count: int
        :param marker: 本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用
        :type marker: str
        :param instances: 设备接入实例的详情列表
        :type instances: list[:class:`huaweicloudsdkiotdm.v5.QueryInstanceSimplify`]
        """
        
        super(ListInstancesResponse, self).__init__()

        self._count = None
        self._marker = None
        self._instances = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if marker is not None:
            self.marker = marker
        if instances is not None:
            self.instances = instances

    @property
    def count(self):
        r"""Gets the count of this ListInstancesResponse.

        设备接入实例的总数

        :return: The count of this ListInstancesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListInstancesResponse.

        设备接入实例的总数

        :param count: The count of this ListInstancesResponse.
        :type count: int
        """
        self._count = count

    @property
    def marker(self):
        r"""Gets the marker of this ListInstancesResponse.

        本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用

        :return: The marker of this ListInstancesResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListInstancesResponse.

        本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用

        :param marker: The marker of this ListInstancesResponse.
        :type marker: str
        """
        self._marker = marker

    @property
    def instances(self):
        r"""Gets the instances of this ListInstancesResponse.

        设备接入实例的详情列表

        :return: The instances of this ListInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkiotdm.v5.QueryInstanceSimplify`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListInstancesResponse.

        设备接入实例的详情列表

        :param instances: The instances of this ListInstancesResponse.
        :type instances: list[:class:`huaweicloudsdkiotdm.v5.QueryInstanceSimplify`]
        """
        self._instances = instances

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
        if not isinstance(other, ListInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
