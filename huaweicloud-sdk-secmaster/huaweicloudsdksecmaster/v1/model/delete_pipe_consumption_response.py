# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePipeConsumptionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_point': 'str',
        'pipe_name': 'str',
        'status': 'str',
        'subscription_name': 'str',
        'table_id': 'str'
    }

    attribute_map = {
        'access_point': 'access_point',
        'pipe_name': 'pipe_name',
        'status': 'status',
        'subscription_name': 'subscription_name',
        'table_id': 'table_id'
    }

    def __init__(self, access_point=None, pipe_name=None, status=None, subscription_name=None, table_id=None):
        r"""DeletePipeConsumptionResponse

        The model defined in huaweicloud sdk

        :param access_point: 接入点域名信息(格式：{dataspace}.{endpoint})
        :type access_point: str
        :param pipe_name: 数据管道名称
        :type pipe_name: str
        :param status: 实时消费的开关状态；enable-开启，disable-关闭
        :type status: str
        :param subscription_name: 订阅名称
        :type subscription_name: str
        :param table_id: 表id
        :type table_id: str
        """
        
        super().__init__()

        self._access_point = None
        self._pipe_name = None
        self._status = None
        self._subscription_name = None
        self._table_id = None
        self.discriminator = None

        if access_point is not None:
            self.access_point = access_point
        if pipe_name is not None:
            self.pipe_name = pipe_name
        if status is not None:
            self.status = status
        if subscription_name is not None:
            self.subscription_name = subscription_name
        if table_id is not None:
            self.table_id = table_id

    @property
    def access_point(self):
        r"""Gets the access_point of this DeletePipeConsumptionResponse.

        接入点域名信息(格式：{dataspace}.{endpoint})

        :return: The access_point of this DeletePipeConsumptionResponse.
        :rtype: str
        """
        return self._access_point

    @access_point.setter
    def access_point(self, access_point):
        r"""Sets the access_point of this DeletePipeConsumptionResponse.

        接入点域名信息(格式：{dataspace}.{endpoint})

        :param access_point: The access_point of this DeletePipeConsumptionResponse.
        :type access_point: str
        """
        self._access_point = access_point

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this DeletePipeConsumptionResponse.

        数据管道名称

        :return: The pipe_name of this DeletePipeConsumptionResponse.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this DeletePipeConsumptionResponse.

        数据管道名称

        :param pipe_name: The pipe_name of this DeletePipeConsumptionResponse.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def status(self):
        r"""Gets the status of this DeletePipeConsumptionResponse.

        实时消费的开关状态；enable-开启，disable-关闭

        :return: The status of this DeletePipeConsumptionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DeletePipeConsumptionResponse.

        实时消费的开关状态；enable-开启，disable-关闭

        :param status: The status of this DeletePipeConsumptionResponse.
        :type status: str
        """
        self._status = status

    @property
    def subscription_name(self):
        r"""Gets the subscription_name of this DeletePipeConsumptionResponse.

        订阅名称

        :return: The subscription_name of this DeletePipeConsumptionResponse.
        :rtype: str
        """
        return self._subscription_name

    @subscription_name.setter
    def subscription_name(self, subscription_name):
        r"""Sets the subscription_name of this DeletePipeConsumptionResponse.

        订阅名称

        :param subscription_name: The subscription_name of this DeletePipeConsumptionResponse.
        :type subscription_name: str
        """
        self._subscription_name = subscription_name

    @property
    def table_id(self):
        r"""Gets the table_id of this DeletePipeConsumptionResponse.

        表id

        :return: The table_id of this DeletePipeConsumptionResponse.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this DeletePipeConsumptionResponse.

        表id

        :param table_id: The table_id of this DeletePipeConsumptionResponse.
        :type table_id: str
        """
        self._table_id = table_id

    def to_dict(self):
        import warnings
        warnings.warn("DeletePipeConsumptionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeletePipeConsumptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
