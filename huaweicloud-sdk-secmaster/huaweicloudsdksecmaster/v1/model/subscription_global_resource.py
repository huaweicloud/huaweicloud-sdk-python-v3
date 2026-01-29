# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionGlobalResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'region_id': 'str',
        'resources': 'list[SubscriptionResourceInfo]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'region_id': 'region_id',
        'resources': 'resources'
    }

    def __init__(self, project_id=None, region_id=None, resources=None):
        r"""SubscriptionGlobalResource

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param region_id: 当前region编码，默认为null，即为当前region
        :type region_id: str
        :param resources: 当前demo-regionon已购资源列表
        :type resources: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionResourceInfo`]
        """
        
        

        self._project_id = None
        self._region_id = None
        self._resources = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id
        if resources is not None:
            self.resources = resources

    @property
    def project_id(self):
        r"""Gets the project_id of this SubscriptionGlobalResource.

        项目ID

        :return: The project_id of this SubscriptionGlobalResource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SubscriptionGlobalResource.

        项目ID

        :param project_id: The project_id of this SubscriptionGlobalResource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this SubscriptionGlobalResource.

        当前region编码，默认为null，即为当前region

        :return: The region_id of this SubscriptionGlobalResource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this SubscriptionGlobalResource.

        当前region编码，默认为null，即为当前region

        :param region_id: The region_id of this SubscriptionGlobalResource.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resources(self):
        r"""Gets the resources of this SubscriptionGlobalResource.

        当前demo-regionon已购资源列表

        :return: The resources of this SubscriptionGlobalResource.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionResourceInfo`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this SubscriptionGlobalResource.

        当前demo-regionon已购资源列表

        :param resources: The resources of this SubscriptionGlobalResource.
        :type resources: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionResourceInfo`]
        """
        self._resources = resources

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
        if not isinstance(other, SubscriptionGlobalResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
