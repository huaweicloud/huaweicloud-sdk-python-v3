# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceInstanceBriefInfo:

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
        'type': 'ServiceType'
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
        'type': 'type'
    }

    def __init__(self, visibility=None, source=None, id=None, name=None, description=None, endpoint_id=None, status=None, create_time=None, update_time=None, duration=None, create_user=None, type=None):
        r"""ServiceInstanceBriefInfo

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
        """
        
        

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

    @property
    def visibility(self):
        r"""Gets the visibility of this ServiceInstanceBriefInfo.

        可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE

        :return: The visibility of this ServiceInstanceBriefInfo.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ServiceInstanceBriefInfo.

        可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE

        :param visibility: The visibility of this ServiceInstanceBriefInfo.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def source(self):
        r"""Gets the source of this ServiceInstanceBriefInfo.

        :return: The source of this ServiceInstanceBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ServiceInstanceBriefInfo.

        :param source: The source of this ServiceInstanceBriefInfo.
        :type source: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        """
        self._source = source

    @property
    def id(self):
        r"""Gets the id of this ServiceInstanceBriefInfo.

        Service Instance的ID

        :return: The id of this ServiceInstanceBriefInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServiceInstanceBriefInfo.

        Service Instance的ID

        :param id: The id of this ServiceInstanceBriefInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ServiceInstanceBriefInfo.

        一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this ServiceInstanceBriefInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServiceInstanceBriefInfo.

        一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this ServiceInstanceBriefInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ServiceInstanceBriefInfo.

        描述信息

        :return: The description of this ServiceInstanceBriefInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServiceInstanceBriefInfo.

        描述信息

        :param description: The description of this ServiceInstanceBriefInfo.
        :type description: str
        """
        self._description = description

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ServiceInstanceBriefInfo.

        endpoint空间id

        :return: The endpoint_id of this ServiceInstanceBriefInfo.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ServiceInstanceBriefInfo.

        endpoint空间id

        :param endpoint_id: The endpoint_id of this ServiceInstanceBriefInfo.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def status(self):
        r"""Gets the status of this ServiceInstanceBriefInfo.

        :return: The status of this ServiceInstanceBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.StatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServiceInstanceBriefInfo.

        :param status: The status of this ServiceInstanceBriefInfo.
        :type status: :class:`huaweicloudsdkdataartsfabricep.v1.StatusEnum`
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ServiceInstanceBriefInfo.

        创建时间

        :return: The create_time of this ServiceInstanceBriefInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ServiceInstanceBriefInfo.

        创建时间

        :param create_time: The create_time of this ServiceInstanceBriefInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ServiceInstanceBriefInfo.

        更新时间

        :return: The update_time of this ServiceInstanceBriefInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ServiceInstanceBriefInfo.

        更新时间

        :param update_time: The update_time of this ServiceInstanceBriefInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def duration(self):
        r"""Gets the duration of this ServiceInstanceBriefInfo.

        运行时长

        :return: The duration of this ServiceInstanceBriefInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ServiceInstanceBriefInfo.

        运行时长

        :param duration: The duration of this ServiceInstanceBriefInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def create_user(self):
        r"""Gets the create_user of this ServiceInstanceBriefInfo.

        :return: The create_user of this ServiceInstanceBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ServiceInstanceBriefInfo.

        :param create_user: The create_user of this ServiceInstanceBriefInfo.
        :type create_user: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        """
        self._create_user = create_user

    @property
    def type(self):
        r"""Gets the type of this ServiceInstanceBriefInfo.

        :return: The type of this ServiceInstanceBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.ServiceType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ServiceInstanceBriefInfo.

        :param type: The type of this ServiceInstanceBriefInfo.
        :type type: :class:`huaweicloudsdkdataartsfabricep.v1.ServiceType`
        """
        self._type = type

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
        if not isinstance(other, ServiceInstanceBriefInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
