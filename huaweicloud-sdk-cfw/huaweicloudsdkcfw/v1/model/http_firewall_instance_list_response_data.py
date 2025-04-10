# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpFirewallInstanceListResponseData:

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
        'project_id': 'str',
        'total': 'int',
        'records': 'list[FirewallInstanceVO]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'project_id': 'project_id',
        'total': 'total',
        'records': 'records'
    }

    def __init__(self, limit=None, offset=None, project_id=None, total=None, records=None):
        r"""HttpFirewallInstanceListResponseData

        The model defined in huaweicloud sdk

        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param project_id: 租户项目ID
        :type project_id: str
        :param total: 防火墙总数量
        :type total: int
        :param records: 查询防火墙列表记录
        :type records: list[:class:`huaweicloudsdkcfw.v1.FirewallInstanceVO`]
        """
        
        

        self._limit = None
        self._offset = None
        self._project_id = None
        self._total = None
        self._records = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if project_id is not None:
            self.project_id = project_id
        if total is not None:
            self.total = total
        if records is not None:
            self.records = records

    @property
    def limit(self):
        r"""Gets the limit of this HttpFirewallInstanceListResponseData.

        每页显示个数，范围为1-1024

        :return: The limit of this HttpFirewallInstanceListResponseData.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this HttpFirewallInstanceListResponseData.

        每页显示个数，范围为1-1024

        :param limit: The limit of this HttpFirewallInstanceListResponseData.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this HttpFirewallInstanceListResponseData.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this HttpFirewallInstanceListResponseData.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this HttpFirewallInstanceListResponseData.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this HttpFirewallInstanceListResponseData.
        :type offset: int
        """
        self._offset = offset

    @property
    def project_id(self):
        r"""Gets the project_id of this HttpFirewallInstanceListResponseData.

        租户项目ID

        :return: The project_id of this HttpFirewallInstanceListResponseData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this HttpFirewallInstanceListResponseData.

        租户项目ID

        :param project_id: The project_id of this HttpFirewallInstanceListResponseData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def total(self):
        r"""Gets the total of this HttpFirewallInstanceListResponseData.

        防火墙总数量

        :return: The total of this HttpFirewallInstanceListResponseData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this HttpFirewallInstanceListResponseData.

        防火墙总数量

        :param total: The total of this HttpFirewallInstanceListResponseData.
        :type total: int
        """
        self._total = total

    @property
    def records(self):
        r"""Gets the records of this HttpFirewallInstanceListResponseData.

        查询防火墙列表记录

        :return: The records of this HttpFirewallInstanceListResponseData.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.FirewallInstanceVO`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this HttpFirewallInstanceListResponseData.

        查询防火墙列表记录

        :param records: The records of this HttpFirewallInstanceListResponseData.
        :type records: list[:class:`huaweicloudsdkcfw.v1.FirewallInstanceVO`]
        """
        self._records = records

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
        if not isinstance(other, HttpFirewallInstanceListResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
