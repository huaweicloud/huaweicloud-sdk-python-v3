# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AzInfo:

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
        'i18n': 'I18n',
        'default_availability_zone': 'bool'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'i18n': 'i18n',
        'default_availability_zone': 'default_availability_zone'
    }

    def __init__(self, availability_zone=None, i18n=None, default_availability_zone=None):
        r"""AzInfo

        The model defined in huaweicloud sdk

        :param availability_zone: 可用区名称。
        :type availability_zone: str
        :param i18n: 
        :type i18n: :class:`huaweicloudsdkworkspace.v2.I18n`
        :param default_availability_zone: 是否为默认可用分区。
        :type default_availability_zone: bool
        """
        
        

        self._availability_zone = None
        self._i18n = None
        self._default_availability_zone = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if i18n is not None:
            self.i18n = i18n
        if default_availability_zone is not None:
            self.default_availability_zone = default_availability_zone

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this AzInfo.

        可用区名称。

        :return: The availability_zone of this AzInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this AzInfo.

        可用区名称。

        :param availability_zone: The availability_zone of this AzInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def i18n(self):
        r"""Gets the i18n of this AzInfo.

        :return: The i18n of this AzInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.I18n`
        """
        return self._i18n

    @i18n.setter
    def i18n(self, i18n):
        r"""Sets the i18n of this AzInfo.

        :param i18n: The i18n of this AzInfo.
        :type i18n: :class:`huaweicloudsdkworkspace.v2.I18n`
        """
        self._i18n = i18n

    @property
    def default_availability_zone(self):
        r"""Gets the default_availability_zone of this AzInfo.

        是否为默认可用分区。

        :return: The default_availability_zone of this AzInfo.
        :rtype: bool
        """
        return self._default_availability_zone

    @default_availability_zone.setter
    def default_availability_zone(self, default_availability_zone):
        r"""Sets the default_availability_zone of this AzInfo.

        是否为默认可用分区。

        :param default_availability_zone: The default_availability_zone of this AzInfo.
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
        if not isinstance(other, AzInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
