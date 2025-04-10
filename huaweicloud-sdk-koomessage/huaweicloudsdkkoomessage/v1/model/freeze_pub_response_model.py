# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FreezePubResponseModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pub_id': 'str'
    }

    attribute_map = {
        'pub_id': 'pub_id'
    }

    def __init__(self, pub_id=None):
        r"""FreezePubResponseModel

        The model defined in huaweicloud sdk

        :param pub_id: 服务号ID。
        :type pub_id: str
        """
        
        

        self._pub_id = None
        self.discriminator = None

        if pub_id is not None:
            self.pub_id = pub_id

    @property
    def pub_id(self):
        r"""Gets the pub_id of this FreezePubResponseModel.

        服务号ID。

        :return: The pub_id of this FreezePubResponseModel.
        :rtype: str
        """
        return self._pub_id

    @pub_id.setter
    def pub_id(self, pub_id):
        r"""Sets the pub_id of this FreezePubResponseModel.

        服务号ID。

        :param pub_id: The pub_id of this FreezePubResponseModel.
        :type pub_id: str
        """
        self._pub_id = pub_id

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
        if not isinstance(other, FreezePubResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
