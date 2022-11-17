# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNetworkInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'status': 'list[str]',
        'type': 'list[str]',
        'cloud_connection_id': 'list[str]',
        'instance_id': 'list[str]',
        'region_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'type': 'type',
        'cloud_connection_id': 'cloud_connection_id',
        'instance_id': 'instance_id',
        'region_id': 'region_id'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, description=None, status=None, type=None, cloud_connection_id=None, instance_id=None, region_id=None):
        """ListNetworkInstancesRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询时，每页返回的个数。
        :type limit: int
        :param marker: 分页查询时，上一页最后一条记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param id: 根据ID过滤网络实例列表。
        :type id: list[str]
        :param name: 根据名称过滤网络实例列表。
        :type name: list[str]
        :param description: 根据描述过滤网络实例列表。
        :type description: list[str]
        :param status: 根据状态过滤网络实例列表。ACTIVE：表示状态可用。
        :type status: list[str]
        :param type: 根据类型过滤网络实例列表。
        :type type: list[str]
        :param cloud_connection_id: 根据云连接实例ID过滤网络实例列表。
        :type cloud_connection_id: list[str]
        :param instance_id: 根据网络实例ID过滤网络实例列表。
        :type instance_id: list[str]
        :param region_id: 根据网络实例所在的Region过滤网络实例列表。
        :type region_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._type = None
        self._cloud_connection_id = None
        self._instance_id = None
        self._region_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if instance_id is not None:
            self.instance_id = instance_id
        if region_id is not None:
            self.region_id = region_id

    @property
    def limit(self):
        """Gets the limit of this ListNetworkInstancesRequest.

        分页查询时，每页返回的个数。

        :return: The limit of this ListNetworkInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListNetworkInstancesRequest.

        分页查询时，每页返回的个数。

        :param limit: The limit of this ListNetworkInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListNetworkInstancesRequest.

        分页查询时，上一页最后一条记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListNetworkInstancesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListNetworkInstancesRequest.

        分页查询时，上一页最后一条记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListNetworkInstancesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListNetworkInstancesRequest.

        根据ID过滤网络实例列表。

        :return: The id of this ListNetworkInstancesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListNetworkInstancesRequest.

        根据ID过滤网络实例列表。

        :param id: The id of this ListNetworkInstancesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListNetworkInstancesRequest.

        根据名称过滤网络实例列表。

        :return: The name of this ListNetworkInstancesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListNetworkInstancesRequest.

        根据名称过滤网络实例列表。

        :param name: The name of this ListNetworkInstancesRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListNetworkInstancesRequest.

        根据描述过滤网络实例列表。

        :return: The description of this ListNetworkInstancesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListNetworkInstancesRequest.

        根据描述过滤网络实例列表。

        :param description: The description of this ListNetworkInstancesRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this ListNetworkInstancesRequest.

        根据状态过滤网络实例列表。ACTIVE：表示状态可用。

        :return: The status of this ListNetworkInstancesRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListNetworkInstancesRequest.

        根据状态过滤网络实例列表。ACTIVE：表示状态可用。

        :param status: The status of this ListNetworkInstancesRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ListNetworkInstancesRequest.

        根据类型过滤网络实例列表。

        :return: The type of this ListNetworkInstancesRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListNetworkInstancesRequest.

        根据类型过滤网络实例列表。

        :param type: The type of this ListNetworkInstancesRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this ListNetworkInstancesRequest.

        根据云连接实例ID过滤网络实例列表。

        :return: The cloud_connection_id of this ListNetworkInstancesRequest.
        :rtype: list[str]
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this ListNetworkInstancesRequest.

        根据云连接实例ID过滤网络实例列表。

        :param cloud_connection_id: The cloud_connection_id of this ListNetworkInstancesRequest.
        :type cloud_connection_id: list[str]
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListNetworkInstancesRequest.

        根据网络实例ID过滤网络实例列表。

        :return: The instance_id of this ListNetworkInstancesRequest.
        :rtype: list[str]
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListNetworkInstancesRequest.

        根据网络实例ID过滤网络实例列表。

        :param instance_id: The instance_id of this ListNetworkInstancesRequest.
        :type instance_id: list[str]
        """
        self._instance_id = instance_id

    @property
    def region_id(self):
        """Gets the region_id of this ListNetworkInstancesRequest.

        根据网络实例所在的Region过滤网络实例列表。

        :return: The region_id of this ListNetworkInstancesRequest.
        :rtype: list[str]
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListNetworkInstancesRequest.

        根据网络实例所在的Region过滤网络实例列表。

        :param region_id: The region_id of this ListNetworkInstancesRequest.
        :type region_id: list[str]
        """
        self._region_id = region_id

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
        if not isinstance(other, ListNetworkInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
