# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowObjectUserRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object': 'str'
    }

    attribute_map = {
        'object': 'object'
    }

    def __init__(self, object=None):
        """ShowObjectUserRequest

        The model defined in huaweicloud sdk

        :param object: 授权对象，和授权接口中的object对应 \&quot;jobs.flink.flink作业ID\&quot;，查询指定的作业。 \&quot;groups.程序包组名\&quot;，查询指定的程序包组。 \&quot;resources.程序包名\&quot;，查询指定程序包。
        :type object: str
        """
        
        

        self._object = None
        self.discriminator = None

        self.object = object

    @property
    def object(self):
        """Gets the object of this ShowObjectUserRequest.

        授权对象，和授权接口中的object对应 \"jobs.flink.flink作业ID\"，查询指定的作业。 \"groups.程序包组名\"，查询指定的程序包组。 \"resources.程序包名\"，查询指定程序包。

        :return: The object of this ShowObjectUserRequest.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ShowObjectUserRequest.

        授权对象，和授权接口中的object对应 \"jobs.flink.flink作业ID\"，查询指定的作业。 \"groups.程序包组名\"，查询指定的程序包组。 \"resources.程序包名\"，查询指定程序包。

        :param object: The object of this ShowObjectUserRequest.
        :type object: str
        """
        self._object = object

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
        if not isinstance(other, ShowObjectUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
