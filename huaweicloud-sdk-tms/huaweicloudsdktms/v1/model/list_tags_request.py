# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_types': 'str',
        'project_id': 'str',
        'tag_types': 'str'
    }

    attribute_map = {
        'resource_types': 'resource_types',
        'project_id': 'project_id',
        'tag_types': 'tag_types'
    }

    def __init__(self, resource_types=None, project_id=None, tag_types=None):
        r"""ListTagsRequest

        The model defined in huaweicloud sdk

        :param resource_types: 资源类型
        :type resource_types: str
        :param project_id: 项目ID
        :type project_id: str
        :param tag_types: 标签类型
        :type tag_types: str
        """
        
        

        self._resource_types = None
        self._project_id = None
        self._tag_types = None
        self.discriminator = None

        self.resource_types = resource_types
        self.project_id = project_id
        self.tag_types = tag_types

    @property
    def resource_types(self):
        r"""Gets the resource_types of this ListTagsRequest.

        资源类型

        :return: The resource_types of this ListTagsRequest.
        :rtype: str
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        r"""Sets the resource_types of this ListTagsRequest.

        资源类型

        :param resource_types: The resource_types of this ListTagsRequest.
        :type resource_types: str
        """
        self._resource_types = resource_types

    @property
    def project_id(self):
        r"""Gets the project_id of this ListTagsRequest.

        项目ID

        :return: The project_id of this ListTagsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListTagsRequest.

        项目ID

        :param project_id: The project_id of this ListTagsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tag_types(self):
        r"""Gets the tag_types of this ListTagsRequest.

        标签类型

        :return: The tag_types of this ListTagsRequest.
        :rtype: str
        """
        return self._tag_types

    @tag_types.setter
    def tag_types(self, tag_types):
        r"""Sets the tag_types of this ListTagsRequest.

        标签类型

        :param tag_types: The tag_types of this ListTagsRequest.
        :type tag_types: str
        """
        self._tag_types = tag_types

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
        if not isinstance(other, ListTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
