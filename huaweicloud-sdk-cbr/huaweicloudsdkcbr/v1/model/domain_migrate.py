# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainMigrate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_regions': 'bool',
        'reservation': 'float'
    }

    attribute_map = {
        'all_regions': 'all_regions',
        'reservation': 'reservation'
    }

    def __init__(self, all_regions=None, reservation=None):
        r"""DomainMigrate

        The model defined in huaweicloud sdk

        :param all_regions: 是否触发其他区域迁移
        :type all_regions: bool
        :param reservation: 存储库默认扩容比，取值范围0到1
        :type reservation: float
        """
        
        

        self._all_regions = None
        self._reservation = None
        self.discriminator = None

        self.all_regions = all_regions
        self.reservation = reservation

    @property
    def all_regions(self):
        r"""Gets the all_regions of this DomainMigrate.

        是否触发其他区域迁移

        :return: The all_regions of this DomainMigrate.
        :rtype: bool
        """
        return self._all_regions

    @all_regions.setter
    def all_regions(self, all_regions):
        r"""Sets the all_regions of this DomainMigrate.

        是否触发其他区域迁移

        :param all_regions: The all_regions of this DomainMigrate.
        :type all_regions: bool
        """
        self._all_regions = all_regions

    @property
    def reservation(self):
        r"""Gets the reservation of this DomainMigrate.

        存储库默认扩容比，取值范围0到1

        :return: The reservation of this DomainMigrate.
        :rtype: float
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        r"""Sets the reservation of this DomainMigrate.

        存储库默认扩容比，取值范围0到1

        :param reservation: The reservation of this DomainMigrate.
        :type reservation: float
        """
        self._reservation = reservation

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
        if not isinstance(other, DomainMigrate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
