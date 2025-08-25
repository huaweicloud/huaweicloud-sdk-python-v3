# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAccessKeyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key_id': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'app_id': 'app_id'
    }

    def __init__(self, access_key_id=None, app_id=None):
        r"""DeleteAccessKeyRequest

        The model defined in huaweicloud sdk

        :param access_key_id: 访问密钥ID
        :type access_key_id: str
        :param app_id: 应用ID
        :type app_id: str
        """
        
        

        self._access_key_id = None
        self._app_id = None
        self.discriminator = None

        self.access_key_id = access_key_id
        self.app_id = app_id

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this DeleteAccessKeyRequest.

        访问密钥ID

        :return: The access_key_id of this DeleteAccessKeyRequest.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this DeleteAccessKeyRequest.

        访问密钥ID

        :param access_key_id: The access_key_id of this DeleteAccessKeyRequest.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def app_id(self):
        r"""Gets the app_id of this DeleteAccessKeyRequest.

        应用ID

        :return: The app_id of this DeleteAccessKeyRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this DeleteAccessKeyRequest.

        应用ID

        :param app_id: The app_id of this DeleteAccessKeyRequest.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, DeleteAccessKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
