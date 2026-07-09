# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceEnvironment:

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
        'ep_id': 'str',
        'ep_name': 'str',
        'project_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'ep_id': 'ep_id',
        'ep_name': 'ep_name',
        'project_id': 'project_id',
        'region_id': 'region_id'
    }

    def __init__(self, domain_id=None, ep_id=None, ep_name=None, project_id=None, region_id=None):
        r"""ResourceEnvironment

        The model defined in huaweicloud sdk

        :param domain_id: 账户ID
        :type domain_id: str
        :param ep_id: 企业项目ID
        :type ep_id: str
        :param ep_name: 企业项目名称
        :type ep_name: str
        :param project_id: 项目ID
        :type project_id: str
        :param region_id: regionID
        :type region_id: str
        """
        
        

        self._domain_id = None
        self._ep_id = None
        self._ep_name = None
        self._project_id = None
        self._region_id = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if ep_id is not None:
            self.ep_id = ep_id
        if ep_name is not None:
            self.ep_name = ep_name
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ResourceEnvironment.

        账户ID

        :return: The domain_id of this ResourceEnvironment.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ResourceEnvironment.

        账户ID

        :param domain_id: The domain_id of this ResourceEnvironment.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ResourceEnvironment.

        企业项目ID

        :return: The ep_id of this ResourceEnvironment.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ResourceEnvironment.

        企业项目ID

        :param ep_id: The ep_id of this ResourceEnvironment.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def ep_name(self):
        r"""Gets the ep_name of this ResourceEnvironment.

        企业项目名称

        :return: The ep_name of this ResourceEnvironment.
        :rtype: str
        """
        return self._ep_name

    @ep_name.setter
    def ep_name(self, ep_name):
        r"""Sets the ep_name of this ResourceEnvironment.

        企业项目名称

        :param ep_name: The ep_name of this ResourceEnvironment.
        :type ep_name: str
        """
        self._ep_name = ep_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ResourceEnvironment.

        项目ID

        :return: The project_id of this ResourceEnvironment.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ResourceEnvironment.

        项目ID

        :param project_id: The project_id of this ResourceEnvironment.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceEnvironment.

        regionID

        :return: The region_id of this ResourceEnvironment.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceEnvironment.

        regionID

        :param region_id: The region_id of this ResourceEnvironment.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, ResourceEnvironment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
