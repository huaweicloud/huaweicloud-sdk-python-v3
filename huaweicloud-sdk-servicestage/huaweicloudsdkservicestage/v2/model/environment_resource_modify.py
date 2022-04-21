# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentResourceModify:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'add_base_resources': 'list[Resource]',
        'add_optional_resources': 'list[Resource]',
        'remove_resources': 'list[Resource]'
    }

    attribute_map = {
        'add_base_resources': 'add_base_resources',
        'add_optional_resources': 'add_optional_resources',
        'remove_resources': 'remove_resources'
    }

    def __init__(self, add_base_resources=None, add_optional_resources=None, remove_resources=None):
        """EnvironmentResourceModify

        The model defined in huaweicloud sdk

        :param add_base_resources: 添加基础资源。
        :type add_base_resources: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        :param add_optional_resources: 添加其他资源。
        :type add_optional_resources: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        :param remove_resources: 移除资源。
        :type remove_resources: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        
        

        self._add_base_resources = None
        self._add_optional_resources = None
        self._remove_resources = None
        self.discriminator = None

        if add_base_resources is not None:
            self.add_base_resources = add_base_resources
        if add_optional_resources is not None:
            self.add_optional_resources = add_optional_resources
        if remove_resources is not None:
            self.remove_resources = remove_resources

    @property
    def add_base_resources(self):
        """Gets the add_base_resources of this EnvironmentResourceModify.

        添加基础资源。

        :return: The add_base_resources of this EnvironmentResourceModify.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        return self._add_base_resources

    @add_base_resources.setter
    def add_base_resources(self, add_base_resources):
        """Sets the add_base_resources of this EnvironmentResourceModify.

        添加基础资源。

        :param add_base_resources: The add_base_resources of this EnvironmentResourceModify.
        :type add_base_resources: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        self._add_base_resources = add_base_resources

    @property
    def add_optional_resources(self):
        """Gets the add_optional_resources of this EnvironmentResourceModify.

        添加其他资源。

        :return: The add_optional_resources of this EnvironmentResourceModify.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        return self._add_optional_resources

    @add_optional_resources.setter
    def add_optional_resources(self, add_optional_resources):
        """Sets the add_optional_resources of this EnvironmentResourceModify.

        添加其他资源。

        :param add_optional_resources: The add_optional_resources of this EnvironmentResourceModify.
        :type add_optional_resources: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        self._add_optional_resources = add_optional_resources

    @property
    def remove_resources(self):
        """Gets the remove_resources of this EnvironmentResourceModify.

        移除资源。

        :return: The remove_resources of this EnvironmentResourceModify.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        return self._remove_resources

    @remove_resources.setter
    def remove_resources(self, remove_resources):
        """Sets the remove_resources of this EnvironmentResourceModify.

        移除资源。

        :param remove_resources: The remove_resources of this EnvironmentResourceModify.
        :type remove_resources: list[:class:`huaweicloudsdkservicestage.v2.Resource`]
        """
        self._remove_resources = remove_resources

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
        if not isinstance(other, EnvironmentResourceModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
