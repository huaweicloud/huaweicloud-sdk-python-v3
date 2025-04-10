# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone_id': 'str',
        'access_info': 'ConnectInfoAccessInfo'
    }

    attribute_map = {
        'phone_id': 'phone_id',
        'access_info': 'access_info'
    }

    def __init__(self, phone_id=None, access_info=None):
        r"""ConnectInfo

        The model defined in huaweicloud sdk

        :param phone_id: 云手机的唯一标识。
        :type phone_id: str
        :param access_info: 
        :type access_info: :class:`huaweicloudsdkcph.v1.ConnectInfoAccessInfo`
        """
        
        

        self._phone_id = None
        self._access_info = None
        self.discriminator = None

        if phone_id is not None:
            self.phone_id = phone_id
        if access_info is not None:
            self.access_info = access_info

    @property
    def phone_id(self):
        r"""Gets the phone_id of this ConnectInfo.

        云手机的唯一标识。

        :return: The phone_id of this ConnectInfo.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        r"""Sets the phone_id of this ConnectInfo.

        云手机的唯一标识。

        :param phone_id: The phone_id of this ConnectInfo.
        :type phone_id: str
        """
        self._phone_id = phone_id

    @property
    def access_info(self):
        r"""Gets the access_info of this ConnectInfo.

        :return: The access_info of this ConnectInfo.
        :rtype: :class:`huaweicloudsdkcph.v1.ConnectInfoAccessInfo`
        """
        return self._access_info

    @access_info.setter
    def access_info(self, access_info):
        r"""Sets the access_info of this ConnectInfo.

        :param access_info: The access_info of this ConnectInfo.
        :type access_info: :class:`huaweicloudsdkcph.v1.ConnectInfoAccessInfo`
        """
        self._access_info = access_info

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
        if not isinstance(other, ConnectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
