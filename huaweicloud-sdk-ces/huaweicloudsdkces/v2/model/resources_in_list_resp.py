# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcesInListResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_group_id': 'str',
        'resource_group_name': 'str',
        'dimensions': 'list[MetricDimension]'
    }

    attribute_map = {
        'resource_group_id': 'resource_group_id',
        'resource_group_name': 'resource_group_name',
        'dimensions': 'dimensions'
    }

    def __init__(self, resource_group_id=None, resource_group_name=None, dimensions=None):
        """ResourcesInListResp

        The model defined in huaweicloud sdk

        :param resource_group_id: 资源分组ID，监控范围为资源分组时存在该值
        :type resource_group_id: str
        :param resource_group_name: 资源分组名称，监控范围为资源分组时存在该值
        :type resource_group_name: str
        :param dimensions: 维度信息
        :type dimensions: list[:class:`huaweicloudsdkces.v2.MetricDimension`]
        """
        
        

        self._resource_group_id = None
        self._resource_group_name = None
        self._dimensions = None
        self.discriminator = None

        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        if resource_group_name is not None:
            self.resource_group_name = resource_group_name
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this ResourcesInListResp.

        资源分组ID，监控范围为资源分组时存在该值

        :return: The resource_group_id of this ResourcesInListResp.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this ResourcesInListResp.

        资源分组ID，监控范围为资源分组时存在该值

        :param resource_group_id: The resource_group_id of this ResourcesInListResp.
        :type resource_group_id: str
        """
        self._resource_group_id = resource_group_id

    @property
    def resource_group_name(self):
        """Gets the resource_group_name of this ResourcesInListResp.

        资源分组名称，监控范围为资源分组时存在该值

        :return: The resource_group_name of this ResourcesInListResp.
        :rtype: str
        """
        return self._resource_group_name

    @resource_group_name.setter
    def resource_group_name(self, resource_group_name):
        """Sets the resource_group_name of this ResourcesInListResp.

        资源分组名称，监控范围为资源分组时存在该值

        :param resource_group_name: The resource_group_name of this ResourcesInListResp.
        :type resource_group_name: str
        """
        self._resource_group_name = resource_group_name

    @property
    def dimensions(self):
        """Gets the dimensions of this ResourcesInListResp.

        维度信息

        :return: The dimensions of this ResourcesInListResp.
        :rtype: list[:class:`huaweicloudsdkces.v2.MetricDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ResourcesInListResp.

        维度信息

        :param dimensions: The dimensions of this ResourcesInListResp.
        :type dimensions: list[:class:`huaweicloudsdkces.v2.MetricDimension`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, ResourcesInListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
