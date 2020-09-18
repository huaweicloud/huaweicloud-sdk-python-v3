# coding: utf-8

import pprint
import re

import six





class QueryCouponQuotasReqExt:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'quota_ids': 'list[str]',
        'quota_status_list': 'list[int]',
        'quota_type': 'int',
        'create_time_begin': 'str',
        'create_time_end': 'str',
        'effective_time_begin': 'str',
        'effective_time_end': 'str',
        'expire_time_begin': 'str',
        'expire_time_end': 'str',
        'offset': 'int',
        'limit': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'quota_ids': 'quota_ids',
        'quota_status_list': 'quota_status_list',
        'quota_type': 'quota_type',
        'create_time_begin': 'create_time_begin',
        'create_time_end': 'create_time_end',
        'effective_time_begin': 'effective_time_begin',
        'effective_time_end': 'effective_time_end',
        'expire_time_begin': 'expire_time_begin',
        'expire_time_end': 'expire_time_end',
        'offset': 'offset',
        'limit': 'limit',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, quota_ids=None, quota_status_list=None, quota_type=None, create_time_begin=None, create_time_end=None, effective_time_begin=None, effective_time_end=None, expire_time_begin=None, expire_time_end=None, offset=0, limit=10, indirect_partner_id=None):
        """QueryCouponQuotasReqExt - a model defined in huaweicloud sdk"""
        
        

        self._quota_ids = None
        self._quota_status_list = None
        self._quota_type = None
        self._create_time_begin = None
        self._create_time_end = None
        self._effective_time_begin = None
        self._effective_time_end = None
        self._expire_time_begin = None
        self._expire_time_end = None
        self._offset = None
        self._limit = None
        self._indirect_partner_id = None
        self.discriminator = None

        if quota_ids is not None:
            self.quota_ids = quota_ids
        if quota_status_list is not None:
            self.quota_status_list = quota_status_list
        if quota_type is not None:
            self.quota_type = quota_type
        if create_time_begin is not None:
            self.create_time_begin = create_time_begin
        if create_time_end is not None:
            self.create_time_end = create_time_end
        if effective_time_begin is not None:
            self.effective_time_begin = effective_time_begin
        if effective_time_end is not None:
            self.effective_time_end = effective_time_end
        if expire_time_begin is not None:
            self.expire_time_begin = expire_time_begin
        if expire_time_end is not None:
            self.expire_time_end = expire_time_end
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def quota_ids(self):
        """Gets the quota_ids of this QueryCouponQuotasReqExt.

        |参数名称：额度ID列表。| |参数约束以及描述：额度ID列表。|

        :return: The quota_ids of this QueryCouponQuotasReqExt.
        :rtype: list[str]
        """
        return self._quota_ids

    @quota_ids.setter
    def quota_ids(self, quota_ids):
        """Sets the quota_ids of this QueryCouponQuotasReqExt.

        |参数名称：额度ID列表。| |参数约束以及描述：额度ID列表。|

        :param quota_ids: The quota_ids of this QueryCouponQuotasReqExt.
        :type: list[str]
        """
        self._quota_ids = quota_ids

    @property
    def quota_status_list(self):
        """Gets the quota_status_list of this QueryCouponQuotasReqExt.

        |参数名称：额度状态列表。| |参数约束以及描述：额度状态列表。|

        :return: The quota_status_list of this QueryCouponQuotasReqExt.
        :rtype: list[int]
        """
        return self._quota_status_list

    @quota_status_list.setter
    def quota_status_list(self, quota_status_list):
        """Sets the quota_status_list of this QueryCouponQuotasReqExt.

        |参数名称：额度状态列表。| |参数约束以及描述：额度状态列表。|

        :param quota_status_list: The quota_status_list of this QueryCouponQuotasReqExt.
        :type: list[int]
        """
        self._quota_status_list = quota_status_list

    @property
    def quota_type(self):
        """Gets the quota_type of this QueryCouponQuotasReqExt.

        |参数名称：额度类型：0：代金券额度；1：现金券额度。| |参数的约束及描述：额度类型：0：代金券额度；1：现金券额度。|

        :return: The quota_type of this QueryCouponQuotasReqExt.
        :rtype: int
        """
        return self._quota_type

    @quota_type.setter
    def quota_type(self, quota_type):
        """Sets the quota_type of this QueryCouponQuotasReqExt.

        |参数名称：额度类型：0：代金券额度；1：现金券额度。| |参数的约束及描述：额度类型：0：代金券额度；1：现金券额度。|

        :param quota_type: The quota_type of this QueryCouponQuotasReqExt.
        :type: int
        """
        self._quota_type = quota_type

    @property
    def create_time_begin(self):
        """Gets the create_time_begin of this QueryCouponQuotasReqExt.

        |参数名称：创建时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出创建时间大于这个时间的记录。| |参数约束及描述：创建时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出创建时间大于这个时间的记录。|

        :return: The create_time_begin of this QueryCouponQuotasReqExt.
        :rtype: str
        """
        return self._create_time_begin

    @create_time_begin.setter
    def create_time_begin(self, create_time_begin):
        """Sets the create_time_begin of this QueryCouponQuotasReqExt.

        |参数名称：创建时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出创建时间大于这个时间的记录。| |参数约束及描述：创建时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出创建时间大于这个时间的记录。|

        :param create_time_begin: The create_time_begin of this QueryCouponQuotasReqExt.
        :type: str
        """
        self._create_time_begin = create_time_begin

    @property
    def create_time_end(self):
        """Gets the create_time_end of this QueryCouponQuotasReqExt.

        |参数名称：创建时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出创建时间小于这个时间的记录。| |参数约束及描述：创建时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出创建时间小于这个时间的记录。|

        :return: The create_time_end of this QueryCouponQuotasReqExt.
        :rtype: str
        """
        return self._create_time_end

    @create_time_end.setter
    def create_time_end(self, create_time_end):
        """Sets the create_time_end of this QueryCouponQuotasReqExt.

        |参数名称：创建时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出创建时间小于这个时间的记录。| |参数约束及描述：创建时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出创建时间小于这个时间的记录。|

        :param create_time_end: The create_time_end of this QueryCouponQuotasReqExt.
        :type: str
        """
        self._create_time_end = create_time_end

    @property
    def effective_time_begin(self):
        """Gets the effective_time_begin of this QueryCouponQuotasReqExt.

        |参数名称：生效时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出生效时间大于这个时间的记录。| |参数约束及描述：生效时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出生效时间大于这个时间的记录。|

        :return: The effective_time_begin of this QueryCouponQuotasReqExt.
        :rtype: str
        """
        return self._effective_time_begin

    @effective_time_begin.setter
    def effective_time_begin(self, effective_time_begin):
        """Sets the effective_time_begin of this QueryCouponQuotasReqExt.

        |参数名称：生效时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出生效时间大于这个时间的记录。| |参数约束及描述：生效时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出生效时间大于这个时间的记录。|

        :param effective_time_begin: The effective_time_begin of this QueryCouponQuotasReqExt.
        :type: str
        """
        self._effective_time_begin = effective_time_begin

    @property
    def effective_time_end(self):
        """Gets the effective_time_end of this QueryCouponQuotasReqExt.

        |参数名称：生效时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出生效时间小于这个时间的记录。| |参数约束及描述：生效时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出生效时间小于这个时间的记录。|

        :return: The effective_time_end of this QueryCouponQuotasReqExt.
        :rtype: str
        """
        return self._effective_time_end

    @effective_time_end.setter
    def effective_time_end(self, effective_time_end):
        """Sets the effective_time_end of this QueryCouponQuotasReqExt.

        |参数名称：生效时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出生效时间小于这个时间的记录。| |参数约束及描述：生效时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出生效时间小于这个时间的记录。|

        :param effective_time_end: The effective_time_end of this QueryCouponQuotasReqExt.
        :type: str
        """
        self._effective_time_end = effective_time_end

    @property
    def expire_time_begin(self):
        """Gets the expire_time_begin of this QueryCouponQuotasReqExt.

        |参数名称：失效时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出失效时间大于这个时间的记录。| |参数约束及描述：失效时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出失效时间大于这个时间的记录。|

        :return: The expire_time_begin of this QueryCouponQuotasReqExt.
        :rtype: str
        """
        return self._expire_time_begin

    @expire_time_begin.setter
    def expire_time_begin(self, expire_time_begin):
        """Sets the expire_time_begin of this QueryCouponQuotasReqExt.

        |参数名称：失效时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出失效时间大于这个时间的记录。| |参数约束及描述：失效时间（开始）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出失效时间大于这个时间的记录。|

        :param expire_time_begin: The expire_time_begin of this QueryCouponQuotasReqExt.
        :type: str
        """
        self._expire_time_begin = expire_time_begin

    @property
    def expire_time_end(self):
        """Gets the expire_time_end of this QueryCouponQuotasReqExt.

        |参数名称：失效时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出失效时间小于这个时间的记录。| |参数约束及描述：失效时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出失效时间小于这个时间的记录。|

        :return: The expire_time_end of this QueryCouponQuotasReqExt.
        :rtype: str
        """
        return self._expire_time_end

    @expire_time_end.setter
    def expire_time_end(self, expire_time_end):
        """Sets the expire_time_end of this QueryCouponQuotasReqExt.

        |参数名称：失效时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出失效时间小于这个时间的记录。| |参数约束及描述：失效时间（结束）。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。输入这个条件，会查询出失效时间小于这个时间的记录。|

        :param expire_time_end: The expire_time_end of this QueryCouponQuotasReqExt.
        :type: str
        """
        self._expire_time_end = expire_time_end

    @property
    def offset(self):
        """Gets the offset of this QueryCouponQuotasReqExt.

        |参数名称：偏移量，从0开始默认取值为0。| |参数的约束及描述：偏移量，从0开始默认取值为0。|

        :return: The offset of this QueryCouponQuotasReqExt.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryCouponQuotasReqExt.

        |参数名称：偏移量，从0开始默认取值为0。| |参数的约束及描述：偏移量，从0开始默认取值为0。|

        :param offset: The offset of this QueryCouponQuotasReqExt.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this QueryCouponQuotasReqExt.

        |参数名称：每次查询记录数。默认取值为10。| |参数的约束及描述：每次查询记录数。默认取值为10。|

        :return: The limit of this QueryCouponQuotasReqExt.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryCouponQuotasReqExt.

        |参数名称：每次查询记录数。默认取值为10。| |参数的约束及描述：每次查询记录数。默认取值为10。|

        :param limit: The limit of this QueryCouponQuotasReqExt.
        :type: int
        """
        self._limit = limit

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this QueryCouponQuotasReqExt.

        |参数名称：精英服务商（二级经销商）ID，如果要查询二级经销商的额度，需要输入这个参数，否则查询的是一级经销商本人的。| |参数的约束及描述：精英服务商（二级经销商）ID，如果要查询二级经销商的额度，需要输入这个参数，否则查询的是一级经销商本人的。|

        :return: The indirect_partner_id of this QueryCouponQuotasReqExt.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this QueryCouponQuotasReqExt.

        |参数名称：精英服务商（二级经销商）ID，如果要查询二级经销商的额度，需要输入这个参数，否则查询的是一级经销商本人的。| |参数的约束及描述：精英服务商（二级经销商）ID，如果要查询二级经销商的额度，需要输入这个参数，否则查询的是一级经销商本人的。|

        :param indirect_partner_id: The indirect_partner_id of this QueryCouponQuotasReqExt.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryCouponQuotasReqExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
