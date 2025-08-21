# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBestPracticeAccountInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_type': 'str',
        'effective_start_time': 'datetime',
        'effective_expiration_time': 'datetime',
        'current_time': 'datetime'
    }

    attribute_map = {
        'account_type': 'account_type',
        'effective_start_time': 'effective_start_time',
        'effective_expiration_time': 'effective_expiration_time',
        'current_time': 'current_time'
    }

    def __init__(self, account_type=None, effective_start_time=None, effective_expiration_time=None, current_time=None):
        r"""ShowBestPracticeAccountInfoResponse

        The model defined in huaweicloud sdk

        :param account_type: 账号类型
        :type account_type: str
        :param effective_start_time: 有效开始时间
        :type effective_start_time: datetime
        :param effective_expiration_time: 有效过期时间
        :type effective_expiration_time: datetime
        :param current_time: 当前时间
        :type current_time: datetime
        """
        
        super(ShowBestPracticeAccountInfoResponse, self).__init__()

        self._account_type = None
        self._effective_start_time = None
        self._effective_expiration_time = None
        self._current_time = None
        self.discriminator = None

        if account_type is not None:
            self.account_type = account_type
        if effective_start_time is not None:
            self.effective_start_time = effective_start_time
        if effective_expiration_time is not None:
            self.effective_expiration_time = effective_expiration_time
        if current_time is not None:
            self.current_time = current_time

    @property
    def account_type(self):
        r"""Gets the account_type of this ShowBestPracticeAccountInfoResponse.

        账号类型

        :return: The account_type of this ShowBestPracticeAccountInfoResponse.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        r"""Sets the account_type of this ShowBestPracticeAccountInfoResponse.

        账号类型

        :param account_type: The account_type of this ShowBestPracticeAccountInfoResponse.
        :type account_type: str
        """
        self._account_type = account_type

    @property
    def effective_start_time(self):
        r"""Gets the effective_start_time of this ShowBestPracticeAccountInfoResponse.

        有效开始时间

        :return: The effective_start_time of this ShowBestPracticeAccountInfoResponse.
        :rtype: datetime
        """
        return self._effective_start_time

    @effective_start_time.setter
    def effective_start_time(self, effective_start_time):
        r"""Sets the effective_start_time of this ShowBestPracticeAccountInfoResponse.

        有效开始时间

        :param effective_start_time: The effective_start_time of this ShowBestPracticeAccountInfoResponse.
        :type effective_start_time: datetime
        """
        self._effective_start_time = effective_start_time

    @property
    def effective_expiration_time(self):
        r"""Gets the effective_expiration_time of this ShowBestPracticeAccountInfoResponse.

        有效过期时间

        :return: The effective_expiration_time of this ShowBestPracticeAccountInfoResponse.
        :rtype: datetime
        """
        return self._effective_expiration_time

    @effective_expiration_time.setter
    def effective_expiration_time(self, effective_expiration_time):
        r"""Sets the effective_expiration_time of this ShowBestPracticeAccountInfoResponse.

        有效过期时间

        :param effective_expiration_time: The effective_expiration_time of this ShowBestPracticeAccountInfoResponse.
        :type effective_expiration_time: datetime
        """
        self._effective_expiration_time = effective_expiration_time

    @property
    def current_time(self):
        r"""Gets the current_time of this ShowBestPracticeAccountInfoResponse.

        当前时间

        :return: The current_time of this ShowBestPracticeAccountInfoResponse.
        :rtype: datetime
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        r"""Sets the current_time of this ShowBestPracticeAccountInfoResponse.

        当前时间

        :param current_time: The current_time of this ShowBestPracticeAccountInfoResponse.
        :type current_time: datetime
        """
        self._current_time = current_time

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
        if not isinstance(other, ShowBestPracticeAccountInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
