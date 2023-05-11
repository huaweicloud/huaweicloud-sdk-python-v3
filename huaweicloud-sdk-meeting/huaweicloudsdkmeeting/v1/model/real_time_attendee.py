# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RealTimeAttendee:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'user_uuid': 'str',
        'name': 'str',
        'phone': 'str',
        'phone_left': 'str',
        'phone_right': 'str'
    }

    attribute_map = {
        'account_id': 'accountID',
        'user_uuid': 'userUUID',
        'name': 'name',
        'phone': 'phone',
        'phone_left': 'phoneLeft',
        'phone_right': 'phoneRight'
    }

    def __init__(self, account_id=None, user_uuid=None, name=None, phone=None, phone_left=None, phone_right=None):
        """RealTimeAttendee

        The model defined in huaweicloud sdk

        :param account_id: 与会者的华为云会议帐号。
        :type account_id: str
        :param user_uuid: 与会者的用户UUID。
        :type user_uuid: str
        :param name: 与会者名称。
        :type name: str
        :param phone: 与会者号码。
        :type phone: str
        :param phone_left: 设备为三屏智真时的左屏号码。 &gt; 该参数将废弃，请勿使用。 
        :type phone_left: str
        :param phone_right: 设备为三屏智真时的右屏号码。 &gt; 该参数将废弃，请勿使用。 
        :type phone_right: str
        """
        
        

        self._account_id = None
        self._user_uuid = None
        self._name = None
        self._phone = None
        self._phone_left = None
        self._phone_right = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if phone_left is not None:
            self.phone_left = phone_left
        if phone_right is not None:
            self.phone_right = phone_right

    @property
    def account_id(self):
        """Gets the account_id of this RealTimeAttendee.

        与会者的华为云会议帐号。

        :return: The account_id of this RealTimeAttendee.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RealTimeAttendee.

        与会者的华为云会议帐号。

        :param account_id: The account_id of this RealTimeAttendee.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this RealTimeAttendee.

        与会者的用户UUID。

        :return: The user_uuid of this RealTimeAttendee.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this RealTimeAttendee.

        与会者的用户UUID。

        :param user_uuid: The user_uuid of this RealTimeAttendee.
        :type user_uuid: str
        """
        self._user_uuid = user_uuid

    @property
    def name(self):
        """Gets the name of this RealTimeAttendee.

        与会者名称。

        :return: The name of this RealTimeAttendee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RealTimeAttendee.

        与会者名称。

        :param name: The name of this RealTimeAttendee.
        :type name: str
        """
        self._name = name

    @property
    def phone(self):
        """Gets the phone of this RealTimeAttendee.

        与会者号码。

        :return: The phone of this RealTimeAttendee.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this RealTimeAttendee.

        与会者号码。

        :param phone: The phone of this RealTimeAttendee.
        :type phone: str
        """
        self._phone = phone

    @property
    def phone_left(self):
        """Gets the phone_left of this RealTimeAttendee.

        设备为三屏智真时的左屏号码。 > 该参数将废弃，请勿使用。 

        :return: The phone_left of this RealTimeAttendee.
        :rtype: str
        """
        return self._phone_left

    @phone_left.setter
    def phone_left(self, phone_left):
        """Sets the phone_left of this RealTimeAttendee.

        设备为三屏智真时的左屏号码。 > 该参数将废弃，请勿使用。 

        :param phone_left: The phone_left of this RealTimeAttendee.
        :type phone_left: str
        """
        self._phone_left = phone_left

    @property
    def phone_right(self):
        """Gets the phone_right of this RealTimeAttendee.

        设备为三屏智真时的右屏号码。 > 该参数将废弃，请勿使用。 

        :return: The phone_right of this RealTimeAttendee.
        :rtype: str
        """
        return self._phone_right

    @phone_right.setter
    def phone_right(self, phone_right):
        """Sets the phone_right of this RealTimeAttendee.

        设备为三屏智真时的右屏号码。 > 该参数将废弃，请勿使用。 

        :param phone_right: The phone_right of this RealTimeAttendee.
        :type phone_right: str
        """
        self._phone_right = phone_right

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
        if not isinstance(other, RealTimeAttendee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
