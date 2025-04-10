# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOperation:

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
        'operation_list': 'list[str]'
    }

    attribute_map = {
        'service_type': 'service_type',
        'resource_type': 'resource_type',
        'operation_list': 'operation_list'
    }

    def __init__(self, service_type=None, resource_type=None, operation_list=None):
        r"""ListOperation

        The model defined in huaweicloud sdk

        :param service_type: 事件对应的云服务类型。
        :type service_type: str
        :param resource_type: 事件对应的资源类型。
        :type resource_type: str
        :param operation_list: 操作事件名称数组。
        :type operation_list: list[str]
        """
        
        

        self._service_type = None
        self._resource_type = None
        self._operation_list = None
        self.discriminator = None

        if service_type is not None:
            self.service_type = service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if operation_list is not None:
            self.operation_list = operation_list

    @property
    def service_type(self):
        r"""Gets the service_type of this ListOperation.

        事件对应的云服务类型。

        :return: The service_type of this ListOperation.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ListOperation.

        事件对应的云服务类型。

        :param service_type: The service_type of this ListOperation.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListOperation.

        事件对应的资源类型。

        :return: The resource_type of this ListOperation.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListOperation.

        事件对应的资源类型。

        :param resource_type: The resource_type of this ListOperation.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def operation_list(self):
        r"""Gets the operation_list of this ListOperation.

        操作事件名称数组。

        :return: The operation_list of this ListOperation.
        :rtype: list[str]
        """
        return self._operation_list

    @operation_list.setter
    def operation_list(self, operation_list):
        r"""Sets the operation_list of this ListOperation.

        操作事件名称数组。

        :param operation_list: The operation_list of this ListOperation.
        :type operation_list: list[str]
        """
        self._operation_list = operation_list

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
        if not isinstance(other, ListOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
