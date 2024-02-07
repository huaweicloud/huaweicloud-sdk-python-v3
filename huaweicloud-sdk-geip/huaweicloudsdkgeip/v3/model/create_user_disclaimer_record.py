# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUserDisclaimerRecord:

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
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, domain_id=None, created_at=None, updated_at=None):
        """CreateUserDisclaimerRecord

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._domain_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateUserDisclaimerRecord.

        租户ID

        :return: The domain_id of this CreateUserDisclaimerRecord.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateUserDisclaimerRecord.

        租户ID

        :param domain_id: The domain_id of this CreateUserDisclaimerRecord.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def created_at(self):
        """Gets the created_at of this CreateUserDisclaimerRecord.

        创建时间

        :return: The created_at of this CreateUserDisclaimerRecord.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateUserDisclaimerRecord.

        创建时间

        :param created_at: The created_at of this CreateUserDisclaimerRecord.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateUserDisclaimerRecord.

        更新时间

        :return: The updated_at of this CreateUserDisclaimerRecord.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateUserDisclaimerRecord.

        更新时间

        :param updated_at: The updated_at of this CreateUserDisclaimerRecord.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, CreateUserDisclaimerRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
