# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContinueTask:

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
        'source_model_id': 'str',
        'source_model_name': 'str',
        'epoch': 'int',
        'steps': 'int',
        'is_best': 'bool',
        'skipped_steps': 'int'
    }

    attribute_map = {
        'checkpoint_id': 'checkpoint_id',
        'source_model_id': 'source_model_id',
        'source_model_name': 'source_model_name',
        'epoch': 'epoch',
        'steps': 'steps',
        'is_best': 'is_best',
        'skipped_steps': 'skipped_steps'
    }

    def __init__(self, checkpoint_id=None, source_model_id=None, source_model_name=None, epoch=None, steps=None, is_best=None, skipped_steps=None):
        r"""ContinueTask

        The model defined in huaweicloud sdk

        :param checkpoint_id: 断点ID
        :type checkpoint_id: str
        :param source_model_id: 续训任务模型ID
        :type source_model_id: str
        :param source_model_name: 续训任务模型名称
        :type source_model_name: str
        :param epoch: 轮数。
        :type epoch: int
        :param steps: 步数。
        :type steps: int
        :param is_best: 是否最优
        :type is_best: bool
        :param skipped_steps: 跳过步数，0表示不跳过。
        :type skipped_steps: int
        """
        
        

        self._checkpoint_id = None
        self._source_model_id = None
        self._source_model_name = None
        self._epoch = None
        self._steps = None
        self._is_best = None
        self._skipped_steps = None
        self.discriminator = None

        if checkpoint_id is not None:
            self.checkpoint_id = checkpoint_id
        if source_model_id is not None:
            self.source_model_id = source_model_id
        if source_model_name is not None:
            self.source_model_name = source_model_name
        if epoch is not None:
            self.epoch = epoch
        if steps is not None:
            self.steps = steps
        if is_best is not None:
            self.is_best = is_best
        if skipped_steps is not None:
            self.skipped_steps = skipped_steps

    @property
    def checkpoint_id(self):
        r"""Gets the checkpoint_id of this ContinueTask.

        断点ID

        :return: The checkpoint_id of this ContinueTask.
        :rtype: str
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        r"""Sets the checkpoint_id of this ContinueTask.

        断点ID

        :param checkpoint_id: The checkpoint_id of this ContinueTask.
        :type checkpoint_id: str
        """
        self._checkpoint_id = checkpoint_id

    @property
    def source_model_id(self):
        r"""Gets the source_model_id of this ContinueTask.

        续训任务模型ID

        :return: The source_model_id of this ContinueTask.
        :rtype: str
        """
        return self._source_model_id

    @source_model_id.setter
    def source_model_id(self, source_model_id):
        r"""Sets the source_model_id of this ContinueTask.

        续训任务模型ID

        :param source_model_id: The source_model_id of this ContinueTask.
        :type source_model_id: str
        """
        self._source_model_id = source_model_id

    @property
    def source_model_name(self):
        r"""Gets the source_model_name of this ContinueTask.

        续训任务模型名称

        :return: The source_model_name of this ContinueTask.
        :rtype: str
        """
        return self._source_model_name

    @source_model_name.setter
    def source_model_name(self, source_model_name):
        r"""Sets the source_model_name of this ContinueTask.

        续训任务模型名称

        :param source_model_name: The source_model_name of this ContinueTask.
        :type source_model_name: str
        """
        self._source_model_name = source_model_name

    @property
    def epoch(self):
        r"""Gets the epoch of this ContinueTask.

        轮数。

        :return: The epoch of this ContinueTask.
        :rtype: int
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        r"""Sets the epoch of this ContinueTask.

        轮数。

        :param epoch: The epoch of this ContinueTask.
        :type epoch: int
        """
        self._epoch = epoch

    @property
    def steps(self):
        r"""Gets the steps of this ContinueTask.

        步数。

        :return: The steps of this ContinueTask.
        :rtype: int
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this ContinueTask.

        步数。

        :param steps: The steps of this ContinueTask.
        :type steps: int
        """
        self._steps = steps

    @property
    def is_best(self):
        r"""Gets the is_best of this ContinueTask.

        是否最优

        :return: The is_best of this ContinueTask.
        :rtype: bool
        """
        return self._is_best

    @is_best.setter
    def is_best(self, is_best):
        r"""Sets the is_best of this ContinueTask.

        是否最优

        :param is_best: The is_best of this ContinueTask.
        :type is_best: bool
        """
        self._is_best = is_best

    @property
    def skipped_steps(self):
        r"""Gets the skipped_steps of this ContinueTask.

        跳过步数，0表示不跳过。

        :return: The skipped_steps of this ContinueTask.
        :rtype: int
        """
        return self._skipped_steps

    @skipped_steps.setter
    def skipped_steps(self, skipped_steps):
        r"""Sets the skipped_steps of this ContinueTask.

        跳过步数，0表示不跳过。

        :param skipped_steps: The skipped_steps of this ContinueTask.
        :type skipped_steps: int
        """
        self._skipped_steps = skipped_steps

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
        if not isinstance(other, ContinueTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
