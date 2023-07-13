# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIncentiveDiscountPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'service_type_code': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'time': 'time',
        'service_type_code': 'service_type_code',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, time=None, service_type_code=None, offset=None, limit=None):
        """ListIncentiveDiscountPoliciesRequest

        The model defined in huaweicloud sdk

        :param time: 查询策略的指定时间。东八区时间，格式：YYYY-MM。 说明： 实际查询结果为指定时间所在月最后一天23:59:59的策略情况。
        :type time: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。
        :type service_type_code: str
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的数量，默认值为10。
        :type limit: int
        """
        
        

        self._time = None
        self._service_type_code = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.time = time
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def time(self):
        """Gets the time of this ListIncentiveDiscountPoliciesRequest.

        查询策略的指定时间。东八区时间，格式：YYYY-MM。 说明： 实际查询结果为指定时间所在月最后一天23:59:59的策略情况。

        :return: The time of this ListIncentiveDiscountPoliciesRequest.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ListIncentiveDiscountPoliciesRequest.

        查询策略的指定时间。东八区时间，格式：YYYY-MM。 说明： 实际查询结果为指定时间所在月最后一天23:59:59的策略情况。

        :param time: The time of this ListIncentiveDiscountPoliciesRequest.
        :type time: str
        """
        self._time = time

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ListIncentiveDiscountPoliciesRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。

        :return: The service_type_code of this ListIncentiveDiscountPoliciesRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ListIncentiveDiscountPoliciesRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。此参数不携带或携带值为空时，不作为筛选条件；携带值为空串时，作为筛选条件。

        :param service_type_code: The service_type_code of this ListIncentiveDiscountPoliciesRequest.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def offset(self):
        """Gets the offset of this ListIncentiveDiscountPoliciesRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListIncentiveDiscountPoliciesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIncentiveDiscountPoliciesRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListIncentiveDiscountPoliciesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListIncentiveDiscountPoliciesRequest.

        每次查询的数量，默认值为10。

        :return: The limit of this ListIncentiveDiscountPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIncentiveDiscountPoliciesRequest.

        每次查询的数量，默认值为10。

        :param limit: The limit of this ListIncentiveDiscountPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListIncentiveDiscountPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
