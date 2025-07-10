# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKeystorePermissionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_absent': 'bool',
        'delete': 'bool',
        'id': 'str',
        'keystore_id': 'str',
        'modify': 'bool',
        'usage': 'bool',
        'user_name': 'str'
    }

    attribute_map = {
        'can_absent': 'can_absent',
        'delete': 'delete',
        'id': 'id',
        'keystore_id': 'keystore_id',
        'modify': 'modify',
        'usage': 'usage',
        'user_name': 'user_name'
    }

    def __init__(self, can_absent=None, delete=None, id=None, keystore_id=None, modify=None, usage=None, user_name=None):
        r"""UpdateKeystorePermissionRequestBody

        The model defined in huaweicloud sdk

        :param can_absent: can_absent
        :type can_absent: bool
        :param delete: delete
        :type delete: bool
        :param id: id
        :type id: str
        :param keystore_id: keystore_id
        :type keystore_id: str
        :param modify: modify
        :type modify: bool
        :param usage: usage
        :type usage: bool
        :param user_name: user_name
        :type user_name: str
        """
        
        

        self._can_absent = None
        self._delete = None
        self._id = None
        self._keystore_id = None
        self._modify = None
        self._usage = None
        self._user_name = None
        self.discriminator = None

        if can_absent is not None:
            self.can_absent = can_absent
        self.delete = delete
        self.id = id
        self.keystore_id = keystore_id
        self.modify = modify
        self.usage = usage
        self.user_name = user_name

    @property
    def can_absent(self):
        r"""Gets the can_absent of this UpdateKeystorePermissionRequestBody.

        can_absent

        :return: The can_absent of this UpdateKeystorePermissionRequestBody.
        :rtype: bool
        """
        return self._can_absent

    @can_absent.setter
    def can_absent(self, can_absent):
        r"""Sets the can_absent of this UpdateKeystorePermissionRequestBody.

        can_absent

        :param can_absent: The can_absent of this UpdateKeystorePermissionRequestBody.
        :type can_absent: bool
        """
        self._can_absent = can_absent

    @property
    def delete(self):
        r"""Gets the delete of this UpdateKeystorePermissionRequestBody.

        delete

        :return: The delete of this UpdateKeystorePermissionRequestBody.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        r"""Sets the delete of this UpdateKeystorePermissionRequestBody.

        delete

        :param delete: The delete of this UpdateKeystorePermissionRequestBody.
        :type delete: bool
        """
        self._delete = delete

    @property
    def id(self):
        r"""Gets the id of this UpdateKeystorePermissionRequestBody.

        id

        :return: The id of this UpdateKeystorePermissionRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateKeystorePermissionRequestBody.

        id

        :param id: The id of this UpdateKeystorePermissionRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def keystore_id(self):
        r"""Gets the keystore_id of this UpdateKeystorePermissionRequestBody.

        keystore_id

        :return: The keystore_id of this UpdateKeystorePermissionRequestBody.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        r"""Sets the keystore_id of this UpdateKeystorePermissionRequestBody.

        keystore_id

        :param keystore_id: The keystore_id of this UpdateKeystorePermissionRequestBody.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

    @property
    def modify(self):
        r"""Gets the modify of this UpdateKeystorePermissionRequestBody.

        modify

        :return: The modify of this UpdateKeystorePermissionRequestBody.
        :rtype: bool
        """
        return self._modify

    @modify.setter
    def modify(self, modify):
        r"""Sets the modify of this UpdateKeystorePermissionRequestBody.

        modify

        :param modify: The modify of this UpdateKeystorePermissionRequestBody.
        :type modify: bool
        """
        self._modify = modify

    @property
    def usage(self):
        r"""Gets the usage of this UpdateKeystorePermissionRequestBody.

        usage

        :return: The usage of this UpdateKeystorePermissionRequestBody.
        :rtype: bool
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this UpdateKeystorePermissionRequestBody.

        usage

        :param usage: The usage of this UpdateKeystorePermissionRequestBody.
        :type usage: bool
        """
        self._usage = usage

    @property
    def user_name(self):
        r"""Gets the user_name of this UpdateKeystorePermissionRequestBody.

        user_name

        :return: The user_name of this UpdateKeystorePermissionRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UpdateKeystorePermissionRequestBody.

        user_name

        :param user_name: The user_name of this UpdateKeystorePermissionRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, UpdateKeystorePermissionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
