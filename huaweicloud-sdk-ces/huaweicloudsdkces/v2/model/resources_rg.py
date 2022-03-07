# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcesRg:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'Namespace',
        'dimensions': 'list[Dimension]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions'
    }

    def __init__(self, namespace=None, dimensions=None):
        """ResourcesRg - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._dimensions = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def namespace(self):
        """Gets the namespace of this ResourcesRg.


        :return: The namespace of this ResourcesRg.
        :rtype: Namespace
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ResourcesRg.


        :param namespace: The namespace of this ResourcesRg.
        :type: Namespace
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        """Gets the dimensions of this ResourcesRg.

        资源实例的维度信息

        :return: The dimensions of this ResourcesRg.
        :rtype: list[Dimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ResourcesRg.

        资源实例的维度信息

        :param dimensions: The dimensions of this ResourcesRg.
        :type: list[Dimension]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, ResourcesRg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
