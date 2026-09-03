# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContinueTrainTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'checkpoint_id': 'str',
        'continue_task_id': 'str',
        'continue_task_name': 'str',
        'continue_train_type': 'str',
        'skipped_steps': 'int',
        'restore_training': 'int',
        'create_time': 'str',
        'checkpoint_config': 'str'
    }

    attribute_map = {
        'checkpoint_id': 'checkpoint_id',
        'continue_task_id': 'continue_task_id',
        'continue_task_name': 'continue_task_name',
        'continue_train_type': 'continue_train_type',
        'skipped_steps': 'skipped_steps',
        'restore_training': 'restore_training',
        'create_time': 'create_time',
        'checkpoint_config': 'checkpoint_config'
    }

    def __init__(self, checkpoint_id=None, continue_task_id=None, continue_task_name=None, continue_train_type=None, skipped_steps=None, restore_training=None, create_time=None, checkpoint_config=None):
        r"""ContinueTrainTask

        The model defined in huaweicloud sdk

        :param checkpoint_id: 中间产物id。
        :type checkpoint_id: str
        :param continue_task_id: 续训任务id。
        :type continue_task_id: str
        :param continue_task_name: 续训任务名称。
        :type continue_task_name: str
        :param continue_train_type: 续训训练类型。
        :type continue_train_type: str
        :param skipped_steps: 跳过步数，0表示不跳过。
        :type skipped_steps: int
        :param restore_training: 是否续训任务。  0: 非续训, 1:续训。
        :type restore_training: int
        :param create_time: 创建时间。
        :type create_time: str
        :param checkpoint_config: 中间产物配置信息。
        :type checkpoint_config: str
        """
        
        

        self._checkpoint_id = None
        self._continue_task_id = None
        self._continue_task_name = None
        self._continue_train_type = None
        self._skipped_steps = None
        self._restore_training = None
        self._create_time = None
        self._checkpoint_config = None
        self.discriminator = None

        if checkpoint_id is not None:
            self.checkpoint_id = checkpoint_id
        if continue_task_id is not None:
            self.continue_task_id = continue_task_id
        if continue_task_name is not None:
            self.continue_task_name = continue_task_name
        if continue_train_type is not None:
            self.continue_train_type = continue_train_type
        if skipped_steps is not None:
            self.skipped_steps = skipped_steps
        if restore_training is not None:
            self.restore_training = restore_training
        if create_time is not None:
            self.create_time = create_time
        if checkpoint_config is not None:
            self.checkpoint_config = checkpoint_config

    @property
    def checkpoint_id(self):
        r"""Gets the checkpoint_id of this ContinueTrainTask.

        中间产物id。

        :return: The checkpoint_id of this ContinueTrainTask.
        :rtype: str
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        r"""Sets the checkpoint_id of this ContinueTrainTask.

        中间产物id。

        :param checkpoint_id: The checkpoint_id of this ContinueTrainTask.
        :type checkpoint_id: str
        """
        self._checkpoint_id = checkpoint_id

    @property
    def continue_task_id(self):
        r"""Gets the continue_task_id of this ContinueTrainTask.

        续训任务id。

        :return: The continue_task_id of this ContinueTrainTask.
        :rtype: str
        """
        return self._continue_task_id

    @continue_task_id.setter
    def continue_task_id(self, continue_task_id):
        r"""Sets the continue_task_id of this ContinueTrainTask.

        续训任务id。

        :param continue_task_id: The continue_task_id of this ContinueTrainTask.
        :type continue_task_id: str
        """
        self._continue_task_id = continue_task_id

    @property
    def continue_task_name(self):
        r"""Gets the continue_task_name of this ContinueTrainTask.

        续训任务名称。

        :return: The continue_task_name of this ContinueTrainTask.
        :rtype: str
        """
        return self._continue_task_name

    @continue_task_name.setter
    def continue_task_name(self, continue_task_name):
        r"""Sets the continue_task_name of this ContinueTrainTask.

        续训任务名称。

        :param continue_task_name: The continue_task_name of this ContinueTrainTask.
        :type continue_task_name: str
        """
        self._continue_task_name = continue_task_name

    @property
    def continue_train_type(self):
        r"""Gets the continue_train_type of this ContinueTrainTask.

        续训训练类型。

        :return: The continue_train_type of this ContinueTrainTask.
        :rtype: str
        """
        return self._continue_train_type

    @continue_train_type.setter
    def continue_train_type(self, continue_train_type):
        r"""Sets the continue_train_type of this ContinueTrainTask.

        续训训练类型。

        :param continue_train_type: The continue_train_type of this ContinueTrainTask.
        :type continue_train_type: str
        """
        self._continue_train_type = continue_train_type

    @property
    def skipped_steps(self):
        r"""Gets the skipped_steps of this ContinueTrainTask.

        跳过步数，0表示不跳过。

        :return: The skipped_steps of this ContinueTrainTask.
        :rtype: int
        """
        return self._skipped_steps

    @skipped_steps.setter
    def skipped_steps(self, skipped_steps):
        r"""Sets the skipped_steps of this ContinueTrainTask.

        跳过步数，0表示不跳过。

        :param skipped_steps: The skipped_steps of this ContinueTrainTask.
        :type skipped_steps: int
        """
        self._skipped_steps = skipped_steps

    @property
    def restore_training(self):
        r"""Gets the restore_training of this ContinueTrainTask.

        是否续训任务。  0: 非续训, 1:续训。

        :return: The restore_training of this ContinueTrainTask.
        :rtype: int
        """
        return self._restore_training

    @restore_training.setter
    def restore_training(self, restore_training):
        r"""Sets the restore_training of this ContinueTrainTask.

        是否续训任务。  0: 非续训, 1:续训。

        :param restore_training: The restore_training of this ContinueTrainTask.
        :type restore_training: int
        """
        self._restore_training = restore_training

    @property
    def create_time(self):
        r"""Gets the create_time of this ContinueTrainTask.

        创建时间。

        :return: The create_time of this ContinueTrainTask.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ContinueTrainTask.

        创建时间。

        :param create_time: The create_time of this ContinueTrainTask.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def checkpoint_config(self):
        r"""Gets the checkpoint_config of this ContinueTrainTask.

        中间产物配置信息。

        :return: The checkpoint_config of this ContinueTrainTask.
        :rtype: str
        """
        return self._checkpoint_config

    @checkpoint_config.setter
    def checkpoint_config(self, checkpoint_config):
        r"""Sets the checkpoint_config of this ContinueTrainTask.

        中间产物配置信息。

        :param checkpoint_config: The checkpoint_config of this ContinueTrainTask.
        :type checkpoint_config: str
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
        if not isinstance(other, ContinueTrainTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
