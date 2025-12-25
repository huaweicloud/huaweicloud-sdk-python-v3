# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPipeIndexResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mapping': 'dict(str, KeyIndex)',
        'pipe_id': 'str',
        'status': 'str',
        'timestamp_field': 'str'
    }

    attribute_map = {
        'mapping': 'mapping',
        'pipe_id': 'pipe_id',
        'status': 'status',
        'timestamp_field': 'timestamp_field'
    }

    def __init__(self, mapping=None, pipe_id=None, status=None, timestamp_field=None):
        r"""ShowPipeIndexResponse

        The model defined in huaweicloud sdk

        :param mapping: 索引映射信息
        :type mapping: dict(str, KeyIndex)
        :param pipe_id: 数据管道ID
        :type pipe_id: str
        :param status: 索引状态；open 开启，closed 关闭
        :type status: str
        :param timestamp_field: 时间戳字段名称
        :type timestamp_field: str
        """
        
        super().__init__()

        self._mapping = None
        self._pipe_id = None
        self._status = None
        self._timestamp_field = None
        self.discriminator = None

        if mapping is not None:
            self.mapping = mapping
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if status is not None:
            self.status = status
        if timestamp_field is not None:
            self.timestamp_field = timestamp_field

    @property
    def mapping(self):
        r"""Gets the mapping of this ShowPipeIndexResponse.

        索引映射信息

        :return: The mapping of this ShowPipeIndexResponse.
        :rtype: dict(str, KeyIndex)
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        r"""Sets the mapping of this ShowPipeIndexResponse.

        索引映射信息

        :param mapping: The mapping of this ShowPipeIndexResponse.
        :type mapping: dict(str, KeyIndex)
        """
        self._mapping = mapping

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this ShowPipeIndexResponse.

        数据管道ID

        :return: The pipe_id of this ShowPipeIndexResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this ShowPipeIndexResponse.

        数据管道ID

        :param pipe_id: The pipe_id of this ShowPipeIndexResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def status(self):
        r"""Gets the status of this ShowPipeIndexResponse.

        索引状态；open 开启，closed 关闭

        :return: The status of this ShowPipeIndexResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowPipeIndexResponse.

        索引状态；open 开启，closed 关闭

        :param status: The status of this ShowPipeIndexResponse.
        :type status: str
        """
        self._status = status

    @property
    def timestamp_field(self):
        r"""Gets the timestamp_field of this ShowPipeIndexResponse.

        时间戳字段名称

        :return: The timestamp_field of this ShowPipeIndexResponse.
        :rtype: str
        """
        return self._timestamp_field

    @timestamp_field.setter
    def timestamp_field(self, timestamp_field):
        r"""Sets the timestamp_field of this ShowPipeIndexResponse.

        时间戳字段名称

        :param timestamp_field: The timestamp_field of this ShowPipeIndexResponse.
        :type timestamp_field: str
        """
        self._timestamp_field = timestamp_field

    def to_dict(self):
        import warnings
        warnings.warn("ShowPipeIndexResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowPipeIndexResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
