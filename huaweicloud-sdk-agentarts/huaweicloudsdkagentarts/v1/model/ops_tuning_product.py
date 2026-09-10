# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTuningProduct:

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
        'name': 'str',
        'epoch': 'int',
        'step': 'int',
        'reward_value': 'float',
        'eval_reward_value': 'float',
        'response_length': 'float',
        'url': 'str',
        'created_at': 'int',
        'status': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'epoch': 'epoch',
        'step': 'step',
        'reward_value': 'reward_value',
        'eval_reward_value': 'eval_reward_value',
        'response_length': 'response_length',
        'url': 'url',
        'created_at': 'created_at',
        'status': 'status',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, id=None, name=None, epoch=None, step=None, reward_value=None, eval_reward_value=None, response_length=None, url=None, created_at=None, status=None, fail_reason=None):
        r"""OpsTuningProduct

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 产物ID，标识模型产物的唯一ID。  **取值范围：** 唯一标识符字符串。
        :type id: str
        :param name: **参数解释：** 产物名称。  **取值范围：** 产物名称字符串。
        :type name: str
        :param epoch: **参数解释：** 训练轮数，生成该产物时模型已完成训练的轮数，单位：轮。  **取值范围：** 大于等于0的整数。
        :type epoch: int
        :param step: **参数解释：** 训练步数，生成该产物时模型已完成训练的步，单位：步。  **取值范围：** 大于等于0的整数。
        :type step: int
        :param reward_value: **参数解释：** 奖励值，该产物模型在评估时的得分。  **取值范围：** 0-1的浮点数。
        :type reward_value: float
        :param eval_reward_value: **参数解释：** 在该步数下计算得出验证集上的奖励值，反映模型生成结果的质量。  **取值范围：** 浮点数。
        :type eval_reward_value: float
        :param response_length: **参数解释：** 平均响应长度，模型生成内容的平均Token数，单位：Token。  **取值范围：** 大于等于0的整数。
        :type response_length: float
        :param url: **参数解释：** 产物地址（如OBS路径）。  **取值范围：** 不涉及
        :type url: str
        :param created_at: **参数解释：** 创建时间。  **取值范围：** 13位毫秒级时间戳。
        :type created_at: int
        :param status: **参数解释：** 产物文件上传状态。  **取值范围：** uploading上传中，uploaded已上传，failed上传失败。
        :type status: str
        :param fail_reason: **参数解释：** 产物转存错误信息。  **取值范围：** 无。
        :type fail_reason: str
        """
        
        

        self._id = None
        self._name = None
        self._epoch = None
        self._step = None
        self._reward_value = None
        self._eval_reward_value = None
        self._response_length = None
        self._url = None
        self._created_at = None
        self._status = None
        self._fail_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if epoch is not None:
            self.epoch = epoch
        if step is not None:
            self.step = step
        if reward_value is not None:
            self.reward_value = reward_value
        if eval_reward_value is not None:
            self.eval_reward_value = eval_reward_value
        if response_length is not None:
            self.response_length = response_length
        if url is not None:
            self.url = url
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def id(self):
        r"""Gets the id of this OpsTuningProduct.

        **参数解释：** 产物ID，标识模型产物的唯一ID。  **取值范围：** 唯一标识符字符串。

        :return: The id of this OpsTuningProduct.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsTuningProduct.

        **参数解释：** 产物ID，标识模型产物的唯一ID。  **取值范围：** 唯一标识符字符串。

        :param id: The id of this OpsTuningProduct.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this OpsTuningProduct.

        **参数解释：** 产物名称。  **取值范围：** 产物名称字符串。

        :return: The name of this OpsTuningProduct.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsTuningProduct.

        **参数解释：** 产物名称。  **取值范围：** 产物名称字符串。

        :param name: The name of this OpsTuningProduct.
        :type name: str
        """
        self._name = name

    @property
    def epoch(self):
        r"""Gets the epoch of this OpsTuningProduct.

        **参数解释：** 训练轮数，生成该产物时模型已完成训练的轮数，单位：轮。  **取值范围：** 大于等于0的整数。

        :return: The epoch of this OpsTuningProduct.
        :rtype: int
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        r"""Sets the epoch of this OpsTuningProduct.

        **参数解释：** 训练轮数，生成该产物时模型已完成训练的轮数，单位：轮。  **取值范围：** 大于等于0的整数。

        :param epoch: The epoch of this OpsTuningProduct.
        :type epoch: int
        """
        self._epoch = epoch

    @property
    def step(self):
        r"""Gets the step of this OpsTuningProduct.

        **参数解释：** 训练步数，生成该产物时模型已完成训练的步，单位：步。  **取值范围：** 大于等于0的整数。

        :return: The step of this OpsTuningProduct.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this OpsTuningProduct.

        **参数解释：** 训练步数，生成该产物时模型已完成训练的步，单位：步。  **取值范围：** 大于等于0的整数。

        :param step: The step of this OpsTuningProduct.
        :type step: int
        """
        self._step = step

    @property
    def reward_value(self):
        r"""Gets the reward_value of this OpsTuningProduct.

        **参数解释：** 奖励值，该产物模型在评估时的得分。  **取值范围：** 0-1的浮点数。

        :return: The reward_value of this OpsTuningProduct.
        :rtype: float
        """
        return self._reward_value

    @reward_value.setter
    def reward_value(self, reward_value):
        r"""Sets the reward_value of this OpsTuningProduct.

        **参数解释：** 奖励值，该产物模型在评估时的得分。  **取值范围：** 0-1的浮点数。

        :param reward_value: The reward_value of this OpsTuningProduct.
        :type reward_value: float
        """
        self._reward_value = reward_value

    @property
    def eval_reward_value(self):
        r"""Gets the eval_reward_value of this OpsTuningProduct.

        **参数解释：** 在该步数下计算得出验证集上的奖励值，反映模型生成结果的质量。  **取值范围：** 浮点数。

        :return: The eval_reward_value of this OpsTuningProduct.
        :rtype: float
        """
        return self._eval_reward_value

    @eval_reward_value.setter
    def eval_reward_value(self, eval_reward_value):
        r"""Sets the eval_reward_value of this OpsTuningProduct.

        **参数解释：** 在该步数下计算得出验证集上的奖励值，反映模型生成结果的质量。  **取值范围：** 浮点数。

        :param eval_reward_value: The eval_reward_value of this OpsTuningProduct.
        :type eval_reward_value: float
        """
        self._eval_reward_value = eval_reward_value

    @property
    def response_length(self):
        r"""Gets the response_length of this OpsTuningProduct.

        **参数解释：** 平均响应长度，模型生成内容的平均Token数，单位：Token。  **取值范围：** 大于等于0的整数。

        :return: The response_length of this OpsTuningProduct.
        :rtype: float
        """
        return self._response_length

    @response_length.setter
    def response_length(self, response_length):
        r"""Sets the response_length of this OpsTuningProduct.

        **参数解释：** 平均响应长度，模型生成内容的平均Token数，单位：Token。  **取值范围：** 大于等于0的整数。

        :param response_length: The response_length of this OpsTuningProduct.
        :type response_length: float
        """
        self._response_length = response_length

    @property
    def url(self):
        r"""Gets the url of this OpsTuningProduct.

        **参数解释：** 产物地址（如OBS路径）。  **取值范围：** 不涉及

        :return: The url of this OpsTuningProduct.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this OpsTuningProduct.

        **参数解释：** 产物地址（如OBS路径）。  **取值范围：** 不涉及

        :param url: The url of this OpsTuningProduct.
        :type url: str
        """
        self._url = url

    @property
    def created_at(self):
        r"""Gets the created_at of this OpsTuningProduct.

        **参数解释：** 创建时间。  **取值范围：** 13位毫秒级时间戳。

        :return: The created_at of this OpsTuningProduct.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OpsTuningProduct.

        **参数解释：** 创建时间。  **取值范围：** 13位毫秒级时间戳。

        :param created_at: The created_at of this OpsTuningProduct.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def status(self):
        r"""Gets the status of this OpsTuningProduct.

        **参数解释：** 产物文件上传状态。  **取值范围：** uploading上传中，uploaded已上传，failed上传失败。

        :return: The status of this OpsTuningProduct.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OpsTuningProduct.

        **参数解释：** 产物文件上传状态。  **取值范围：** uploading上传中，uploaded已上传，failed上传失败。

        :param status: The status of this OpsTuningProduct.
        :type status: str
        """
        self._status = status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this OpsTuningProduct.

        **参数解释：** 产物转存错误信息。  **取值范围：** 无。

        :return: The fail_reason of this OpsTuningProduct.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this OpsTuningProduct.

        **参数解释：** 产物转存错误信息。  **取值范围：** 无。

        :param fail_reason: The fail_reason of this OpsTuningProduct.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, OpsTuningProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
