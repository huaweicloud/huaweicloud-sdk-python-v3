# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetaDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'created': 'str',
        'last_modified': 'str'
    }

    attribute_map = {
        'resource_type': 'resourceType',
        'created': 'created',
        'last_modified': 'lastModified'
    }

    def __init__(self, resource_type=None, created=None, last_modified=None):
        r"""MetaDto

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型
        :type resource_type: str
        :param created: 资源创建时间
        :type created: str
        :param last_modified: 资源最后更新时间
        :type last_modified: str
        """
        
        

        self._resource_type = None
        self._created = None
        self._last_modified = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if created is not None:
            self.created = created
        if last_modified is not None:
            self.last_modified = last_modified

    @property
    def resource_type(self):
        r"""Gets the resource_type of this MetaDto.

        资源类型

        :return: The resource_type of this MetaDto.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this MetaDto.

        资源类型

        :param resource_type: The resource_type of this MetaDto.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def created(self):
        r"""Gets the created of this MetaDto.

        资源创建时间

        :return: The created of this MetaDto.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this MetaDto.

        资源创建时间

        :param created: The created of this MetaDto.
        :type created: str
        """
        self._created = created

    @property
    def last_modified(self):
        r"""Gets the last_modified of this MetaDto.

        资源最后更新时间

        :return: The last_modified of this MetaDto.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this MetaDto.

        资源最后更新时间

        :param last_modified: The last_modified of this MetaDto.
        :type last_modified: str
        """
        self._last_modified = last_modified

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
        if not isinstance(other, MetaDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
