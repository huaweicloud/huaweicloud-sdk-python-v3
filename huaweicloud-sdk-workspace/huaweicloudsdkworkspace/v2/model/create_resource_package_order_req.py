# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourcePackageOrderReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'resource_packages': 'list[ResourcePackage]',
        'resource_size': 'int',
        'extend_param': 'OrderExtendParam'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'resource_packages': 'resource_packages',
        'resource_size': 'resource_size',
        'extend_param': 'extend_param'
    }

    def __init__(self, enterprise_project_id=None, resource_packages=None, resource_size=None, extend_param=None):
        r"""CreateResourcePackageOrderReq

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，上传则指定企业项目，不上传则表示所有企业项目。
        :type enterprise_project_id: str
        :param resource_packages: 资源包。
        :type resource_packages: list[:class:`huaweicloudsdkworkspace.v2.ResourcePackage`]
        :param resource_size: 购买资源包数量。
        :type resource_size: int
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        
        

        self._enterprise_project_id = None
        self._resource_packages = None
        self._resource_size = None
        self._extend_param = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.resource_packages = resource_packages
        if resource_size is not None:
            self.resource_size = resource_size
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateResourcePackageOrderReq.

        企业项目ID，上传则指定企业项目，不上传则表示所有企业项目。

        :return: The enterprise_project_id of this CreateResourcePackageOrderReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateResourcePackageOrderReq.

        企业项目ID，上传则指定企业项目，不上传则表示所有企业项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateResourcePackageOrderReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def resource_packages(self):
        r"""Gets the resource_packages of this CreateResourcePackageOrderReq.

        资源包。

        :return: The resource_packages of this CreateResourcePackageOrderReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ResourcePackage`]
        """
        return self._resource_packages

    @resource_packages.setter
    def resource_packages(self, resource_packages):
        r"""Sets the resource_packages of this CreateResourcePackageOrderReq.

        资源包。

        :param resource_packages: The resource_packages of this CreateResourcePackageOrderReq.
        :type resource_packages: list[:class:`huaweicloudsdkworkspace.v2.ResourcePackage`]
        """
        self._resource_packages = resource_packages

    @property
    def resource_size(self):
        r"""Gets the resource_size of this CreateResourcePackageOrderReq.

        购买资源包数量。

        :return: The resource_size of this CreateResourcePackageOrderReq.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this CreateResourcePackageOrderReq.

        购买资源包数量。

        :param resource_size: The resource_size of this CreateResourcePackageOrderReq.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def extend_param(self):
        r"""Gets the extend_param of this CreateResourcePackageOrderReq.

        :return: The extend_param of this CreateResourcePackageOrderReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this CreateResourcePackageOrderReq.

        :param extend_param: The extend_param of this CreateResourcePackageOrderReq.
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        self._extend_param = extend_param

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateResourcePackageOrderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
