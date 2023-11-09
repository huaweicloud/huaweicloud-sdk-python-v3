# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MeshSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str',
        'extend_params': 'MeshExtendParams',
        'tags': 'list[MeshTags]'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'extend_params': 'extendParams',
        'tags': 'tags'
    }

    def __init__(self, type=None, version=None, extend_params=None, tags=None):
        """MeshSpec

        The model defined in huaweicloud sdk

        :param type: 网格类型： InCluster: 集群内控制平面形态，基础版网格取值为InCluster
        :type type: str
        :param version: 网格版本
        :type version: str
        :param extend_params: 
        :type extend_params: :class:`huaweicloudsdkasm.v1.MeshExtendParams`
        :param tags: 网格资源标签
        :type tags: list[:class:`huaweicloudsdkasm.v1.MeshTags`]
        """
        
        

        self._type = None
        self._version = None
        self._extend_params = None
        self._tags = None
        self.discriminator = None

        self.type = type
        self.version = version
        if extend_params is not None:
            self.extend_params = extend_params
        if tags is not None:
            self.tags = tags

    @property
    def type(self):
        """Gets the type of this MeshSpec.

        网格类型： InCluster: 集群内控制平面形态，基础版网格取值为InCluster

        :return: The type of this MeshSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MeshSpec.

        网格类型： InCluster: 集群内控制平面形态，基础版网格取值为InCluster

        :param type: The type of this MeshSpec.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this MeshSpec.

        网格版本

        :return: The version of this MeshSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MeshSpec.

        网格版本

        :param version: The version of this MeshSpec.
        :type version: str
        """
        self._version = version

    @property
    def extend_params(self):
        """Gets the extend_params of this MeshSpec.

        :return: The extend_params of this MeshSpec.
        :rtype: :class:`huaweicloudsdkasm.v1.MeshExtendParams`
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        """Sets the extend_params of this MeshSpec.

        :param extend_params: The extend_params of this MeshSpec.
        :type extend_params: :class:`huaweicloudsdkasm.v1.MeshExtendParams`
        """
        self._extend_params = extend_params

    @property
    def tags(self):
        """Gets the tags of this MeshSpec.

        网格资源标签

        :return: The tags of this MeshSpec.
        :rtype: list[:class:`huaweicloudsdkasm.v1.MeshTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MeshSpec.

        网格资源标签

        :param tags: The tags of this MeshSpec.
        :type tags: list[:class:`huaweicloudsdkasm.v1.MeshTags`]
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
        if not isinstance(other, MeshSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
