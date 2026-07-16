# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckpointConf:

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
        'save_checkpoints_max': 'int',
        'skipped_steps': 'int',
        'restore_training': 'int'
    }

    attribute_map = {
        'checkpoint_id': 'checkpoint_id',
        'save_checkpoints_max': 'save_checkpoints_max',
        'skipped_steps': 'skipped_steps',
        'restore_training': 'restore_training'
    }

    def __init__(self, checkpoint_id=None, save_checkpoints_max=None, skipped_steps=None, restore_training=None):
        r"""CheckpointConf

        The model defined in huaweicloud sdk

        :param checkpoint_id: 断点ID
        :type checkpoint_id: str
        :param save_checkpoints_max: 保存续训任务的步数。 0：关闭不保，-1：自动无限制。
        :type save_checkpoints_max: int
        :param skipped_steps: 跳过步数，0表示不跳过。
        :type skipped_steps: int
        :param restore_training: 是否续训任务。  0：非续训,，1:续训。
        :type restore_training: int
        """
        
        

        self._checkpoint_id = None
        self._save_checkpoints_max = None
        self._skipped_steps = None
        self._restore_training = None
        self.discriminator = None

        if checkpoint_id is not None:
            self.checkpoint_id = checkpoint_id
        if save_checkpoints_max is not None:
            self.save_checkpoints_max = save_checkpoints_max
        if skipped_steps is not None:
            self.skipped_steps = skipped_steps
        if restore_training is not None:
            self.restore_training = restore_training

    @property
    def checkpoint_id(self):
        r"""Gets the checkpoint_id of this CheckpointConf.

        断点ID

        :return: The checkpoint_id of this CheckpointConf.
        :rtype: str
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        r"""Sets the checkpoint_id of this CheckpointConf.

        断点ID

        :param checkpoint_id: The checkpoint_id of this CheckpointConf.
        :type checkpoint_id: str
        """
        self._checkpoint_id = checkpoint_id

    @property
    def save_checkpoints_max(self):
        r"""Gets the save_checkpoints_max of this CheckpointConf.

        保存续训任务的步数。 0：关闭不保，-1：自动无限制。

        :return: The save_checkpoints_max of this CheckpointConf.
        :rtype: int
        """
        return self._save_checkpoints_max

    @save_checkpoints_max.setter
    def save_checkpoints_max(self, save_checkpoints_max):
        r"""Sets the save_checkpoints_max of this CheckpointConf.

        保存续训任务的步数。 0：关闭不保，-1：自动无限制。

        :param save_checkpoints_max: The save_checkpoints_max of this CheckpointConf.
        :type save_checkpoints_max: int
        """
        self._save_checkpoints_max = save_checkpoints_max

    @property
    def skipped_steps(self):
        r"""Gets the skipped_steps of this CheckpointConf.

        跳过步数，0表示不跳过。

        :return: The skipped_steps of this CheckpointConf.
        :rtype: int
        """
        return self._skipped_steps

    @skipped_steps.setter
    def skipped_steps(self, skipped_steps):
        r"""Sets the skipped_steps of this CheckpointConf.

        跳过步数，0表示不跳过。

        :param skipped_steps: The skipped_steps of this CheckpointConf.
        :type skipped_steps: int
        """
        self._skipped_steps = skipped_steps

    @property
    def restore_training(self):
        r"""Gets the restore_training of this CheckpointConf.

        是否续训任务。  0：非续训,，1:续训。

        :return: The restore_training of this CheckpointConf.
        :rtype: int
        """
        return self._restore_training

    @restore_training.setter
    def restore_training(self, restore_training):
        r"""Sets the restore_training of this CheckpointConf.

        是否续训任务。  0：非续训,，1:续训。

        :param restore_training: The restore_training of this CheckpointConf.
        :type restore_training: int
        """
        self._restore_training = restore_training

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
        if not isinstance(other, CheckpointConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
