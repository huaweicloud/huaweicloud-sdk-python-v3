# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Operations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_type': 'str',
        'resource_type': 'str',
        'trace_names': 'list[str]'
    }

    attribute_map = {
        'service_type': 'service_type',
        'resource_type': 'resource_type',
        'trace_names': 'trace_names'
    }

    def __init__(self, service_type=None, resource_type=None, trace_names=None):
        """Operations

        The model defined in huaweicloud sdk

        :param service_type: 标识云服务类型。必须为已对接CTS的云服务的英文缩写，且服务类型一般为大写字母。 已对接的云服务列表参见《云审计服务用户指南》“支持的服务”章节。
        :type service_type: str
        :param resource_type: 标识资源类型。
        :type resource_type: str
        :param trace_names: 标识事件名称。
        :type trace_names: list[str]
        """
        
        

        self._service_type = None
        self._resource_type = None
        self._trace_names = None
        self.discriminator = None

        self.service_type = service_type
        self.resource_type = resource_type
        self.trace_names = trace_names

    @property
    def service_type(self):
        """Gets the service_type of this Operations.

        标识云服务类型。必须为已对接CTS的云服务的英文缩写，且服务类型一般为大写字母。 已对接的云服务列表参见《云审计服务用户指南》“支持的服务”章节。

        :return: The service_type of this Operations.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this Operations.

        标识云服务类型。必须为已对接CTS的云服务的英文缩写，且服务类型一般为大写字母。 已对接的云服务列表参见《云审计服务用户指南》“支持的服务”章节。

        :param service_type: The service_type of this Operations.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this Operations.

        标识资源类型。

        :return: The resource_type of this Operations.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Operations.

        标识资源类型。

        :param resource_type: The resource_type of this Operations.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def trace_names(self):
        """Gets the trace_names of this Operations.

        标识事件名称。

        :return: The trace_names of this Operations.
        :rtype: list[str]
        """
        return self._trace_names

    @trace_names.setter
    def trace_names(self, trace_names):
        """Sets the trace_names of this Operations.

        标识事件名称。

        :param trace_names: The trace_names of this Operations.
        :type trace_names: list[str]
        """
        self._trace_names = trace_names

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
        if not isinstance(other, Operations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
