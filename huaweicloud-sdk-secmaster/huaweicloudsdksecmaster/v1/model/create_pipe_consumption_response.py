# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePipeConsumptionResponse(SdkResponse):

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
        'dataspace_id': 'str',
        'pipe_id': 'str',
        'pipe_name': 'str',
        'status': 'str',
        'subscription': 'str',
        'type': 'str'
    }

    attribute_map = {
        'access_point': 'access_point',
        'dataspace_id': 'dataspace_id',
        'pipe_id': 'pipe_id',
        'pipe_name': 'pipe_name',
        'status': 'status',
        'subscription': 'subscription',
        'type': 'type'
    }

    def __init__(self, access_point=None, dataspace_id=None, pipe_id=None, pipe_name=None, status=None, subscription=None, type=None):
        r"""CreatePipeConsumptionResponse

        The model defined in huaweicloud sdk

        :param access_point: 访问点地址
        :type access_point: str
        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param pipe_id: 管道ID
        :type pipe_id: str
        :param pipe_name: 管道名称
        :type pipe_name: str
        :param status: 管道状态
        :type status: str
        :param subscription: 订阅ID
        :type subscription: str
        :param type: 管道类型
        :type type: str
        """
        
        super().__init__()

        self._access_point = None
        self._dataspace_id = None
        self._pipe_id = None
        self._pipe_name = None
        self._status = None
        self._subscription = None
        self._type = None
        self.discriminator = None

        if access_point is not None:
            self.access_point = access_point
        if dataspace_id is not None:
            self.dataspace_id = dataspace_id
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if pipe_name is not None:
            self.pipe_name = pipe_name
        if status is not None:
            self.status = status
        if subscription is not None:
            self.subscription = subscription
        if type is not None:
            self.type = type

    @property
    def access_point(self):
        r"""Gets the access_point of this CreatePipeConsumptionResponse.

        访问点地址

        :return: The access_point of this CreatePipeConsumptionResponse.
        :rtype: str
        """
        return self._access_point

    @access_point.setter
    def access_point(self, access_point):
        r"""Sets the access_point of this CreatePipeConsumptionResponse.

        访问点地址

        :param access_point: The access_point of this CreatePipeConsumptionResponse.
        :type access_point: str
        """
        self._access_point = access_point

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this CreatePipeConsumptionResponse.

        数据空间ID

        :return: The dataspace_id of this CreatePipeConsumptionResponse.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this CreatePipeConsumptionResponse.

        数据空间ID

        :param dataspace_id: The dataspace_id of this CreatePipeConsumptionResponse.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this CreatePipeConsumptionResponse.

        管道ID

        :return: The pipe_id of this CreatePipeConsumptionResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this CreatePipeConsumptionResponse.

        管道ID

        :param pipe_id: The pipe_id of this CreatePipeConsumptionResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this CreatePipeConsumptionResponse.

        管道名称

        :return: The pipe_name of this CreatePipeConsumptionResponse.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this CreatePipeConsumptionResponse.

        管道名称

        :param pipe_name: The pipe_name of this CreatePipeConsumptionResponse.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def status(self):
        r"""Gets the status of this CreatePipeConsumptionResponse.

        管道状态

        :return: The status of this CreatePipeConsumptionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreatePipeConsumptionResponse.

        管道状态

        :param status: The status of this CreatePipeConsumptionResponse.
        :type status: str
        """
        self._status = status

    @property
    def subscription(self):
        r"""Gets the subscription of this CreatePipeConsumptionResponse.

        订阅ID

        :return: The subscription of this CreatePipeConsumptionResponse.
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        r"""Sets the subscription of this CreatePipeConsumptionResponse.

        订阅ID

        :param subscription: The subscription of this CreatePipeConsumptionResponse.
        :type subscription: str
        """
        self._subscription = subscription

    @property
    def type(self):
        r"""Gets the type of this CreatePipeConsumptionResponse.

        管道类型

        :return: The type of this CreatePipeConsumptionResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreatePipeConsumptionResponse.

        管道类型

        :param type: The type of this CreatePipeConsumptionResponse.
        :type type: str
        """
        self._type = type

    def to_dict(self):
        import warnings
        warnings.warn("CreatePipeConsumptionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreatePipeConsumptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
