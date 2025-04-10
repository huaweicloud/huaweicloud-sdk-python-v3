# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetailResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'specification': 'str',
        'order_id': 'str',
        'resource_id': 'str',
        'data_disk_size': 'float',
        'disk_resource_id': 'list[str]'
    }

    attribute_map = {
        'specification': 'specification',
        'order_id': 'order_id',
        'resource_id': 'resource_id',
        'data_disk_size': 'data_disk_size',
        'disk_resource_id': 'disk_resource_id'
    }

    def __init__(self, specification=None, order_id=None, resource_id=None, data_disk_size=None, disk_resource_id=None):
        r"""InstanceDetailResourceInfo

        The model defined in huaweicloud sdk

        :param specification: 云堡垒机实例规格。
        :type specification: str
        :param order_id: 订单id。
        :type order_id: str
        :param resource_id: 云堡垒机实例的资源id，UUID格式显示。
        :type resource_id: str
        :param data_disk_size: 云堡垒机实例数据盘大小，单位TB。
        :type data_disk_size: float
        :param disk_resource_id: 云堡垒机实例数据盘资源ID。
        :type disk_resource_id: list[str]
        """
        
        

        self._specification = None
        self._order_id = None
        self._resource_id = None
        self._data_disk_size = None
        self._disk_resource_id = None
        self.discriminator = None

        self.specification = specification
        self.order_id = order_id
        self.resource_id = resource_id
        self.data_disk_size = data_disk_size
        self.disk_resource_id = disk_resource_id

    @property
    def specification(self):
        r"""Gets the specification of this InstanceDetailResourceInfo.

        云堡垒机实例规格。

        :return: The specification of this InstanceDetailResourceInfo.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this InstanceDetailResourceInfo.

        云堡垒机实例规格。

        :param specification: The specification of this InstanceDetailResourceInfo.
        :type specification: str
        """
        self._specification = specification

    @property
    def order_id(self):
        r"""Gets the order_id of this InstanceDetailResourceInfo.

        订单id。

        :return: The order_id of this InstanceDetailResourceInfo.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this InstanceDetailResourceInfo.

        订单id。

        :param order_id: The order_id of this InstanceDetailResourceInfo.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this InstanceDetailResourceInfo.

        云堡垒机实例的资源id，UUID格式显示。

        :return: The resource_id of this InstanceDetailResourceInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this InstanceDetailResourceInfo.

        云堡垒机实例的资源id，UUID格式显示。

        :param resource_id: The resource_id of this InstanceDetailResourceInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def data_disk_size(self):
        r"""Gets the data_disk_size of this InstanceDetailResourceInfo.

        云堡垒机实例数据盘大小，单位TB。

        :return: The data_disk_size of this InstanceDetailResourceInfo.
        :rtype: float
        """
        return self._data_disk_size

    @data_disk_size.setter
    def data_disk_size(self, data_disk_size):
        r"""Sets the data_disk_size of this InstanceDetailResourceInfo.

        云堡垒机实例数据盘大小，单位TB。

        :param data_disk_size: The data_disk_size of this InstanceDetailResourceInfo.
        :type data_disk_size: float
        """
        self._data_disk_size = data_disk_size

    @property
    def disk_resource_id(self):
        r"""Gets the disk_resource_id of this InstanceDetailResourceInfo.

        云堡垒机实例数据盘资源ID。

        :return: The disk_resource_id of this InstanceDetailResourceInfo.
        :rtype: list[str]
        """
        return self._disk_resource_id

    @disk_resource_id.setter
    def disk_resource_id(self, disk_resource_id):
        r"""Sets the disk_resource_id of this InstanceDetailResourceInfo.

        云堡垒机实例数据盘资源ID。

        :param disk_resource_id: The disk_resource_id of this InstanceDetailResourceInfo.
        :type disk_resource_id: list[str]
        """
        self._disk_resource_id = disk_resource_id

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
        if not isinstance(other, InstanceDetailResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
