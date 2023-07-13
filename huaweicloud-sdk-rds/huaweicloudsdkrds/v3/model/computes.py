# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Computes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_type': 'str',
        'compute_flavors': 'list[ScaleFlavors]'
    }

    attribute_map = {
        'group_type': 'group_type',
        'compute_flavors': 'compute_flavors'
    }

    def __init__(self, group_type=None, compute_flavors=None):
        """Computes

        The model defined in huaweicloud sdk

        :param group_type: 群组类型。  - X86：X86架构。 - ARM：ARM架构。
        :type group_type: str
        :param compute_flavors: 计算规格信息。
        :type compute_flavors: list[:class:`huaweicloudsdkrds.v3.ScaleFlavors`]
        """
        
        

        self._group_type = None
        self._compute_flavors = None
        self.discriminator = None

        if group_type is not None:
            self.group_type = group_type
        if compute_flavors is not None:
            self.compute_flavors = compute_flavors

    @property
    def group_type(self):
        """Gets the group_type of this Computes.

        群组类型。  - X86：X86架构。 - ARM：ARM架构。

        :return: The group_type of this Computes.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this Computes.

        群组类型。  - X86：X86架构。 - ARM：ARM架构。

        :param group_type: The group_type of this Computes.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def compute_flavors(self):
        """Gets the compute_flavors of this Computes.

        计算规格信息。

        :return: The compute_flavors of this Computes.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ScaleFlavors`]
        """
        return self._compute_flavors

    @compute_flavors.setter
    def compute_flavors(self, compute_flavors):
        """Sets the compute_flavors of this Computes.

        计算规格信息。

        :param compute_flavors: The compute_flavors of this Computes.
        :type compute_flavors: list[:class:`huaweicloudsdkrds.v3.ScaleFlavors`]
        """
        self._compute_flavors = compute_flavors

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
        if not isinstance(other, Computes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
