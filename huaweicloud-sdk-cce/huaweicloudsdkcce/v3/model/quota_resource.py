# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_key': 'str',
        'quota_limit': 'int',
        'used': 'int',
        'unit': 'str',
        'region_id': 'str',
        'availability_zone_id': 'str'
    }

    attribute_map = {
        'quota_key': 'quotaKey',
        'quota_limit': 'quotaLimit',
        'used': 'used',
        'unit': 'unit',
        'region_id': 'regionId',
        'availability_zone_id': 'availabilityZoneId'
    }

    def __init__(self, quota_key=None, quota_limit=None, used=None, unit=None, region_id=None, availability_zone_id=None):
        r"""QuotaResource

        The model defined in huaweicloud sdk

        :param quota_key: 资源类型
        :type quota_key: str
        :param quota_limit: 配额值
        :type quota_limit: int
        :param used: 已创建的资源个数
        :type used: int
        :param unit: 单位
        :type unit: str
        :param region_id: 局点ID。若资源不涉及此参数，则不返回该参数。
        :type region_id: str
        :param availability_zone_id: 可用区ID。若资源不涉及此参数，则不返回该参数。
        :type availability_zone_id: str
        """
        
        

        self._quota_key = None
        self._quota_limit = None
        self._used = None
        self._unit = None
        self._region_id = None
        self._availability_zone_id = None
        self.discriminator = None

        if quota_key is not None:
            self.quota_key = quota_key
        if quota_limit is not None:
            self.quota_limit = quota_limit
        if used is not None:
            self.used = used
        if unit is not None:
            self.unit = unit
        if region_id is not None:
            self.region_id = region_id
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id

    @property
    def quota_key(self):
        r"""Gets the quota_key of this QuotaResource.

        资源类型

        :return: The quota_key of this QuotaResource.
        :rtype: str
        """
        return self._quota_key

    @quota_key.setter
    def quota_key(self, quota_key):
        r"""Sets the quota_key of this QuotaResource.

        资源类型

        :param quota_key: The quota_key of this QuotaResource.
        :type quota_key: str
        """
        self._quota_key = quota_key

    @property
    def quota_limit(self):
        r"""Gets the quota_limit of this QuotaResource.

        配额值

        :return: The quota_limit of this QuotaResource.
        :rtype: int
        """
        return self._quota_limit

    @quota_limit.setter
    def quota_limit(self, quota_limit):
        r"""Sets the quota_limit of this QuotaResource.

        配额值

        :param quota_limit: The quota_limit of this QuotaResource.
        :type quota_limit: int
        """
        self._quota_limit = quota_limit

    @property
    def used(self):
        r"""Gets the used of this QuotaResource.

        已创建的资源个数

        :return: The used of this QuotaResource.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this QuotaResource.

        已创建的资源个数

        :param used: The used of this QuotaResource.
        :type used: int
        """
        self._used = used

    @property
    def unit(self):
        r"""Gets the unit of this QuotaResource.

        单位

        :return: The unit of this QuotaResource.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this QuotaResource.

        单位

        :param unit: The unit of this QuotaResource.
        :type unit: str
        """
        self._unit = unit

    @property
    def region_id(self):
        r"""Gets the region_id of this QuotaResource.

        局点ID。若资源不涉及此参数，则不返回该参数。

        :return: The region_id of this QuotaResource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this QuotaResource.

        局点ID。若资源不涉及此参数，则不返回该参数。

        :param region_id: The region_id of this QuotaResource.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this QuotaResource.

        可用区ID。若资源不涉及此参数，则不返回该参数。

        :return: The availability_zone_id of this QuotaResource.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this QuotaResource.

        可用区ID。若资源不涉及此参数，则不返回该参数。

        :param availability_zone_id: The availability_zone_id of this QuotaResource.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

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
        if not isinstance(other, QuotaResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
