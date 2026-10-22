# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowV2ComputeVersionResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'compute_id': 'str',
        'name': 'str',
        'capacity': 'CapacityVersion',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'creator': 'Creator',
        'error': 'Error',
        'operation': 'Operation'
    }

    attribute_map = {
        'id': 'id',
        'compute_id': 'compute_id',
        'name': 'name',
        'capacity': 'capacity',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'creator': 'creator',
        'error': 'error',
        'operation': 'operation'
    }

    def __init__(self, id=None, compute_id=None, name=None, capacity=None, create_time=None, update_time=None, creator=None, error=None, operation=None):
        r"""ShowV2ComputeVersionResponseBody

        The model defined in huaweicloud sdk

        :param id: **参数解释**：计算资源记录ID。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 
        :type id: str
        :param compute_id: **参数解释**：计算资源ID。 **取值范围**：长度为1~36的英文字母、数字和中划线的组合。 
        :type compute_id: str
        :param name: **参数解释**：计算资源名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 
        :type name: str
        :param capacity: 
        :type capacity: CapacityVersion
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        :param update_time: **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type update_time: datetime
        :param creator: 
        :type creator: :class:`huaweicloudsdkaidatalake.v2.Creator`
        :param error: 
        :type error: :class:`huaweicloudsdkaidatalake.v2.Error`
        :param operation: 
        :type operation: :class:`huaweicloudsdkaidatalake.v2.Operation`
        """
        
        

        self._id = None
        self._compute_id = None
        self._name = None
        self._capacity = None
        self._create_time = None
        self._update_time = None
        self._creator = None
        self._error = None
        self._operation = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if compute_id is not None:
            self.compute_id = compute_id
        if name is not None:
            self.name = name
        if capacity is not None:
            self.capacity = capacity
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if creator is not None:
            self.creator = creator
        if error is not None:
            self.error = error
        if operation is not None:
            self.operation = operation

    @property
    def id(self):
        r"""Gets the id of this ShowV2ComputeVersionResponseBody.

        **参数解释**：计算资源记录ID。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 

        :return: The id of this ShowV2ComputeVersionResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowV2ComputeVersionResponseBody.

        **参数解释**：计算资源记录ID。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 

        :param id: The id of this ShowV2ComputeVersionResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def compute_id(self):
        r"""Gets the compute_id of this ShowV2ComputeVersionResponseBody.

        **参数解释**：计算资源ID。 **取值范围**：长度为1~36的英文字母、数字和中划线的组合。 

        :return: The compute_id of this ShowV2ComputeVersionResponseBody.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        r"""Sets the compute_id of this ShowV2ComputeVersionResponseBody.

        **参数解释**：计算资源ID。 **取值范围**：长度为1~36的英文字母、数字和中划线的组合。 

        :param compute_id: The compute_id of this ShowV2ComputeVersionResponseBody.
        :type compute_id: str
        """
        self._compute_id = compute_id

    @property
    def name(self):
        r"""Gets the name of this ShowV2ComputeVersionResponseBody.

        **参数解释**：计算资源名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 

        :return: The name of this ShowV2ComputeVersionResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowV2ComputeVersionResponseBody.

        **参数解释**：计算资源名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 

        :param name: The name of this ShowV2ComputeVersionResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def capacity(self):
        r"""Gets the capacity of this ShowV2ComputeVersionResponseBody.

        :return: The capacity of this ShowV2ComputeVersionResponseBody.
        :rtype: CapacityVersion
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this ShowV2ComputeVersionResponseBody.

        :param capacity: The capacity of this ShowV2ComputeVersionResponseBody.
        :type capacity: CapacityVersion
        """
        self._capacity = capacity

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowV2ComputeVersionResponseBody.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this ShowV2ComputeVersionResponseBody.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowV2ComputeVersionResponseBody.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this ShowV2ComputeVersionResponseBody.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowV2ComputeVersionResponseBody.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The update_time of this ShowV2ComputeVersionResponseBody.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowV2ComputeVersionResponseBody.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param update_time: The update_time of this ShowV2ComputeVersionResponseBody.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def creator(self):
        r"""Gets the creator of this ShowV2ComputeVersionResponseBody.

        :return: The creator of this ShowV2ComputeVersionResponseBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.Creator`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ShowV2ComputeVersionResponseBody.

        :param creator: The creator of this ShowV2ComputeVersionResponseBody.
        :type creator: :class:`huaweicloudsdkaidatalake.v2.Creator`
        """
        self._creator = creator

    @property
    def error(self):
        r"""Gets the error of this ShowV2ComputeVersionResponseBody.

        :return: The error of this ShowV2ComputeVersionResponseBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.Error`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ShowV2ComputeVersionResponseBody.

        :param error: The error of this ShowV2ComputeVersionResponseBody.
        :type error: :class:`huaweicloudsdkaidatalake.v2.Error`
        """
        self._error = error

    @property
    def operation(self):
        r"""Gets the operation of this ShowV2ComputeVersionResponseBody.

        :return: The operation of this ShowV2ComputeVersionResponseBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.Operation`
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ShowV2ComputeVersionResponseBody.

        :param operation: The operation of this ShowV2ComputeVersionResponseBody.
        :type operation: :class:`huaweicloudsdkaidatalake.v2.Operation`
        """
        self._operation = operation

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
        if not isinstance(other, ShowV2ComputeVersionResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
