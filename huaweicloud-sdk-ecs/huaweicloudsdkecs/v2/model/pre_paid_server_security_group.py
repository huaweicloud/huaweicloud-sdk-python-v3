# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidServerSecurityGroup:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str'
    }

    attribute_map = {
        'id': 'id'
    }

    def __init__(self, id=None):
        """PrePaidServerSecurityGroup - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self.discriminator = None

        if id is not None:
            self.id = id

    @property
    def id(self):
        """Gets the id of this PrePaidServerSecurityGroup.

        可以为空，待创建云服务器的安全组，会对创建云服务器中配置的网卡生效。需要指定已有安全组的ID，UUID格式；若不传值，底层会按照空处理，不会创建安全组。

        :return: The id of this PrePaidServerSecurityGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrePaidServerSecurityGroup.

        可以为空，待创建云服务器的安全组，会对创建云服务器中配置的网卡生效。需要指定已有安全组的ID，UUID格式；若不传值，底层会按照空处理，不会创建安全组。

        :param id: The id of this PrePaidServerSecurityGroup.
        :type: str
        """
        self._id = id

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PrePaidServerSecurityGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
