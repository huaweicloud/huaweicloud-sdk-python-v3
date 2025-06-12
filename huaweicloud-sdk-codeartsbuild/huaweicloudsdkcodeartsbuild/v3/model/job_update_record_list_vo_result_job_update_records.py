# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobUpdateRecordListVoResultJobUpdateRecords:

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
        'update_number': 'int',
        'update_type': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'nick_name': 'str',
        'update_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'update_number': 'update_number',
        'update_type': 'update_type',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'nick_name': 'nick_name',
        'update_at': 'update_at'
    }

    def __init__(self, id=None, update_number=None, update_type=None, user_id=None, user_name=None, nick_name=None, update_at=None):
        r"""JobUpdateRecordListVoResultJobUpdateRecords

        The model defined in huaweicloud sdk

        :param id: 修改编号
        :type id: str
        :param update_number: 更新编号
        :type update_number: int
        :param update_type: 类型
        :type update_type: str
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param nick_name: 昵称
        :type nick_name: str
        :param update_at: 更新时间
        :type update_at: int
        """
        
        

        self._id = None
        self._update_number = None
        self._update_type = None
        self._user_id = None
        self._user_name = None
        self._nick_name = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if update_number is not None:
            self.update_number = update_number
        if update_type is not None:
            self.update_type = update_type
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if nick_name is not None:
            self.nick_name = nick_name
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this JobUpdateRecordListVoResultJobUpdateRecords.

        修改编号

        :return: The id of this JobUpdateRecordListVoResultJobUpdateRecords.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobUpdateRecordListVoResultJobUpdateRecords.

        修改编号

        :param id: The id of this JobUpdateRecordListVoResultJobUpdateRecords.
        :type id: str
        """
        self._id = id

    @property
    def update_number(self):
        r"""Gets the update_number of this JobUpdateRecordListVoResultJobUpdateRecords.

        更新编号

        :return: The update_number of this JobUpdateRecordListVoResultJobUpdateRecords.
        :rtype: int
        """
        return self._update_number

    @update_number.setter
    def update_number(self, update_number):
        r"""Sets the update_number of this JobUpdateRecordListVoResultJobUpdateRecords.

        更新编号

        :param update_number: The update_number of this JobUpdateRecordListVoResultJobUpdateRecords.
        :type update_number: int
        """
        self._update_number = update_number

    @property
    def update_type(self):
        r"""Gets the update_type of this JobUpdateRecordListVoResultJobUpdateRecords.

        类型

        :return: The update_type of this JobUpdateRecordListVoResultJobUpdateRecords.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        r"""Sets the update_type of this JobUpdateRecordListVoResultJobUpdateRecords.

        类型

        :param update_type: The update_type of this JobUpdateRecordListVoResultJobUpdateRecords.
        :type update_type: str
        """
        self._update_type = update_type

    @property
    def user_id(self):
        r"""Gets the user_id of this JobUpdateRecordListVoResultJobUpdateRecords.

        用户id

        :return: The user_id of this JobUpdateRecordListVoResultJobUpdateRecords.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this JobUpdateRecordListVoResultJobUpdateRecords.

        用户id

        :param user_id: The user_id of this JobUpdateRecordListVoResultJobUpdateRecords.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this JobUpdateRecordListVoResultJobUpdateRecords.

        用户名

        :return: The user_name of this JobUpdateRecordListVoResultJobUpdateRecords.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this JobUpdateRecordListVoResultJobUpdateRecords.

        用户名

        :param user_name: The user_name of this JobUpdateRecordListVoResultJobUpdateRecords.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this JobUpdateRecordListVoResultJobUpdateRecords.

        昵称

        :return: The nick_name of this JobUpdateRecordListVoResultJobUpdateRecords.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this JobUpdateRecordListVoResultJobUpdateRecords.

        昵称

        :param nick_name: The nick_name of this JobUpdateRecordListVoResultJobUpdateRecords.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def update_at(self):
        r"""Gets the update_at of this JobUpdateRecordListVoResultJobUpdateRecords.

        更新时间

        :return: The update_at of this JobUpdateRecordListVoResultJobUpdateRecords.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this JobUpdateRecordListVoResultJobUpdateRecords.

        更新时间

        :param update_at: The update_at of this JobUpdateRecordListVoResultJobUpdateRecords.
        :type update_at: int
        """
        self._update_at = update_at

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
        if not isinstance(other, JobUpdateRecordListVoResultJobUpdateRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
