# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Bandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'band_width_name': 'str',
        'band_width_id': 'str',
        'band_width_size': 'int',
        'band_width_charge_mode': 'int',
        'band_width_share_type': 'int',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'band_width_name': 'band_width_name',
        'band_width_id': 'band_width_id',
        'band_width_size': 'band_width_size',
        'band_width_charge_mode': 'band_width_charge_mode',
        'band_width_share_type': 'band_width_share_type',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, band_width_name=None, band_width_id=None, band_width_size=None, band_width_charge_mode=None, band_width_share_type=None, create_time=None, update_time=None):
        """Bandwidth

        The model defined in huaweicloud sdk

        :param band_width_name: 云手机服务器的带宽名称。
        :type band_width_name: str
        :param band_width_id: 云手机服务器的带宽唯一标识。
        :type band_width_id: str
        :param band_width_size: 云手机服务器的带宽大小。
        :type band_width_size: int
        :param band_width_charge_mode: 云手机服务器带宽的计费方式。  - 0：bandwidth, 按带宽计费  - 1：traffic, 按流量计费
        :type band_width_charge_mode: int
        :param band_width_share_type: 云手机服务器的带宽类型。  - 0：per，独享带宽 - 1：whole，共享带宽
        :type band_width_share_type: int
        :param create_time: 带宽创建时间，  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。
        :type create_time: str
        :param update_time: 带宽更新时间，  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。
        :type update_time: str
        """
        
        

        self._band_width_name = None
        self._band_width_id = None
        self._band_width_size = None
        self._band_width_charge_mode = None
        self._band_width_share_type = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if band_width_name is not None:
            self.band_width_name = band_width_name
        if band_width_id is not None:
            self.band_width_id = band_width_id
        if band_width_size is not None:
            self.band_width_size = band_width_size
        if band_width_charge_mode is not None:
            self.band_width_charge_mode = band_width_charge_mode
        if band_width_share_type is not None:
            self.band_width_share_type = band_width_share_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def band_width_name(self):
        """Gets the band_width_name of this Bandwidth.

        云手机服务器的带宽名称。

        :return: The band_width_name of this Bandwidth.
        :rtype: str
        """
        return self._band_width_name

    @band_width_name.setter
    def band_width_name(self, band_width_name):
        """Sets the band_width_name of this Bandwidth.

        云手机服务器的带宽名称。

        :param band_width_name: The band_width_name of this Bandwidth.
        :type band_width_name: str
        """
        self._band_width_name = band_width_name

    @property
    def band_width_id(self):
        """Gets the band_width_id of this Bandwidth.

        云手机服务器的带宽唯一标识。

        :return: The band_width_id of this Bandwidth.
        :rtype: str
        """
        return self._band_width_id

    @band_width_id.setter
    def band_width_id(self, band_width_id):
        """Sets the band_width_id of this Bandwidth.

        云手机服务器的带宽唯一标识。

        :param band_width_id: The band_width_id of this Bandwidth.
        :type band_width_id: str
        """
        self._band_width_id = band_width_id

    @property
    def band_width_size(self):
        """Gets the band_width_size of this Bandwidth.

        云手机服务器的带宽大小。

        :return: The band_width_size of this Bandwidth.
        :rtype: int
        """
        return self._band_width_size

    @band_width_size.setter
    def band_width_size(self, band_width_size):
        """Sets the band_width_size of this Bandwidth.

        云手机服务器的带宽大小。

        :param band_width_size: The band_width_size of this Bandwidth.
        :type band_width_size: int
        """
        self._band_width_size = band_width_size

    @property
    def band_width_charge_mode(self):
        """Gets the band_width_charge_mode of this Bandwidth.

        云手机服务器带宽的计费方式。  - 0：bandwidth, 按带宽计费  - 1：traffic, 按流量计费

        :return: The band_width_charge_mode of this Bandwidth.
        :rtype: int
        """
        return self._band_width_charge_mode

    @band_width_charge_mode.setter
    def band_width_charge_mode(self, band_width_charge_mode):
        """Sets the band_width_charge_mode of this Bandwidth.

        云手机服务器带宽的计费方式。  - 0：bandwidth, 按带宽计费  - 1：traffic, 按流量计费

        :param band_width_charge_mode: The band_width_charge_mode of this Bandwidth.
        :type band_width_charge_mode: int
        """
        self._band_width_charge_mode = band_width_charge_mode

    @property
    def band_width_share_type(self):
        """Gets the band_width_share_type of this Bandwidth.

        云手机服务器的带宽类型。  - 0：per，独享带宽 - 1：whole，共享带宽

        :return: The band_width_share_type of this Bandwidth.
        :rtype: int
        """
        return self._band_width_share_type

    @band_width_share_type.setter
    def band_width_share_type(self, band_width_share_type):
        """Sets the band_width_share_type of this Bandwidth.

        云手机服务器的带宽类型。  - 0：per，独享带宽 - 1：whole，共享带宽

        :param band_width_share_type: The band_width_share_type of this Bandwidth.
        :type band_width_share_type: int
        """
        self._band_width_share_type = band_width_share_type

    @property
    def create_time(self):
        """Gets the create_time of this Bandwidth.

        带宽创建时间，  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :return: The create_time of this Bandwidth.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Bandwidth.

        带宽创建时间，  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :param create_time: The create_time of this Bandwidth.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Bandwidth.

        带宽更新时间，  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :return: The update_time of this Bandwidth.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Bandwidth.

        带宽更新时间，  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :param update_time: The update_time of this Bandwidth.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, Bandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
