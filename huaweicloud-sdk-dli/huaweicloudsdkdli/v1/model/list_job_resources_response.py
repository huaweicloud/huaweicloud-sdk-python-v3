# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'resources': 'list[PackageResource]',
        'modules': 'list[PackageResourceMoudle]',
        'groups': 'list[PackageResourceGroup]'
    }

    attribute_map = {
        'total': 'total',
        'resources': 'resources',
        'modules': 'modules',
        'groups': 'groups'
    }

    def __init__(self, total=None, resources=None, modules=None, groups=None):
        r"""ListJobResourcesResponse

        The model defined in huaweicloud sdk

        :param total: 资源包返回总数
        :type total: int
        :param resources: 已上传的用户资源名列表。
        :type resources: list[:class:`huaweicloudsdkdli.v1.PackageResource`]
        :param modules: 系统内置资源模块列表
        :type modules: list[:class:`huaweicloudsdkdli.v1.PackageResourceMoudle`]
        :param groups: 已上传的用户分组资源。
        :type groups: list[:class:`huaweicloudsdkdli.v1.PackageResourceGroup`]
        """
        
        super(ListJobResourcesResponse, self).__init__()

        self._total = None
        self._resources = None
        self._modules = None
        self._groups = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if resources is not None:
            self.resources = resources
        if modules is not None:
            self.modules = modules
        if groups is not None:
            self.groups = groups

    @property
    def total(self):
        r"""Gets the total of this ListJobResourcesResponse.

        资源包返回总数

        :return: The total of this ListJobResourcesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListJobResourcesResponse.

        资源包返回总数

        :param total: The total of this ListJobResourcesResponse.
        :type total: int
        """
        self._total = total

    @property
    def resources(self):
        r"""Gets the resources of this ListJobResourcesResponse.

        已上传的用户资源名列表。

        :return: The resources of this ListJobResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.PackageResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListJobResourcesResponse.

        已上传的用户资源名列表。

        :param resources: The resources of this ListJobResourcesResponse.
        :type resources: list[:class:`huaweicloudsdkdli.v1.PackageResource`]
        """
        self._resources = resources

    @property
    def modules(self):
        r"""Gets the modules of this ListJobResourcesResponse.

        系统内置资源模块列表

        :return: The modules of this ListJobResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.PackageResourceMoudle`]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        r"""Sets the modules of this ListJobResourcesResponse.

        系统内置资源模块列表

        :param modules: The modules of this ListJobResourcesResponse.
        :type modules: list[:class:`huaweicloudsdkdli.v1.PackageResourceMoudle`]
        """
        self._modules = modules

    @property
    def groups(self):
        r"""Gets the groups of this ListJobResourcesResponse.

        已上传的用户分组资源。

        :return: The groups of this ListJobResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.PackageResourceGroup`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this ListJobResourcesResponse.

        已上传的用户分组资源。

        :param groups: The groups of this ListJobResourcesResponse.
        :type groups: list[:class:`huaweicloudsdkdli.v1.PackageResourceGroup`]
        """
        self._groups = groups

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
        if not isinstance(other, ListJobResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
