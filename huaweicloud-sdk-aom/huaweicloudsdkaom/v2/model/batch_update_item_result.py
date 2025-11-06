# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateItemResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_alias': 'str',
        'resource_name': 'str',
        'ret_status': 'str'
    }

    attribute_map = {
        'resource_alias': 'resource_alias',
        'resource_name': 'resource_name',
        'ret_status': 'ret_status'
    }

    def __init__(self, resource_alias=None, resource_name=None, ret_status=None):
        r"""BatchUpdateItemResult

        The model defined in huaweicloud sdk

        :param resource_alias: 资源名称别名。
        :type resource_alias: str
        :param resource_name: 资源名称。
        :type resource_name: str
        :param ret_status: 资源更新状态。
        :type ret_status: str
        """
        
        

        self._resource_alias = None
        self._resource_name = None
        self._ret_status = None
        self.discriminator = None

        if resource_alias is not None:
            self.resource_alias = resource_alias
        if resource_name is not None:
            self.resource_name = resource_name
        if ret_status is not None:
            self.ret_status = ret_status

    @property
    def resource_alias(self):
        r"""Gets the resource_alias of this BatchUpdateItemResult.

        资源名称别名。

        :return: The resource_alias of this BatchUpdateItemResult.
        :rtype: str
        """
        return self._resource_alias

    @resource_alias.setter
    def resource_alias(self, resource_alias):
        r"""Sets the resource_alias of this BatchUpdateItemResult.

        资源名称别名。

        :param resource_alias: The resource_alias of this BatchUpdateItemResult.
        :type resource_alias: str
        """
        self._resource_alias = resource_alias

    @property
    def resource_name(self):
        r"""Gets the resource_name of this BatchUpdateItemResult.

        资源名称。

        :return: The resource_name of this BatchUpdateItemResult.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this BatchUpdateItemResult.

        资源名称。

        :param resource_name: The resource_name of this BatchUpdateItemResult.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def ret_status(self):
        r"""Gets the ret_status of this BatchUpdateItemResult.

        资源更新状态。

        :return: The ret_status of this BatchUpdateItemResult.
        :rtype: str
        """
        return self._ret_status

    @ret_status.setter
    def ret_status(self, ret_status):
        r"""Sets the ret_status of this BatchUpdateItemResult.

        资源更新状态。

        :param ret_status: The ret_status of this BatchUpdateItemResult.
        :type ret_status: str
        """
        self._ret_status = ret_status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchUpdateItemResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
