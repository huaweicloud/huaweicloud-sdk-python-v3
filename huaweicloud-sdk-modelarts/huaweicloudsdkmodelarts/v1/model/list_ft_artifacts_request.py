# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFtArtifactsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'training_job_id': 'str',
        'steps': 'int',
        'epoch': 'int',
        'loss': 'float',
        'status': 'str',
        'order_by_create_time_asc': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'training_job_id': 'training_job_id',
        'steps': 'steps',
        'epoch': 'epoch',
        'loss': 'loss',
        'status': 'status',
        'order_by_create_time_asc': 'order_by_create_time_asc',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, training_job_id=None, steps=None, epoch=None, loss=None, status=None, order_by_create_time_asc=None, limit=None, offset=None):
        r"""ListFtArtifactsRequest

        The model defined in huaweicloud sdk

        :param training_job_id: 训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。
        :type training_job_id: str
        :param steps: 步数。
        :type steps: int
        :param epoch: 轮数。
        :type epoch: int
        :param loss: loss值。
        :type loss: float
        :param status: 状态。
        :type status: str
        :param order_by_create_time_asc: 是否按照创建时间排序。
        :type order_by_create_time_asc: bool
        :param limit: 返回的数据条目数。
        :type limit: int
        :param offset: 数据条目偏移量。
        :type offset: int
        """
        
        

        self._training_job_id = None
        self._steps = None
        self._epoch = None
        self._loss = None
        self._status = None
        self._order_by_create_time_asc = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.training_job_id = training_job_id
        if steps is not None:
            self.steps = steps
        if epoch is not None:
            self.epoch = epoch
        if loss is not None:
            self.loss = loss
        if status is not None:
            self.status = status
        if order_by_create_time_asc is not None:
            self.order_by_create_time_asc = order_by_create_time_asc
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def training_job_id(self):
        r"""Gets the training_job_id of this ListFtArtifactsRequest.

        训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。

        :return: The training_job_id of this ListFtArtifactsRequest.
        :rtype: str
        """
        return self._training_job_id

    @training_job_id.setter
    def training_job_id(self, training_job_id):
        r"""Sets the training_job_id of this ListFtArtifactsRequest.

        训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。

        :param training_job_id: The training_job_id of this ListFtArtifactsRequest.
        :type training_job_id: str
        """
        self._training_job_id = training_job_id

    @property
    def steps(self):
        r"""Gets the steps of this ListFtArtifactsRequest.

        步数。

        :return: The steps of this ListFtArtifactsRequest.
        :rtype: int
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this ListFtArtifactsRequest.

        步数。

        :param steps: The steps of this ListFtArtifactsRequest.
        :type steps: int
        """
        self._steps = steps

    @property
    def epoch(self):
        r"""Gets the epoch of this ListFtArtifactsRequest.

        轮数。

        :return: The epoch of this ListFtArtifactsRequest.
        :rtype: int
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        r"""Sets the epoch of this ListFtArtifactsRequest.

        轮数。

        :param epoch: The epoch of this ListFtArtifactsRequest.
        :type epoch: int
        """
        self._epoch = epoch

    @property
    def loss(self):
        r"""Gets the loss of this ListFtArtifactsRequest.

        loss值。

        :return: The loss of this ListFtArtifactsRequest.
        :rtype: float
        """
        return self._loss

    @loss.setter
    def loss(self, loss):
        r"""Sets the loss of this ListFtArtifactsRequest.

        loss值。

        :param loss: The loss of this ListFtArtifactsRequest.
        :type loss: float
        """
        self._loss = loss

    @property
    def status(self):
        r"""Gets the status of this ListFtArtifactsRequest.

        状态。

        :return: The status of this ListFtArtifactsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListFtArtifactsRequest.

        状态。

        :param status: The status of this ListFtArtifactsRequest.
        :type status: str
        """
        self._status = status

    @property
    def order_by_create_time_asc(self):
        r"""Gets the order_by_create_time_asc of this ListFtArtifactsRequest.

        是否按照创建时间排序。

        :return: The order_by_create_time_asc of this ListFtArtifactsRequest.
        :rtype: bool
        """
        return self._order_by_create_time_asc

    @order_by_create_time_asc.setter
    def order_by_create_time_asc(self, order_by_create_time_asc):
        r"""Sets the order_by_create_time_asc of this ListFtArtifactsRequest.

        是否按照创建时间排序。

        :param order_by_create_time_asc: The order_by_create_time_asc of this ListFtArtifactsRequest.
        :type order_by_create_time_asc: bool
        """
        self._order_by_create_time_asc = order_by_create_time_asc

    @property
    def limit(self):
        r"""Gets the limit of this ListFtArtifactsRequest.

        返回的数据条目数。

        :return: The limit of this ListFtArtifactsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFtArtifactsRequest.

        返回的数据条目数。

        :param limit: The limit of this ListFtArtifactsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListFtArtifactsRequest.

        数据条目偏移量。

        :return: The offset of this ListFtArtifactsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFtArtifactsRequest.

        数据条目偏移量。

        :param offset: The offset of this ListFtArtifactsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListFtArtifactsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
