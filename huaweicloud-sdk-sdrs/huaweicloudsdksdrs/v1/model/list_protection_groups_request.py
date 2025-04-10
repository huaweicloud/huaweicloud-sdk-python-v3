# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectionGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'status': 'str',
        'name': 'str',
        'query_type': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status',
        'name': 'name',
        'query_type': 'query_type',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, limit=None, offset=None, status=None, name=None, query_type=None, availability_zone=None):
        r"""ListProtectionGroupsRequest

        The model defined in huaweicloud sdk

        :param limit: 每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。
        :type limit: int
        :param offset: 每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。
        :type offset: int
        :param status: 保护组状态。
        :type status: str
        :param name: 保护组的名称。支持模糊查询。
        :type name: str
        :param query_type: 查询场景类型。 status_abnormal：表示查询异常状态的保护组列表。 stop_protected：表示查询停止保护的保护组列表。 period_no_dr_drill：表示查询一段时间未做容灾演练的保护组，默认为三个月。 general或空时：该参数不生效。
        :type query_type: str
        :param availability_zone: 保护组的当前生产站点可用区。
        :type availability_zone: str
        """
        
        

        self._limit = None
        self._offset = None
        self._status = None
        self._name = None
        self._query_type = None
        self._availability_zone = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if query_type is not None:
            self.query_type = query_type
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def limit(self):
        r"""Gets the limit of this ListProtectionGroupsRequest.

        每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。

        :return: The limit of this ListProtectionGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProtectionGroupsRequest.

        每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。

        :param limit: The limit of this ListProtectionGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListProtectionGroupsRequest.

        每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。

        :return: The offset of this ListProtectionGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProtectionGroupsRequest.

        每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。

        :param offset: The offset of this ListProtectionGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListProtectionGroupsRequest.

        保护组状态。

        :return: The status of this ListProtectionGroupsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListProtectionGroupsRequest.

        保护组状态。

        :param status: The status of this ListProtectionGroupsRequest.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ListProtectionGroupsRequest.

        保护组的名称。支持模糊查询。

        :return: The name of this ListProtectionGroupsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListProtectionGroupsRequest.

        保护组的名称。支持模糊查询。

        :param name: The name of this ListProtectionGroupsRequest.
        :type name: str
        """
        self._name = name

    @property
    def query_type(self):
        r"""Gets the query_type of this ListProtectionGroupsRequest.

        查询场景类型。 status_abnormal：表示查询异常状态的保护组列表。 stop_protected：表示查询停止保护的保护组列表。 period_no_dr_drill：表示查询一段时间未做容灾演练的保护组，默认为三个月。 general或空时：该参数不生效。

        :return: The query_type of this ListProtectionGroupsRequest.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this ListProtectionGroupsRequest.

        查询场景类型。 status_abnormal：表示查询异常状态的保护组列表。 stop_protected：表示查询停止保护的保护组列表。 period_no_dr_drill：表示查询一段时间未做容灾演练的保护组，默认为三个月。 general或空时：该参数不生效。

        :param query_type: The query_type of this ListProtectionGroupsRequest.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListProtectionGroupsRequest.

        保护组的当前生产站点可用区。

        :return: The availability_zone of this ListProtectionGroupsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListProtectionGroupsRequest.

        保护组的当前生产站点可用区。

        :param availability_zone: The availability_zone of this ListProtectionGroupsRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, ListProtectionGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
