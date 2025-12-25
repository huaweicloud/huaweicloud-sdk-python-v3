# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAdhocResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch': 'object',
        'schema': 'list[AdhocQueryAnalysisField]',
        'datarows': 'list[list[object]]',
        'datarows_upsert': 'list[list[DataRow]]',
        'total': 'int',
        'size': 'int',
        'next': 'int',
        'tips': 'ShowAdhocQueryResultResponseBodyTips',
        'job_id': 'str'
    }

    attribute_map = {
        'batch': 'batch',
        'schema': 'schema',
        'datarows': 'datarows',
        'datarows_upsert': 'datarows_upsert',
        'total': 'total',
        'size': 'size',
        'next': 'next',
        'tips': 'tips',
        'job_id': 'job_id'
    }

    def __init__(self, batch=None, schema=None, datarows=None, datarows_upsert=None, total=None, size=None, next=None, tips=None, job_id=None):
        r"""ShowAdhocResultResponse

        The model defined in huaweicloud sdk

        :param batch: 获取数据的批次，为0则为第一次查询
        :type batch: object
        :param schema: 统计分析结果字段类型
        :type schema: list[:class:`huaweicloudsdksecmaster.v2.AdhocQueryAnalysisField`]
        :param datarows: 统计分析结果数据
        :type datarows: list[list[object]]
        :param datarows_upsert: 统计分析结果数据
        :type datarows_upsert: list[list[DataRow]]
        :param total: 统计分析结果总数
        :type total: int
        :param size: 返回的统计分析结果条数
        :type size: int
        :param next: 是否有下一批数据
        :type next: int
        :param tips: 
        :type tips: :class:`huaweicloudsdksecmaster.v2.ShowAdhocQueryResultResponseBodyTips`
        :param job_id: UUID
        :type job_id: str
        """
        
        super().__init__()

        self._batch = None
        self._schema = None
        self._datarows = None
        self._datarows_upsert = None
        self._total = None
        self._size = None
        self._next = None
        self._tips = None
        self._job_id = None
        self.discriminator = None

        if batch is not None:
            self.batch = batch
        if schema is not None:
            self.schema = schema
        if datarows is not None:
            self.datarows = datarows
        if datarows_upsert is not None:
            self.datarows_upsert = datarows_upsert
        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if next is not None:
            self.next = next
        if tips is not None:
            self.tips = tips
        if job_id is not None:
            self.job_id = job_id

    @property
    def batch(self):
        r"""Gets the batch of this ShowAdhocResultResponse.

        获取数据的批次，为0则为第一次查询

        :return: The batch of this ShowAdhocResultResponse.
        :rtype: object
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        r"""Sets the batch of this ShowAdhocResultResponse.

        获取数据的批次，为0则为第一次查询

        :param batch: The batch of this ShowAdhocResultResponse.
        :type batch: object
        """
        self._batch = batch

    @property
    def schema(self):
        r"""Gets the schema of this ShowAdhocResultResponse.

        统计分析结果字段类型

        :return: The schema of this ShowAdhocResultResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AdhocQueryAnalysisField`]
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ShowAdhocResultResponse.

        统计分析结果字段类型

        :param schema: The schema of this ShowAdhocResultResponse.
        :type schema: list[:class:`huaweicloudsdksecmaster.v2.AdhocQueryAnalysisField`]
        """
        self._schema = schema

    @property
    def datarows(self):
        r"""Gets the datarows of this ShowAdhocResultResponse.

        统计分析结果数据

        :return: The datarows of this ShowAdhocResultResponse.
        :rtype: list[list[object]]
        """
        return self._datarows

    @datarows.setter
    def datarows(self, datarows):
        r"""Sets the datarows of this ShowAdhocResultResponse.

        统计分析结果数据

        :param datarows: The datarows of this ShowAdhocResultResponse.
        :type datarows: list[list[object]]
        """
        self._datarows = datarows

    @property
    def datarows_upsert(self):
        r"""Gets the datarows_upsert of this ShowAdhocResultResponse.

        统计分析结果数据

        :return: The datarows_upsert of this ShowAdhocResultResponse.
        :rtype: list[list[DataRow]]
        """
        return self._datarows_upsert

    @datarows_upsert.setter
    def datarows_upsert(self, datarows_upsert):
        r"""Sets the datarows_upsert of this ShowAdhocResultResponse.

        统计分析结果数据

        :param datarows_upsert: The datarows_upsert of this ShowAdhocResultResponse.
        :type datarows_upsert: list[list[DataRow]]
        """
        self._datarows_upsert = datarows_upsert

    @property
    def total(self):
        r"""Gets the total of this ShowAdhocResultResponse.

        统计分析结果总数

        :return: The total of this ShowAdhocResultResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowAdhocResultResponse.

        统计分析结果总数

        :param total: The total of this ShowAdhocResultResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        r"""Gets the size of this ShowAdhocResultResponse.

        返回的统计分析结果条数

        :return: The size of this ShowAdhocResultResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowAdhocResultResponse.

        返回的统计分析结果条数

        :param size: The size of this ShowAdhocResultResponse.
        :type size: int
        """
        self._size = size

    @property
    def next(self):
        r"""Gets the next of this ShowAdhocResultResponse.

        是否有下一批数据

        :return: The next of this ShowAdhocResultResponse.
        :rtype: int
        """
        return self._next

    @next.setter
    def next(self, next):
        r"""Sets the next of this ShowAdhocResultResponse.

        是否有下一批数据

        :param next: The next of this ShowAdhocResultResponse.
        :type next: int
        """
        self._next = next

    @property
    def tips(self):
        r"""Gets the tips of this ShowAdhocResultResponse.

        :return: The tips of this ShowAdhocResultResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAdhocQueryResultResponseBodyTips`
        """
        return self._tips

    @tips.setter
    def tips(self, tips):
        r"""Sets the tips of this ShowAdhocResultResponse.

        :param tips: The tips of this ShowAdhocResultResponse.
        :type tips: :class:`huaweicloudsdksecmaster.v2.ShowAdhocQueryResultResponseBodyTips`
        """
        self._tips = tips

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowAdhocResultResponse.

        UUID

        :return: The job_id of this ShowAdhocResultResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowAdhocResultResponse.

        UUID

        :param job_id: The job_id of this ShowAdhocResultResponse.
        :type job_id: str
        """
        self._job_id = job_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowAdhocResultResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowAdhocResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
