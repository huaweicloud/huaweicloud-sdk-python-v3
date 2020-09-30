# coding: utf-8

import pprint
import re

import six





class RemovePublicipInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publicip_type': 'str',
        'publicip_id': 'str'
    }

    attribute_map = {
        'publicip_type': 'publicip_type',
        'publicip_id': 'publicip_id'
    }

    def __init__(self, publicip_type=None, publicip_id=None):
        """RemovePublicipInfo - a model defined in huaweicloud sdk"""
        
        

        self._publicip_type = None
        self._publicip_id = None
        self.discriminator = None

        if publicip_type is not None:
            self.publicip_type = publicip_type
        self.publicip_id = publicip_id

    @property
    def publicip_type(self):
        """Gets the publicip_type of this RemovePublicipInfo.

        功能说明：若publicip_id为弹性公网IP的id，则该字段可自动忽略。若publicip_id为IPv6端口PORT的id，则该字段必填：5_dualStack(目前仅北京4局点支持)

        :return: The publicip_type of this RemovePublicipInfo.
        :rtype: str
        """
        return self._publicip_type

    @publicip_type.setter
    def publicip_type(self, publicip_type):
        """Sets the publicip_type of this RemovePublicipInfo.

        功能说明：若publicip_id为弹性公网IP的id，则该字段可自动忽略。若publicip_id为IPv6端口PORT的id，则该字段必填：5_dualStack(目前仅北京4局点支持)

        :param publicip_type: The publicip_type of this RemovePublicipInfo.
        :type: str
        """
        self._publicip_type = publicip_type

    @property
    def publicip_id(self):
        """Gets the publicip_id of this RemovePublicipInfo.

        功能说明：带宽对应的弹性公网IP或IPv6端口PORT的唯一标识

        :return: The publicip_id of this RemovePublicipInfo.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this RemovePublicipInfo.

        功能说明：带宽对应的弹性公网IP或IPv6端口PORT的唯一标识

        :param publicip_id: The publicip_id of this RemovePublicipInfo.
        :type: str
        """
        self._publicip_id = publicip_id

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
        if not isinstance(other, RemovePublicipInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
