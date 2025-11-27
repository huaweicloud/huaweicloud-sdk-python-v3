# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFederationCertRequestBody:

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
        'vpc_id': 'str',
        'subnet_id': 'str',
        'duration': 'int'
    }

    attribute_map = {
        'project_id': 'projectID',
        'vpc_id': 'vpcID',
        'subnet_id': 'subnetID',
        'duration': 'duration'
    }

    def __init__(self, project_id=None, vpc_id=None, subnet_id=None, duration=None):
        r"""CreateFederationCertRequestBody

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param vpc_id: VPC id，必须属于上述项目
        :type vpc_id: str
        :param subnet_id: 子网id，必须属于上述vpc
        :type subnet_id: str
        :param duration: kubeconfig证书有效期，单位为天
        :type duration: int
        """
        
        

        self._project_id = None
        self._vpc_id = None
        self._subnet_id = None
        self._duration = None
        self.discriminator = None

        self.project_id = project_id
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.duration = duration

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateFederationCertRequestBody.

        项目id

        :return: The project_id of this CreateFederationCertRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateFederationCertRequestBody.

        项目id

        :param project_id: The project_id of this CreateFederationCertRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateFederationCertRequestBody.

        VPC id，必须属于上述项目

        :return: The vpc_id of this CreateFederationCertRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateFederationCertRequestBody.

        VPC id，必须属于上述项目

        :param vpc_id: The vpc_id of this CreateFederationCertRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateFederationCertRequestBody.

        子网id，必须属于上述vpc

        :return: The subnet_id of this CreateFederationCertRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateFederationCertRequestBody.

        子网id，必须属于上述vpc

        :param subnet_id: The subnet_id of this CreateFederationCertRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def duration(self):
        r"""Gets the duration of this CreateFederationCertRequestBody.

        kubeconfig证书有效期，单位为天

        :return: The duration of this CreateFederationCertRequestBody.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this CreateFederationCertRequestBody.

        kubeconfig证书有效期，单位为天

        :param duration: The duration of this CreateFederationCertRequestBody.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, CreateFederationCertRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
