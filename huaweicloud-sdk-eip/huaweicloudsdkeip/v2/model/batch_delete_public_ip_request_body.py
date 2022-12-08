# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeletePublicIpRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_ids': 'list[str]'
    }

    attribute_map = {
        'publicip_ids': 'publicip_ids'
    }

    def __init__(self, publicip_ids=None):
        """BatchDeletePublicIpRequestBody

        The model defined in huaweicloud sdk

        :param publicip_ids: 弹性公网ip的id列表。
        :type publicip_ids: list[str]
        """
        
        

        self._publicip_ids = None
        self.discriminator = None

        self.publicip_ids = publicip_ids

    @property
    def publicip_ids(self):
        """Gets the publicip_ids of this BatchDeletePublicIpRequestBody.

        弹性公网ip的id列表。

        :return: The publicip_ids of this BatchDeletePublicIpRequestBody.
        :rtype: list[str]
        """
        return self._publicip_ids

    @publicip_ids.setter
    def publicip_ids(self, publicip_ids):
        """Sets the publicip_ids of this BatchDeletePublicIpRequestBody.

        弹性公网ip的id列表。

        :param publicip_ids: The publicip_ids of this BatchDeletePublicIpRequestBody.
        :type publicip_ids: list[str]
        """
        self._publicip_ids = publicip_ids

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
        if not isinstance(other, BatchDeletePublicIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
