# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCaseContactInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'area_code': 'str',
        'remind_mobile': 'str',
        'remind_mail': 'str',
        'remind_time': 'str',
        'group_id': 'str',
        'extension_map': 'dict(str, object)'
    }

    attribute_map = {
        'area_code': 'area_code',
        'remind_mobile': 'remind_mobile',
        'remind_mail': 'remind_mail',
        'remind_time': 'remind_time',
        'group_id': 'group_id',
        'extension_map': 'extension_map'
    }

    def __init__(self, area_code=None, remind_mobile=None, remind_mail=None, remind_time=None, group_id=None, extension_map=None):
        """UpdateCaseContactInfoReq

        The model defined in huaweicloud sdk

        :param area_code: 国家码
        :type area_code: str
        :param remind_mobile: 联系手机号
        :type remind_mobile: str
        :param remind_mail: 联系邮箱
        :type remind_mail: str
        :param remind_time: 联系时间
        :type remind_time: str
        :param group_id: 组id
        :type group_id: str
        :param extension_map: 扩展参数
        :type extension_map: dict(str, object)
        """
        
        

        self._area_code = None
        self._remind_mobile = None
        self._remind_mail = None
        self._remind_time = None
        self._group_id = None
        self._extension_map = None
        self.discriminator = None

        if area_code is not None:
            self.area_code = area_code
        if remind_mobile is not None:
            self.remind_mobile = remind_mobile
        if remind_mail is not None:
            self.remind_mail = remind_mail
        if remind_time is not None:
            self.remind_time = remind_time
        if group_id is not None:
            self.group_id = group_id
        if extension_map is not None:
            self.extension_map = extension_map

    @property
    def area_code(self):
        """Gets the area_code of this UpdateCaseContactInfoReq.

        国家码

        :return: The area_code of this UpdateCaseContactInfoReq.
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this UpdateCaseContactInfoReq.

        国家码

        :param area_code: The area_code of this UpdateCaseContactInfoReq.
        :type area_code: str
        """
        self._area_code = area_code

    @property
    def remind_mobile(self):
        """Gets the remind_mobile of this UpdateCaseContactInfoReq.

        联系手机号

        :return: The remind_mobile of this UpdateCaseContactInfoReq.
        :rtype: str
        """
        return self._remind_mobile

    @remind_mobile.setter
    def remind_mobile(self, remind_mobile):
        """Sets the remind_mobile of this UpdateCaseContactInfoReq.

        联系手机号

        :param remind_mobile: The remind_mobile of this UpdateCaseContactInfoReq.
        :type remind_mobile: str
        """
        self._remind_mobile = remind_mobile

    @property
    def remind_mail(self):
        """Gets the remind_mail of this UpdateCaseContactInfoReq.

        联系邮箱

        :return: The remind_mail of this UpdateCaseContactInfoReq.
        :rtype: str
        """
        return self._remind_mail

    @remind_mail.setter
    def remind_mail(self, remind_mail):
        """Sets the remind_mail of this UpdateCaseContactInfoReq.

        联系邮箱

        :param remind_mail: The remind_mail of this UpdateCaseContactInfoReq.
        :type remind_mail: str
        """
        self._remind_mail = remind_mail

    @property
    def remind_time(self):
        """Gets the remind_time of this UpdateCaseContactInfoReq.

        联系时间

        :return: The remind_time of this UpdateCaseContactInfoReq.
        :rtype: str
        """
        return self._remind_time

    @remind_time.setter
    def remind_time(self, remind_time):
        """Sets the remind_time of this UpdateCaseContactInfoReq.

        联系时间

        :param remind_time: The remind_time of this UpdateCaseContactInfoReq.
        :type remind_time: str
        """
        self._remind_time = remind_time

    @property
    def group_id(self):
        """Gets the group_id of this UpdateCaseContactInfoReq.

        组id

        :return: The group_id of this UpdateCaseContactInfoReq.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UpdateCaseContactInfoReq.

        组id

        :param group_id: The group_id of this UpdateCaseContactInfoReq.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def extension_map(self):
        """Gets the extension_map of this UpdateCaseContactInfoReq.

        扩展参数

        :return: The extension_map of this UpdateCaseContactInfoReq.
        :rtype: dict(str, object)
        """
        return self._extension_map

    @extension_map.setter
    def extension_map(self, extension_map):
        """Sets the extension_map of this UpdateCaseContactInfoReq.

        扩展参数

        :param extension_map: The extension_map of this UpdateCaseContactInfoReq.
        :type extension_map: dict(str, object)
        """
        self._extension_map = extension_map

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
        if not isinstance(other, UpdateCaseContactInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
