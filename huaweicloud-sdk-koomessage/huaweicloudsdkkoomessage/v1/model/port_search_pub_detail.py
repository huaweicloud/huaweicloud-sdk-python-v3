# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortSearchPubDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pub_name': 'str',
        'pub_reference': 'str'
    }

    attribute_map = {
        'pub_name': 'pub_name',
        'pub_reference': 'pub_reference'
    }

    def __init__(self, pub_name=None, pub_reference=None):
        """PortSearchPubDetail

        The model defined in huaweicloud sdk

        :param pub_name: 服务号名称。
        :type pub_name: str
        :param pub_reference: 服务号备注。
        :type pub_reference: str
        """
        
        

        self._pub_name = None
        self._pub_reference = None
        self.discriminator = None

        if pub_name is not None:
            self.pub_name = pub_name
        if pub_reference is not None:
            self.pub_reference = pub_reference

    @property
    def pub_name(self):
        """Gets the pub_name of this PortSearchPubDetail.

        服务号名称。

        :return: The pub_name of this PortSearchPubDetail.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        """Sets the pub_name of this PortSearchPubDetail.

        服务号名称。

        :param pub_name: The pub_name of this PortSearchPubDetail.
        :type pub_name: str
        """
        self._pub_name = pub_name

    @property
    def pub_reference(self):
        """Gets the pub_reference of this PortSearchPubDetail.

        服务号备注。

        :return: The pub_reference of this PortSearchPubDetail.
        :rtype: str
        """
        return self._pub_reference

    @pub_reference.setter
    def pub_reference(self, pub_reference):
        """Sets the pub_reference of this PortSearchPubDetail.

        服务号备注。

        :param pub_reference: The pub_reference of this PortSearchPubDetail.
        :type pub_reference: str
        """
        self._pub_reference = pub_reference

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
        if not isinstance(other, PortSearchPubDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
