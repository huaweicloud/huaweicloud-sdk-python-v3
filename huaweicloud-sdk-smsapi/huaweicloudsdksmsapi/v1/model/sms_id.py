# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsID:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "SmsID"

    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        '_from': 'str',
        'origin_to': 'str',
        'sms_msg_id': 'str',
        'status': 'str',
        'country_id': 'str',
        'total': 'int'
    }

    attribute_map = {
        'create_time': 'createTime',
        '_from': 'from',
        'origin_to': 'originTo',
        'sms_msg_id': 'smsMsgId',
        'status': 'status',
        'country_id': 'countryId',
        'total': 'total'
    }

    def __init__(self, create_time=None, _from=None, origin_to=None, sms_msg_id=None, status=None, country_id=None, total=None):
        r"""SmsID

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param _from: 发送短信号码
        :type _from: str
        :param origin_to: 接收短信号码
        :type origin_to: str
        :param sms_msg_id: 短信id
        :type sms_msg_id: str
        :param status: 短信当前状态
        :type status: str
        :param country_id: 国家码
        :type country_id: str
        :param total: 短信拆分条数
        :type total: int
        """
        
        

        self._create_time = None
        self.__from = None
        self._origin_to = None
        self._sms_msg_id = None
        self._status = None
        self._country_id = None
        self._total = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if _from is not None:
            self._from = _from
        if origin_to is not None:
            self.origin_to = origin_to
        if sms_msg_id is not None:
            self.sms_msg_id = sms_msg_id
        if status is not None:
            self.status = status
        if country_id is not None:
            self.country_id = country_id
        if total is not None:
            self.total = total

    @property
    def create_time(self):
        r"""Gets the create_time of this SmsID.

        创建时间

        :return: The create_time of this SmsID.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SmsID.

        创建时间

        :param create_time: The create_time of this SmsID.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def _from(self):
        r"""Gets the _from of this SmsID.

        发送短信号码

        :return: The _from of this SmsID.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this SmsID.

        发送短信号码

        :param _from: The _from of this SmsID.
        :type _from: str
        """
        self.__from = _from

    @property
    def origin_to(self):
        r"""Gets the origin_to of this SmsID.

        接收短信号码

        :return: The origin_to of this SmsID.
        :rtype: str
        """
        return self._origin_to

    @origin_to.setter
    def origin_to(self, origin_to):
        r"""Sets the origin_to of this SmsID.

        接收短信号码

        :param origin_to: The origin_to of this SmsID.
        :type origin_to: str
        """
        self._origin_to = origin_to

    @property
    def sms_msg_id(self):
        r"""Gets the sms_msg_id of this SmsID.

        短信id

        :return: The sms_msg_id of this SmsID.
        :rtype: str
        """
        return self._sms_msg_id

    @sms_msg_id.setter
    def sms_msg_id(self, sms_msg_id):
        r"""Sets the sms_msg_id of this SmsID.

        短信id

        :param sms_msg_id: The sms_msg_id of this SmsID.
        :type sms_msg_id: str
        """
        self._sms_msg_id = sms_msg_id

    @property
    def status(self):
        r"""Gets the status of this SmsID.

        短信当前状态

        :return: The status of this SmsID.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SmsID.

        短信当前状态

        :param status: The status of this SmsID.
        :type status: str
        """
        self._status = status

    @property
    def country_id(self):
        r"""Gets the country_id of this SmsID.

        国家码

        :return: The country_id of this SmsID.
        :rtype: str
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        r"""Sets the country_id of this SmsID.

        国家码

        :param country_id: The country_id of this SmsID.
        :type country_id: str
        """
        self._country_id = country_id

    @property
    def total(self):
        r"""Gets the total of this SmsID.

        短信拆分条数

        :return: The total of this SmsID.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SmsID.

        短信拆分条数

        :param total: The total of this SmsID.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, SmsID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
