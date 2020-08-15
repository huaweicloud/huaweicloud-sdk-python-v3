# coding: utf-8

import pprint
import re

import six





class SignBindingReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sign_id': 'str',
        'publish_ids': 'list[str]'
    }

    attribute_map = {
        'sign_id': 'sign_id',
        'publish_ids': 'publish_ids'
    }

    def __init__(self, sign_id=None, publish_ids=None):
        """SignBindingReq - a model defined in huaweicloud sdk"""
        
        

        self._sign_id = None
        self._publish_ids = None
        self.discriminator = None

        self.sign_id = sign_id
        self.publish_ids = publish_ids

    @property
    def sign_id(self):
        """Gets the sign_id of this SignBindingReq.

        签名密钥编号

        :return: The sign_id of this SignBindingReq.
        :rtype: str
        """
        return self._sign_id

    @sign_id.setter
    def sign_id(self, sign_id):
        """Sets the sign_id of this SignBindingReq.

        签名密钥编号

        :param sign_id: The sign_id of this SignBindingReq.
        :type: str
        """
        self._sign_id = sign_id

    @property
    def publish_ids(self):
        """Gets the publish_ids of this SignBindingReq.

        API的发布记录编号

        :return: The publish_ids of this SignBindingReq.
        :rtype: list[str]
        """
        return self._publish_ids

    @publish_ids.setter
    def publish_ids(self, publish_ids):
        """Sets the publish_ids of this SignBindingReq.

        API的发布记录编号

        :param publish_ids: The publish_ids of this SignBindingReq.
        :type: list[str]
        """
        self._publish_ids = publish_ids

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
        if not isinstance(other, SignBindingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
