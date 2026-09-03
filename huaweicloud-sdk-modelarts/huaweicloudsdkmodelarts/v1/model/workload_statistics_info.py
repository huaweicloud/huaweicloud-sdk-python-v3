# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadStatisticsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'infer': 'int',
        'notebook': 'int',
        'train': 'int',
        'warm_up_task': 'int',
        'x_infer': 'int',
        'sum': 'int'
    }

    attribute_map = {
        'infer': 'infer',
        'notebook': 'notebook',
        'train': 'train',
        'warm_up_task': 'warmUpTask',
        'x_infer': 'x-infer',
        'sum': 'sum'
    }

    def __init__(self, infer=None, notebook=None, train=None, warm_up_task=None, x_infer=None, sum=None):
        r"""WorkloadStatisticsInfo

        The model defined in huaweicloud sdk

        :param infer: 旧版模型部署作业数量。
        :type infer: int
        :param notebook: 开发环境作业数量。
        :type notebook: int
        :param train: 训练作业数量。
        :type train: int
        :param warm_up_task: 权重预热作业数量。
        :type warm_up_task: int
        :param x_infer: 模型部署作业数量。
        :type x_infer: int
        :param sum: 所有作业总和。
        :type sum: int
        """
        
        

        self._infer = None
        self._notebook = None
        self._train = None
        self._warm_up_task = None
        self._x_infer = None
        self._sum = None
        self.discriminator = None

        if infer is not None:
            self.infer = infer
        if notebook is not None:
            self.notebook = notebook
        if train is not None:
            self.train = train
        if warm_up_task is not None:
            self.warm_up_task = warm_up_task
        if x_infer is not None:
            self.x_infer = x_infer
        if sum is not None:
            self.sum = sum

    @property
    def infer(self):
        r"""Gets the infer of this WorkloadStatisticsInfo.

        旧版模型部署作业数量。

        :return: The infer of this WorkloadStatisticsInfo.
        :rtype: int
        """
        return self._infer

    @infer.setter
    def infer(self, infer):
        r"""Sets the infer of this WorkloadStatisticsInfo.

        旧版模型部署作业数量。

        :param infer: The infer of this WorkloadStatisticsInfo.
        :type infer: int
        """
        self._infer = infer

    @property
    def notebook(self):
        r"""Gets the notebook of this WorkloadStatisticsInfo.

        开发环境作业数量。

        :return: The notebook of this WorkloadStatisticsInfo.
        :rtype: int
        """
        return self._notebook

    @notebook.setter
    def notebook(self, notebook):
        r"""Sets the notebook of this WorkloadStatisticsInfo.

        开发环境作业数量。

        :param notebook: The notebook of this WorkloadStatisticsInfo.
        :type notebook: int
        """
        self._notebook = notebook

    @property
    def train(self):
        r"""Gets the train of this WorkloadStatisticsInfo.

        训练作业数量。

        :return: The train of this WorkloadStatisticsInfo.
        :rtype: int
        """
        return self._train

    @train.setter
    def train(self, train):
        r"""Sets the train of this WorkloadStatisticsInfo.

        训练作业数量。

        :param train: The train of this WorkloadStatisticsInfo.
        :type train: int
        """
        self._train = train

    @property
    def warm_up_task(self):
        r"""Gets the warm_up_task of this WorkloadStatisticsInfo.

        权重预热作业数量。

        :return: The warm_up_task of this WorkloadStatisticsInfo.
        :rtype: int
        """
        return self._warm_up_task

    @warm_up_task.setter
    def warm_up_task(self, warm_up_task):
        r"""Sets the warm_up_task of this WorkloadStatisticsInfo.

        权重预热作业数量。

        :param warm_up_task: The warm_up_task of this WorkloadStatisticsInfo.
        :type warm_up_task: int
        """
        self._warm_up_task = warm_up_task

    @property
    def x_infer(self):
        r"""Gets the x_infer of this WorkloadStatisticsInfo.

        模型部署作业数量。

        :return: The x_infer of this WorkloadStatisticsInfo.
        :rtype: int
        """
        return self._x_infer

    @x_infer.setter
    def x_infer(self, x_infer):
        r"""Sets the x_infer of this WorkloadStatisticsInfo.

        模型部署作业数量。

        :param x_infer: The x_infer of this WorkloadStatisticsInfo.
        :type x_infer: int
        """
        self._x_infer = x_infer

    @property
    def sum(self):
        r"""Gets the sum of this WorkloadStatisticsInfo.

        所有作业总和。

        :return: The sum of this WorkloadStatisticsInfo.
        :rtype: int
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        r"""Sets the sum of this WorkloadStatisticsInfo.

        所有作业总和。

        :param sum: The sum of this WorkloadStatisticsInfo.
        :type sum: int
        """
        self._sum = sum

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
        if not isinstance(other, WorkloadStatisticsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
