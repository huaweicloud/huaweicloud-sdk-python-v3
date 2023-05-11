# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCredentialResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'create_time': 'str',
        'description': 'str',
        'status': 'str'
    }

    attribute_map = {
        'key': 'key',
        'create_time': 'create_time',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, key=None, create_time=None, description=None, status=None):
        """CreateCredentialResponse

        The model defined in huaweicloud sdk

        :param key: 凭证
        :type key: str
        :param create_time: 创建凭证的时间UTC时间格式：YYYY-mm-dd&#39;T&#39;HH:mm:ss.SSSSSS&#39;Z&#39;，e.g. \&quot;2020-01-08T06:26:08.123059Z\&quot;
        :type create_time: str
        :param description: 凭证的描述信息。
        :type description: str
        :param status: 凭证状态“ACTIVE”
        :type status: str
        """
        
        super(CreateCredentialResponse, self).__init__()

        self._key = None
        self._create_time = None
        self._description = None
        self._status = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status

    @property
    def key(self):
        """Gets the key of this CreateCredentialResponse.

        凭证

        :return: The key of this CreateCredentialResponse.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateCredentialResponse.

        凭证

        :param key: The key of this CreateCredentialResponse.
        :type key: str
        """
        self._key = key

    @property
    def create_time(self):
        """Gets the create_time of this CreateCredentialResponse.

        创建凭证的时间UTC时间格式：YYYY-mm-dd'T'HH:mm:ss.SSSSSS'Z'，e.g. \"2020-01-08T06:26:08.123059Z\"

        :return: The create_time of this CreateCredentialResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateCredentialResponse.

        创建凭证的时间UTC时间格式：YYYY-mm-dd'T'HH:mm:ss.SSSSSS'Z'，e.g. \"2020-01-08T06:26:08.123059Z\"

        :param create_time: The create_time of this CreateCredentialResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this CreateCredentialResponse.

        凭证的描述信息。

        :return: The description of this CreateCredentialResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCredentialResponse.

        凭证的描述信息。

        :param description: The description of this CreateCredentialResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this CreateCredentialResponse.

        凭证状态“ACTIVE”

        :return: The status of this CreateCredentialResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateCredentialResponse.

        凭证状态“ACTIVE”

        :param status: The status of this CreateCredentialResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, CreateCredentialResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
