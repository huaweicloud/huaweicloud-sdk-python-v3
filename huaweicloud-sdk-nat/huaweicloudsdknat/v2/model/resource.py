# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_detail': 'object',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_tag': 'list[ResourceTag]'
    }

    attribute_map = {
        'resource_detail': 'resource_detail',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_tag': 'resource_tag'
    }

    def __init__(self, resource_detail=None, resource_id=None, resource_name=None, resource_tag=None):
        r"""Resource

        The model defined in huaweicloud sdk

        :param resource_detail: 资源详情。用于扩展。默认为空。
        :type resource_detail: object
        :param resource_id: 资源的ID。
        :type resource_id: str
        :param resource_name: 资源名称，资源没有名称时默认为空字符串。
        :type resource_name: str
        :param resource_tag: 标签列表，没有标签默认为空数组。
        :type resource_tag: list[:class:`huaweicloudsdknat.v2.ResourceTag`]
        """
        
        

        self._resource_detail = None
        self._resource_id = None
        self._resource_name = None
        self._resource_tag = None
        self.discriminator = None

        self.resource_detail = resource_detail
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_tag = resource_tag

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this Resource.

        资源详情。用于扩展。默认为空。

        :return: The resource_detail of this Resource.
        :rtype: object
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this Resource.

        资源详情。用于扩展。默认为空。

        :param resource_detail: The resource_detail of this Resource.
        :type resource_detail: object
        """
        self._resource_detail = resource_detail

    @property
    def resource_id(self):
        r"""Gets the resource_id of this Resource.

        资源的ID。

        :return: The resource_id of this Resource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this Resource.

        资源的ID。

        :param resource_id: The resource_id of this Resource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this Resource.

        资源名称，资源没有名称时默认为空字符串。

        :return: The resource_name of this Resource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this Resource.

        资源名称，资源没有名称时默认为空字符串。

        :param resource_name: The resource_name of this Resource.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_tag(self):
        r"""Gets the resource_tag of this Resource.

        标签列表，没有标签默认为空数组。

        :return: The resource_tag of this Resource.
        :rtype: list[:class:`huaweicloudsdknat.v2.ResourceTag`]
        """
        return self._resource_tag

    @resource_tag.setter
    def resource_tag(self, resource_tag):
        r"""Sets the resource_tag of this Resource.

        标签列表，没有标签默认为空数组。

        :param resource_tag: The resource_tag of this Resource.
        :type resource_tag: list[:class:`huaweicloudsdknat.v2.ResourceTag`]
        """
        self._resource_tag = resource_tag

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
