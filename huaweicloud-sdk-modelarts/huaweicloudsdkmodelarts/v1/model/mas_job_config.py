# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MasJobConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ft_job_uuid': 'str',
        'ft_train_type': 'str',
        'model_type': 'str',
        'train_output_path': 'str',
        'train_process': 'float',
        'checkpoint_id': 'str',
        'task_env': 'TaskEnv',
        'checkpoint_config': 'CheckpointConf'
    }

    attribute_map = {
        'ft_job_uuid': 'ft_job_uuid',
        'ft_train_type': 'ft_train_type',
        'model_type': 'model_type',
        'train_output_path': 'train_output_path',
        'train_process': 'train_process',
        'checkpoint_id': 'checkpoint_id',
        'task_env': 'task_env',
        'checkpoint_config': 'checkpoint_config'
    }

    def __init__(self, ft_job_uuid=None, ft_train_type=None, model_type=None, train_output_path=None, train_process=None, checkpoint_id=None, task_env=None, checkpoint_config=None):
        r"""MasJobConfig

        The model defined in huaweicloud sdk

        :param ft_job_uuid: 模型ID
        :type ft_job_uuid: str
        :param ft_train_type: 模型训练类型
        :type ft_train_type: str
        :param model_type: 模型类型
        :type model_type: str
        :param train_output_path: 训练作业输出路径
        :type train_output_path: str
        :param train_process: 训练作业进度
        :type train_process: float
        :param checkpoint_id: 断点ID
        :type checkpoint_id: str
        :param task_env: 
        :type task_env: :class:`huaweicloudsdkmodelarts.v1.TaskEnv`
        :param checkpoint_config: 
        :type checkpoint_config: :class:`huaweicloudsdkmodelarts.v1.CheckpointConf`
        """
        
        

        self._ft_job_uuid = None
        self._ft_train_type = None
        self._model_type = None
        self._train_output_path = None
        self._train_process = None
        self._checkpoint_id = None
        self._task_env = None
        self._checkpoint_config = None
        self.discriminator = None

        if ft_job_uuid is not None:
            self.ft_job_uuid = ft_job_uuid
        if ft_train_type is not None:
            self.ft_train_type = ft_train_type
        if model_type is not None:
            self.model_type = model_type
        if train_output_path is not None:
            self.train_output_path = train_output_path
        if train_process is not None:
            self.train_process = train_process
        if checkpoint_id is not None:
            self.checkpoint_id = checkpoint_id
        if task_env is not None:
            self.task_env = task_env
        if checkpoint_config is not None:
            self.checkpoint_config = checkpoint_config

    @property
    def ft_job_uuid(self):
        r"""Gets the ft_job_uuid of this MasJobConfig.

        模型ID

        :return: The ft_job_uuid of this MasJobConfig.
        :rtype: str
        """
        return self._ft_job_uuid

    @ft_job_uuid.setter
    def ft_job_uuid(self, ft_job_uuid):
        r"""Sets the ft_job_uuid of this MasJobConfig.

        模型ID

        :param ft_job_uuid: The ft_job_uuid of this MasJobConfig.
        :type ft_job_uuid: str
        """
        self._ft_job_uuid = ft_job_uuid

    @property
    def ft_train_type(self):
        r"""Gets the ft_train_type of this MasJobConfig.

        模型训练类型

        :return: The ft_train_type of this MasJobConfig.
        :rtype: str
        """
        return self._ft_train_type

    @ft_train_type.setter
    def ft_train_type(self, ft_train_type):
        r"""Sets the ft_train_type of this MasJobConfig.

        模型训练类型

        :param ft_train_type: The ft_train_type of this MasJobConfig.
        :type ft_train_type: str
        """
        self._ft_train_type = ft_train_type

    @property
    def model_type(self):
        r"""Gets the model_type of this MasJobConfig.

        模型类型

        :return: The model_type of this MasJobConfig.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        r"""Sets the model_type of this MasJobConfig.

        模型类型

        :param model_type: The model_type of this MasJobConfig.
        :type model_type: str
        """
        self._model_type = model_type

    @property
    def train_output_path(self):
        r"""Gets the train_output_path of this MasJobConfig.

        训练作业输出路径

        :return: The train_output_path of this MasJobConfig.
        :rtype: str
        """
        return self._train_output_path

    @train_output_path.setter
    def train_output_path(self, train_output_path):
        r"""Sets the train_output_path of this MasJobConfig.

        训练作业输出路径

        :param train_output_path: The train_output_path of this MasJobConfig.
        :type train_output_path: str
        """
        self._train_output_path = train_output_path

    @property
    def train_process(self):
        r"""Gets the train_process of this MasJobConfig.

        训练作业进度

        :return: The train_process of this MasJobConfig.
        :rtype: float
        """
        return self._train_process

    @train_process.setter
    def train_process(self, train_process):
        r"""Sets the train_process of this MasJobConfig.

        训练作业进度

        :param train_process: The train_process of this MasJobConfig.
        :type train_process: float
        """
        self._train_process = train_process

    @property
    def checkpoint_id(self):
        r"""Gets the checkpoint_id of this MasJobConfig.

        断点ID

        :return: The checkpoint_id of this MasJobConfig.
        :rtype: str
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        r"""Sets the checkpoint_id of this MasJobConfig.

        断点ID

        :param checkpoint_id: The checkpoint_id of this MasJobConfig.
        :type checkpoint_id: str
        """
        self._checkpoint_id = checkpoint_id

    @property
    def task_env(self):
        r"""Gets the task_env of this MasJobConfig.

        :return: The task_env of this MasJobConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TaskEnv`
        """
        return self._task_env

    @task_env.setter
    def task_env(self, task_env):
        r"""Sets the task_env of this MasJobConfig.

        :param task_env: The task_env of this MasJobConfig.
        :type task_env: :class:`huaweicloudsdkmodelarts.v1.TaskEnv`
        """
        self._task_env = task_env

    @property
    def checkpoint_config(self):
        r"""Gets the checkpoint_config of this MasJobConfig.

        :return: The checkpoint_config of this MasJobConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CheckpointConf`
        """
        return self._checkpoint_config

    @checkpoint_config.setter
    def checkpoint_config(self, checkpoint_config):
        r"""Sets the checkpoint_config of this MasJobConfig.

        :param checkpoint_config: The checkpoint_config of this MasJobConfig.
        :type checkpoint_config: :class:`huaweicloudsdkmodelarts.v1.CheckpointConf`
        """
        self._checkpoint_config = checkpoint_config

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
        if not isinstance(other, MasJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
