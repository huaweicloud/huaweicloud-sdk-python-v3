# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFtMetricsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loss': 'object',
        'eval_loss': 'object',
        'training_info': 'object',
        'train_process': 'float',
        'data': 'FtMetricData'
    }

    attribute_map = {
        'loss': 'loss',
        'eval_loss': 'eval_loss',
        'training_info': 'training_info',
        'train_process': 'train_process',
        'data': 'data'
    }

    def __init__(self, loss=None, eval_loss=None, training_info=None, train_process=None, data=None):
        r"""ShowFtMetricsResponse

        The model defined in huaweicloud sdk

        :param loss: 训练loss信息
        :type loss: object
        :param eval_loss: 评测loss信息
        :type eval_loss: object
        :param training_info: 训练预估时长信息
        :type training_info: object
        :param train_process: 训练进度信息
        :type train_process: float
        :param data: 
        :type data: :class:`huaweicloudsdkmodelarts.v1.FtMetricData`
        """
        
        super().__init__()

        self._loss = None
        self._eval_loss = None
        self._training_info = None
        self._train_process = None
        self._data = None
        self.discriminator = None

        if loss is not None:
            self.loss = loss
        if eval_loss is not None:
            self.eval_loss = eval_loss
        if training_info is not None:
            self.training_info = training_info
        if train_process is not None:
            self.train_process = train_process
        if data is not None:
            self.data = data

    @property
    def loss(self):
        r"""Gets the loss of this ShowFtMetricsResponse.

        训练loss信息

        :return: The loss of this ShowFtMetricsResponse.
        :rtype: object
        """
        return self._loss

    @loss.setter
    def loss(self, loss):
        r"""Sets the loss of this ShowFtMetricsResponse.

        训练loss信息

        :param loss: The loss of this ShowFtMetricsResponse.
        :type loss: object
        """
        self._loss = loss

    @property
    def eval_loss(self):
        r"""Gets the eval_loss of this ShowFtMetricsResponse.

        评测loss信息

        :return: The eval_loss of this ShowFtMetricsResponse.
        :rtype: object
        """
        return self._eval_loss

    @eval_loss.setter
    def eval_loss(self, eval_loss):
        r"""Sets the eval_loss of this ShowFtMetricsResponse.

        评测loss信息

        :param eval_loss: The eval_loss of this ShowFtMetricsResponse.
        :type eval_loss: object
        """
        self._eval_loss = eval_loss

    @property
    def training_info(self):
        r"""Gets the training_info of this ShowFtMetricsResponse.

        训练预估时长信息

        :return: The training_info of this ShowFtMetricsResponse.
        :rtype: object
        """
        return self._training_info

    @training_info.setter
    def training_info(self, training_info):
        r"""Sets the training_info of this ShowFtMetricsResponse.

        训练预估时长信息

        :param training_info: The training_info of this ShowFtMetricsResponse.
        :type training_info: object
        """
        self._training_info = training_info

    @property
    def train_process(self):
        r"""Gets the train_process of this ShowFtMetricsResponse.

        训练进度信息

        :return: The train_process of this ShowFtMetricsResponse.
        :rtype: float
        """
        return self._train_process

    @train_process.setter
    def train_process(self, train_process):
        r"""Sets the train_process of this ShowFtMetricsResponse.

        训练进度信息

        :param train_process: The train_process of this ShowFtMetricsResponse.
        :type train_process: float
        """
        self._train_process = train_process

    @property
    def data(self):
        r"""Gets the data of this ShowFtMetricsResponse.

        :return: The data of this ShowFtMetricsResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.FtMetricData`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowFtMetricsResponse.

        :param data: The data of this ShowFtMetricsResponse.
        :type data: :class:`huaweicloudsdkmodelarts.v1.FtMetricData`
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("ShowFtMetricsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowFtMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
