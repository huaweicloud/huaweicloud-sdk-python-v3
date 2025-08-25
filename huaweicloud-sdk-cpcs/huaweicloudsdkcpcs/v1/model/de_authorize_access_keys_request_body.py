# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeAuthorizeAccessKeysRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key_ids': 'list[str]',
        'app_id': 'str'
    }

    attribute_map = {
        'access_key_ids': 'access_key_ids',
        'app_id': 'app_id'
    }

    def __init__(self, access_key_ids=None, app_id=None):
        r"""DeAuthorizeAccessKeysRequestBody

        The model defined in huaweicloud sdk

        :param access_key_ids: 需要被解除授权的访问密钥的ID列表，若需要解除所有访问密钥的授权，则仅传入一个元素，且该元素值为“all”，如body为“{\&quot;access_key_ids\&quot;: [\&quot;all\&quot;]}”
        :type access_key_ids: list[str]
        :param app_id: 应用ID
        :type app_id: str
        """
        
        

        self._access_key_ids = None
        self._app_id = None
        self.discriminator = None

        self.access_key_ids = access_key_ids
        self.app_id = app_id

    @property
    def access_key_ids(self):
        r"""Gets the access_key_ids of this DeAuthorizeAccessKeysRequestBody.

        需要被解除授权的访问密钥的ID列表，若需要解除所有访问密钥的授权，则仅传入一个元素，且该元素值为“all”，如body为“{\"access_key_ids\": [\"all\"]}”

        :return: The access_key_ids of this DeAuthorizeAccessKeysRequestBody.
        :rtype: list[str]
        """
        return self._access_key_ids

    @access_key_ids.setter
    def access_key_ids(self, access_key_ids):
        r"""Sets the access_key_ids of this DeAuthorizeAccessKeysRequestBody.

        需要被解除授权的访问密钥的ID列表，若需要解除所有访问密钥的授权，则仅传入一个元素，且该元素值为“all”，如body为“{\"access_key_ids\": [\"all\"]}”

        :param access_key_ids: The access_key_ids of this DeAuthorizeAccessKeysRequestBody.
        :type access_key_ids: list[str]
        """
        self._access_key_ids = access_key_ids

    @property
    def app_id(self):
        r"""Gets the app_id of this DeAuthorizeAccessKeysRequestBody.

        应用ID

        :return: The app_id of this DeAuthorizeAccessKeysRequestBody.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this DeAuthorizeAccessKeysRequestBody.

        应用ID

        :param app_id: The app_id of this DeAuthorizeAccessKeysRequestBody.
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
        if not isinstance(other, DeAuthorizeAccessKeysRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
