# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRenewRateOnPeriodReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_ids': 'list[str]',
        'period_type': 'int',
        'period_num': 'int',
        'include_relative_resources': 'bool'
    }

    attribute_map = {
        'resource_ids': 'resource_ids',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'include_relative_resources': 'include_relative_resources'
    }

    def __init__(self, resource_ids=None, period_type=None, period_num=None, include_relative_resources=None):
        r"""ListRenewRateOnPeriodReq

        The model defined in huaweicloud sdk

        :param resource_ids: |参数名称：资源ID列表。只支持传入主资源ID，最多10个资源ID。| |参数约束以及描述：资源ID列表。只支持传入主资源ID，最多10个资源ID。|
        :type resource_ids: list[str]
        :param period_type: |参数名称：周期类型：2：月3：年| |参数的约束及描述：周期类型：2：月3：年|
        :type period_type: int
        :param period_num: |参数名称：周期数目：如果是月，目前支持1-11如果是年，目前支持1-3| |参数的约束及描述：周期数目：如果是月，目前支持1-11如果是年，目前支持1-3|
        :type period_num: int
        :param include_relative_resources: |参数名称：是否包含关联资源一起询价| |参数的约束及描述：该参数非必填，true:包含。false:不包含|
        :type include_relative_resources: bool
        """
        
        

        self._resource_ids = None
        self._period_type = None
        self._period_num = None
        self._include_relative_resources = None
        self.discriminator = None

        self.resource_ids = resource_ids
        self.period_type = period_type
        self.period_num = period_num
        if include_relative_resources is not None:
            self.include_relative_resources = include_relative_resources

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this ListRenewRateOnPeriodReq.

        |参数名称：资源ID列表。只支持传入主资源ID，最多10个资源ID。| |参数约束以及描述：资源ID列表。只支持传入主资源ID，最多10个资源ID。|

        :return: The resource_ids of this ListRenewRateOnPeriodReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this ListRenewRateOnPeriodReq.

        |参数名称：资源ID列表。只支持传入主资源ID，最多10个资源ID。| |参数约束以及描述：资源ID列表。只支持传入主资源ID，最多10个资源ID。|

        :param resource_ids: The resource_ids of this ListRenewRateOnPeriodReq.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def period_type(self):
        r"""Gets the period_type of this ListRenewRateOnPeriodReq.

        |参数名称：周期类型：2：月3：年| |参数的约束及描述：周期类型：2：月3：年|

        :return: The period_type of this ListRenewRateOnPeriodReq.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ListRenewRateOnPeriodReq.

        |参数名称：周期类型：2：月3：年| |参数的约束及描述：周期类型：2：月3：年|

        :param period_type: The period_type of this ListRenewRateOnPeriodReq.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this ListRenewRateOnPeriodReq.

        |参数名称：周期数目：如果是月，目前支持1-11如果是年，目前支持1-3| |参数的约束及描述：周期数目：如果是月，目前支持1-11如果是年，目前支持1-3|

        :return: The period_num of this ListRenewRateOnPeriodReq.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ListRenewRateOnPeriodReq.

        |参数名称：周期数目：如果是月，目前支持1-11如果是年，目前支持1-3| |参数的约束及描述：周期数目：如果是月，目前支持1-11如果是年，目前支持1-3|

        :param period_num: The period_num of this ListRenewRateOnPeriodReq.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def include_relative_resources(self):
        r"""Gets the include_relative_resources of this ListRenewRateOnPeriodReq.

        |参数名称：是否包含关联资源一起询价| |参数的约束及描述：该参数非必填，true:包含。false:不包含|

        :return: The include_relative_resources of this ListRenewRateOnPeriodReq.
        :rtype: bool
        """
        return self._include_relative_resources

    @include_relative_resources.setter
    def include_relative_resources(self, include_relative_resources):
        r"""Sets the include_relative_resources of this ListRenewRateOnPeriodReq.

        |参数名称：是否包含关联资源一起询价| |参数的约束及描述：该参数非必填，true:包含。false:不包含|

        :param include_relative_resources: The include_relative_resources of this ListRenewRateOnPeriodReq.
        :type include_relative_resources: bool
        """
        self._include_relative_resources = include_relative_resources

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
        if not isinstance(other, ListRenewRateOnPeriodReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
