# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_version': 'str',
        '_continue': 'str',
        'remaining_item_count': 'str'
    }

    attribute_map = {
        'resource_version': 'resourceVersion',
        '_continue': 'continue',
        'remaining_item_count': 'remainingItemCount'
    }

    def __init__(self, resource_version=None, _continue=None, remaining_item_count=None):
        r"""ListMeta

        The model defined in huaweicloud sdk

        :param resource_version: 服务器内部版本标识符
        :type resource_version: str
        :param _continue: 表示当前请求返回的结果是否还有下一页数据
        :type _continue: str
        :param remaining_item_count: 表示在当前响应之后，列表中还有多少项未被包含进来
        :type remaining_item_count: str
        """
        
        

        self._resource_version = None
        self.__continue = None
        self._remaining_item_count = None
        self.discriminator = None

        if resource_version is not None:
            self.resource_version = resource_version
        if _continue is not None:
            self._continue = _continue
        if remaining_item_count is not None:
            self.remaining_item_count = remaining_item_count

    @property
    def resource_version(self):
        r"""Gets the resource_version of this ListMeta.

        服务器内部版本标识符

        :return: The resource_version of this ListMeta.
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        r"""Sets the resource_version of this ListMeta.

        服务器内部版本标识符

        :param resource_version: The resource_version of this ListMeta.
        :type resource_version: str
        """
        self._resource_version = resource_version

    @property
    def _continue(self):
        r"""Gets the _continue of this ListMeta.

        表示当前请求返回的结果是否还有下一页数据

        :return: The _continue of this ListMeta.
        :rtype: str
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        r"""Sets the _continue of this ListMeta.

        表示当前请求返回的结果是否还有下一页数据

        :param _continue: The _continue of this ListMeta.
        :type _continue: str
        """
        self.__continue = _continue

    @property
    def remaining_item_count(self):
        r"""Gets the remaining_item_count of this ListMeta.

        表示在当前响应之后，列表中还有多少项未被包含进来

        :return: The remaining_item_count of this ListMeta.
        :rtype: str
        """
        return self._remaining_item_count

    @remaining_item_count.setter
    def remaining_item_count(self, remaining_item_count):
        r"""Sets the remaining_item_count of this ListMeta.

        表示在当前响应之后，列表中还有多少项未被包含进来

        :param remaining_item_count: The remaining_item_count of this ListMeta.
        :type remaining_item_count: str
        """
        self._remaining_item_count = remaining_item_count

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
        if not isinstance(other, ListMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
