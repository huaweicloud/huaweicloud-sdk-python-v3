# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbrPolicyDetail:

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
        'resource_name': 'str',
        'provider': 'str',
        'region_id': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'resource_label': 'list[Tag]',
        'resource_detail': 'CbrPolicyDetailResourceDetail'
    }

    attribute_map = {
        'id': 'id',
        'resource_name': 'resource_name',
        'provider': 'provider',
        'region_id': 'region_id',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'resource_label': 'resource_label',
        'resource_detail': 'resource_detail'
    }

    def __init__(self, id=None, resource_name=None, provider=None, region_id=None, domain_id=None, project_id=None, enterprise_project_id=None, resource_label=None, resource_detail=None):
        r"""CbrPolicyDetail

        The model defined in huaweicloud sdk

        :param id: 策略ID
        :type id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param provider: 资源归属云服务
        :type provider: str
        :param region_id: 区域ID
        :type region_id: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param resource_label: 资源标签
        :type resource_label: list[:class:`huaweicloudsdkbcc.v1.Tag`]
        :param resource_detail: 
        :type resource_detail: :class:`huaweicloudsdkbcc.v1.CbrPolicyDetailResourceDetail`
        """
        
        

        self._id = None
        self._resource_name = None
        self._provider = None
        self._region_id = None
        self._domain_id = None
        self._project_id = None
        self._enterprise_project_id = None
        self._resource_label = None
        self._resource_detail = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_name is not None:
            self.resource_name = resource_name
        if provider is not None:
            self.provider = provider
        if region_id is not None:
            self.region_id = region_id
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if resource_label is not None:
            self.resource_label = resource_label
        if resource_detail is not None:
            self.resource_detail = resource_detail

    @property
    def id(self):
        r"""Gets the id of this CbrPolicyDetail.

        策略ID

        :return: The id of this CbrPolicyDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CbrPolicyDetail.

        策略ID

        :param id: The id of this CbrPolicyDetail.
        :type id: str
        """
        self._id = id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this CbrPolicyDetail.

        资源名称

        :return: The resource_name of this CbrPolicyDetail.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this CbrPolicyDetail.

        资源名称

        :param resource_name: The resource_name of this CbrPolicyDetail.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def provider(self):
        r"""Gets the provider of this CbrPolicyDetail.

        资源归属云服务

        :return: The provider of this CbrPolicyDetail.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this CbrPolicyDetail.

        资源归属云服务

        :param provider: The provider of this CbrPolicyDetail.
        :type provider: str
        """
        self._provider = provider

    @property
    def region_id(self):
        r"""Gets the region_id of this CbrPolicyDetail.

        区域ID

        :return: The region_id of this CbrPolicyDetail.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CbrPolicyDetail.

        区域ID

        :param region_id: The region_id of this CbrPolicyDetail.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CbrPolicyDetail.

        账号ID

        :return: The domain_id of this CbrPolicyDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CbrPolicyDetail.

        账号ID

        :param domain_id: The domain_id of this CbrPolicyDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CbrPolicyDetail.

        项目ID

        :return: The project_id of this CbrPolicyDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CbrPolicyDetail.

        项目ID

        :param project_id: The project_id of this CbrPolicyDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CbrPolicyDetail.

        企业项目ID

        :return: The enterprise_project_id of this CbrPolicyDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CbrPolicyDetail.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CbrPolicyDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def resource_label(self):
        r"""Gets the resource_label of this CbrPolicyDetail.

        资源标签

        :return: The resource_label of this CbrPolicyDetail.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.Tag`]
        """
        return self._resource_label

    @resource_label.setter
    def resource_label(self, resource_label):
        r"""Sets the resource_label of this CbrPolicyDetail.

        资源标签

        :param resource_label: The resource_label of this CbrPolicyDetail.
        :type resource_label: list[:class:`huaweicloudsdkbcc.v1.Tag`]
        """
        self._resource_label = resource_label

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this CbrPolicyDetail.

        :return: The resource_detail of this CbrPolicyDetail.
        :rtype: :class:`huaweicloudsdkbcc.v1.CbrPolicyDetailResourceDetail`
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this CbrPolicyDetail.

        :param resource_detail: The resource_detail of this CbrPolicyDetail.
        :type resource_detail: :class:`huaweicloudsdkbcc.v1.CbrPolicyDetailResourceDetail`
        """
        self._resource_detail = resource_detail

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
        if not isinstance(other, CbrPolicyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
