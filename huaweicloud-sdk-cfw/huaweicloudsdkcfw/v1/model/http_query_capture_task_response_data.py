# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpQueryCaptureTaskResponseData:

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
        'object_id': 'str',
        'offset': 'int',
        'project_id': 'str',
        'total': 'int',
        'records': 'list[CaptureTaskVO]'
    }

    attribute_map = {
        'limit': 'limit',
        'object_id': 'object_id',
        'offset': 'offset',
        'project_id': 'project_id',
        'total': 'total',
        'records': 'records'
    }

    def __init__(self, limit=None, object_id=None, offset=None, project_id=None, total=None, records=None):
        """HttpQueryCaptureTaskResponseData

        The model defined in huaweicloud sdk

        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。
        :type object_id: str
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param project_id: 租户project_id
        :type project_id: str
        :param total: 抓包任务总数
        :type total: int
        :param records: 抓包任务列表
        :type records: list[:class:`huaweicloudsdkcfw.v1.CaptureTaskVO`]
        """
        
        

        self._limit = None
        self._object_id = None
        self._offset = None
        self._project_id = None
        self._total = None
        self._records = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if object_id is not None:
            self.object_id = object_id
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
        """Gets the limit of this HttpQueryCaptureTaskResponseData.

        每页显示个数，范围为1-1024

        :return: The limit of this HttpQueryCaptureTaskResponseData.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this HttpQueryCaptureTaskResponseData.

        每页显示个数，范围为1-1024

        :param limit: The limit of this HttpQueryCaptureTaskResponseData.
        :type limit: int
        """
        self._limit = limit

    @property
    def object_id(self):
        """Gets the object_id of this HttpQueryCaptureTaskResponseData.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。

        :return: The object_id of this HttpQueryCaptureTaskResponseData.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this HttpQueryCaptureTaskResponseData.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。

        :param object_id: The object_id of this HttpQueryCaptureTaskResponseData.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def offset(self):
        """Gets the offset of this HttpQueryCaptureTaskResponseData.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this HttpQueryCaptureTaskResponseData.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this HttpQueryCaptureTaskResponseData.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this HttpQueryCaptureTaskResponseData.
        :type offset: int
        """
        self._offset = offset

    @property
    def project_id(self):
        """Gets the project_id of this HttpQueryCaptureTaskResponseData.

        租户project_id

        :return: The project_id of this HttpQueryCaptureTaskResponseData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this HttpQueryCaptureTaskResponseData.

        租户project_id

        :param project_id: The project_id of this HttpQueryCaptureTaskResponseData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def total(self):
        """Gets the total of this HttpQueryCaptureTaskResponseData.

        抓包任务总数

        :return: The total of this HttpQueryCaptureTaskResponseData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this HttpQueryCaptureTaskResponseData.

        抓包任务总数

        :param total: The total of this HttpQueryCaptureTaskResponseData.
        :type total: int
        """
        self._total = total

    @property
    def records(self):
        """Gets the records of this HttpQueryCaptureTaskResponseData.

        抓包任务列表

        :return: The records of this HttpQueryCaptureTaskResponseData.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.CaptureTaskVO`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this HttpQueryCaptureTaskResponseData.

        抓包任务列表

        :param records: The records of this HttpQueryCaptureTaskResponseData.
        :type records: list[:class:`huaweicloudsdkcfw.v1.CaptureTaskVO`]
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
        if not isinstance(other, HttpQueryCaptureTaskResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
