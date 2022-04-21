# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Stage:

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
        'update_time': 'int',
        'secret_name': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'update_time': 'update_time',
        'secret_name': 'secret_name',
        'version_id': 'version_id'
    }

    def __init__(self, name=None, update_time=None, secret_name=None, version_id=None):
        """Stage

        The model defined in huaweicloud sdk

        :param name: 凭据的版本状态名称。  约束：最小长度1，最大长度64。 
        :type name: str
        :param update_time: 凭据的版本状态更新的时间戳，时间戳，即从1970年1月1日至该时间的总秒数。
        :type update_time: int
        :param secret_name: 凭据名称。
        :type secret_name: str
        :param version_id: 凭据的版本号标识符。 
        :type version_id: str
        """
        
        

        self._name = None
        self._update_time = None
        self._secret_name = None
        self._version_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if update_time is not None:
            self.update_time = update_time
        if secret_name is not None:
            self.secret_name = secret_name
        if version_id is not None:
            self.version_id = version_id

    @property
    def name(self):
        """Gets the name of this Stage.

        凭据的版本状态名称。  约束：最小长度1，最大长度64。 

        :return: The name of this Stage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Stage.

        凭据的版本状态名称。  约束：最小长度1，最大长度64。 

        :param name: The name of this Stage.
        :type name: str
        """
        self._name = name

    @property
    def update_time(self):
        """Gets the update_time of this Stage.

        凭据的版本状态更新的时间戳，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The update_time of this Stage.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Stage.

        凭据的版本状态更新的时间戳，时间戳，即从1970年1月1日至该时间的总秒数。

        :param update_time: The update_time of this Stage.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def secret_name(self):
        """Gets the secret_name of this Stage.

        凭据名称。

        :return: The secret_name of this Stage.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this Stage.

        凭据名称。

        :param secret_name: The secret_name of this Stage.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def version_id(self):
        """Gets the version_id of this Stage.

        凭据的版本号标识符。 

        :return: The version_id of this Stage.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this Stage.

        凭据的版本号标识符。 

        :param version_id: The version_id of this Stage.
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
        if not isinstance(other, Stage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
