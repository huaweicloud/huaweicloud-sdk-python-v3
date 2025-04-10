# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServiceInstanceDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'visibility': 'str',
        'source': 'SourceRef',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'endpoint_id': 'str',
        'status': 'StatusEnum',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'duration': 'int',
        'create_user': 'User',
        'type': 'ServiceType',
        'update_user': 'User',
        'url': 'Url',
        'config': 'AppInstanceConfig',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'visibility': 'visibility',
        'source': 'source',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'endpoint_id': 'endpoint_id',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'duration': 'duration',
        'create_user': 'create_user',
        'type': 'type',
        'update_user': 'update_user',
        'url': 'url',
        'config': 'config',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, visibility=None, source=None, id=None, name=None, description=None, endpoint_id=None, status=None, create_time=None, update_time=None, duration=None, create_user=None, type=None, update_user=None, url=None, config=None, error_code=None, error_msg=None):
        r"""ShowServiceInstanceDetailResponse

        The model defined in huaweicloud sdk

        :param visibility: 可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE
        :type visibility: str
        :param source: 
        :type source: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        :param id: Service Instance的ID
        :type id: str
        :param name: 一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param description: 描述信息
        :type description: str
        :param endpoint_id: endpoint空间id
        :type endpoint_id: str
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsfabricep.v1.StatusEnum`
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param duration: 运行时长
        :type duration: int
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        :param type: 
        :type type: :class:`huaweicloudsdkdataartsfabricep.v1.ServiceType`
        :param update_user: 
        :type update_user: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        :param url: 
        :type url: :class:`huaweicloudsdkdataartsfabricep.v1.Url`
        :param config: 
        :type config: :class:`huaweicloudsdkdataartsfabricep.v1.AppInstanceConfig`
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误描述
        :type error_msg: str
        """
        
        super(ShowServiceInstanceDetailResponse, self).__init__()

        self._visibility = None
        self._source = None
        self._id = None
        self._name = None
        self._description = None
        self._endpoint_id = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._duration = None
        self._create_user = None
        self._type = None
        self._update_user = None
        self._url = None
        self._config = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if visibility is not None:
            self.visibility = visibility
        if source is not None:
            self.source = source
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if duration is not None:
            self.duration = duration
        if create_user is not None:
            self.create_user = create_user
        if type is not None:
            self.type = type
        if update_user is not None:
            self.update_user = update_user
        if url is not None:
            self.url = url
        if config is not None:
            self.config = config
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def visibility(self):
        r"""Gets the visibility of this ShowServiceInstanceDetailResponse.

        可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE

        :return: The visibility of this ShowServiceInstanceDetailResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ShowServiceInstanceDetailResponse.

        可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE

        :param visibility: The visibility of this ShowServiceInstanceDetailResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def source(self):
        r"""Gets the source of this ShowServiceInstanceDetailResponse.

        :return: The source of this ShowServiceInstanceDetailResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ShowServiceInstanceDetailResponse.

        :param source: The source of this ShowServiceInstanceDetailResponse.
        :type source: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        """
        self._source = source

    @property
    def id(self):
        r"""Gets the id of this ShowServiceInstanceDetailResponse.

        Service Instance的ID

        :return: The id of this ShowServiceInstanceDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowServiceInstanceDetailResponse.

        Service Instance的ID

        :param id: The id of this ShowServiceInstanceDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowServiceInstanceDetailResponse.

        一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this ShowServiceInstanceDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowServiceInstanceDetailResponse.

        一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this ShowServiceInstanceDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowServiceInstanceDetailResponse.

        描述信息

        :return: The description of this ShowServiceInstanceDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowServiceInstanceDetailResponse.

        描述信息

        :param description: The description of this ShowServiceInstanceDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ShowServiceInstanceDetailResponse.

        endpoint空间id

        :return: The endpoint_id of this ShowServiceInstanceDetailResponse.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ShowServiceInstanceDetailResponse.

        endpoint空间id

        :param endpoint_id: The endpoint_id of this ShowServiceInstanceDetailResponse.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def status(self):
        r"""Gets the status of this ShowServiceInstanceDetailResponse.

        :return: The status of this ShowServiceInstanceDetailResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.StatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowServiceInstanceDetailResponse.

        :param status: The status of this ShowServiceInstanceDetailResponse.
        :type status: :class:`huaweicloudsdkdataartsfabricep.v1.StatusEnum`
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowServiceInstanceDetailResponse.

        创建时间

        :return: The create_time of this ShowServiceInstanceDetailResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowServiceInstanceDetailResponse.

        创建时间

        :param create_time: The create_time of this ShowServiceInstanceDetailResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowServiceInstanceDetailResponse.

        更新时间

        :return: The update_time of this ShowServiceInstanceDetailResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowServiceInstanceDetailResponse.

        更新时间

        :param update_time: The update_time of this ShowServiceInstanceDetailResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def duration(self):
        r"""Gets the duration of this ShowServiceInstanceDetailResponse.

        运行时长

        :return: The duration of this ShowServiceInstanceDetailResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ShowServiceInstanceDetailResponse.

        运行时长

        :param duration: The duration of this ShowServiceInstanceDetailResponse.
        :type duration: int
        """
        self._duration = duration

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowServiceInstanceDetailResponse.

        :return: The create_user of this ShowServiceInstanceDetailResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowServiceInstanceDetailResponse.

        :param create_user: The create_user of this ShowServiceInstanceDetailResponse.
        :type create_user: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        """
        self._create_user = create_user

    @property
    def type(self):
        r"""Gets the type of this ShowServiceInstanceDetailResponse.

        :return: The type of this ShowServiceInstanceDetailResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.ServiceType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowServiceInstanceDetailResponse.

        :param type: The type of this ShowServiceInstanceDetailResponse.
        :type type: :class:`huaweicloudsdkdataartsfabricep.v1.ServiceType`
        """
        self._type = type

    @property
    def update_user(self):
        r"""Gets the update_user of this ShowServiceInstanceDetailResponse.

        :return: The update_user of this ShowServiceInstanceDetailResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this ShowServiceInstanceDetailResponse.

        :param update_user: The update_user of this ShowServiceInstanceDetailResponse.
        :type update_user: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        """
        self._update_user = update_user

    @property
    def url(self):
        r"""Gets the url of this ShowServiceInstanceDetailResponse.

        :return: The url of this ShowServiceInstanceDetailResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.Url`
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowServiceInstanceDetailResponse.

        :param url: The url of this ShowServiceInstanceDetailResponse.
        :type url: :class:`huaweicloudsdkdataartsfabricep.v1.Url`
        """
        self._url = url

    @property
    def config(self):
        r"""Gets the config of this ShowServiceInstanceDetailResponse.

        :return: The config of this ShowServiceInstanceDetailResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.AppInstanceConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this ShowServiceInstanceDetailResponse.

        :param config: The config of this ShowServiceInstanceDetailResponse.
        :type config: :class:`huaweicloudsdkdataartsfabricep.v1.AppInstanceConfig`
        """
        self._config = config

    @property
    def error_code(self):
        r"""Gets the error_code of this ShowServiceInstanceDetailResponse.

        错误码

        :return: The error_code of this ShowServiceInstanceDetailResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ShowServiceInstanceDetailResponse.

        错误码

        :param error_code: The error_code of this ShowServiceInstanceDetailResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ShowServiceInstanceDetailResponse.

        错误描述

        :return: The error_msg of this ShowServiceInstanceDetailResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ShowServiceInstanceDetailResponse.

        错误描述

        :param error_msg: The error_msg of this ShowServiceInstanceDetailResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ShowServiceInstanceDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
