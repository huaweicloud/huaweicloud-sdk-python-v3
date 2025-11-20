# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantAssginRecordResponse(SdkResponse):

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
        'resources_overview': 'list[AllocateSpResourceSummaryInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'customer_project_id': 'customer_project_id',
        'customer_name': 'customer_name',
        'region_id': 'region_id',
        'resource_count': 'resource_count',
        'resources': 'resources',
        'resources_overview': 'resources_overview',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, customer_project_id=None, customer_name=None, region_id=None, resource_count=None, resources=None, resources_overview=None, x_request_id=None):
        r"""ShowTenantAssginRecordResponse

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
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._customer_project_id = None
        self._customer_name = None
        self._region_id = None
        self._resource_count = None
        self._resources = None
        self._resources_overview = None
        self._x_request_id = None
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
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def customer_project_id(self):
        r"""Gets the customer_project_id of this ShowTenantAssginRecordResponse.

        租户ID

        :return: The customer_project_id of this ShowTenantAssginRecordResponse.
        :rtype: str
        """
        return self._customer_project_id

    @customer_project_id.setter
    def customer_project_id(self, customer_project_id):
        r"""Sets the customer_project_id of this ShowTenantAssginRecordResponse.

        租户ID

        :param customer_project_id: The customer_project_id of this ShowTenantAssginRecordResponse.
        :type customer_project_id: str
        """
        self._customer_project_id = customer_project_id

    @property
    def customer_name(self):
        r"""Gets the customer_name of this ShowTenantAssginRecordResponse.

        被关联租户的名称。

        :return: The customer_name of this ShowTenantAssginRecordResponse.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        r"""Sets the customer_name of this ShowTenantAssginRecordResponse.

        被关联租户的名称。

        :param customer_name: The customer_name of this ShowTenantAssginRecordResponse.
        :type customer_name: str
        """
        self._customer_name = customer_name

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowTenantAssginRecordResponse.

        租户的可用区。

        :return: The region_id of this ShowTenantAssginRecordResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowTenantAssginRecordResponse.

        租户的可用区。

        :param region_id: The region_id of this ShowTenantAssginRecordResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_count(self):
        r"""Gets the resource_count of this ShowTenantAssginRecordResponse.

        分配表记录总数，用于分页。

        :return: The resource_count of this ShowTenantAssginRecordResponse.
        :rtype: int
        """
        return self._resource_count

    @resource_count.setter
    def resource_count(self, resource_count):
        r"""Sets the resource_count of this ShowTenantAssginRecordResponse.

        分配表记录总数，用于分页。

        :param resource_count: The resource_count of this ShowTenantAssginRecordResponse.
        :type resource_count: int
        """
        self._resource_count = resource_count

    @property
    def resources(self):
        r"""Gets the resources of this ShowTenantAssginRecordResponse.

        分配给租户的资源。

        :return: The resources of this ShowTenantAssginRecordResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AllocateSpResourceInfo`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ShowTenantAssginRecordResponse.

        分配给租户的资源。

        :param resources: The resources of this ShowTenantAssginRecordResponse.
        :type resources: list[:class:`huaweicloudsdkmetastudio.v1.AllocateSpResourceInfo`]
        """
        self._resources = resources

    @property
    def resources_overview(self):
        r"""Gets the resources_overview of this ShowTenantAssginRecordResponse.

        分配给租户的资源总览。

        :return: The resources_overview of this ShowTenantAssginRecordResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AllocateSpResourceSummaryInfo`]
        """
        return self._resources_overview

    @resources_overview.setter
    def resources_overview(self, resources_overview):
        r"""Sets the resources_overview of this ShowTenantAssginRecordResponse.

        分配给租户的资源总览。

        :param resources_overview: The resources_overview of this ShowTenantAssginRecordResponse.
        :type resources_overview: list[:class:`huaweicloudsdkmetastudio.v1.AllocateSpResourceSummaryInfo`]
        """
        self._resources_overview = resources_overview

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowTenantAssginRecordResponse.

        :return: The x_request_id of this ShowTenantAssginRecordResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowTenantAssginRecordResponse.

        :param x_request_id: The x_request_id of this ShowTenantAssginRecordResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowTenantAssginRecordResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowTenantAssginRecordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
