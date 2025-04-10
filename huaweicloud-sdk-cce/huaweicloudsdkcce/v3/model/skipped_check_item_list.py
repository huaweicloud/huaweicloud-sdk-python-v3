# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SkippedCheckItemList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'resource_selector': 'ResourceSelector'
    }

    attribute_map = {
        'name': 'name',
        'resource_selector': 'resourceSelector'
    }

    def __init__(self, name=None, resource_selector=None):
        r"""SkippedCheckItemList

        The model defined in huaweicloud sdk

        :param name: 跳过的检查项名称
        :type name: str
        :param resource_selector: 
        :type resource_selector: :class:`huaweicloudsdkcce.v3.ResourceSelector`
        """
        
        

        self._name = None
        self._resource_selector = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if resource_selector is not None:
            self.resource_selector = resource_selector

    @property
    def name(self):
        r"""Gets the name of this SkippedCheckItemList.

        跳过的检查项名称

        :return: The name of this SkippedCheckItemList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SkippedCheckItemList.

        跳过的检查项名称

        :param name: The name of this SkippedCheckItemList.
        :type name: str
        """
        self._name = name

    @property
    def resource_selector(self):
        r"""Gets the resource_selector of this SkippedCheckItemList.

        :return: The resource_selector of this SkippedCheckItemList.
        :rtype: :class:`huaweicloudsdkcce.v3.ResourceSelector`
        """
        return self._resource_selector

    @resource_selector.setter
    def resource_selector(self, resource_selector):
        r"""Sets the resource_selector of this SkippedCheckItemList.

        :param resource_selector: The resource_selector of this SkippedCheckItemList.
        :type resource_selector: :class:`huaweicloudsdkcce.v3.ResourceSelector`
        """
        self._resource_selector = resource_selector

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
        if not isinstance(other, SkippedCheckItemList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
