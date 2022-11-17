# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNamespacesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'filter': 'filter'
    }

    def __init__(self, namespace=None, filter=None):
        """ListNamespacesRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param filter: 应填写namespace::{namespace}|mode::{mode}。其中{namespace}是组织名称，{mode}如果不设置，查看有权限的组织列表；设置为visible，查看可见的组织列表（部分组织：仓库有权限，组织没有权限）。
        :type filter: str
        """
        
        

        self._namespace = None
        self._filter = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if filter is not None:
            self.filter = filter

    @property
    def namespace(self):
        """Gets the namespace of this ListNamespacesRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this ListNamespacesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListNamespacesRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this ListNamespacesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def filter(self):
        """Gets the filter of this ListNamespacesRequest.

        应填写namespace::{namespace}|mode::{mode}。其中{namespace}是组织名称，{mode}如果不设置，查看有权限的组织列表；设置为visible，查看可见的组织列表（部分组织：仓库有权限，组织没有权限）。

        :return: The filter of this ListNamespacesRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListNamespacesRequest.

        应填写namespace::{namespace}|mode::{mode}。其中{namespace}是组织名称，{mode}如果不设置，查看有权限的组织列表；设置为visible，查看可见的组织列表（部分组织：仓库有权限，组织没有权限）。

        :param filter: The filter of this ListNamespacesRequest.
        :type filter: str
        """
        self._filter = filter

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
        if not isinstance(other, ListNamespacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
