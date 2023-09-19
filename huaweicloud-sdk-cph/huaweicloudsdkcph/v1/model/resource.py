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
        'resource_id': 'str',
        'resource_detail': 'str',
        'resource_name': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_detail': 'resource_detail',
        'resource_name': 'resource_name',
        'tags': 'tags'
    }

    def __init__(self, resource_id=None, resource_detail=None, resource_name=None, tags=None):
        """Resource

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_detail: 资源详情。
        :type resource_detail: str
        :param resource_name: 资源名称。
        :type resource_name: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkcph.v1.Tag`]
        """
        
        

        self._resource_id = None
        self._resource_detail = None
        self._resource_name = None
        self._tags = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_detail is not None:
            self.resource_detail = resource_detail
        if resource_name is not None:
            self.resource_name = resource_name
        if tags is not None:
            self.tags = tags

    @property
    def resource_id(self):
        """Gets the resource_id of this Resource.

        资源ID。

        :return: The resource_id of this Resource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Resource.

        资源ID。

        :param resource_id: The resource_id of this Resource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_detail(self):
        """Gets the resource_detail of this Resource.

        资源详情。

        :return: The resource_detail of this Resource.
        :rtype: str
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        """Sets the resource_detail of this Resource.

        资源详情。

        :param resource_detail: The resource_detail of this Resource.
        :type resource_detail: str
        """
        self._resource_detail = resource_detail

    @property
    def resource_name(self):
        """Gets the resource_name of this Resource.

        资源名称。

        :return: The resource_name of this Resource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this Resource.

        资源名称。

        :param resource_name: The resource_name of this Resource.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def tags(self):
        """Gets the tags of this Resource.

        标签列表。

        :return: The tags of this Resource.
        :rtype: list[:class:`huaweicloudsdkcph.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Resource.

        标签列表。

        :param tags: The tags of this Resource.
        :type tags: list[:class:`huaweicloudsdkcph.v1.Tag`]
        """
        self._tags = tags

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
