# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JoinRequestSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'name': 'str',
        'email': 'str',
        'organization': 'str',
        'phone_number': 'str',
        'invitation_code': 'str'
    }

    attribute_map = {
        'region': 'region',
        'name': 'name',
        'email': 'email',
        'organization': 'organization',
        'phone_number': 'phone_number',
        'invitation_code': 'invitation_code'
    }

    def __init__(self, region=None, name=None, email=None, organization=None, phone_number=None, invitation_code=None):
        """JoinRequestSchema

        The model defined in huaweicloud sdk

        :param region: the region of user
        :type region: str
        :param name: the name of user
        :type name: str
        :param email: the email of user
        :type email: str
        :param organization: the organization of user
        :type organization: str
        :param phone_number: the phone_number of user
        :type phone_number: str
        :param invitation_code: the invitation_code
        :type invitation_code: str
        """
        
        

        self._region = None
        self._name = None
        self._email = None
        self._organization = None
        self._phone_number = None
        self._invitation_code = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if organization is not None:
            self.organization = organization
        if phone_number is not None:
            self.phone_number = phone_number
        if invitation_code is not None:
            self.invitation_code = invitation_code

    @property
    def region(self):
        """Gets the region of this JoinRequestSchema.

        the region of user

        :return: The region of this JoinRequestSchema.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this JoinRequestSchema.

        the region of user

        :param region: The region of this JoinRequestSchema.
        :type region: str
        """
        self._region = region

    @property
    def name(self):
        """Gets the name of this JoinRequestSchema.

        the name of user

        :return: The name of this JoinRequestSchema.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JoinRequestSchema.

        the name of user

        :param name: The name of this JoinRequestSchema.
        :type name: str
        """
        self._name = name

    @property
    def email(self):
        """Gets the email of this JoinRequestSchema.

        the email of user

        :return: The email of this JoinRequestSchema.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this JoinRequestSchema.

        the email of user

        :param email: The email of this JoinRequestSchema.
        :type email: str
        """
        self._email = email

    @property
    def organization(self):
        """Gets the organization of this JoinRequestSchema.

        the organization of user

        :return: The organization of this JoinRequestSchema.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this JoinRequestSchema.

        the organization of user

        :param organization: The organization of this JoinRequestSchema.
        :type organization: str
        """
        self._organization = organization

    @property
    def phone_number(self):
        """Gets the phone_number of this JoinRequestSchema.

        the phone_number of user

        :return: The phone_number of this JoinRequestSchema.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this JoinRequestSchema.

        the phone_number of user

        :param phone_number: The phone_number of this JoinRequestSchema.
        :type phone_number: str
        """
        self._phone_number = phone_number

    @property
    def invitation_code(self):
        """Gets the invitation_code of this JoinRequestSchema.

        the invitation_code

        :return: The invitation_code of this JoinRequestSchema.
        :rtype: str
        """
        return self._invitation_code

    @invitation_code.setter
    def invitation_code(self, invitation_code):
        """Sets the invitation_code of this JoinRequestSchema.

        the invitation_code

        :param invitation_code: The invitation_code of this JoinRequestSchema.
        :type invitation_code: str
        """
        self._invitation_code = invitation_code

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
        if not isinstance(other, JoinRequestSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
