# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'type': 'str',
        'create_time': 'str',
        'finish_time': 'str',
        'creator': 'str',
        'status': 'str',
        'shareable': 'bool',
        'data_quantity': 'int',
        'file': 'ModelFile',
        'value_range': 'ValueRange2',
        'description': 'str',
        'failed_message': 'str',
        'losses': 'list[float]',
        'metrics': 'list[ModelMetric]',
        'base_model_id': 'str',
        'base_model_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'type': 'type',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'creator': 'creator',
        'status': 'status',
        'shareable': 'shareable',
        'data_quantity': 'data_quantity',
        'file': 'file',
        'value_range': 'value_range',
        'description': 'description',
        'failed_message': 'failed_message',
        'losses': 'losses',
        'metrics': 'metrics',
        'base_model_id': 'base_model_id',
        'base_model_name': 'base_model_name'
    }

    def __init__(self, name=None, id=None, type=None, create_time=None, finish_time=None, creator=None, status=None, shareable=None, data_quantity=None, file=None, value_range=None, description=None, failed_message=None, losses=None, metrics=None, base_model_id=None, base_model_name=None):
        r"""ModelDto

        The model defined in huaweicloud sdk

        :param name: 模型名称
        :type name: str
        :param id: 模型ID
        :type id: str
        :param type: 模型类型
        :type type: str
        :param create_time: 模型创建时间
        :type create_time: str
        :param finish_time: 模型结束时间
        :type finish_time: str
        :param creator: 创建模型的用户名称
        :type creator: str
        :param status: 作业状态
        :type status: str
        :param shareable: 是否打开组织共享
        :type shareable: bool
        :param data_quantity: 模型数据量
        :type data_quantity: int
        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.ModelFile`
        :param value_range: 
        :type value_range: :class:`huaweicloudsdkeihealth.v1.ValueRange2`
        :param description: 模型描述信息
        :type description: str
        :param failed_message: 失败提示，当作业执行失败时会返回
        :type failed_message: str
        :param losses: 模型训练loss信息
        :type losses: list[float]
        :param metrics: 模型评估指标
        :type metrics: list[:class:`huaweicloudsdkeihealth.v1.ModelMetric`]
        :param base_model_id: 基模型id
        :type base_model_id: str
        :param base_model_name: 基模型名称
        :type base_model_name: str
        """
        
        

        self._name = None
        self._id = None
        self._type = None
        self._create_time = None
        self._finish_time = None
        self._creator = None
        self._status = None
        self._shareable = None
        self._data_quantity = None
        self._file = None
        self._value_range = None
        self._description = None
        self._failed_message = None
        self._losses = None
        self._metrics = None
        self._base_model_id = None
        self._base_model_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if creator is not None:
            self.creator = creator
        if status is not None:
            self.status = status
        if shareable is not None:
            self.shareable = shareable
        if data_quantity is not None:
            self.data_quantity = data_quantity
        if file is not None:
            self.file = file
        if value_range is not None:
            self.value_range = value_range
        if description is not None:
            self.description = description
        if failed_message is not None:
            self.failed_message = failed_message
        if losses is not None:
            self.losses = losses
        if metrics is not None:
            self.metrics = metrics
        if base_model_id is not None:
            self.base_model_id = base_model_id
        if base_model_name is not None:
            self.base_model_name = base_model_name

    @property
    def name(self):
        r"""Gets the name of this ModelDto.

        模型名称

        :return: The name of this ModelDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModelDto.

        模型名称

        :param name: The name of this ModelDto.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ModelDto.

        模型ID

        :return: The id of this ModelDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelDto.

        模型ID

        :param id: The id of this ModelDto.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ModelDto.

        模型类型

        :return: The type of this ModelDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ModelDto.

        模型类型

        :param type: The type of this ModelDto.
        :type type: str
        """
        self._type = type

    @property
    def create_time(self):
        r"""Gets the create_time of this ModelDto.

        模型创建时间

        :return: The create_time of this ModelDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ModelDto.

        模型创建时间

        :param create_time: The create_time of this ModelDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this ModelDto.

        模型结束时间

        :return: The finish_time of this ModelDto.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this ModelDto.

        模型结束时间

        :param finish_time: The finish_time of this ModelDto.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def creator(self):
        r"""Gets the creator of this ModelDto.

        创建模型的用户名称

        :return: The creator of this ModelDto.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ModelDto.

        创建模型的用户名称

        :param creator: The creator of this ModelDto.
        :type creator: str
        """
        self._creator = creator

    @property
    def status(self):
        r"""Gets the status of this ModelDto.

        作业状态

        :return: The status of this ModelDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ModelDto.

        作业状态

        :param status: The status of this ModelDto.
        :type status: str
        """
        self._status = status

    @property
    def shareable(self):
        r"""Gets the shareable of this ModelDto.

        是否打开组织共享

        :return: The shareable of this ModelDto.
        :rtype: bool
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        r"""Sets the shareable of this ModelDto.

        是否打开组织共享

        :param shareable: The shareable of this ModelDto.
        :type shareable: bool
        """
        self._shareable = shareable

    @property
    def data_quantity(self):
        r"""Gets the data_quantity of this ModelDto.

        模型数据量

        :return: The data_quantity of this ModelDto.
        :rtype: int
        """
        return self._data_quantity

    @data_quantity.setter
    def data_quantity(self, data_quantity):
        r"""Sets the data_quantity of this ModelDto.

        模型数据量

        :param data_quantity: The data_quantity of this ModelDto.
        :type data_quantity: int
        """
        self._data_quantity = data_quantity

    @property
    def file(self):
        r"""Gets the file of this ModelDto.

        :return: The file of this ModelDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ModelFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this ModelDto.

        :param file: The file of this ModelDto.
        :type file: :class:`huaweicloudsdkeihealth.v1.ModelFile`
        """
        self._file = file

    @property
    def value_range(self):
        r"""Gets the value_range of this ModelDto.

        :return: The value_range of this ModelDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ValueRange2`
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        r"""Sets the value_range of this ModelDto.

        :param value_range: The value_range of this ModelDto.
        :type value_range: :class:`huaweicloudsdkeihealth.v1.ValueRange2`
        """
        self._value_range = value_range

    @property
    def description(self):
        r"""Gets the description of this ModelDto.

        模型描述信息

        :return: The description of this ModelDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModelDto.

        模型描述信息

        :param description: The description of this ModelDto.
        :type description: str
        """
        self._description = description

    @property
    def failed_message(self):
        r"""Gets the failed_message of this ModelDto.

        失败提示，当作业执行失败时会返回

        :return: The failed_message of this ModelDto.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        r"""Sets the failed_message of this ModelDto.

        失败提示，当作业执行失败时会返回

        :param failed_message: The failed_message of this ModelDto.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def losses(self):
        r"""Gets the losses of this ModelDto.

        模型训练loss信息

        :return: The losses of this ModelDto.
        :rtype: list[float]
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        r"""Sets the losses of this ModelDto.

        模型训练loss信息

        :param losses: The losses of this ModelDto.
        :type losses: list[float]
        """
        self._losses = losses

    @property
    def metrics(self):
        r"""Gets the metrics of this ModelDto.

        模型评估指标

        :return: The metrics of this ModelDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ModelMetric`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this ModelDto.

        模型评估指标

        :param metrics: The metrics of this ModelDto.
        :type metrics: list[:class:`huaweicloudsdkeihealth.v1.ModelMetric`]
        """
        self._metrics = metrics

    @property
    def base_model_id(self):
        r"""Gets the base_model_id of this ModelDto.

        基模型id

        :return: The base_model_id of this ModelDto.
        :rtype: str
        """
        return self._base_model_id

    @base_model_id.setter
    def base_model_id(self, base_model_id):
        r"""Sets the base_model_id of this ModelDto.

        基模型id

        :param base_model_id: The base_model_id of this ModelDto.
        :type base_model_id: str
        """
        self._base_model_id = base_model_id

    @property
    def base_model_name(self):
        r"""Gets the base_model_name of this ModelDto.

        基模型名称

        :return: The base_model_name of this ModelDto.
        :rtype: str
        """
        return self._base_model_name

    @base_model_name.setter
    def base_model_name(self, base_model_name):
        r"""Sets the base_model_name of this ModelDto.

        基模型名称

        :param base_model_name: The base_model_name of this ModelDto.
        :type base_model_name: str
        """
        self._base_model_name = base_model_name

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
        if not isinstance(other, ModelDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
