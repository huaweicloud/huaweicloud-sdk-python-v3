# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShipperAuthorizeResponseBodyDataData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorize_status': 'int',
        'data_source_query': 'str',
        'data_type': 'int',
        'dataspace': 'str',
        'id': 'int',
        'pipe': 'str',
        'region': 'str',
        'request_time': 'int',
        'handler_time': 'int',
        'run_status': 'int',
        'shipper_id': 'str',
        'shipper_name': 'str',
        'workspace': 'str'
    }

    attribute_map = {
        'authorize_status': 'authorize_status',
        'data_source_query': 'data_source_query',
        'data_type': 'data_type',
        'dataspace': 'dataspace',
        'id': 'id',
        'pipe': 'pipe',
        'region': 'region',
        'request_time': 'request_time',
        'handler_time': 'handler_time',
        'run_status': 'run_status',
        'shipper_id': 'shipper_id',
        'shipper_name': 'shipper_name',
        'workspace': 'workspace'
    }

    def __init__(self, authorize_status=None, data_source_query=None, data_type=None, dataspace=None, id=None, pipe=None, region=None, request_time=None, handler_time=None, run_status=None, shipper_id=None, shipper_name=None, workspace=None):
        r"""ShowShipperAuthorizeResponseBodyDataData

        The model defined in huaweicloud sdk

        :param authorize_status: 授权状态，0-已授权，1-未授权，2-拒绝授权
        :type authorize_status: int
        :param data_source_query: 数据源查询字符串，表示数据源的路径
        :type data_source_query: str
        :param data_type: 数据类型，具体含义根据业务定义
        :type data_type: int
        :param dataspace: 数据空间ID，唯一标识
        :type dataspace: str
        :param id: 唯一标识ID
        :type id: int
        :param pipe: 管道ID，唯一标识
        :type pipe: str
        :param region: 地域信息
        :type region: str
        :param request_time: 请求时间，单位为毫秒的时间戳
        :type request_time: int
        :param handler_time: 授权时间，单位为毫秒的时间戳
        :type handler_time: int
        :param run_status: 运行状态，具体含义根据业务定义
        :type run_status: int
        :param shipper_id: 船运ID，唯一标识
        :type shipper_id: str
        :param shipper_name: 船运名称
        :type shipper_name: str
        :param workspace: 工作空间ID，唯一标识
        :type workspace: str
        """
        
        

        self._authorize_status = None
        self._data_source_query = None
        self._data_type = None
        self._dataspace = None
        self._id = None
        self._pipe = None
        self._region = None
        self._request_time = None
        self._handler_time = None
        self._run_status = None
        self._shipper_id = None
        self._shipper_name = None
        self._workspace = None
        self.discriminator = None

        if authorize_status is not None:
            self.authorize_status = authorize_status
        if data_source_query is not None:
            self.data_source_query = data_source_query
        if data_type is not None:
            self.data_type = data_type
        if dataspace is not None:
            self.dataspace = dataspace
        if id is not None:
            self.id = id
        if pipe is not None:
            self.pipe = pipe
        if region is not None:
            self.region = region
        if request_time is not None:
            self.request_time = request_time
        if handler_time is not None:
            self.handler_time = handler_time
        if run_status is not None:
            self.run_status = run_status
        if shipper_id is not None:
            self.shipper_id = shipper_id
        if shipper_name is not None:
            self.shipper_name = shipper_name
        if workspace is not None:
            self.workspace = workspace

    @property
    def authorize_status(self):
        r"""Gets the authorize_status of this ShowShipperAuthorizeResponseBodyDataData.

        授权状态，0-已授权，1-未授权，2-拒绝授权

        :return: The authorize_status of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: int
        """
        return self._authorize_status

    @authorize_status.setter
    def authorize_status(self, authorize_status):
        r"""Sets the authorize_status of this ShowShipperAuthorizeResponseBodyDataData.

        授权状态，0-已授权，1-未授权，2-拒绝授权

        :param authorize_status: The authorize_status of this ShowShipperAuthorizeResponseBodyDataData.
        :type authorize_status: int
        """
        self._authorize_status = authorize_status

    @property
    def data_source_query(self):
        r"""Gets the data_source_query of this ShowShipperAuthorizeResponseBodyDataData.

        数据源查询字符串，表示数据源的路径

        :return: The data_source_query of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: str
        """
        return self._data_source_query

    @data_source_query.setter
    def data_source_query(self, data_source_query):
        r"""Sets the data_source_query of this ShowShipperAuthorizeResponseBodyDataData.

        数据源查询字符串，表示数据源的路径

        :param data_source_query: The data_source_query of this ShowShipperAuthorizeResponseBodyDataData.
        :type data_source_query: str
        """
        self._data_source_query = data_source_query

    @property
    def data_type(self):
        r"""Gets the data_type of this ShowShipperAuthorizeResponseBodyDataData.

        数据类型，具体含义根据业务定义

        :return: The data_type of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: int
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this ShowShipperAuthorizeResponseBodyDataData.

        数据类型，具体含义根据业务定义

        :param data_type: The data_type of this ShowShipperAuthorizeResponseBodyDataData.
        :type data_type: int
        """
        self._data_type = data_type

    @property
    def dataspace(self):
        r"""Gets the dataspace of this ShowShipperAuthorizeResponseBodyDataData.

        数据空间ID，唯一标识

        :return: The dataspace of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: str
        """
        return self._dataspace

    @dataspace.setter
    def dataspace(self, dataspace):
        r"""Sets the dataspace of this ShowShipperAuthorizeResponseBodyDataData.

        数据空间ID，唯一标识

        :param dataspace: The dataspace of this ShowShipperAuthorizeResponseBodyDataData.
        :type dataspace: str
        """
        self._dataspace = dataspace

    @property
    def id(self):
        r"""Gets the id of this ShowShipperAuthorizeResponseBodyDataData.

        唯一标识ID

        :return: The id of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowShipperAuthorizeResponseBodyDataData.

        唯一标识ID

        :param id: The id of this ShowShipperAuthorizeResponseBodyDataData.
        :type id: int
        """
        self._id = id

    @property
    def pipe(self):
        r"""Gets the pipe of this ShowShipperAuthorizeResponseBodyDataData.

        管道ID，唯一标识

        :return: The pipe of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: str
        """
        return self._pipe

    @pipe.setter
    def pipe(self, pipe):
        r"""Sets the pipe of this ShowShipperAuthorizeResponseBodyDataData.

        管道ID，唯一标识

        :param pipe: The pipe of this ShowShipperAuthorizeResponseBodyDataData.
        :type pipe: str
        """
        self._pipe = pipe

    @property
    def region(self):
        r"""Gets the region of this ShowShipperAuthorizeResponseBodyDataData.

        地域信息

        :return: The region of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowShipperAuthorizeResponseBodyDataData.

        地域信息

        :param region: The region of this ShowShipperAuthorizeResponseBodyDataData.
        :type region: str
        """
        self._region = region

    @property
    def request_time(self):
        r"""Gets the request_time of this ShowShipperAuthorizeResponseBodyDataData.

        请求时间，单位为毫秒的时间戳

        :return: The request_time of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: int
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        r"""Sets the request_time of this ShowShipperAuthorizeResponseBodyDataData.

        请求时间，单位为毫秒的时间戳

        :param request_time: The request_time of this ShowShipperAuthorizeResponseBodyDataData.
        :type request_time: int
        """
        self._request_time = request_time

    @property
    def handler_time(self):
        r"""Gets the handler_time of this ShowShipperAuthorizeResponseBodyDataData.

        授权时间，单位为毫秒的时间戳

        :return: The handler_time of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: int
        """
        return self._handler_time

    @handler_time.setter
    def handler_time(self, handler_time):
        r"""Sets the handler_time of this ShowShipperAuthorizeResponseBodyDataData.

        授权时间，单位为毫秒的时间戳

        :param handler_time: The handler_time of this ShowShipperAuthorizeResponseBodyDataData.
        :type handler_time: int
        """
        self._handler_time = handler_time

    @property
    def run_status(self):
        r"""Gets the run_status of this ShowShipperAuthorizeResponseBodyDataData.

        运行状态，具体含义根据业务定义

        :return: The run_status of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: int
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        r"""Sets the run_status of this ShowShipperAuthorizeResponseBodyDataData.

        运行状态，具体含义根据业务定义

        :param run_status: The run_status of this ShowShipperAuthorizeResponseBodyDataData.
        :type run_status: int
        """
        self._run_status = run_status

    @property
    def shipper_id(self):
        r"""Gets the shipper_id of this ShowShipperAuthorizeResponseBodyDataData.

        船运ID，唯一标识

        :return: The shipper_id of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: str
        """
        return self._shipper_id

    @shipper_id.setter
    def shipper_id(self, shipper_id):
        r"""Sets the shipper_id of this ShowShipperAuthorizeResponseBodyDataData.

        船运ID，唯一标识

        :param shipper_id: The shipper_id of this ShowShipperAuthorizeResponseBodyDataData.
        :type shipper_id: str
        """
        self._shipper_id = shipper_id

    @property
    def shipper_name(self):
        r"""Gets the shipper_name of this ShowShipperAuthorizeResponseBodyDataData.

        船运名称

        :return: The shipper_name of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: str
        """
        return self._shipper_name

    @shipper_name.setter
    def shipper_name(self, shipper_name):
        r"""Sets the shipper_name of this ShowShipperAuthorizeResponseBodyDataData.

        船运名称

        :param shipper_name: The shipper_name of this ShowShipperAuthorizeResponseBodyDataData.
        :type shipper_name: str
        """
        self._shipper_name = shipper_name

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowShipperAuthorizeResponseBodyDataData.

        工作空间ID，唯一标识

        :return: The workspace of this ShowShipperAuthorizeResponseBodyDataData.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowShipperAuthorizeResponseBodyDataData.

        工作空间ID，唯一标识

        :param workspace: The workspace of this ShowShipperAuthorizeResponseBodyDataData.
        :type workspace: str
        """
        self._workspace = workspace

    def to_dict(self):
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
        if not isinstance(other, ShowShipperAuthorizeResponseBodyDataData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
