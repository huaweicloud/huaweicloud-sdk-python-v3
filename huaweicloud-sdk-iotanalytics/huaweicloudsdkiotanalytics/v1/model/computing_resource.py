# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputingResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'computing_resource_id': 'str',
        'computing_resource_name': 'str',
        'description': 'str',
        'owner': 'str',
        'created_time': 'str',
        'computing_resource_type': 'str',
        'cu_count': 'int',
        'charging_mode': 'int',
        'resource_mode': 'int'
    }

    attribute_map = {
        'computing_resource_id': 'computing_resource_id',
        'computing_resource_name': 'computing_resource_name',
        'description': 'description',
        'owner': 'owner',
        'created_time': 'created_time',
        'computing_resource_type': 'computing_resource_type',
        'cu_count': 'cu_count',
        'charging_mode': 'charging_mode',
        'resource_mode': 'resource_mode'
    }

    def __init__(self, computing_resource_id=None, computing_resource_name=None, description=None, owner=None, created_time=None, computing_resource_type=None, cu_count=None, charging_mode=None, resource_mode=None):
        """ComputingResource

        The model defined in huaweicloud sdk

        :param computing_resource_id: 计算资源ID。
        :type computing_resource_id: str
        :param computing_resource_name: 计算资源名称。
        :type computing_resource_name: str
        :param description: 计算资源描述信息。
        :type description: str
        :param owner: 创建计算资源的用户。
        :type owner: str
        :param created_time: 创建计算资源的时间。时间格式为ISO日期时间格式yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;
        :type created_time: str
        :param computing_resource_type: 计算资源的类型,。目前支持：sql
        :type computing_resource_type: str
        :param cu_count: 与该计算资源绑定的计算单元数。设置值当前只支持16，64，256。
        :type cu_count: int
        :param charging_mode: 计算资源的收费模式。“1”表示按照CU时收费。“2”表示按照包年包月收费。
        :type charging_mode: int
        :param resource_mode: 计算资源类型。0：共享资源 1：专属资源
        :type resource_mode: int
        """
        
        

        self._computing_resource_id = None
        self._computing_resource_name = None
        self._description = None
        self._owner = None
        self._created_time = None
        self._computing_resource_type = None
        self._cu_count = None
        self._charging_mode = None
        self._resource_mode = None
        self.discriminator = None

        if computing_resource_id is not None:
            self.computing_resource_id = computing_resource_id
        if computing_resource_name is not None:
            self.computing_resource_name = computing_resource_name
        if description is not None:
            self.description = description
        if owner is not None:
            self.owner = owner
        if created_time is not None:
            self.created_time = created_time
        if computing_resource_type is not None:
            self.computing_resource_type = computing_resource_type
        if cu_count is not None:
            self.cu_count = cu_count
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_mode is not None:
            self.resource_mode = resource_mode

    @property
    def computing_resource_id(self):
        """Gets the computing_resource_id of this ComputingResource.

        计算资源ID。

        :return: The computing_resource_id of this ComputingResource.
        :rtype: str
        """
        return self._computing_resource_id

    @computing_resource_id.setter
    def computing_resource_id(self, computing_resource_id):
        """Sets the computing_resource_id of this ComputingResource.

        计算资源ID。

        :param computing_resource_id: The computing_resource_id of this ComputingResource.
        :type computing_resource_id: str
        """
        self._computing_resource_id = computing_resource_id

    @property
    def computing_resource_name(self):
        """Gets the computing_resource_name of this ComputingResource.

        计算资源名称。

        :return: The computing_resource_name of this ComputingResource.
        :rtype: str
        """
        return self._computing_resource_name

    @computing_resource_name.setter
    def computing_resource_name(self, computing_resource_name):
        """Sets the computing_resource_name of this ComputingResource.

        计算资源名称。

        :param computing_resource_name: The computing_resource_name of this ComputingResource.
        :type computing_resource_name: str
        """
        self._computing_resource_name = computing_resource_name

    @property
    def description(self):
        """Gets the description of this ComputingResource.

        计算资源描述信息。

        :return: The description of this ComputingResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComputingResource.

        计算资源描述信息。

        :param description: The description of this ComputingResource.
        :type description: str
        """
        self._description = description

    @property
    def owner(self):
        """Gets the owner of this ComputingResource.

        创建计算资源的用户。

        :return: The owner of this ComputingResource.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ComputingResource.

        创建计算资源的用户。

        :param owner: The owner of this ComputingResource.
        :type owner: str
        """
        self._owner = owner

    @property
    def created_time(self):
        """Gets the created_time of this ComputingResource.

        创建计算资源的时间。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The created_time of this ComputingResource.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ComputingResource.

        创建计算资源的时间。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :param created_time: The created_time of this ComputingResource.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def computing_resource_type(self):
        """Gets the computing_resource_type of this ComputingResource.

        计算资源的类型,。目前支持：sql

        :return: The computing_resource_type of this ComputingResource.
        :rtype: str
        """
        return self._computing_resource_type

    @computing_resource_type.setter
    def computing_resource_type(self, computing_resource_type):
        """Sets the computing_resource_type of this ComputingResource.

        计算资源的类型,。目前支持：sql

        :param computing_resource_type: The computing_resource_type of this ComputingResource.
        :type computing_resource_type: str
        """
        self._computing_resource_type = computing_resource_type

    @property
    def cu_count(self):
        """Gets the cu_count of this ComputingResource.

        与该计算资源绑定的计算单元数。设置值当前只支持16，64，256。

        :return: The cu_count of this ComputingResource.
        :rtype: int
        """
        return self._cu_count

    @cu_count.setter
    def cu_count(self, cu_count):
        """Sets the cu_count of this ComputingResource.

        与该计算资源绑定的计算单元数。设置值当前只支持16，64，256。

        :param cu_count: The cu_count of this ComputingResource.
        :type cu_count: int
        """
        self._cu_count = cu_count

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ComputingResource.

        计算资源的收费模式。“1”表示按照CU时收费。“2”表示按照包年包月收费。

        :return: The charging_mode of this ComputingResource.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ComputingResource.

        计算资源的收费模式。“1”表示按照CU时收费。“2”表示按照包年包月收费。

        :param charging_mode: The charging_mode of this ComputingResource.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def resource_mode(self):
        """Gets the resource_mode of this ComputingResource.

        计算资源类型。0：共享资源 1：专属资源

        :return: The resource_mode of this ComputingResource.
        :rtype: int
        """
        return self._resource_mode

    @resource_mode.setter
    def resource_mode(self, resource_mode):
        """Sets the resource_mode of this ComputingResource.

        计算资源类型。0：共享资源 1：专属资源

        :param resource_mode: The resource_mode of this ComputingResource.
        :type resource_mode: int
        """
        self._resource_mode = resource_mode

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
        if not isinstance(other, ComputingResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
