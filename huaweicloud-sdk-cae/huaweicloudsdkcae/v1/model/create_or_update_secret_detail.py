# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrUpdateSecretDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'version_id': 'version_id'
    }

    def __init__(self, name=None, version_id=None):
        r"""CreateOrUpdateSecretDetail

        The model defined in huaweicloud sdk

        :param name: 凭证名字。
        :type name: str
        :param version_id: 当前使用的凭证版本号。
        :type version_id: str
        """
        
        

        self._name = None
        self._version_id = None
        self.discriminator = None

        self.name = name
        self.version_id = version_id

    @property
    def name(self):
        r"""Gets the name of this CreateOrUpdateSecretDetail.

        凭证名字。

        :return: The name of this CreateOrUpdateSecretDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOrUpdateSecretDetail.

        凭证名字。

        :param name: The name of this CreateOrUpdateSecretDetail.
        :type name: str
        """
        self._name = name

    @property
    def version_id(self):
        r"""Gets the version_id of this CreateOrUpdateSecretDetail.

        当前使用的凭证版本号。

        :return: The version_id of this CreateOrUpdateSecretDetail.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this CreateOrUpdateSecretDetail.

        当前使用的凭证版本号。

        :param version_id: The version_id of this CreateOrUpdateSecretDetail.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, CreateOrUpdateSecretDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
