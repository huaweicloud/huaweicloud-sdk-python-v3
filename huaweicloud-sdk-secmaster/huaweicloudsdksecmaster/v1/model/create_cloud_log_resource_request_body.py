# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCloudLogResourceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'resources': 'list[ResourceDto]'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'resources': 'resources'
    }

    def __init__(self, domain_id=None, resources=None):
        r"""CreateCloudLogResourceRequestBody

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param resources: 资源列表
        :type resources: list[:class:`huaweicloudsdksecmaster.v1.ResourceDto`]
        """
        
        

        self._domain_id = None
        self._resources = None
        self.discriminator = None

        self.domain_id = domain_id
        self.resources = resources

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateCloudLogResourceRequestBody.

        租户ID

        :return: The domain_id of this CreateCloudLogResourceRequestBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateCloudLogResourceRequestBody.

        租户ID

        :param domain_id: The domain_id of this CreateCloudLogResourceRequestBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def resources(self):
        r"""Gets the resources of this CreateCloudLogResourceRequestBody.

        资源列表

        :return: The resources of this CreateCloudLogResourceRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ResourceDto`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this CreateCloudLogResourceRequestBody.

        资源列表

        :param resources: The resources of this CreateCloudLogResourceRequestBody.
        :type resources: list[:class:`huaweicloudsdksecmaster.v1.ResourceDto`]
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
        if not isinstance(other, CreateCloudLogResourceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
