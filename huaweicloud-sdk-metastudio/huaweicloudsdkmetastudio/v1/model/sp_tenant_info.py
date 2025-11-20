# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpTenantInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_project_id': 'str',
        'customer_name': 'str',
        'region_id': 'str',
        'resource_count': 'int',
        'resources': 'list[AllocateSpResourceInfo]',
        'resources_overview': 'list[AllocateSpResourceSummaryInfo]'
    }

    attribute_map = {
        'customer_project_id': 'customer_project_id',
        'customer_name': 'customer_name',
        'region_id': 'region_id',
        'resource_count': 'resource_count',
        'resources': 'resources',
        'resources_overview': 'resources_overview'
    }

    def __init__(self, customer_project_id=None, customer_name=None, region_id=None, resource_count=None, resources=None, resources_overview=None):
        r"""SpTenantInfo

        The model defined in huaweicloud sdk

        :param customer_project_id: 租户ID
        :type customer_project_id: str
        :param customer_name: 被关联租户的名称。
        :type customer_name: str
        :param region_id: 租户的可用区。
        :type region_id: str
        :param resource_count: 分配表记录总数，用于分页。
        :type resource_count: int
        :param resources: 分配给租户的资源。
        :type resources: list[:class:`huaweicloudsdkmetastudio.v1.AllocateSpResourceInfo`]
        :param resources_overview: 分配给租户的资源总览。
        :type resources_overview: list[:class:`huaweicloudsdkmetastudio.v1.AllocateSpResourceSummaryInfo`]
        """
        
        

        self._customer_project_id = None
        self._customer_name = None
        self._region_id = None
        self._resource_count = None
        self._resources = None
        self._resources_overview = None
        self.discriminator = None

        if customer_project_id is not None:
            self.customer_project_id = customer_project_id
        if customer_name is not None:
            self.customer_name = customer_name
        if region_id is not None:
            self.region_id = region_id
        if resource_count is not None:
            self.resource_count = resource_count
        if resources is not None:
            self.resources = resources
        if resources_overview is not None:
            self.resources_overview = resources_overview

    @property
    def customer_project_id(self):
        r"""Gets the customer_project_id of this SpTenantInfo.

        租户ID

        :return: The customer_project_id of this SpTenantInfo.
        :rtype: str
        """
        return self._customer_project_id

    @customer_project_id.setter
    def customer_project_id(self, customer_project_id):
        r"""Sets the customer_project_id of this SpTenantInfo.

        租户ID

        :param customer_project_id: The customer_project_id of this SpTenantInfo.
        :type customer_project_id: str
        """
        self._customer_project_id = customer_project_id

    @property
    def customer_name(self):
        r"""Gets the customer_name of this SpTenantInfo.

        被关联租户的名称。

        :return: The customer_name of this SpTenantInfo.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        r"""Sets the customer_name of this SpTenantInfo.

        被关联租户的名称。

        :param customer_name: The customer_name of this SpTenantInfo.
        :type customer_name: str
        """
        self._customer_name = customer_name

    @property
    def region_id(self):
        r"""Gets the region_id of this SpTenantInfo.

        租户的可用区。

        :return: The region_id of this SpTenantInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this SpTenantInfo.

        租户的可用区。

        :param region_id: The region_id of this SpTenantInfo.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_count(self):
        r"""Gets the resource_count of this SpTenantInfo.

        分配表记录总数，用于分页。

        :return: The resource_count of this SpTenantInfo.
        :rtype: int
        """
        return self._resource_count

    @resource_count.setter
    def resource_count(self, resource_count):
        r"""Sets the resource_count of this SpTenantInfo.

        分配表记录总数，用于分页。

        :param resource_count: The resource_count of this SpTenantInfo.
        :type resource_count: int
        """
        self._resource_count = resource_count

    @property
    def resources(self):
        r"""Gets the resources of this SpTenantInfo.

        分配给租户的资源。

        :return: The resources of this SpTenantInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AllocateSpResourceInfo`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this SpTenantInfo.

        分配给租户的资源。

        :param resources: The resources of this SpTenantInfo.
        :type resources: list[:class:`huaweicloudsdkmetastudio.v1.AllocateSpResourceInfo`]
        """
        self._resources = resources

    @property
    def resources_overview(self):
        r"""Gets the resources_overview of this SpTenantInfo.

        分配给租户的资源总览。

        :return: The resources_overview of this SpTenantInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AllocateSpResourceSummaryInfo`]
        """
        return self._resources_overview

    @resources_overview.setter
    def resources_overview(self, resources_overview):
        r"""Sets the resources_overview of this SpTenantInfo.

        分配给租户的资源总览。

        :param resources_overview: The resources_overview of this SpTenantInfo.
        :type resources_overview: list[:class:`huaweicloudsdkmetastudio.v1.AllocateSpResourceSummaryInfo`]
        """
        self._resources_overview = resources_overview

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
        if not isinstance(other, SpTenantInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
