# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeliveryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'room_code': 'str',
        'contacts': 'list[ContactInformation]',
        'assets': 'list[AssetInfo]'
    }

    attribute_map = {
        'type': 'type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'room_code': 'room_code',
        'contacts': 'contacts',
        'assets': 'assets'
    }

    def __init__(self, type=None, start_time=None, end_time=None, room_code=None, contacts=None, assets=None):
        r"""DeliveryInfo

        The model defined in huaweicloud sdk

        :param type: 类型，收货/发货
        :type type: str
        :param start_time: 起始时间，UTC格式
        :type start_time: str
        :param end_time: 结束时间，UTC格式
        :type end_time: str
        :param room_code: 机房编码
        :type room_code: str
        :param contacts: 联系人
        :type contacts: list[:class:`huaweicloudsdkdcos.v1.ContactInformation`]
        :param assets: 资产清单
        :type assets: list[:class:`huaweicloudsdkdcos.v1.AssetInfo`]
        """
        
        

        self._type = None
        self._start_time = None
        self._end_time = None
        self._room_code = None
        self._contacts = None
        self._assets = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if room_code is not None:
            self.room_code = room_code
        if contacts is not None:
            self.contacts = contacts
        if assets is not None:
            self.assets = assets

    @property
    def type(self):
        r"""Gets the type of this DeliveryInfo.

        类型，收货/发货

        :return: The type of this DeliveryInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeliveryInfo.

        类型，收货/发货

        :param type: The type of this DeliveryInfo.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        r"""Gets the start_time of this DeliveryInfo.

        起始时间，UTC格式

        :return: The start_time of this DeliveryInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DeliveryInfo.

        起始时间，UTC格式

        :param start_time: The start_time of this DeliveryInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DeliveryInfo.

        结束时间，UTC格式

        :return: The end_time of this DeliveryInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DeliveryInfo.

        结束时间，UTC格式

        :param end_time: The end_time of this DeliveryInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def room_code(self):
        r"""Gets the room_code of this DeliveryInfo.

        机房编码

        :return: The room_code of this DeliveryInfo.
        :rtype: str
        """
        return self._room_code

    @room_code.setter
    def room_code(self, room_code):
        r"""Sets the room_code of this DeliveryInfo.

        机房编码

        :param room_code: The room_code of this DeliveryInfo.
        :type room_code: str
        """
        self._room_code = room_code

    @property
    def contacts(self):
        r"""Gets the contacts of this DeliveryInfo.

        联系人

        :return: The contacts of this DeliveryInfo.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.ContactInformation`]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        r"""Sets the contacts of this DeliveryInfo.

        联系人

        :param contacts: The contacts of this DeliveryInfo.
        :type contacts: list[:class:`huaweicloudsdkdcos.v1.ContactInformation`]
        """
        self._contacts = contacts

    @property
    def assets(self):
        r"""Gets the assets of this DeliveryInfo.

        资产清单

        :return: The assets of this DeliveryInfo.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.AssetInfo`]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        r"""Sets the assets of this DeliveryInfo.

        资产清单

        :param assets: The assets of this DeliveryInfo.
        :type assets: list[:class:`huaweicloudsdkdcos.v1.AssetInfo`]
        """
        self._assets = assets

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
        if not isinstance(other, DeliveryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
