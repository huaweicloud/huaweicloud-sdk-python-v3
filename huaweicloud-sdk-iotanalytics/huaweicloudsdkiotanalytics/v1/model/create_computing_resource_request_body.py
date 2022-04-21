# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateComputingResourceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'computing_resource_name': 'str',
        'computing_resource_type': 'str',
        'description': 'str',
        'cu_count': 'int',
        'charging_mode': 'int'
    }

    attribute_map = {
        'computing_resource_name': 'computing_resource_name',
        'computing_resource_type': 'computing_resource_type',
        'description': 'description',
        'cu_count': 'cu_count',
        'charging_mode': 'charging_mode'
    }

    def __init__(self, computing_resource_name=None, computing_resource_type=None, description=None, cu_count=None, charging_mode=None):
        """CreateComputingResourceRequestBody

        The model defined in huaweicloud sdk

        :param computing_resource_name: 新建的计算资源名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。
        :type computing_resource_name: str
        :param computing_resource_type: 计算资源的类型。默认为sql。
        :type computing_resource_type: str
        :param description: 计算资源的描述信息。
        :type description: str
        :param cu_count: 与计算资源绑定的最小计算单元个数。设置值当前只支持16，64，256。
        :type cu_count: int
        :param charging_mode: 计算资源的收费模式。只能设置为“1”，表示按照CU时收费。
        :type charging_mode: int
        """
        
        

        self._computing_resource_name = None
        self._computing_resource_type = None
        self._description = None
        self._cu_count = None
        self._charging_mode = None
        self.discriminator = None

        self.computing_resource_name = computing_resource_name
        if computing_resource_type is not None:
            self.computing_resource_type = computing_resource_type
        if description is not None:
            self.description = description
        self.cu_count = cu_count
        if charging_mode is not None:
            self.charging_mode = charging_mode

    @property
    def computing_resource_name(self):
        """Gets the computing_resource_name of this CreateComputingResourceRequestBody.

        新建的计算资源名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。

        :return: The computing_resource_name of this CreateComputingResourceRequestBody.
        :rtype: str
        """
        return self._computing_resource_name

    @computing_resource_name.setter
    def computing_resource_name(self, computing_resource_name):
        """Sets the computing_resource_name of this CreateComputingResourceRequestBody.

        新建的计算资源名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。

        :param computing_resource_name: The computing_resource_name of this CreateComputingResourceRequestBody.
        :type computing_resource_name: str
        """
        self._computing_resource_name = computing_resource_name

    @property
    def computing_resource_type(self):
        """Gets the computing_resource_type of this CreateComputingResourceRequestBody.

        计算资源的类型。默认为sql。

        :return: The computing_resource_type of this CreateComputingResourceRequestBody.
        :rtype: str
        """
        return self._computing_resource_type

    @computing_resource_type.setter
    def computing_resource_type(self, computing_resource_type):
        """Sets the computing_resource_type of this CreateComputingResourceRequestBody.

        计算资源的类型。默认为sql。

        :param computing_resource_type: The computing_resource_type of this CreateComputingResourceRequestBody.
        :type computing_resource_type: str
        """
        self._computing_resource_type = computing_resource_type

    @property
    def description(self):
        """Gets the description of this CreateComputingResourceRequestBody.

        计算资源的描述信息。

        :return: The description of this CreateComputingResourceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateComputingResourceRequestBody.

        计算资源的描述信息。

        :param description: The description of this CreateComputingResourceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def cu_count(self):
        """Gets the cu_count of this CreateComputingResourceRequestBody.

        与计算资源绑定的最小计算单元个数。设置值当前只支持16，64，256。

        :return: The cu_count of this CreateComputingResourceRequestBody.
        :rtype: int
        """
        return self._cu_count

    @cu_count.setter
    def cu_count(self, cu_count):
        """Sets the cu_count of this CreateComputingResourceRequestBody.

        与计算资源绑定的最小计算单元个数。设置值当前只支持16，64，256。

        :param cu_count: The cu_count of this CreateComputingResourceRequestBody.
        :type cu_count: int
        """
        self._cu_count = cu_count

    @property
    def charging_mode(self):
        """Gets the charging_mode of this CreateComputingResourceRequestBody.

        计算资源的收费模式。只能设置为“1”，表示按照CU时收费。

        :return: The charging_mode of this CreateComputingResourceRequestBody.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this CreateComputingResourceRequestBody.

        计算资源的收费模式。只能设置为“1”，表示按照CU时收费。

        :param charging_mode: The charging_mode of this CreateComputingResourceRequestBody.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

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
        if not isinstance(other, CreateComputingResourceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
