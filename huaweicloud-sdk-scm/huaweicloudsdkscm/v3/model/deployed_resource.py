# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployedResource:

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
        'type': 'str',
        'domain_name': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, type=None, domain_name=None, enterprise_project_id=None):
        """DeployedResource

        The model defined in huaweicloud sdk

        :param id: 资源Id,部署WAF与ELB时，必传此字段。
        :type id: str
        :param type: 资源类型，当前仅部署WAF资源时需传入，即独享模式（premium）与云模式（cloud）。
        :type type: str
        :param domain_name: 需部署的域名，当前仅部署CDN时需传入，即需加速的域名，域名与证书必须可匹配。
        :type domain_name: str
        :param enterprise_project_id: 需部署的资源所属的企业项目ID，当前仅部署WAF资源时，需传入。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._type = None
        self._domain_name = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if domain_name is not None:
            self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this DeployedResource.

        资源Id,部署WAF与ELB时，必传此字段。

        :return: The id of this DeployedResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeployedResource.

        资源Id,部署WAF与ELB时，必传此字段。

        :param id: The id of this DeployedResource.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this DeployedResource.

        资源类型，当前仅部署WAF资源时需传入，即独享模式（premium）与云模式（cloud）。

        :return: The type of this DeployedResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeployedResource.

        资源类型，当前仅部署WAF资源时需传入，即独享模式（premium）与云模式（cloud）。

        :param type: The type of this DeployedResource.
        :type type: str
        """
        self._type = type

    @property
    def domain_name(self):
        """Gets the domain_name of this DeployedResource.

        需部署的域名，当前仅部署CDN时需传入，即需加速的域名，域名与证书必须可匹配。

        :return: The domain_name of this DeployedResource.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DeployedResource.

        需部署的域名，当前仅部署CDN时需传入，即需加速的域名，域名与证书必须可匹配。

        :param domain_name: The domain_name of this DeployedResource.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DeployedResource.

        需部署的资源所属的企业项目ID，当前仅部署WAF资源时，需传入。

        :return: The enterprise_project_id of this DeployedResource.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DeployedResource.

        需部署的资源所属的企业项目ID，当前仅部署WAF资源时，需传入。

        :param enterprise_project_id: The enterprise_project_id of this DeployedResource.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, DeployedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
