# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecretDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'if_update_available': 'bool',
        'secret_status': 'str',
        'status': 'str',
        'version_id': 'str',
        'modified_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'if_update_available': 'if_update_available',
        'secret_status': 'secret_status',
        'status': 'status',
        'version_id': 'version_id',
        'modified_time': 'modified_time'
    }

    def __init__(self, id=None, name=None, if_update_available=None, secret_status=None, status=None, version_id=None, modified_time=None):
        r"""SecretDetail

        The model defined in huaweicloud sdk

        :param id: 凭据ID
        :type id: str
        :param name: 凭证名字。
        :type name: str
        :param if_update_available: 当前凭据是否有更新版本。
        :type if_update_available: bool
        :param secret_status: 凭据在DEW的状态。
        :type secret_status: str
        :param status: 凭据在CAE使用状态。
        :type status: str
        :param version_id: 当前使用的凭证版本号。
        :type version_id: str
        :param modified_time: 当前版本凭证在dew的创建时间。
        :type modified_time: int
        """
        
        

        self._id = None
        self._name = None
        self._if_update_available = None
        self._secret_status = None
        self._status = None
        self._version_id = None
        self._modified_time = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.if_update_available = if_update_available
        self.secret_status = secret_status
        self.status = status
        self.version_id = version_id
        if modified_time is not None:
            self.modified_time = modified_time

    @property
    def id(self):
        r"""Gets the id of this SecretDetail.

        凭据ID

        :return: The id of this SecretDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SecretDetail.

        凭据ID

        :param id: The id of this SecretDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SecretDetail.

        凭证名字。

        :return: The name of this SecretDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SecretDetail.

        凭证名字。

        :param name: The name of this SecretDetail.
        :type name: str
        """
        self._name = name

    @property
    def if_update_available(self):
        r"""Gets the if_update_available of this SecretDetail.

        当前凭据是否有更新版本。

        :return: The if_update_available of this SecretDetail.
        :rtype: bool
        """
        return self._if_update_available

    @if_update_available.setter
    def if_update_available(self, if_update_available):
        r"""Sets the if_update_available of this SecretDetail.

        当前凭据是否有更新版本。

        :param if_update_available: The if_update_available of this SecretDetail.
        :type if_update_available: bool
        """
        self._if_update_available = if_update_available

    @property
    def secret_status(self):
        r"""Gets the secret_status of this SecretDetail.

        凭据在DEW的状态。

        :return: The secret_status of this SecretDetail.
        :rtype: str
        """
        return self._secret_status

    @secret_status.setter
    def secret_status(self, secret_status):
        r"""Sets the secret_status of this SecretDetail.

        凭据在DEW的状态。

        :param secret_status: The secret_status of this SecretDetail.
        :type secret_status: str
        """
        self._secret_status = secret_status

    @property
    def status(self):
        r"""Gets the status of this SecretDetail.

        凭据在CAE使用状态。

        :return: The status of this SecretDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SecretDetail.

        凭据在CAE使用状态。

        :param status: The status of this SecretDetail.
        :type status: str
        """
        self._status = status

    @property
    def version_id(self):
        r"""Gets the version_id of this SecretDetail.

        当前使用的凭证版本号。

        :return: The version_id of this SecretDetail.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this SecretDetail.

        当前使用的凭证版本号。

        :param version_id: The version_id of this SecretDetail.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def modified_time(self):
        r"""Gets the modified_time of this SecretDetail.

        当前版本凭证在dew的创建时间。

        :return: The modified_time of this SecretDetail.
        :rtype: int
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this SecretDetail.

        当前版本凭证在dew的创建时间。

        :param modified_time: The modified_time of this SecretDetail.
        :type modified_time: int
        """
        self._modified_time = modified_time

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
        if not isinstance(other, SecretDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
