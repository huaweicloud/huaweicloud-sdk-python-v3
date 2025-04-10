# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_name': 'str',
        'project_id': 'str',
        'domain_id': 'str',
        'domain_name': 'str'
    }

    attribute_map = {
        'project_name': 'project_name',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name'
    }

    def __init__(self, project_name=None, project_id=None, domain_id=None, domain_name=None):
        r"""ShowDomainResponse

        The model defined in huaweicloud sdk

        :param project_name: 
        :type project_name: str
        :param project_id: 
        :type project_id: str
        :param domain_id: 
        :type domain_id: str
        :param domain_name: 
        :type domain_name: str
        """
        
        super(ShowDomainResponse, self).__init__()

        self._project_name = None
        self._project_id = None
        self._domain_id = None
        self._domain_name = None
        self.discriminator = None

        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def project_name(self):
        r"""Gets the project_name of this ShowDomainResponse.

        

        :return: The project_name of this ShowDomainResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ShowDomainResponse.

        

        :param project_name: The project_name of this ShowDomainResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowDomainResponse.

        

        :return: The project_id of this ShowDomainResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowDomainResponse.

        

        :param project_id: The project_id of this ShowDomainResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowDomainResponse.

        

        :return: The domain_id of this ShowDomainResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowDomainResponse.

        

        :param domain_id: The domain_id of this ShowDomainResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainResponse.

        

        :return: The domain_name of this ShowDomainResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainResponse.

        

        :param domain_name: The domain_name of this ShowDomainResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, ShowDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
