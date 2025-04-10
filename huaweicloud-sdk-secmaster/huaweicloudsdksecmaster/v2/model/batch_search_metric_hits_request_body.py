# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSearchMetricHitsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_ids': 'list[str]',
        'workspace_ids': 'list[str]',
        'params': 'list[dict(str, str)]',
        'interactive_params': 'list[dict(str, str)]',
        'field_ids': 'list[str]'
    }

    attribute_map = {
        'metric_ids': 'metric_ids',
        'workspace_ids': 'workspace_ids',
        'params': 'params',
        'interactive_params': 'interactive_params',
        'field_ids': 'field_ids'
    }

    def __init__(self, metric_ids=None, workspace_ids=None, params=None, interactive_params=None, field_ids=None):
        r"""BatchSearchMetricHitsRequestBody

        The model defined in huaweicloud sdk

        :param metric_ids: 待查询的指标Id列表, 可参照附录中指标信息说明获取已有指标信息。
        :type metric_ids: list[str]
        :param workspace_ids: 工作空间列表, 当指标支持获取多工作空间数据时填写。
        :type workspace_ids: list[str]
        :param params: 待查询指标的参数列表，列表内每个元素为&lt;String, String&gt;的K-V形式，元素数量必须与metric_ids列表相同，具体填写方式请参照附录。
        :type params: list[dict(str, str)]
        :param interactive_params: 交互式参数查询，当指标支持交互式参数时，填写&lt;String, String&gt;的K-V形式的参数列表，具体填写方式请参照附录。
        :type interactive_params: list[dict(str, str)]
        :param field_ids: 指标卡片ID列表
        :type field_ids: list[str]
        """
        
        

        self._metric_ids = None
        self._workspace_ids = None
        self._params = None
        self._interactive_params = None
        self._field_ids = None
        self.discriminator = None

        self.metric_ids = metric_ids
        if workspace_ids is not None:
            self.workspace_ids = workspace_ids
        if params is not None:
            self.params = params
        if interactive_params is not None:
            self.interactive_params = interactive_params
        if field_ids is not None:
            self.field_ids = field_ids

    @property
    def metric_ids(self):
        r"""Gets the metric_ids of this BatchSearchMetricHitsRequestBody.

        待查询的指标Id列表, 可参照附录中指标信息说明获取已有指标信息。

        :return: The metric_ids of this BatchSearchMetricHitsRequestBody.
        :rtype: list[str]
        """
        return self._metric_ids

    @metric_ids.setter
    def metric_ids(self, metric_ids):
        r"""Sets the metric_ids of this BatchSearchMetricHitsRequestBody.

        待查询的指标Id列表, 可参照附录中指标信息说明获取已有指标信息。

        :param metric_ids: The metric_ids of this BatchSearchMetricHitsRequestBody.
        :type metric_ids: list[str]
        """
        self._metric_ids = metric_ids

    @property
    def workspace_ids(self):
        r"""Gets the workspace_ids of this BatchSearchMetricHitsRequestBody.

        工作空间列表, 当指标支持获取多工作空间数据时填写。

        :return: The workspace_ids of this BatchSearchMetricHitsRequestBody.
        :rtype: list[str]
        """
        return self._workspace_ids

    @workspace_ids.setter
    def workspace_ids(self, workspace_ids):
        r"""Sets the workspace_ids of this BatchSearchMetricHitsRequestBody.

        工作空间列表, 当指标支持获取多工作空间数据时填写。

        :param workspace_ids: The workspace_ids of this BatchSearchMetricHitsRequestBody.
        :type workspace_ids: list[str]
        """
        self._workspace_ids = workspace_ids

    @property
    def params(self):
        r"""Gets the params of this BatchSearchMetricHitsRequestBody.

        待查询指标的参数列表，列表内每个元素为<String, String>的K-V形式，元素数量必须与metric_ids列表相同，具体填写方式请参照附录。

        :return: The params of this BatchSearchMetricHitsRequestBody.
        :rtype: list[dict(str, str)]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this BatchSearchMetricHitsRequestBody.

        待查询指标的参数列表，列表内每个元素为<String, String>的K-V形式，元素数量必须与metric_ids列表相同，具体填写方式请参照附录。

        :param params: The params of this BatchSearchMetricHitsRequestBody.
        :type params: list[dict(str, str)]
        """
        self._params = params

    @property
    def interactive_params(self):
        r"""Gets the interactive_params of this BatchSearchMetricHitsRequestBody.

        交互式参数查询，当指标支持交互式参数时，填写<String, String>的K-V形式的参数列表，具体填写方式请参照附录。

        :return: The interactive_params of this BatchSearchMetricHitsRequestBody.
        :rtype: list[dict(str, str)]
        """
        return self._interactive_params

    @interactive_params.setter
    def interactive_params(self, interactive_params):
        r"""Sets the interactive_params of this BatchSearchMetricHitsRequestBody.

        交互式参数查询，当指标支持交互式参数时，填写<String, String>的K-V形式的参数列表，具体填写方式请参照附录。

        :param interactive_params: The interactive_params of this BatchSearchMetricHitsRequestBody.
        :type interactive_params: list[dict(str, str)]
        """
        self._interactive_params = interactive_params

    @property
    def field_ids(self):
        r"""Gets the field_ids of this BatchSearchMetricHitsRequestBody.

        指标卡片ID列表

        :return: The field_ids of this BatchSearchMetricHitsRequestBody.
        :rtype: list[str]
        """
        return self._field_ids

    @field_ids.setter
    def field_ids(self, field_ids):
        r"""Sets the field_ids of this BatchSearchMetricHitsRequestBody.

        指标卡片ID列表

        :param field_ids: The field_ids of this BatchSearchMetricHitsRequestBody.
        :type field_ids: list[str]
        """
        self._field_ids = field_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchSearchMetricHitsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
