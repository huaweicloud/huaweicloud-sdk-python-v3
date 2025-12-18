# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAvailableResourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'list[str]',
        'flavor_id': 'list[str]',
        'dec_project_id': 'list[str]',
        'check_limit': 'list[str]',
        'expectation': 'list[str]',
        'resource_type': 'list[str]'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'flavor_id': 'flavor_id',
        'dec_project_id': 'dec_project_id',
        'check_limit': 'check_limit',
        'expectation': 'expectation',
        'resource_type': 'resource_type'
    }

    def __init__(self, availability_zone=None, flavor_id=None, dec_project_id=None, check_limit=None, expectation=None, resource_type=None):
        r"""ShowAvailableResourceRequest

        The model defined in huaweicloud sdk

        :param availability_zone: 
        :type availability_zone: list[str]
        :param flavor_id: 
        :type flavor_id: list[str]
        :param dec_project_id: 
        :type dec_project_id: list[str]
        :param check_limit: 
        :type check_limit: list[str]
        :param expectation: 
        :type expectation: list[str]
        :param resource_type: 
        :type resource_type: list[str]
        """
        
        

        self._availability_zone = None
        self._flavor_id = None
        self._dec_project_id = None
        self._check_limit = None
        self._expectation = None
        self._resource_type = None
        self.discriminator = None

        self.availability_zone = availability_zone
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if dec_project_id is not None:
            self.dec_project_id = dec_project_id
        if check_limit is not None:
            self.check_limit = check_limit
        if expectation is not None:
            self.expectation = expectation
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ShowAvailableResourceRequest.

        :return: The availability_zone of this ShowAvailableResourceRequest.
        :rtype: list[str]
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ShowAvailableResourceRequest.

        :param availability_zone: The availability_zone of this ShowAvailableResourceRequest.
        :type availability_zone: list[str]
        """
        self._availability_zone = availability_zone

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ShowAvailableResourceRequest.

        :return: The flavor_id of this ShowAvailableResourceRequest.
        :rtype: list[str]
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ShowAvailableResourceRequest.

        :param flavor_id: The flavor_id of this ShowAvailableResourceRequest.
        :type flavor_id: list[str]
        """
        self._flavor_id = flavor_id

    @property
    def dec_project_id(self):
        r"""Gets the dec_project_id of this ShowAvailableResourceRequest.

        :return: The dec_project_id of this ShowAvailableResourceRequest.
        :rtype: list[str]
        """
        return self._dec_project_id

    @dec_project_id.setter
    def dec_project_id(self, dec_project_id):
        r"""Sets the dec_project_id of this ShowAvailableResourceRequest.

        :param dec_project_id: The dec_project_id of this ShowAvailableResourceRequest.
        :type dec_project_id: list[str]
        """
        self._dec_project_id = dec_project_id

    @property
    def check_limit(self):
        r"""Gets the check_limit of this ShowAvailableResourceRequest.

        :return: The check_limit of this ShowAvailableResourceRequest.
        :rtype: list[str]
        """
        return self._check_limit

    @check_limit.setter
    def check_limit(self, check_limit):
        r"""Sets the check_limit of this ShowAvailableResourceRequest.

        :param check_limit: The check_limit of this ShowAvailableResourceRequest.
        :type check_limit: list[str]
        """
        self._check_limit = check_limit

    @property
    def expectation(self):
        r"""Gets the expectation of this ShowAvailableResourceRequest.

        :return: The expectation of this ShowAvailableResourceRequest.
        :rtype: list[str]
        """
        return self._expectation

    @expectation.setter
    def expectation(self, expectation):
        r"""Sets the expectation of this ShowAvailableResourceRequest.

        :param expectation: The expectation of this ShowAvailableResourceRequest.
        :type expectation: list[str]
        """
        self._expectation = expectation

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowAvailableResourceRequest.

        :return: The resource_type of this ShowAvailableResourceRequest.
        :rtype: list[str]
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowAvailableResourceRequest.

        :param resource_type: The resource_type of this ShowAvailableResourceRequest.
        :type resource_type: list[str]
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ShowAvailableResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
