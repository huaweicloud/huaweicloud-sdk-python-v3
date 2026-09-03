# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArtifactInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'artifact_type': 'str',
        'is_best': 'bool',
        'artifact_id': 'str',
        'continue_train_nums': 'int',
        'asset_id': 'str',
        'asset_name': 'str',
        'status': 'str',
        'epoch': 'int',
        'steps': 'int',
        'loss': 'float',
        'create_time': 'str',
        'publish_error_msg': 'str',
        'task_infos': 'list[ContinueTrainTask]'
    }

    attribute_map = {
        'artifact_type': 'artifact_type',
        'is_best': 'is_best',
        'artifact_id': 'artifact_id',
        'continue_train_nums': 'continue_train_nums',
        'asset_id': 'asset_id',
        'asset_name': 'asset_name',
        'status': 'status',
        'epoch': 'epoch',
        'steps': 'steps',
        'loss': 'loss',
        'create_time': 'create_time',
        'publish_error_msg': 'publish_error_msg',
        'task_infos': 'task_infos'
    }

    def __init__(self, artifact_type=None, is_best=None, artifact_id=None, continue_train_nums=None, asset_id=None, asset_name=None, status=None, epoch=None, steps=None, loss=None, create_time=None, publish_error_msg=None, task_infos=None):
        r"""ArtifactInfo

        The model defined in huaweicloud sdk

        :param artifact_type: 产物类型，可选值：final(最终产物)、middle(中间产物)。
        :type artifact_type: str
        :param is_best: 是否最优。
        :type is_best: bool
        :param artifact_id: 产物id。最终产物为模型ID，中间产物为断点ID。
        :type artifact_id: str
        :param continue_train_nums: 续训任务数量。
        :type continue_train_nums: int
        :param asset_id: 产物发布成功后的资产id。
        :type asset_id: str
        :param asset_name: 产物发布成功后的资产名称。
        :type asset_name: str
        :param status: 发布状态。
        :type status: str
        :param epoch: 轮数。
        :type epoch: int
        :param steps: 步数。
        :type steps: int
        :param loss: loss值
        :type loss: float
        :param create_time: 创建时间。
        :type create_time: str
        :param publish_error_msg: 产物发布失败的错误信息。
        :type publish_error_msg: str
        :param task_infos: 相关任务信息
        :type task_infos: list[:class:`huaweicloudsdkmodelarts.v1.ContinueTrainTask`]
        """
        
        

        self._artifact_type = None
        self._is_best = None
        self._artifact_id = None
        self._continue_train_nums = None
        self._asset_id = None
        self._asset_name = None
        self._status = None
        self._epoch = None
        self._steps = None
        self._loss = None
        self._create_time = None
        self._publish_error_msg = None
        self._task_infos = None
        self.discriminator = None

        if artifact_type is not None:
            self.artifact_type = artifact_type
        if is_best is not None:
            self.is_best = is_best
        if artifact_id is not None:
            self.artifact_id = artifact_id
        if continue_train_nums is not None:
            self.continue_train_nums = continue_train_nums
        if asset_id is not None:
            self.asset_id = asset_id
        if asset_name is not None:
            self.asset_name = asset_name
        if status is not None:
            self.status = status
        if epoch is not None:
            self.epoch = epoch
        if steps is not None:
            self.steps = steps
        if loss is not None:
            self.loss = loss
        if create_time is not None:
            self.create_time = create_time
        if publish_error_msg is not None:
            self.publish_error_msg = publish_error_msg
        if task_infos is not None:
            self.task_infos = task_infos

    @property
    def artifact_type(self):
        r"""Gets the artifact_type of this ArtifactInfo.

        产物类型，可选值：final(最终产物)、middle(中间产物)。

        :return: The artifact_type of this ArtifactInfo.
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        r"""Sets the artifact_type of this ArtifactInfo.

        产物类型，可选值：final(最终产物)、middle(中间产物)。

        :param artifact_type: The artifact_type of this ArtifactInfo.
        :type artifact_type: str
        """
        self._artifact_type = artifact_type

    @property
    def is_best(self):
        r"""Gets the is_best of this ArtifactInfo.

        是否最优。

        :return: The is_best of this ArtifactInfo.
        :rtype: bool
        """
        return self._is_best

    @is_best.setter
    def is_best(self, is_best):
        r"""Sets the is_best of this ArtifactInfo.

        是否最优。

        :param is_best: The is_best of this ArtifactInfo.
        :type is_best: bool
        """
        self._is_best = is_best

    @property
    def artifact_id(self):
        r"""Gets the artifact_id of this ArtifactInfo.

        产物id。最终产物为模型ID，中间产物为断点ID。

        :return: The artifact_id of this ArtifactInfo.
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        r"""Sets the artifact_id of this ArtifactInfo.

        产物id。最终产物为模型ID，中间产物为断点ID。

        :param artifact_id: The artifact_id of this ArtifactInfo.
        :type artifact_id: str
        """
        self._artifact_id = artifact_id

    @property
    def continue_train_nums(self):
        r"""Gets the continue_train_nums of this ArtifactInfo.

        续训任务数量。

        :return: The continue_train_nums of this ArtifactInfo.
        :rtype: int
        """
        return self._continue_train_nums

    @continue_train_nums.setter
    def continue_train_nums(self, continue_train_nums):
        r"""Sets the continue_train_nums of this ArtifactInfo.

        续训任务数量。

        :param continue_train_nums: The continue_train_nums of this ArtifactInfo.
        :type continue_train_nums: int
        """
        self._continue_train_nums = continue_train_nums

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ArtifactInfo.

        产物发布成功后的资产id。

        :return: The asset_id of this ArtifactInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ArtifactInfo.

        产物发布成功后的资产id。

        :param asset_id: The asset_id of this ArtifactInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_name(self):
        r"""Gets the asset_name of this ArtifactInfo.

        产物发布成功后的资产名称。

        :return: The asset_name of this ArtifactInfo.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this ArtifactInfo.

        产物发布成功后的资产名称。

        :param asset_name: The asset_name of this ArtifactInfo.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def status(self):
        r"""Gets the status of this ArtifactInfo.

        发布状态。

        :return: The status of this ArtifactInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ArtifactInfo.

        发布状态。

        :param status: The status of this ArtifactInfo.
        :type status: str
        """
        self._status = status

    @property
    def epoch(self):
        r"""Gets the epoch of this ArtifactInfo.

        轮数。

        :return: The epoch of this ArtifactInfo.
        :rtype: int
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        r"""Sets the epoch of this ArtifactInfo.

        轮数。

        :param epoch: The epoch of this ArtifactInfo.
        :type epoch: int
        """
        self._epoch = epoch

    @property
    def steps(self):
        r"""Gets the steps of this ArtifactInfo.

        步数。

        :return: The steps of this ArtifactInfo.
        :rtype: int
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this ArtifactInfo.

        步数。

        :param steps: The steps of this ArtifactInfo.
        :type steps: int
        """
        self._steps = steps

    @property
    def loss(self):
        r"""Gets the loss of this ArtifactInfo.

        loss值

        :return: The loss of this ArtifactInfo.
        :rtype: float
        """
        return self._loss

    @loss.setter
    def loss(self, loss):
        r"""Sets the loss of this ArtifactInfo.

        loss值

        :param loss: The loss of this ArtifactInfo.
        :type loss: float
        """
        self._loss = loss

    @property
    def create_time(self):
        r"""Gets the create_time of this ArtifactInfo.

        创建时间。

        :return: The create_time of this ArtifactInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ArtifactInfo.

        创建时间。

        :param create_time: The create_time of this ArtifactInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def publish_error_msg(self):
        r"""Gets the publish_error_msg of this ArtifactInfo.

        产物发布失败的错误信息。

        :return: The publish_error_msg of this ArtifactInfo.
        :rtype: str
        """
        return self._publish_error_msg

    @publish_error_msg.setter
    def publish_error_msg(self, publish_error_msg):
        r"""Sets the publish_error_msg of this ArtifactInfo.

        产物发布失败的错误信息。

        :param publish_error_msg: The publish_error_msg of this ArtifactInfo.
        :type publish_error_msg: str
        """
        self._publish_error_msg = publish_error_msg

    @property
    def task_infos(self):
        r"""Gets the task_infos of this ArtifactInfo.

        相关任务信息

        :return: The task_infos of this ArtifactInfo.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ContinueTrainTask`]
        """
        return self._task_infos

    @task_infos.setter
    def task_infos(self, task_infos):
        r"""Sets the task_infos of this ArtifactInfo.

        相关任务信息

        :param task_infos: The task_infos of this ArtifactInfo.
        :type task_infos: list[:class:`huaweicloudsdkmodelarts.v1.ContinueTrainTask`]
        """
        self._task_infos = task_infos

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
        if not isinstance(other, ArtifactInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
