# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateComputingResourceResponse(SdkResponse):

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
        'computing_resource_type': 'str',
        'description': 'str',
        'cu_count': 'int',
        'charging_mode': 'int',
        'created_time': 'str'
    }

    attribute_map = {
        'computing_resource_id': 'computing_resource_id',
        'computing_resource_name': 'computing_resource_name',
        'computing_resource_type': 'computing_resource_type',
        'description': 'description',
        'cu_count': 'cu_count',
        'charging_mode': 'charging_mode',
        'created_time': 'created_time'
    }

    def __init__(self, computing_resource_id=None, computing_resource_name=None, computing_resource_type=None, description=None, cu_count=None, charging_mode=None, created_time=None):
        """CreateComputingResourceResponse

        The model defined in huaweicloud sdk

        :param computing_resource_id: 新增计算资源ID。
        :type computing_resource_id: str
        :param computing_resource_name: 新增计算资源名称。
        :type computing_resource_name: str
        :param computing_resource_type: 计算资源的类型。目前支持：sql。如果不指定，默认为sql。
        :type computing_resource_type: str
        :param description: 计算资源的描述信息。
        :type description: str
        :param cu_count: 与计算资源绑定的最小计算单元个数。设置值当前只支持16，64，256。
        :type cu_count: int
        :param charging_mode: 计算资源的收费模式。只能设置为“1”，表示按照CU时收费。
        :type charging_mode: int
        :param created_time: 创建计算资源时间。时间格式为ISO日期时间格式yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;。
        :type created_time: str
        """
        
        super(CreateComputingResourceResponse, self).__init__()

        self._computing_resource_id = None
        self._computing_resource_name = None
        self._computing_resource_type = None
        self._description = None
        self._cu_count = None
        self._charging_mode = None
        self._created_time = None
        self.discriminator = None

        if computing_resource_id is not None:
            self.computing_resource_id = computing_resource_id
        if computing_resource_name is not None:
            self.computing_resource_name = computing_resource_name
        if computing_resource_type is not None:
            self.computing_resource_type = computing_resource_type
        if description is not None:
            self.description = description
        if cu_count is not None:
            self.cu_count = cu_count
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if created_time is not None:
            self.created_time = created_time

    @property
    def computing_resource_id(self):
        """Gets the computing_resource_id of this CreateComputingResourceResponse.

        新增计算资源ID。

        :return: The computing_resource_id of this CreateComputingResourceResponse.
        :rtype: str
        """
        return self._computing_resource_id

    @computing_resource_id.setter
    def computing_resource_id(self, computing_resource_id):
        """Sets the computing_resource_id of this CreateComputingResourceResponse.

        新增计算资源ID。

        :param computing_resource_id: The computing_resource_id of this CreateComputingResourceResponse.
        :type computing_resource_id: str
        """
        self._computing_resource_id = computing_resource_id

    @property
    def computing_resource_name(self):
        """Gets the computing_resource_name of this CreateComputingResourceResponse.

        新增计算资源名称。

        :return: The computing_resource_name of this CreateComputingResourceResponse.
        :rtype: str
        """
        return self._computing_resource_name

    @computing_resource_name.setter
    def computing_resource_name(self, computing_resource_name):
        """Sets the computing_resource_name of this CreateComputingResourceResponse.

        新增计算资源名称。

        :param computing_resource_name: The computing_resource_name of this CreateComputingResourceResponse.
        :type computing_resource_name: str
        """
        self._computing_resource_name = computing_resource_name

    @property
    def computing_resource_type(self):
        """Gets the computing_resource_type of this CreateComputingResourceResponse.

        计算资源的类型。目前支持：sql。如果不指定，默认为sql。

        :return: The computing_resource_type of this CreateComputingResourceResponse.
        :rtype: str
        """
        return self._computing_resource_type

    @computing_resource_type.setter
    def computing_resource_type(self, computing_resource_type):
        """Sets the computing_resource_type of this CreateComputingResourceResponse.

        计算资源的类型。目前支持：sql。如果不指定，默认为sql。

        :param computing_resource_type: The computing_resource_type of this CreateComputingResourceResponse.
        :type computing_resource_type: str
        """
        self._computing_resource_type = computing_resource_type

    @property
    def description(self):
        """Gets the description of this CreateComputingResourceResponse.

        计算资源的描述信息。

        :return: The description of this CreateComputingResourceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateComputingResourceResponse.

        计算资源的描述信息。

        :param description: The description of this CreateComputingResourceResponse.
        :type description: str
        """
        self._description = description

    @property
    def cu_count(self):
        """Gets the cu_count of this CreateComputingResourceResponse.

        与计算资源绑定的最小计算单元个数。设置值当前只支持16，64，256。

        :return: The cu_count of this CreateComputingResourceResponse.
        :rtype: int
        """
        return self._cu_count

    @cu_count.setter
    def cu_count(self, cu_count):
        """Sets the cu_count of this CreateComputingResourceResponse.

        与计算资源绑定的最小计算单元个数。设置值当前只支持16，64，256。

        :param cu_count: The cu_count of this CreateComputingResourceResponse.
        :type cu_count: int
        """
        self._cu_count = cu_count

    @property
    def charging_mode(self):
        """Gets the charging_mode of this CreateComputingResourceResponse.

        计算资源的收费模式。只能设置为“1”，表示按照CU时收费。

        :return: The charging_mode of this CreateComputingResourceResponse.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this CreateComputingResourceResponse.

        计算资源的收费模式。只能设置为“1”，表示按照CU时收费。

        :param charging_mode: The charging_mode of this CreateComputingResourceResponse.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def created_time(self):
        """Gets the created_time of this CreateComputingResourceResponse.

        创建计算资源时间。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss'Z'。

        :return: The created_time of this CreateComputingResourceResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this CreateComputingResourceResponse.

        创建计算资源时间。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss'Z'。

        :param created_time: The created_time of this CreateComputingResourceResponse.
        :type created_time: str
        """
        self._created_time = created_time

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
        if not isinstance(other, CreateComputingResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
