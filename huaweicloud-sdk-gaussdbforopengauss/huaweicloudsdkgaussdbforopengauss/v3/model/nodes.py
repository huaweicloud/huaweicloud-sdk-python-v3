# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Nodes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'components': 'list[Components]'
    }

    attribute_map = {
        'id': 'id',
        'components': 'components'
    }

    def __init__(self, id=None, components=None):
        """Nodes

        The model defined in huaweicloud sdk

        :param id: 节点ID。
        :type id: str
        :param components: 组件列表。
        :type components: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Components`]
        """
        
        

        self._id = None
        self._components = None
        self.discriminator = None

        self.id = id
        self.components = components

    @property
    def id(self):
        """Gets the id of this Nodes.

        节点ID。

        :return: The id of this Nodes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Nodes.

        节点ID。

        :param id: The id of this Nodes.
        :type id: str
        """
        self._id = id

    @property
    def components(self):
        """Gets the components of this Nodes.

        组件列表。

        :return: The components of this Nodes.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Components`]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this Nodes.

        组件列表。

        :param components: The components of this Nodes.
        :type components: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Components`]
        """
        self._components = components

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
        if not isinstance(other, Nodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
