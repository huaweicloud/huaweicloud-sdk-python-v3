# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserStoredValueCard:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'card_id': 'str',
        'card_name': 'str',
        'status': 'int',
        'face_value': 'str',
        'balance': 'str',
        'effective_time': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'card_id': 'card_id',
        'card_name': 'card_name',
        'status': 'status',
        'face_value': 'face_value',
        'balance': 'balance',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time'
    }

    def __init__(self, card_id=None, card_name=None, status=None, face_value=None, balance=None, effective_time=None, expire_time=None):
        r"""UserStoredValueCard

        The model defined in huaweicloud sdk

        :param card_id: 储值卡ID。
        :type card_id: str
        :param card_name: 储值卡名称。
        :type card_name: str
        :param status: 状态： 1：可使用 2：已用完
        :type status: int
        :param face_value: 储值卡面值。
        :type face_value: str
        :param balance: 储值卡余额。
        :type balance: str
        :param effective_time: 生效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type effective_time: str
        :param expire_time: 失效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type expire_time: str
        """
        
        

        self._card_id = None
        self._card_name = None
        self._status = None
        self._face_value = None
        self._balance = None
        self._effective_time = None
        self._expire_time = None
        self.discriminator = None

        if card_id is not None:
            self.card_id = card_id
        if card_name is not None:
            self.card_name = card_name
        if status is not None:
            self.status = status
        if face_value is not None:
            self.face_value = face_value
        if balance is not None:
            self.balance = balance
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def card_id(self):
        r"""Gets the card_id of this UserStoredValueCard.

        储值卡ID。

        :return: The card_id of this UserStoredValueCard.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        r"""Sets the card_id of this UserStoredValueCard.

        储值卡ID。

        :param card_id: The card_id of this UserStoredValueCard.
        :type card_id: str
        """
        self._card_id = card_id

    @property
    def card_name(self):
        r"""Gets the card_name of this UserStoredValueCard.

        储值卡名称。

        :return: The card_name of this UserStoredValueCard.
        :rtype: str
        """
        return self._card_name

    @card_name.setter
    def card_name(self, card_name):
        r"""Sets the card_name of this UserStoredValueCard.

        储值卡名称。

        :param card_name: The card_name of this UserStoredValueCard.
        :type card_name: str
        """
        self._card_name = card_name

    @property
    def status(self):
        r"""Gets the status of this UserStoredValueCard.

        状态： 1：可使用 2：已用完

        :return: The status of this UserStoredValueCard.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UserStoredValueCard.

        状态： 1：可使用 2：已用完

        :param status: The status of this UserStoredValueCard.
        :type status: int
        """
        self._status = status

    @property
    def face_value(self):
        r"""Gets the face_value of this UserStoredValueCard.

        储值卡面值。

        :return: The face_value of this UserStoredValueCard.
        :rtype: str
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        r"""Sets the face_value of this UserStoredValueCard.

        储值卡面值。

        :param face_value: The face_value of this UserStoredValueCard.
        :type face_value: str
        """
        self._face_value = face_value

    @property
    def balance(self):
        r"""Gets the balance of this UserStoredValueCard.

        储值卡余额。

        :return: The balance of this UserStoredValueCard.
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        r"""Sets the balance of this UserStoredValueCard.

        储值卡余额。

        :param balance: The balance of this UserStoredValueCard.
        :type balance: str
        """
        self._balance = balance

    @property
    def effective_time(self):
        r"""Gets the effective_time of this UserStoredValueCard.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The effective_time of this UserStoredValueCard.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this UserStoredValueCard.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param effective_time: The effective_time of this UserStoredValueCard.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this UserStoredValueCard.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The expire_time of this UserStoredValueCard.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this UserStoredValueCard.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param expire_time: The expire_time of this UserStoredValueCard.
        :type expire_time: str
        """
        self._expire_time = expire_time

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
        if not isinstance(other, UserStoredValueCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
