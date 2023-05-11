# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRepoDomainsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_domain': 'str',
        'permit': 'str',
        'deadline': 'str',
        'description': 'str'
    }

    attribute_map = {
        'access_domain': 'access_domain',
        'permit': 'permit',
        'deadline': 'deadline',
        'description': 'description'
    }

    def __init__(self, access_domain=None, permit=None, deadline=None, description=None):
        """CreateRepoDomainsRequestBody

        The model defined in huaweicloud sdk

        :param access_domain: 共享租户名称
        :type access_domain: str
        :param permit: 当前只支持read权限
        :type permit: str
        :param deadline: 截止时间，UTC时间格式。永久有效为forever
        :type deadline: str
        :param description: 描述
        :type description: str
        """
        
        

        self._access_domain = None
        self._permit = None
        self._deadline = None
        self._description = None
        self.discriminator = None

        self.access_domain = access_domain
        self.permit = permit
        self.deadline = deadline
        if description is not None:
            self.description = description

    @property
    def access_domain(self):
        """Gets the access_domain of this CreateRepoDomainsRequestBody.

        共享租户名称

        :return: The access_domain of this CreateRepoDomainsRequestBody.
        :rtype: str
        """
        return self._access_domain

    @access_domain.setter
    def access_domain(self, access_domain):
        """Sets the access_domain of this CreateRepoDomainsRequestBody.

        共享租户名称

        :param access_domain: The access_domain of this CreateRepoDomainsRequestBody.
        :type access_domain: str
        """
        self._access_domain = access_domain

    @property
    def permit(self):
        """Gets the permit of this CreateRepoDomainsRequestBody.

        当前只支持read权限

        :return: The permit of this CreateRepoDomainsRequestBody.
        :rtype: str
        """
        return self._permit

    @permit.setter
    def permit(self, permit):
        """Sets the permit of this CreateRepoDomainsRequestBody.

        当前只支持read权限

        :param permit: The permit of this CreateRepoDomainsRequestBody.
        :type permit: str
        """
        self._permit = permit

    @property
    def deadline(self):
        """Gets the deadline of this CreateRepoDomainsRequestBody.

        截止时间，UTC时间格式。永久有效为forever

        :return: The deadline of this CreateRepoDomainsRequestBody.
        :rtype: str
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this CreateRepoDomainsRequestBody.

        截止时间，UTC时间格式。永久有效为forever

        :param deadline: The deadline of this CreateRepoDomainsRequestBody.
        :type deadline: str
        """
        self._deadline = deadline

    @property
    def description(self):
        """Gets the description of this CreateRepoDomainsRequestBody.

        描述

        :return: The description of this CreateRepoDomainsRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRepoDomainsRequestBody.

        描述

        :param description: The description of this CreateRepoDomainsRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateRepoDomainsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
