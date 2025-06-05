# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKeystoreResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keystore_name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'keystore_name': 'keystore_name',
        'id': 'id'
    }

    def __init__(self, keystore_name=None, id=None):
        r"""ListKeystoreResult

        The model defined in huaweicloud sdk

        :param keystore_name: 文件名
        :type keystore_name: str
        :param id: 文件ID
        :type id: str
        """
        
        

        self._keystore_name = None
        self._id = None
        self.discriminator = None

        if keystore_name is not None:
            self.keystore_name = keystore_name
        if id is not None:
            self.id = id

    @property
    def keystore_name(self):
        r"""Gets the keystore_name of this ListKeystoreResult.

        文件名

        :return: The keystore_name of this ListKeystoreResult.
        :rtype: str
        """
        return self._keystore_name

    @keystore_name.setter
    def keystore_name(self, keystore_name):
        r"""Sets the keystore_name of this ListKeystoreResult.

        文件名

        :param keystore_name: The keystore_name of this ListKeystoreResult.
        :type keystore_name: str
        """
        self._keystore_name = keystore_name

    @property
    def id(self):
        r"""Gets the id of this ListKeystoreResult.

        文件ID

        :return: The id of this ListKeystoreResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListKeystoreResult.

        文件ID

        :param id: The id of this ListKeystoreResult.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ListKeystoreResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
