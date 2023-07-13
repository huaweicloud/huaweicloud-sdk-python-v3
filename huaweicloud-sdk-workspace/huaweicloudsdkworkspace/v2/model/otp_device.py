# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OtpDevice:

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
        'user_id': 'str',
        'user_name': 'str',
        'status': 'str',
        'create_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'status': 'status',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, user_id=None, user_name=None, status=None, create_time=None):
        """OtpDevice

        The model defined in huaweicloud sdk

        :param id: 用户otp 信息id。
        :type id: str
        :param user_id: 用户id。
        :type user_id: str
        :param user_name: 用户名。
        :type user_name: str
        :param status: 用户otp设备状态 UNREGISTER: 未绑定 REGISTERED：已绑定
        :type status: str
        :param create_time: 用户otp设备绑定时间。
        :type create_time: datetime
        """
        
        

        self._id = None
        self._user_id = None
        self._user_name = None
        self._status = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        """Gets the id of this OtpDevice.

        用户otp 信息id。

        :return: The id of this OtpDevice.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OtpDevice.

        用户otp 信息id。

        :param id: The id of this OtpDevice.
        :type id: str
        """
        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this OtpDevice.

        用户id。

        :return: The user_id of this OtpDevice.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OtpDevice.

        用户id。

        :param user_id: The user_id of this OtpDevice.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this OtpDevice.

        用户名。

        :return: The user_name of this OtpDevice.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this OtpDevice.

        用户名。

        :param user_name: The user_name of this OtpDevice.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def status(self):
        """Gets the status of this OtpDevice.

        用户otp设备状态 UNREGISTER: 未绑定 REGISTERED：已绑定

        :return: The status of this OtpDevice.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OtpDevice.

        用户otp设备状态 UNREGISTER: 未绑定 REGISTERED：已绑定

        :param status: The status of this OtpDevice.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this OtpDevice.

        用户otp设备绑定时间。

        :return: The create_time of this OtpDevice.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this OtpDevice.

        用户otp设备绑定时间。

        :param create_time: The create_time of this OtpDevice.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, OtpDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
