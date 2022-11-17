# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignApiBinding:

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
        """SignApiBinding

        The model defined in huaweicloud sdk

        :param sign_id: 签名密钥编号
        :type sign_id: str
        :param publish_ids: API的发布记录编号
        :type publish_ids: list[str]
        """
        
        

        self._sign_id = None
        self._publish_ids = None
        self.discriminator = None

        self.sign_id = sign_id
        self.publish_ids = publish_ids

    @property
    def sign_id(self):
        """Gets the sign_id of this SignApiBinding.

        签名密钥编号

        :return: The sign_id of this SignApiBinding.
        :rtype: str
        """
        return self._sign_id

    @sign_id.setter
    def sign_id(self, sign_id):
        """Sets the sign_id of this SignApiBinding.

        签名密钥编号

        :param sign_id: The sign_id of this SignApiBinding.
        :type sign_id: str
        """
        self._sign_id = sign_id

    @property
    def publish_ids(self):
        """Gets the publish_ids of this SignApiBinding.

        API的发布记录编号

        :return: The publish_ids of this SignApiBinding.
        :rtype: list[str]
        """
        return self._publish_ids

    @publish_ids.setter
    def publish_ids(self, publish_ids):
        """Sets the publish_ids of this SignApiBinding.

        API的发布记录编号

        :param publish_ids: The publish_ids of this SignApiBinding.
        :type publish_ids: list[str]
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
        if not isinstance(other, SignApiBinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
