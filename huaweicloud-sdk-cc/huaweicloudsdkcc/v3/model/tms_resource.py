# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TmsResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'tags': 'list[Tag]',
        'resource_name': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'tags': 'tags',
        'resource_name': 'resource_name'
    }

    def __init__(self, resource_id=None, tags=None, resource_name=None):
        r"""TmsResource

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID。
        :type resource_id: str
        :param tags: 标签列表，没有标签默认为空数组。
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        :param resource_name: 资源名称，资源没有名称时默认为空字符串。
        :type resource_name: str
        """
        
        

        self._resource_id = None
        self._tags = None
        self._resource_name = None
        self.discriminator = None

        self.resource_id = resource_id
        self.tags = tags
        self.resource_name = resource_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this TmsResource.

        资源ID。

        :return: The resource_id of this TmsResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this TmsResource.

        资源ID。

        :param resource_id: The resource_id of this TmsResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def tags(self):
        r"""Gets the tags of this TmsResource.

        标签列表，没有标签默认为空数组。

        :return: The tags of this TmsResource.
        :rtype: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TmsResource.

        标签列表，没有标签默认为空数组。

        :param tags: The tags of this TmsResource.
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        self._tags = tags

    @property
    def resource_name(self):
        r"""Gets the resource_name of this TmsResource.

        资源名称，资源没有名称时默认为空字符串。

        :return: The resource_name of this TmsResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this TmsResource.

        资源名称，资源没有名称时默认为空字符串。

        :param resource_name: The resource_name of this TmsResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, TmsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
