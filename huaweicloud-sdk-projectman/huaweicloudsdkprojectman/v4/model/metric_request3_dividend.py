# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricRequest3Dividend:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'on_time': 'str',
        'custom_field16': 'str',
        'custom_field17': 'str',
        'custom_field18': 'str',
        'custom_field19': 'str',
        'custom_field20': 'str',
        'custom_field21': 'str',
        'custom_field22': 'str',
        'custom_field23': 'str',
        'custom_field24': 'str',
        'custom_field25': 'str',
        'custom_field26': 'str',
        'custom_field27': 'str',
        'custom_field28': 'str',
        'custom_field29': 'str',
        'custom_field30': 'str',
        'custom_field31': 'str',
        'custom_field32': 'str',
        'custom_field33': 'str',
        'custom_field34': 'str',
        'custom_field35': 'str',
        'custom_field36': 'str',
        'custom_field37': 'str',
        'custom_field38': 'str',
        'custom_field39': 'str',
        'custom_field40': 'str'
    }

    attribute_map = {
        'on_time': 'on_time',
        'custom_field16': 'custom_field16',
        'custom_field17': 'custom_field17',
        'custom_field18': 'custom_field18',
        'custom_field19': 'custom_field19',
        'custom_field20': 'custom_field20',
        'custom_field21': 'custom_field21',
        'custom_field22': 'custom_field22',
        'custom_field23': 'custom_field23',
        'custom_field24': 'custom_field24',
        'custom_field25': 'custom_field25',
        'custom_field26': 'custom_field26',
        'custom_field27': 'custom_field27',
        'custom_field28': 'custom_field28',
        'custom_field29': 'custom_field29',
        'custom_field30': 'custom_field30',
        'custom_field31': 'custom_field31',
        'custom_field32': 'custom_field32',
        'custom_field33': 'custom_field33',
        'custom_field34': 'custom_field34',
        'custom_field35': 'custom_field35',
        'custom_field36': 'custom_field36',
        'custom_field37': 'custom_field37',
        'custom_field38': 'custom_field38',
        'custom_field39': 'custom_field39',
        'custom_field40': 'custom_field40'
    }

    def __init__(self, on_time=None, custom_field16=None, custom_field17=None, custom_field18=None, custom_field19=None, custom_field20=None, custom_field21=None, custom_field22=None, custom_field23=None, custom_field24=None, custom_field25=None, custom_field26=None, custom_field27=None, custom_field28=None, custom_field29=None, custom_field30=None, custom_field31=None, custom_field32=None, custom_field33=None, custom_field34=None, custom_field35=None, custom_field36=None, custom_field37=None, custom_field38=None, custom_field39=None, custom_field40=None):
        """MetricRequest3Dividend

        The model defined in huaweicloud sdk

        :param on_time: 是否按时
        :type on_time: str
        :param custom_field16: 自定义字段
        :type custom_field16: str
        :param custom_field17: 自定义字段
        :type custom_field17: str
        :param custom_field18: 自定义字段
        :type custom_field18: str
        :param custom_field19: 自定义字段
        :type custom_field19: str
        :param custom_field20: 自定义字段
        :type custom_field20: str
        :param custom_field21: 自定义字段
        :type custom_field21: str
        :param custom_field22: 自定义字段
        :type custom_field22: str
        :param custom_field23: 自定义字段
        :type custom_field23: str
        :param custom_field24: 自定义字段
        :type custom_field24: str
        :param custom_field25: 自定义字段
        :type custom_field25: str
        :param custom_field26: 自定义字段
        :type custom_field26: str
        :param custom_field27: 自定义字段
        :type custom_field27: str
        :param custom_field28: 自定义字段
        :type custom_field28: str
        :param custom_field29: 自定义字段
        :type custom_field29: str
        :param custom_field30: 自定义字段
        :type custom_field30: str
        :param custom_field31: 自定义字段
        :type custom_field31: str
        :param custom_field32: 自定义字段
        :type custom_field32: str
        :param custom_field33: 自定义字段
        :type custom_field33: str
        :param custom_field34: 自定义字段
        :type custom_field34: str
        :param custom_field35: 自定义字段
        :type custom_field35: str
        :param custom_field36: 自定义字段
        :type custom_field36: str
        :param custom_field37: 自定义字段
        :type custom_field37: str
        :param custom_field38: 自定义字段
        :type custom_field38: str
        :param custom_field39: 自定义字段
        :type custom_field39: str
        :param custom_field40: 自定义字段
        :type custom_field40: str
        """
        
        

        self._on_time = None
        self._custom_field16 = None
        self._custom_field17 = None
        self._custom_field18 = None
        self._custom_field19 = None
        self._custom_field20 = None
        self._custom_field21 = None
        self._custom_field22 = None
        self._custom_field23 = None
        self._custom_field24 = None
        self._custom_field25 = None
        self._custom_field26 = None
        self._custom_field27 = None
        self._custom_field28 = None
        self._custom_field29 = None
        self._custom_field30 = None
        self._custom_field31 = None
        self._custom_field32 = None
        self._custom_field33 = None
        self._custom_field34 = None
        self._custom_field35 = None
        self._custom_field36 = None
        self._custom_field37 = None
        self._custom_field38 = None
        self._custom_field39 = None
        self._custom_field40 = None
        self.discriminator = None

        if on_time is not None:
            self.on_time = on_time
        if custom_field16 is not None:
            self.custom_field16 = custom_field16
        if custom_field17 is not None:
            self.custom_field17 = custom_field17
        if custom_field18 is not None:
            self.custom_field18 = custom_field18
        if custom_field19 is not None:
            self.custom_field19 = custom_field19
        if custom_field20 is not None:
            self.custom_field20 = custom_field20
        if custom_field21 is not None:
            self.custom_field21 = custom_field21
        if custom_field22 is not None:
            self.custom_field22 = custom_field22
        if custom_field23 is not None:
            self.custom_field23 = custom_field23
        if custom_field24 is not None:
            self.custom_field24 = custom_field24
        if custom_field25 is not None:
            self.custom_field25 = custom_field25
        if custom_field26 is not None:
            self.custom_field26 = custom_field26
        if custom_field27 is not None:
            self.custom_field27 = custom_field27
        if custom_field28 is not None:
            self.custom_field28 = custom_field28
        if custom_field29 is not None:
            self.custom_field29 = custom_field29
        if custom_field30 is not None:
            self.custom_field30 = custom_field30
        if custom_field31 is not None:
            self.custom_field31 = custom_field31
        if custom_field32 is not None:
            self.custom_field32 = custom_field32
        if custom_field33 is not None:
            self.custom_field33 = custom_field33
        if custom_field34 is not None:
            self.custom_field34 = custom_field34
        if custom_field35 is not None:
            self.custom_field35 = custom_field35
        if custom_field36 is not None:
            self.custom_field36 = custom_field36
        if custom_field37 is not None:
            self.custom_field37 = custom_field37
        if custom_field38 is not None:
            self.custom_field38 = custom_field38
        if custom_field39 is not None:
            self.custom_field39 = custom_field39
        if custom_field40 is not None:
            self.custom_field40 = custom_field40

    @property
    def on_time(self):
        """Gets the on_time of this MetricRequest3Dividend.

        是否按时

        :return: The on_time of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._on_time

    @on_time.setter
    def on_time(self, on_time):
        """Sets the on_time of this MetricRequest3Dividend.

        是否按时

        :param on_time: The on_time of this MetricRequest3Dividend.
        :type on_time: str
        """
        self._on_time = on_time

    @property
    def custom_field16(self):
        """Gets the custom_field16 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field16 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field16

    @custom_field16.setter
    def custom_field16(self, custom_field16):
        """Sets the custom_field16 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field16: The custom_field16 of this MetricRequest3Dividend.
        :type custom_field16: str
        """
        self._custom_field16 = custom_field16

    @property
    def custom_field17(self):
        """Gets the custom_field17 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field17 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field17

    @custom_field17.setter
    def custom_field17(self, custom_field17):
        """Sets the custom_field17 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field17: The custom_field17 of this MetricRequest3Dividend.
        :type custom_field17: str
        """
        self._custom_field17 = custom_field17

    @property
    def custom_field18(self):
        """Gets the custom_field18 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field18 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field18

    @custom_field18.setter
    def custom_field18(self, custom_field18):
        """Sets the custom_field18 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field18: The custom_field18 of this MetricRequest3Dividend.
        :type custom_field18: str
        """
        self._custom_field18 = custom_field18

    @property
    def custom_field19(self):
        """Gets the custom_field19 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field19 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field19

    @custom_field19.setter
    def custom_field19(self, custom_field19):
        """Sets the custom_field19 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field19: The custom_field19 of this MetricRequest3Dividend.
        :type custom_field19: str
        """
        self._custom_field19 = custom_field19

    @property
    def custom_field20(self):
        """Gets the custom_field20 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field20 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field20

    @custom_field20.setter
    def custom_field20(self, custom_field20):
        """Sets the custom_field20 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field20: The custom_field20 of this MetricRequest3Dividend.
        :type custom_field20: str
        """
        self._custom_field20 = custom_field20

    @property
    def custom_field21(self):
        """Gets the custom_field21 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field21 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field21

    @custom_field21.setter
    def custom_field21(self, custom_field21):
        """Sets the custom_field21 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field21: The custom_field21 of this MetricRequest3Dividend.
        :type custom_field21: str
        """
        self._custom_field21 = custom_field21

    @property
    def custom_field22(self):
        """Gets the custom_field22 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field22 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field22

    @custom_field22.setter
    def custom_field22(self, custom_field22):
        """Sets the custom_field22 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field22: The custom_field22 of this MetricRequest3Dividend.
        :type custom_field22: str
        """
        self._custom_field22 = custom_field22

    @property
    def custom_field23(self):
        """Gets the custom_field23 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field23 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field23

    @custom_field23.setter
    def custom_field23(self, custom_field23):
        """Sets the custom_field23 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field23: The custom_field23 of this MetricRequest3Dividend.
        :type custom_field23: str
        """
        self._custom_field23 = custom_field23

    @property
    def custom_field24(self):
        """Gets the custom_field24 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field24 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field24

    @custom_field24.setter
    def custom_field24(self, custom_field24):
        """Sets the custom_field24 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field24: The custom_field24 of this MetricRequest3Dividend.
        :type custom_field24: str
        """
        self._custom_field24 = custom_field24

    @property
    def custom_field25(self):
        """Gets the custom_field25 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field25 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field25

    @custom_field25.setter
    def custom_field25(self, custom_field25):
        """Sets the custom_field25 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field25: The custom_field25 of this MetricRequest3Dividend.
        :type custom_field25: str
        """
        self._custom_field25 = custom_field25

    @property
    def custom_field26(self):
        """Gets the custom_field26 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field26 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field26

    @custom_field26.setter
    def custom_field26(self, custom_field26):
        """Sets the custom_field26 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field26: The custom_field26 of this MetricRequest3Dividend.
        :type custom_field26: str
        """
        self._custom_field26 = custom_field26

    @property
    def custom_field27(self):
        """Gets the custom_field27 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field27 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field27

    @custom_field27.setter
    def custom_field27(self, custom_field27):
        """Sets the custom_field27 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field27: The custom_field27 of this MetricRequest3Dividend.
        :type custom_field27: str
        """
        self._custom_field27 = custom_field27

    @property
    def custom_field28(self):
        """Gets the custom_field28 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field28 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field28

    @custom_field28.setter
    def custom_field28(self, custom_field28):
        """Sets the custom_field28 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field28: The custom_field28 of this MetricRequest3Dividend.
        :type custom_field28: str
        """
        self._custom_field28 = custom_field28

    @property
    def custom_field29(self):
        """Gets the custom_field29 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field29 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field29

    @custom_field29.setter
    def custom_field29(self, custom_field29):
        """Sets the custom_field29 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field29: The custom_field29 of this MetricRequest3Dividend.
        :type custom_field29: str
        """
        self._custom_field29 = custom_field29

    @property
    def custom_field30(self):
        """Gets the custom_field30 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field30 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field30

    @custom_field30.setter
    def custom_field30(self, custom_field30):
        """Sets the custom_field30 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field30: The custom_field30 of this MetricRequest3Dividend.
        :type custom_field30: str
        """
        self._custom_field30 = custom_field30

    @property
    def custom_field31(self):
        """Gets the custom_field31 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field31 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field31

    @custom_field31.setter
    def custom_field31(self, custom_field31):
        """Sets the custom_field31 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field31: The custom_field31 of this MetricRequest3Dividend.
        :type custom_field31: str
        """
        self._custom_field31 = custom_field31

    @property
    def custom_field32(self):
        """Gets the custom_field32 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field32 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field32

    @custom_field32.setter
    def custom_field32(self, custom_field32):
        """Sets the custom_field32 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field32: The custom_field32 of this MetricRequest3Dividend.
        :type custom_field32: str
        """
        self._custom_field32 = custom_field32

    @property
    def custom_field33(self):
        """Gets the custom_field33 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field33 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field33

    @custom_field33.setter
    def custom_field33(self, custom_field33):
        """Sets the custom_field33 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field33: The custom_field33 of this MetricRequest3Dividend.
        :type custom_field33: str
        """
        self._custom_field33 = custom_field33

    @property
    def custom_field34(self):
        """Gets the custom_field34 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field34 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field34

    @custom_field34.setter
    def custom_field34(self, custom_field34):
        """Sets the custom_field34 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field34: The custom_field34 of this MetricRequest3Dividend.
        :type custom_field34: str
        """
        self._custom_field34 = custom_field34

    @property
    def custom_field35(self):
        """Gets the custom_field35 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field35 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field35

    @custom_field35.setter
    def custom_field35(self, custom_field35):
        """Sets the custom_field35 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field35: The custom_field35 of this MetricRequest3Dividend.
        :type custom_field35: str
        """
        self._custom_field35 = custom_field35

    @property
    def custom_field36(self):
        """Gets the custom_field36 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field36 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field36

    @custom_field36.setter
    def custom_field36(self, custom_field36):
        """Sets the custom_field36 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field36: The custom_field36 of this MetricRequest3Dividend.
        :type custom_field36: str
        """
        self._custom_field36 = custom_field36

    @property
    def custom_field37(self):
        """Gets the custom_field37 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field37 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field37

    @custom_field37.setter
    def custom_field37(self, custom_field37):
        """Sets the custom_field37 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field37: The custom_field37 of this MetricRequest3Dividend.
        :type custom_field37: str
        """
        self._custom_field37 = custom_field37

    @property
    def custom_field38(self):
        """Gets the custom_field38 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field38 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field38

    @custom_field38.setter
    def custom_field38(self, custom_field38):
        """Sets the custom_field38 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field38: The custom_field38 of this MetricRequest3Dividend.
        :type custom_field38: str
        """
        self._custom_field38 = custom_field38

    @property
    def custom_field39(self):
        """Gets the custom_field39 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field39 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field39

    @custom_field39.setter
    def custom_field39(self, custom_field39):
        """Sets the custom_field39 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field39: The custom_field39 of this MetricRequest3Dividend.
        :type custom_field39: str
        """
        self._custom_field39 = custom_field39

    @property
    def custom_field40(self):
        """Gets the custom_field40 of this MetricRequest3Dividend.

        自定义字段

        :return: The custom_field40 of this MetricRequest3Dividend.
        :rtype: str
        """
        return self._custom_field40

    @custom_field40.setter
    def custom_field40(self, custom_field40):
        """Sets the custom_field40 of this MetricRequest3Dividend.

        自定义字段

        :param custom_field40: The custom_field40 of this MetricRequest3Dividend.
        :type custom_field40: str
        """
        self._custom_field40 = custom_field40

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
        if not isinstance(other, MetricRequest3Dividend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
