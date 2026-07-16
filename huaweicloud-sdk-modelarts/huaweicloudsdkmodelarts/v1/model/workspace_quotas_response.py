# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkspaceQuotasResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_quota': 'int',
        'update_time': 'int',
        'resource': 'str',
        'quota': 'int',
        'min_quota': 'int',
        'name_cn': 'str',
        'unit_cn': 'str',
        'name_en': 'str',
        'unit_en': 'str',
        'used_quota': 'int'
    }

    attribute_map = {
        'max_quota': 'max_quota',
        'update_time': 'update_time',
        'resource': 'resource',
        'quota': 'quota',
        'min_quota': 'min_quota',
        'name_cn': 'name_cn',
        'unit_cn': 'unit_cn',
        'name_en': 'name_en',
        'unit_en': 'unit_en',
        'used_quota': 'used_quota'
    }

    def __init__(self, max_quota=None, update_time=None, resource=None, quota=None, min_quota=None, name_cn=None, unit_cn=None, name_en=None, unit_en=None, used_quota=None):
        r"""WorkspaceQuotasResponse

        The model defined in huaweicloud sdk

        :param max_quota: 配额允许设置的最大值。
        :type max_quota: int
        :param update_time: 最后修改时间，UTC。如用户未修改过该资源配额,则该值默认为该工作空间的创建时间。
        :type update_time: int
        :param resource: 资源的唯一标识。
        :type resource: str
        :param quota: 当前配额值。配额值为-1代表不限制配额。
        :type quota: int
        :param min_quota: 配额允许设置的最小值。
        :type min_quota: int
        :param name_cn: 配额名称[(中文)](tag:hc,hk)。
        :type name_cn: str
        :param unit_cn: 数量单位[(中文)](tag:hc,hk)。
        :type unit_cn: str
        :param name_en: 工作空间ID，系统生成的32位UUID，不带橫线。默认的工作空间id为&#39;0&#39;。
        :type name_en: str
        :param unit_en: 数量单位(英文)。
        :type unit_en: str
        :param used_quota: 已用配额值。当quota为-1（不限制配额）时，used_quota为null。
        :type used_quota: int
        """
        
        

        self._max_quota = None
        self._update_time = None
        self._resource = None
        self._quota = None
        self._min_quota = None
        self._name_cn = None
        self._unit_cn = None
        self._name_en = None
        self._unit_en = None
        self._used_quota = None
        self.discriminator = None

        if max_quota is not None:
            self.max_quota = max_quota
        if update_time is not None:
            self.update_time = update_time
        if resource is not None:
            self.resource = resource
        if quota is not None:
            self.quota = quota
        if min_quota is not None:
            self.min_quota = min_quota
        if name_cn is not None:
            self.name_cn = name_cn
        if unit_cn is not None:
            self.unit_cn = unit_cn
        if name_en is not None:
            self.name_en = name_en
        if unit_en is not None:
            self.unit_en = unit_en
        if used_quota is not None:
            self.used_quota = used_quota

    @property
    def max_quota(self):
        r"""Gets the max_quota of this WorkspaceQuotasResponse.

        配额允许设置的最大值。

        :return: The max_quota of this WorkspaceQuotasResponse.
        :rtype: int
        """
        return self._max_quota

    @max_quota.setter
    def max_quota(self, max_quota):
        r"""Sets the max_quota of this WorkspaceQuotasResponse.

        配额允许设置的最大值。

        :param max_quota: The max_quota of this WorkspaceQuotasResponse.
        :type max_quota: int
        """
        self._max_quota = max_quota

    @property
    def update_time(self):
        r"""Gets the update_time of this WorkspaceQuotasResponse.

        最后修改时间，UTC。如用户未修改过该资源配额,则该值默认为该工作空间的创建时间。

        :return: The update_time of this WorkspaceQuotasResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this WorkspaceQuotasResponse.

        最后修改时间，UTC。如用户未修改过该资源配额,则该值默认为该工作空间的创建时间。

        :param update_time: The update_time of this WorkspaceQuotasResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def resource(self):
        r"""Gets the resource of this WorkspaceQuotasResponse.

        资源的唯一标识。

        :return: The resource of this WorkspaceQuotasResponse.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this WorkspaceQuotasResponse.

        资源的唯一标识。

        :param resource: The resource of this WorkspaceQuotasResponse.
        :type resource: str
        """
        self._resource = resource

    @property
    def quota(self):
        r"""Gets the quota of this WorkspaceQuotasResponse.

        当前配额值。配额值为-1代表不限制配额。

        :return: The quota of this WorkspaceQuotasResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this WorkspaceQuotasResponse.

        当前配额值。配额值为-1代表不限制配额。

        :param quota: The quota of this WorkspaceQuotasResponse.
        :type quota: int
        """
        self._quota = quota

    @property
    def min_quota(self):
        r"""Gets the min_quota of this WorkspaceQuotasResponse.

        配额允许设置的最小值。

        :return: The min_quota of this WorkspaceQuotasResponse.
        :rtype: int
        """
        return self._min_quota

    @min_quota.setter
    def min_quota(self, min_quota):
        r"""Sets the min_quota of this WorkspaceQuotasResponse.

        配额允许设置的最小值。

        :param min_quota: The min_quota of this WorkspaceQuotasResponse.
        :type min_quota: int
        """
        self._min_quota = min_quota

    @property
    def name_cn(self):
        r"""Gets the name_cn of this WorkspaceQuotasResponse.

        配额名称[(中文)](tag:hc,hk)。

        :return: The name_cn of this WorkspaceQuotasResponse.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this WorkspaceQuotasResponse.

        配额名称[(中文)](tag:hc,hk)。

        :param name_cn: The name_cn of this WorkspaceQuotasResponse.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def unit_cn(self):
        r"""Gets the unit_cn of this WorkspaceQuotasResponse.

        数量单位[(中文)](tag:hc,hk)。

        :return: The unit_cn of this WorkspaceQuotasResponse.
        :rtype: str
        """
        return self._unit_cn

    @unit_cn.setter
    def unit_cn(self, unit_cn):
        r"""Sets the unit_cn of this WorkspaceQuotasResponse.

        数量单位[(中文)](tag:hc,hk)。

        :param unit_cn: The unit_cn of this WorkspaceQuotasResponse.
        :type unit_cn: str
        """
        self._unit_cn = unit_cn

    @property
    def name_en(self):
        r"""Gets the name_en of this WorkspaceQuotasResponse.

        工作空间ID，系统生成的32位UUID，不带橫线。默认的工作空间id为'0'。

        :return: The name_en of this WorkspaceQuotasResponse.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this WorkspaceQuotasResponse.

        工作空间ID，系统生成的32位UUID，不带橫线。默认的工作空间id为'0'。

        :param name_en: The name_en of this WorkspaceQuotasResponse.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def unit_en(self):
        r"""Gets the unit_en of this WorkspaceQuotasResponse.

        数量单位(英文)。

        :return: The unit_en of this WorkspaceQuotasResponse.
        :rtype: str
        """
        return self._unit_en

    @unit_en.setter
    def unit_en(self, unit_en):
        r"""Sets the unit_en of this WorkspaceQuotasResponse.

        数量单位(英文)。

        :param unit_en: The unit_en of this WorkspaceQuotasResponse.
        :type unit_en: str
        """
        self._unit_en = unit_en

    @property
    def used_quota(self):
        r"""Gets the used_quota of this WorkspaceQuotasResponse.

        已用配额值。当quota为-1（不限制配额）时，used_quota为null。

        :return: The used_quota of this WorkspaceQuotasResponse.
        :rtype: int
        """
        return self._used_quota

    @used_quota.setter
    def used_quota(self, used_quota):
        r"""Sets the used_quota of this WorkspaceQuotasResponse.

        已用配额值。当quota为-1（不限制配额）时，used_quota为null。

        :param used_quota: The used_quota of this WorkspaceQuotasResponse.
        :type used_quota: int
        """
        self._used_quota = used_quota

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkspaceQuotasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
