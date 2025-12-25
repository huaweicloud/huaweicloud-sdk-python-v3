# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataConsumptionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'dataspace_id': 'str',
        'pipe_id': 'str',
        'pipe_name': 'str',
        'status': 'str',
        'type': 'str',
        'access_point': 'str',
        'subscription': 'str',
        'table_id': 'str'
    }

    attribute_map = {
        'table_name': 'table_name',
        'dataspace_id': 'dataspace_id',
        'pipe_id': 'pipe_id',
        'pipe_name': 'pipe_name',
        'status': 'status',
        'type': 'type',
        'access_point': 'access_point',
        'subscription': 'subscription',
        'table_id': 'table_id'
    }

    def __init__(self, table_name=None, dataspace_id=None, pipe_id=None, pipe_name=None, status=None, type=None, access_point=None, subscription=None, table_id=None):
        r"""ShowDataConsumptionResponse

        The model defined in huaweicloud sdk

        :param table_name: 表名称
        :type table_name: str
        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param pipe_id: 管道ID
        :type pipe_id: str
        :param pipe_name: 管道名称
        :type pipe_name: str
        :param status: **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及   
        :type status: str
        :param type: **参数解释**: 网络类型 - INTERNET 互联网 - INTRANET 内联网  **约束限制** 不涉及 **取值范围**: - INTERNET - INTRANET  **默认值** 不涉及         
        :type type: str
        :param access_point: 接入点域名信息(格式：{dataspace}.{endpoint})
        :type access_point: str
        :param subscription: 订阅名称
        :type subscription: str
        :param table_id: 表Id
        :type table_id: str
        """
        
        super().__init__()

        self._table_name = None
        self._dataspace_id = None
        self._pipe_id = None
        self._pipe_name = None
        self._status = None
        self._type = None
        self._access_point = None
        self._subscription = None
        self._table_id = None
        self.discriminator = None

        if table_name is not None:
            self.table_name = table_name
        if dataspace_id is not None:
            self.dataspace_id = dataspace_id
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if pipe_name is not None:
            self.pipe_name = pipe_name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if access_point is not None:
            self.access_point = access_point
        if subscription is not None:
            self.subscription = subscription
        if table_id is not None:
            self.table_id = table_id

    @property
    def table_name(self):
        r"""Gets the table_name of this ShowDataConsumptionResponse.

        表名称

        :return: The table_name of this ShowDataConsumptionResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ShowDataConsumptionResponse.

        表名称

        :param table_name: The table_name of this ShowDataConsumptionResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this ShowDataConsumptionResponse.

        数据空间ID

        :return: The dataspace_id of this ShowDataConsumptionResponse.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this ShowDataConsumptionResponse.

        数据空间ID

        :param dataspace_id: The dataspace_id of this ShowDataConsumptionResponse.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this ShowDataConsumptionResponse.

        管道ID

        :return: The pipe_id of this ShowDataConsumptionResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this ShowDataConsumptionResponse.

        管道ID

        :param pipe_id: The pipe_id of this ShowDataConsumptionResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this ShowDataConsumptionResponse.

        管道名称

        :return: The pipe_name of this ShowDataConsumptionResponse.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this ShowDataConsumptionResponse.

        管道名称

        :param pipe_name: The pipe_name of this ShowDataConsumptionResponse.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def status(self):
        r"""Gets the status of this ShowDataConsumptionResponse.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及   

        :return: The status of this ShowDataConsumptionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDataConsumptionResponse.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及   

        :param status: The status of this ShowDataConsumptionResponse.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ShowDataConsumptionResponse.

        **参数解释**: 网络类型 - INTERNET 互联网 - INTRANET 内联网  **约束限制** 不涉及 **取值范围**: - INTERNET - INTRANET  **默认值** 不涉及         

        :return: The type of this ShowDataConsumptionResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowDataConsumptionResponse.

        **参数解释**: 网络类型 - INTERNET 互联网 - INTRANET 内联网  **约束限制** 不涉及 **取值范围**: - INTERNET - INTRANET  **默认值** 不涉及         

        :param type: The type of this ShowDataConsumptionResponse.
        :type type: str
        """
        self._type = type

    @property
    def access_point(self):
        r"""Gets the access_point of this ShowDataConsumptionResponse.

        接入点域名信息(格式：{dataspace}.{endpoint})

        :return: The access_point of this ShowDataConsumptionResponse.
        :rtype: str
        """
        return self._access_point

    @access_point.setter
    def access_point(self, access_point):
        r"""Sets the access_point of this ShowDataConsumptionResponse.

        接入点域名信息(格式：{dataspace}.{endpoint})

        :param access_point: The access_point of this ShowDataConsumptionResponse.
        :type access_point: str
        """
        self._access_point = access_point

    @property
    def subscription(self):
        r"""Gets the subscription of this ShowDataConsumptionResponse.

        订阅名称

        :return: The subscription of this ShowDataConsumptionResponse.
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        r"""Sets the subscription of this ShowDataConsumptionResponse.

        订阅名称

        :param subscription: The subscription of this ShowDataConsumptionResponse.
        :type subscription: str
        """
        self._subscription = subscription

    @property
    def table_id(self):
        r"""Gets the table_id of this ShowDataConsumptionResponse.

        表Id

        :return: The table_id of this ShowDataConsumptionResponse.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this ShowDataConsumptionResponse.

        表Id

        :param table_id: The table_id of this ShowDataConsumptionResponse.
        :type table_id: str
        """
        self._table_id = table_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowDataConsumptionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDataConsumptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
