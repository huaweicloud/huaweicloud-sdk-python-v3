# coding: utf-8

import pprint
import re

import six





class RestInviteWithPwdReqBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'call_num': 'str',
        'org_id': 'str',
        'conf_id': 'str',
        'pwd': 'str',
        'num_belongs_type': 'int',
        'is_not_overlay_pid_name': 'bool'
    }

    attribute_map = {
        'call_num': 'callNum',
        'org_id': 'orgID',
        'conf_id': 'confID',
        'pwd': 'pwd',
        'num_belongs_type': 'numBelongsType',
        'is_not_overlay_pid_name': 'isNotOverlayPidName'
    }

    def __init__(self, call_num=None, org_id=None, conf_id=None, pwd=None, num_belongs_type=None, is_not_overlay_pid_name=None):
        """RestInviteWithPwdReqBody - a model defined in huaweicloud sdk"""
        
        

        self._call_num = None
        self._org_id = None
        self._conf_id = None
        self._pwd = None
        self._num_belongs_type = None
        self._is_not_overlay_pid_name = None
        self.discriminator = None

        if call_num is not None:
            self.call_num = call_num
        if org_id is not None:
            self.org_id = org_id
        if conf_id is not None:
            self.conf_id = conf_id
        if pwd is not None:
            self.pwd = pwd
        if num_belongs_type is not None:
            self.num_belongs_type = num_belongs_type
        if is_not_overlay_pid_name is not None:
            self.is_not_overlay_pid_name = is_not_overlay_pid_name

    @property
    def call_num(self):
        """Gets the call_num of this RestInviteWithPwdReqBody.

        被邀请的会议人号码。

        :return: The call_num of this RestInviteWithPwdReqBody.
        :rtype: str
        """
        return self._call_num

    @call_num.setter
    def call_num(self, call_num):
        """Sets the call_num of this RestInviteWithPwdReqBody.

        被邀请的会议人号码。

        :param call_num: The call_num of this RestInviteWithPwdReqBody.
        :type: str
        """
        self._call_num = call_num

    @property
    def org_id(self):
        """Gets the org_id of this RestInviteWithPwdReqBody.

        被邀请的会议人所属企业ID。

        :return: The org_id of this RestInviteWithPwdReqBody.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this RestInviteWithPwdReqBody.

        被邀请的会议人所属企业ID。

        :param org_id: The org_id of this RestInviteWithPwdReqBody.
        :type: str
        """
        self._org_id = org_id

    @property
    def conf_id(self):
        """Gets the conf_id of this RestInviteWithPwdReqBody.

        当前会议ID。

        :return: The conf_id of this RestInviteWithPwdReqBody.
        :rtype: str
        """
        return self._conf_id

    @conf_id.setter
    def conf_id(self, conf_id):
        """Sets the conf_id of this RestInviteWithPwdReqBody.

        当前会议ID。

        :param conf_id: The conf_id of this RestInviteWithPwdReqBody.
        :type: str
        """
        self._conf_id = conf_id

    @property
    def pwd(self):
        """Gets the pwd of this RestInviteWithPwdReqBody.

        当前会议的密码。

        :return: The pwd of this RestInviteWithPwdReqBody.
        :rtype: str
        """
        return self._pwd

    @pwd.setter
    def pwd(self, pwd):
        """Sets the pwd of this RestInviteWithPwdReqBody.

        当前会议的密码。

        :param pwd: The pwd of this RestInviteWithPwdReqBody.
        :type: str
        """
        self._pwd = pwd

    @property
    def num_belongs_type(self):
        """Gets the num_belongs_type of this RestInviteWithPwdReqBody.

        号码类型0是本局号码，1是中继号码。

        :return: The num_belongs_type of this RestInviteWithPwdReqBody.
        :rtype: int
        """
        return self._num_belongs_type

    @num_belongs_type.setter
    def num_belongs_type(self, num_belongs_type):
        """Sets the num_belongs_type of this RestInviteWithPwdReqBody.

        号码类型0是本局号码，1是中继号码。

        :param num_belongs_type: The num_belongs_type of this RestInviteWithPwdReqBody.
        :type: int
        """
        self._num_belongs_type = num_belongs_type

    @property
    def is_not_overlay_pid_name(self):
        """Gets the is_not_overlay_pid_name of this RestInviteWithPwdReqBody.

        是否不叠加会场名。

        :return: The is_not_overlay_pid_name of this RestInviteWithPwdReqBody.
        :rtype: bool
        """
        return self._is_not_overlay_pid_name

    @is_not_overlay_pid_name.setter
    def is_not_overlay_pid_name(self, is_not_overlay_pid_name):
        """Sets the is_not_overlay_pid_name of this RestInviteWithPwdReqBody.

        是否不叠加会场名。

        :param is_not_overlay_pid_name: The is_not_overlay_pid_name of this RestInviteWithPwdReqBody.
        :type: bool
        """
        self._is_not_overlay_pid_name = is_not_overlay_pid_name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RestInviteWithPwdReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
