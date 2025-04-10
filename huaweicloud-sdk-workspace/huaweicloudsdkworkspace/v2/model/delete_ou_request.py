# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteOuRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ou_id': 'str'
    }

    attribute_map = {
        'ou_id': 'ou_id'
    }

    def __init__(self, ou_id=None):
        r"""DeleteOuRequest

        The model defined in huaweicloud sdk

        :param ou_id: OU的id。
        :type ou_id: str
        """
        
        

        self._ou_id = None
        self.discriminator = None

        self.ou_id = ou_id

    @property
    def ou_id(self):
        r"""Gets the ou_id of this DeleteOuRequest.

        OU的id。

        :return: The ou_id of this DeleteOuRequest.
        :rtype: str
        """
        return self._ou_id

    @ou_id.setter
    def ou_id(self, ou_id):
        r"""Sets the ou_id of this DeleteOuRequest.

        OU的id。

        :param ou_id: The ou_id of this DeleteOuRequest.
        :type ou_id: str
        """
        self._ou_id = ou_id

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
        if not isinstance(other, DeleteOuRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
