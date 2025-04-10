# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPhysicalProcessesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'keyword': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'keyword': 'keyword'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, keyword=None):
        r"""ShowPhysicalProcessesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 关联RDS的ID。
        :type instance_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。
        :type offset: int
        :param limit: 查询个数上限值。取值范围：1~128。不传该参数时，默认值为10。
        :type limit: int
        :param keyword: 会话结果筛选关键子，长度最大255
        :type keyword: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._keyword = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if keyword is not None:
            self.keyword = keyword

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowPhysicalProcessesRequest.

        关联RDS的ID。

        :return: The instance_id of this ShowPhysicalProcessesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowPhysicalProcessesRequest.

        关联RDS的ID。

        :param instance_id: The instance_id of this ShowPhysicalProcessesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowPhysicalProcessesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。

        :return: The offset of this ShowPhysicalProcessesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowPhysicalProcessesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。

        :param offset: The offset of this ShowPhysicalProcessesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowPhysicalProcessesRequest.

        查询个数上限值。取值范围：1~128。不传该参数时，默认值为10。

        :return: The limit of this ShowPhysicalProcessesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowPhysicalProcessesRequest.

        查询个数上限值。取值范围：1~128。不传该参数时，默认值为10。

        :param limit: The limit of this ShowPhysicalProcessesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def keyword(self):
        r"""Gets the keyword of this ShowPhysicalProcessesRequest.

        会话结果筛选关键子，长度最大255

        :return: The keyword of this ShowPhysicalProcessesRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ShowPhysicalProcessesRequest.

        会话结果筛选关键子，长度最大255

        :param keyword: The keyword of this ShowPhysicalProcessesRequest.
        :type keyword: str
        """
        self._keyword = keyword

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
        if not isinstance(other, ShowPhysicalProcessesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
