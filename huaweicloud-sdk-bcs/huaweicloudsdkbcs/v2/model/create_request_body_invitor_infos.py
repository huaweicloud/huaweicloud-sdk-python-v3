# coding: utf-8

import pprint
import re

import six





class CreateRequestBodyInvitorInfos:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'project_id': 'str',
        'blockchain_id': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'blockchain_id': 'blockchain_id'
    }

    def __init__(self, tenant_id=None, project_id=None, blockchain_id=None):
        """CreateRequestBodyInvitorInfos - a model defined in huaweicloud sdk"""
        
        

        self._tenant_id = None
        self._project_id = None
        self._blockchain_id = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if project_id is not None:
            self.project_id = project_id
        if blockchain_id is not None:
            self.blockchain_id = blockchain_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateRequestBodyInvitorInfos.

        邀请方租户ID

        :return: The tenant_id of this CreateRequestBodyInvitorInfos.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateRequestBodyInvitorInfos.

        邀请方租户ID

        :param tenant_id: The tenant_id of this CreateRequestBodyInvitorInfos.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateRequestBodyInvitorInfos.

        邀请方项目ID

        :return: The project_id of this CreateRequestBodyInvitorInfos.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateRequestBodyInvitorInfos.

        邀请方项目ID

        :param project_id: The project_id of this CreateRequestBodyInvitorInfos.
        :type: str
        """
        self._project_id = project_id

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this CreateRequestBodyInvitorInfos.

        邀请方服务实例ID

        :return: The blockchain_id of this CreateRequestBodyInvitorInfos.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this CreateRequestBodyInvitorInfos.

        邀请方服务实例ID

        :param blockchain_id: The blockchain_id of this CreateRequestBodyInvitorInfos.
        :type: str
        """
        self._blockchain_id = blockchain_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRequestBodyInvitorInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
