# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailabilityZoneInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'display_name': 'str',
        'i18n': 'dict(str, str)',
        'sold_out': 'SoldOutInfo',
        'product_ids': 'list[str]',
        'visible': 'bool',
        'default_availability_zone': 'bool'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'display_name': 'display_name',
        'i18n': 'i18n',
        'sold_out': 'sold_out',
        'product_ids': 'product_ids',
        'visible': 'visible',
        'default_availability_zone': 'default_availability_zone'
    }

    def __init__(self, availability_zone=None, display_name=None, i18n=None, sold_out=None, product_ids=None, visible=None, default_availability_zone=None):
        """AvailabilityZoneInfo

        The model defined in huaweicloud sdk

        :param availability_zone: 可用分区编码。
        :type availability_zone: str
        :param display_name: 可用分区名称。
        :type display_name: str
        :param i18n: 可用分区国际化信息。
        :type i18n: dict(str, str)
        :param sold_out: 
        :type sold_out: :class:`huaweicloudsdkworkspaceapp.v1.SoldOutInfo`
        :param product_ids: 指定当前分区下自定义支持的产品ID列表，如果为空则支持所有套餐。
        :type product_ids: list[str]
        :param visible: 是否可见。
        :type visible: bool
        :param default_availability_zone: 是否默认可用分区。
        :type default_availability_zone: bool
        """
        
        

        self._availability_zone = None
        self._display_name = None
        self._i18n = None
        self._sold_out = None
        self._product_ids = None
        self._visible = None
        self._default_availability_zone = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if display_name is not None:
            self.display_name = display_name
        if i18n is not None:
            self.i18n = i18n
        if sold_out is not None:
            self.sold_out = sold_out
        if product_ids is not None:
            self.product_ids = product_ids
        if visible is not None:
            self.visible = visible
        if default_availability_zone is not None:
            self.default_availability_zone = default_availability_zone

    @property
    def availability_zone(self):
        """Gets the availability_zone of this AvailabilityZoneInfo.

        可用分区编码。

        :return: The availability_zone of this AvailabilityZoneInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this AvailabilityZoneInfo.

        可用分区编码。

        :param availability_zone: The availability_zone of this AvailabilityZoneInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def display_name(self):
        """Gets the display_name of this AvailabilityZoneInfo.

        可用分区名称。

        :return: The display_name of this AvailabilityZoneInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AvailabilityZoneInfo.

        可用分区名称。

        :param display_name: The display_name of this AvailabilityZoneInfo.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def i18n(self):
        """Gets the i18n of this AvailabilityZoneInfo.

        可用分区国际化信息。

        :return: The i18n of this AvailabilityZoneInfo.
        :rtype: dict(str, str)
        """
        return self._i18n

    @i18n.setter
    def i18n(self, i18n):
        """Sets the i18n of this AvailabilityZoneInfo.

        可用分区国际化信息。

        :param i18n: The i18n of this AvailabilityZoneInfo.
        :type i18n: dict(str, str)
        """
        self._i18n = i18n

    @property
    def sold_out(self):
        """Gets the sold_out of this AvailabilityZoneInfo.

        :return: The sold_out of this AvailabilityZoneInfo.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.SoldOutInfo`
        """
        return self._sold_out

    @sold_out.setter
    def sold_out(self, sold_out):
        """Sets the sold_out of this AvailabilityZoneInfo.

        :param sold_out: The sold_out of this AvailabilityZoneInfo.
        :type sold_out: :class:`huaweicloudsdkworkspaceapp.v1.SoldOutInfo`
        """
        self._sold_out = sold_out

    @property
    def product_ids(self):
        """Gets the product_ids of this AvailabilityZoneInfo.

        指定当前分区下自定义支持的产品ID列表，如果为空则支持所有套餐。

        :return: The product_ids of this AvailabilityZoneInfo.
        :rtype: list[str]
        """
        return self._product_ids

    @product_ids.setter
    def product_ids(self, product_ids):
        """Sets the product_ids of this AvailabilityZoneInfo.

        指定当前分区下自定义支持的产品ID列表，如果为空则支持所有套餐。

        :param product_ids: The product_ids of this AvailabilityZoneInfo.
        :type product_ids: list[str]
        """
        self._product_ids = product_ids

    @property
    def visible(self):
        """Gets the visible of this AvailabilityZoneInfo.

        是否可见。

        :return: The visible of this AvailabilityZoneInfo.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this AvailabilityZoneInfo.

        是否可见。

        :param visible: The visible of this AvailabilityZoneInfo.
        :type visible: bool
        """
        self._visible = visible

    @property
    def default_availability_zone(self):
        """Gets the default_availability_zone of this AvailabilityZoneInfo.

        是否默认可用分区。

        :return: The default_availability_zone of this AvailabilityZoneInfo.
        :rtype: bool
        """
        return self._default_availability_zone

    @default_availability_zone.setter
    def default_availability_zone(self, default_availability_zone):
        """Sets the default_availability_zone of this AvailabilityZoneInfo.

        是否默认可用分区。

        :param default_availability_zone: The default_availability_zone of this AvailabilityZoneInfo.
        :type default_availability_zone: bool
        """
        self._default_availability_zone = default_availability_zone

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
        if not isinstance(other, AvailabilityZoneInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
