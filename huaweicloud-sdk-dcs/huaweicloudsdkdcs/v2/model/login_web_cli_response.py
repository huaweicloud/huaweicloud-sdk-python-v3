# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginWebCliResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_id': 'str',
        'databases': 'int'
    }

    attribute_map = {
        'client_id': 'client_id',
        'databases': 'databases'
    }

    def __init__(self, client_id=None, databases=None):
        """LoginWebCliResponse

        The model defined in huaweicloud sdk

        :param client_id: 客户端ID
        :type client_id: str
        :param databases: DB数量
        :type databases: int
        """
        
        super(LoginWebCliResponse, self).__init__()

        self._client_id = None
        self._databases = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if databases is not None:
            self.databases = databases

    @property
    def client_id(self):
        """Gets the client_id of this LoginWebCliResponse.

        客户端ID

        :return: The client_id of this LoginWebCliResponse.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this LoginWebCliResponse.

        客户端ID

        :param client_id: The client_id of this LoginWebCliResponse.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def databases(self):
        """Gets the databases of this LoginWebCliResponse.

        DB数量

        :return: The databases of this LoginWebCliResponse.
        :rtype: int
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this LoginWebCliResponse.

        DB数量

        :param databases: The databases of this LoginWebCliResponse.
        :type databases: int
        """
        self._databases = databases

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
        if not isinstance(other, LoginWebCliResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
