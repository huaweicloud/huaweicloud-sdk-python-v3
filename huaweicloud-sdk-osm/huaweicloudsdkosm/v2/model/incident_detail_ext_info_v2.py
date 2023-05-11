# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentDetailExtInfoV2:

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
        'contact_type': 'str',
        'remind_time': 'str',
        'cc_email': 'str',
        'commodity_id': 'str'
    }

    attribute_map = {
        'area_code': 'area_code',
        'remind_mobile': 'remind_mobile',
        'remind_mail': 'remind_mail',
        'contact_type': 'contact_type',
        'remind_time': 'remind_time',
        'cc_email': 'cc_email',
        'commodity_id': 'commodity_id'
    }

    def __init__(self, area_code=None, remind_mobile=None, remind_mail=None, contact_type=None, remind_time=None, cc_email=None, commodity_id=None):
        """IncidentDetailExtInfoV2

        The model defined in huaweicloud sdk

        :param area_code: 国家码
        :type area_code: str
        :param remind_mobile: 提醒手机
        :type remind_mobile: str
        :param remind_mail: 提醒邮箱
        :type remind_mail: str
        :param contact_type: 联系方式类型
        :type contact_type: str
        :param remind_time: 提醒时间
        :type remind_time: str
        :param cc_email: 抄送邮箱
        :type cc_email: str
        :param commodity_id: ISV商品id
        :type commodity_id: str
        """
        
        

        self._area_code = None
        self._remind_mobile = None
        self._remind_mail = None
        self._contact_type = None
        self._remind_time = None
        self._cc_email = None
        self._commodity_id = None
        self.discriminator = None

        if area_code is not None:
            self.area_code = area_code
        if remind_mobile is not None:
            self.remind_mobile = remind_mobile
        if remind_mail is not None:
            self.remind_mail = remind_mail
        if contact_type is not None:
            self.contact_type = contact_type
        if remind_time is not None:
            self.remind_time = remind_time
        if cc_email is not None:
            self.cc_email = cc_email
        if commodity_id is not None:
            self.commodity_id = commodity_id

    @property
    def area_code(self):
        """Gets the area_code of this IncidentDetailExtInfoV2.

        国家码

        :return: The area_code of this IncidentDetailExtInfoV2.
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this IncidentDetailExtInfoV2.

        国家码

        :param area_code: The area_code of this IncidentDetailExtInfoV2.
        :type area_code: str
        """
        self._area_code = area_code

    @property
    def remind_mobile(self):
        """Gets the remind_mobile of this IncidentDetailExtInfoV2.

        提醒手机

        :return: The remind_mobile of this IncidentDetailExtInfoV2.
        :rtype: str
        """
        return self._remind_mobile

    @remind_mobile.setter
    def remind_mobile(self, remind_mobile):
        """Sets the remind_mobile of this IncidentDetailExtInfoV2.

        提醒手机

        :param remind_mobile: The remind_mobile of this IncidentDetailExtInfoV2.
        :type remind_mobile: str
        """
        self._remind_mobile = remind_mobile

    @property
    def remind_mail(self):
        """Gets the remind_mail of this IncidentDetailExtInfoV2.

        提醒邮箱

        :return: The remind_mail of this IncidentDetailExtInfoV2.
        :rtype: str
        """
        return self._remind_mail

    @remind_mail.setter
    def remind_mail(self, remind_mail):
        """Sets the remind_mail of this IncidentDetailExtInfoV2.

        提醒邮箱

        :param remind_mail: The remind_mail of this IncidentDetailExtInfoV2.
        :type remind_mail: str
        """
        self._remind_mail = remind_mail

    @property
    def contact_type(self):
        """Gets the contact_type of this IncidentDetailExtInfoV2.

        联系方式类型

        :return: The contact_type of this IncidentDetailExtInfoV2.
        :rtype: str
        """
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        """Sets the contact_type of this IncidentDetailExtInfoV2.

        联系方式类型

        :param contact_type: The contact_type of this IncidentDetailExtInfoV2.
        :type contact_type: str
        """
        self._contact_type = contact_type

    @property
    def remind_time(self):
        """Gets the remind_time of this IncidentDetailExtInfoV2.

        提醒时间

        :return: The remind_time of this IncidentDetailExtInfoV2.
        :rtype: str
        """
        return self._remind_time

    @remind_time.setter
    def remind_time(self, remind_time):
        """Sets the remind_time of this IncidentDetailExtInfoV2.

        提醒时间

        :param remind_time: The remind_time of this IncidentDetailExtInfoV2.
        :type remind_time: str
        """
        self._remind_time = remind_time

    @property
    def cc_email(self):
        """Gets the cc_email of this IncidentDetailExtInfoV2.

        抄送邮箱

        :return: The cc_email of this IncidentDetailExtInfoV2.
        :rtype: str
        """
        return self._cc_email

    @cc_email.setter
    def cc_email(self, cc_email):
        """Sets the cc_email of this IncidentDetailExtInfoV2.

        抄送邮箱

        :param cc_email: The cc_email of this IncidentDetailExtInfoV2.
        :type cc_email: str
        """
        self._cc_email = cc_email

    @property
    def commodity_id(self):
        """Gets the commodity_id of this IncidentDetailExtInfoV2.

        ISV商品id

        :return: The commodity_id of this IncidentDetailExtInfoV2.
        :rtype: str
        """
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, commodity_id):
        """Sets the commodity_id of this IncidentDetailExtInfoV2.

        ISV商品id

        :param commodity_id: The commodity_id of this IncidentDetailExtInfoV2.
        :type commodity_id: str
        """
        self._commodity_id = commodity_id

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
        if not isinstance(other, IncidentDetailExtInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
