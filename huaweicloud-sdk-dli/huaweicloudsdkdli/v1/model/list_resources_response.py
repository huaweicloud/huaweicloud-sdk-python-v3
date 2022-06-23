# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resources': 'list[ListGroupPackagesResource]',
        'modules': 'list[ListResourcePackagesRespMoudle]',
        'groups': 'list[object]',
        'total': 'int'
    }

    attribute_map = {
        'resources': 'resources',
        'modules': 'modules',
        'groups': 'groups',
        'total': 'total'
    }

    def __init__(self, resources=None, modules=None, groups=None, total=None):
        """ListResourcesResponse

        The model defined in huaweicloud sdk

        :param resources: 已上传的用户资源名列表。
        :type resources: list[:class:`huaweicloudsdkdli.v1.ListGroupPackagesResource`]
        :param modules: 系统内置资源模块列表
        :type modules: list[:class:`huaweicloudsdkdli.v1.ListResourcePackagesRespMoudle`]
        :param groups: 已上传的用户分组资源。
        :type groups: list[object]
        :param total: 资源包返回总数
        :type total: int
        """
        
        super(ListResourcesResponse, self).__init__()

        self._resources = None
        self._modules = None
        self._groups = None
        self._total = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if modules is not None:
            self.modules = modules
        if groups is not None:
            self.groups = groups
        if total is not None:
            self.total = total

    @property
    def resources(self):
        """Gets the resources of this ListResourcesResponse.

        已上传的用户资源名列表。

        :return: The resources of this ListResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.ListGroupPackagesResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListResourcesResponse.

        已上传的用户资源名列表。

        :param resources: The resources of this ListResourcesResponse.
        :type resources: list[:class:`huaweicloudsdkdli.v1.ListGroupPackagesResource`]
        """
        self._resources = resources

    @property
    def modules(self):
        """Gets the modules of this ListResourcesResponse.

        系统内置资源模块列表

        :return: The modules of this ListResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.ListResourcePackagesRespMoudle`]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """Sets the modules of this ListResourcesResponse.

        系统内置资源模块列表

        :param modules: The modules of this ListResourcesResponse.
        :type modules: list[:class:`huaweicloudsdkdli.v1.ListResourcePackagesRespMoudle`]
        """
        self._modules = modules

    @property
    def groups(self):
        """Gets the groups of this ListResourcesResponse.

        已上传的用户分组资源。

        :return: The groups of this ListResourcesResponse.
        :rtype: list[object]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ListResourcesResponse.

        已上传的用户分组资源。

        :param groups: The groups of this ListResourcesResponse.
        :type groups: list[object]
        """
        self._groups = groups

    @property
    def total(self):
        """Gets the total of this ListResourcesResponse.

        资源包返回总数

        :return: The total of this ListResourcesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListResourcesResponse.

        资源包返回总数

        :param total: The total of this ListResourcesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
