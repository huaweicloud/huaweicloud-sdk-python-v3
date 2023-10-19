# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FilterTagResource:

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
        'resource_name': 'str',
        'resource_detail': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_detail': 'resource_detail',
        'tags': 'tags'
    }

    def __init__(self, resource_id=None, resource_name=None, resource_detail=None, tags=None):
        """FilterTagResource

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_detail: 资源详情
        :type resource_detail: str
        :param tags: 资源下包含的标签
        :type tags: list[:class:`huaweicloudsdkcc.v2.Tag`]
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._resource_detail = None
        self._tags = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        self.resource_name = resource_name
        if resource_detail is not None:
            self.resource_detail = resource_detail
        if tags is not None:
            self.tags = tags

    @property
    def resource_id(self):
        """Gets the resource_id of this FilterTagResource.

        资源ID

        :return: The resource_id of this FilterTagResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this FilterTagResource.

        资源ID

        :param resource_id: The resource_id of this FilterTagResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this FilterTagResource.

        资源名称

        :return: The resource_name of this FilterTagResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this FilterTagResource.

        资源名称

        :param resource_name: The resource_name of this FilterTagResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_detail(self):
        """Gets the resource_detail of this FilterTagResource.

        资源详情

        :return: The resource_detail of this FilterTagResource.
        :rtype: str
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        """Sets the resource_detail of this FilterTagResource.

        资源详情

        :param resource_detail: The resource_detail of this FilterTagResource.
        :type resource_detail: str
        """
        self._resource_detail = resource_detail

    @property
    def tags(self):
        """Gets the tags of this FilterTagResource.

        资源下包含的标签

        :return: The tags of this FilterTagResource.
        :rtype: list[:class:`huaweicloudsdkcc.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FilterTagResource.

        资源下包含的标签

        :param tags: The tags of this FilterTagResource.
        :type tags: list[:class:`huaweicloudsdkcc.v2.Tag`]
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
        if not isinstance(other, FilterTagResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
