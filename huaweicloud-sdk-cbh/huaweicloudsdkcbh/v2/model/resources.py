# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resources:

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
        'resource_detail': 'InstanceDetail',
        'tags': 'list[ResourceTag]',
        'sys_tags': 'list[ResourceTag]',
        'resource_name': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_detail': 'resource_detail',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'resource_name': 'resource_name'
    }

    def __init__(self, resource_id=None, resource_detail=None, tags=None, sys_tags=None, resource_name=None):
        r"""Resources

        The model defined in huaweicloud sdk

        :param resource_id: 实例ID。
        :type resource_id: str
        :param resource_detail: 
        :type resource_detail: :class:`huaweicloudsdkcbh.v2.InstanceDetail`
        :param tags: tags。
        :type tags: list[:class:`huaweicloudsdkcbh.v2.ResourceTag`]
        :param sys_tags: sys_tags。
        :type sys_tags: list[:class:`huaweicloudsdkcbh.v2.ResourceTag`]
        :param resource_name: 资源名称。
        :type resource_name: str
        """
        
        

        self._resource_id = None
        self._resource_detail = None
        self._tags = None
        self._sys_tags = None
        self._resource_name = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_detail = resource_detail
        self.tags = tags
        self.sys_tags = sys_tags
        self.resource_name = resource_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this Resources.

        实例ID。

        :return: The resource_id of this Resources.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this Resources.

        实例ID。

        :param resource_id: The resource_id of this Resources.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this Resources.

        :return: The resource_detail of this Resources.
        :rtype: :class:`huaweicloudsdkcbh.v2.InstanceDetail`
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this Resources.

        :param resource_detail: The resource_detail of this Resources.
        :type resource_detail: :class:`huaweicloudsdkcbh.v2.InstanceDetail`
        """
        self._resource_detail = resource_detail

    @property
    def tags(self):
        r"""Gets the tags of this Resources.

        tags。

        :return: The tags of this Resources.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Resources.

        tags。

        :param tags: The tags of this Resources.
        :type tags: list[:class:`huaweicloudsdkcbh.v2.ResourceTag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this Resources.

        sys_tags。

        :return: The sys_tags of this Resources.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.ResourceTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this Resources.

        sys_tags。

        :param sys_tags: The sys_tags of this Resources.
        :type sys_tags: list[:class:`huaweicloudsdkcbh.v2.ResourceTag`]
        """
        self._sys_tags = sys_tags

    @property
    def resource_name(self):
        r"""Gets the resource_name of this Resources.

        资源名称。

        :return: The resource_name of this Resources.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this Resources.

        资源名称。

        :param resource_name: The resource_name of this Resources.
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
        if not isinstance(other, Resources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
