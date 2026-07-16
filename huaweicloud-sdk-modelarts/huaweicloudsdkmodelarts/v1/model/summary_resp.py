# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SummaryResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_type': 'str',
        'log_dir': 'LogDirResp',
        'data_sources': 'list[DataSourceResp]'
    }

    attribute_map = {
        'log_type': 'log_type',
        'log_dir': 'log_dir',
        'data_sources': 'data_sources'
    }

    def __init__(self, log_type=None, log_dir=None, data_sources=None):
        r"""SummaryResp

        The model defined in huaweicloud sdk

        :param log_type: **参数解释**：训练作业可视化日志类型，配置后训练作业可作为可视化作业数据源。 **取值范围**： - tensorboard：输出TensorBoard可视化工具类型的日志 - mindstudio-insight：输出mindstudio-insight可视化工具类型的日志
        :type log_type: str
        :param log_dir: 
        :type log_dir: :class:`huaweicloudsdkmodelarts.v1.LogDirResp`
        :param data_sources: **参数解释**：可视化作业或训练作业调试模式的可视化日志输入。
        :type data_sources: list[:class:`huaweicloudsdkmodelarts.v1.DataSourceResp`]
        """
        
        

        self._log_type = None
        self._log_dir = None
        self._data_sources = None
        self.discriminator = None

        if log_type is not None:
            self.log_type = log_type
        if log_dir is not None:
            self.log_dir = log_dir
        if data_sources is not None:
            self.data_sources = data_sources

    @property
    def log_type(self):
        r"""Gets the log_type of this SummaryResp.

        **参数解释**：训练作业可视化日志类型，配置后训练作业可作为可视化作业数据源。 **取值范围**： - tensorboard：输出TensorBoard可视化工具类型的日志 - mindstudio-insight：输出mindstudio-insight可视化工具类型的日志

        :return: The log_type of this SummaryResp.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this SummaryResp.

        **参数解释**：训练作业可视化日志类型，配置后训练作业可作为可视化作业数据源。 **取值范围**： - tensorboard：输出TensorBoard可视化工具类型的日志 - mindstudio-insight：输出mindstudio-insight可视化工具类型的日志

        :param log_type: The log_type of this SummaryResp.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def log_dir(self):
        r"""Gets the log_dir of this SummaryResp.

        :return: The log_dir of this SummaryResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.LogDirResp`
        """
        return self._log_dir

    @log_dir.setter
    def log_dir(self, log_dir):
        r"""Sets the log_dir of this SummaryResp.

        :param log_dir: The log_dir of this SummaryResp.
        :type log_dir: :class:`huaweicloudsdkmodelarts.v1.LogDirResp`
        """
        self._log_dir = log_dir

    @property
    def data_sources(self):
        r"""Gets the data_sources of this SummaryResp.

        **参数解释**：可视化作业或训练作业调试模式的可视化日志输入。

        :return: The data_sources of this SummaryResp.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DataSourceResp`]
        """
        return self._data_sources

    @data_sources.setter
    def data_sources(self, data_sources):
        r"""Sets the data_sources of this SummaryResp.

        **参数解释**：可视化作业或训练作业调试模式的可视化日志输入。

        :param data_sources: The data_sources of this SummaryResp.
        :type data_sources: list[:class:`huaweicloudsdkmodelarts.v1.DataSourceResp`]
        """
        self._data_sources = data_sources

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
        if not isinstance(other, SummaryResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
