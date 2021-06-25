# coding: utf-8

import pprint
import re

import six





class IncidentOrderCCEmailInfoV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'customer_id': 'str',
        'cc_email': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'customer_id': 'customer_id',
        'cc_email': 'cc_email'
    }

    def __init__(self, user_id=None, customer_id=None, cc_email=None):
        """IncidentOrderCCEmailInfoV2 - a model defined in huaweicloud sdk"""
        
        

        self._user_id = None
        self._customer_id = None
        self._cc_email = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if customer_id is not None:
            self.customer_id = customer_id
        if cc_email is not None:
            self.cc_email = cc_email

    @property
    def user_id(self):
        """Gets the user_id of this IncidentOrderCCEmailInfoV2.

        用户id

        :return: The user_id of this IncidentOrderCCEmailInfoV2.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this IncidentOrderCCEmailInfoV2.

        用户id

        :param user_id: The user_id of this IncidentOrderCCEmailInfoV2.
        :type: str
        """
        self._user_id = user_id

    @property
    def customer_id(self):
        """Gets the customer_id of this IncidentOrderCCEmailInfoV2.

        客户id

        :return: The customer_id of this IncidentOrderCCEmailInfoV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this IncidentOrderCCEmailInfoV2.

        客户id

        :param customer_id: The customer_id of this IncidentOrderCCEmailInfoV2.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def cc_email(self):
        """Gets the cc_email of this IncidentOrderCCEmailInfoV2.

        操作邮箱

        :return: The cc_email of this IncidentOrderCCEmailInfoV2.
        :rtype: str
        """
        return self._cc_email

    @cc_email.setter
    def cc_email(self, cc_email):
        """Sets the cc_email of this IncidentOrderCCEmailInfoV2.

        操作邮箱

        :param cc_email: The cc_email of this IncidentOrderCCEmailInfoV2.
        :type: str
        """
        self._cc_email = cc_email

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
        if not isinstance(other, IncidentOrderCCEmailInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other