# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePublicipTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_id': 'str',
        'key': 'str'
    }

    attribute_map = {
        'publicip_id': 'publicip_id',
        'key': 'key'
    }

    def __init__(self, publicip_id=None, key=None):
        """DeletePublicipTagRequest

        The model defined in huaweicloud sdk

        :param publicip_id: 弹性公网IP的id
        :type publicip_id: str
        :param key: 标签的键
        :type key: str
        """
        
        

        self._publicip_id = None
        self._key = None
        self.discriminator = None

        self.publicip_id = publicip_id
        self.key = key

    @property
    def publicip_id(self):
        """Gets the publicip_id of this DeletePublicipTagRequest.

        弹性公网IP的id

        :return: The publicip_id of this DeletePublicipTagRequest.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this DeletePublicipTagRequest.

        弹性公网IP的id

        :param publicip_id: The publicip_id of this DeletePublicipTagRequest.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def key(self):
        """Gets the key of this DeletePublicipTagRequest.

        标签的键

        :return: The key of this DeletePublicipTagRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeletePublicipTagRequest.

        标签的键

        :param key: The key of this DeletePublicipTagRequest.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, DeletePublicipTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
