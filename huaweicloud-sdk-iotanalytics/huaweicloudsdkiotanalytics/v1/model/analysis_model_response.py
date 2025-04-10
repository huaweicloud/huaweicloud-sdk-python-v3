# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalysisModelResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'display_name': 'str',
        'type': 'str',
        'transform': 'TransformModel',
        'aggregate': 'AggregateModel',
        'stream': 'StreamModel',
        'analysis_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'display_name',
        'type': 'type',
        'transform': 'transform',
        'aggregate': 'aggregate',
        'stream': 'stream',
        'analysis_id': 'analysis_id'
    }

    def __init__(self, name=None, display_name=None, type=None, transform=None, aggregate=None, stream=None, analysis_id=None):
        r"""AnalysisModelResponse

        The model defined in huaweicloud sdk

        :param name: 分析任务名称，正则：\&quot;^[a-zA-Z][a-zA-Z0-9_]{0,63}$\&quot;
        :type name: str
        :param display_name: 分析任务显示名称，正则：\&quot;^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{1,64}$\&quot;
        :type display_name: str
        :param type: 分析任务类型，转换计算（transform）、聚合计算（aggregate）、流计算（stream）
        :type type: str
        :param transform: 
        :type transform: :class:`huaweicloudsdkiotanalytics.v1.TransformModel`
        :param aggregate: 
        :type aggregate: :class:`huaweicloudsdkiotanalytics.v1.AggregateModel`
        :param stream: 
        :type stream: :class:`huaweicloudsdkiotanalytics.v1.StreamModel`
        :param analysis_id: 分析任务ID
        :type analysis_id: str
        """
        
        

        self._name = None
        self._display_name = None
        self._type = None
        self._transform = None
        self._aggregate = None
        self._stream = None
        self._analysis_id = None
        self.discriminator = None

        self.name = name
        if display_name is not None:
            self.display_name = display_name
        self.type = type
        if transform is not None:
            self.transform = transform
        if aggregate is not None:
            self.aggregate = aggregate
        if stream is not None:
            self.stream = stream
        if analysis_id is not None:
            self.analysis_id = analysis_id

    @property
    def name(self):
        r"""Gets the name of this AnalysisModelResponse.

        分析任务名称，正则：\"^[a-zA-Z][a-zA-Z0-9_]{0,63}$\"

        :return: The name of this AnalysisModelResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AnalysisModelResponse.

        分析任务名称，正则：\"^[a-zA-Z][a-zA-Z0-9_]{0,63}$\"

        :param name: The name of this AnalysisModelResponse.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this AnalysisModelResponse.

        分析任务显示名称，正则：\"^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{1,64}$\"

        :return: The display_name of this AnalysisModelResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this AnalysisModelResponse.

        分析任务显示名称，正则：\"^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{1,64}$\"

        :param display_name: The display_name of this AnalysisModelResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def type(self):
        r"""Gets the type of this AnalysisModelResponse.

        分析任务类型，转换计算（transform）、聚合计算（aggregate）、流计算（stream）

        :return: The type of this AnalysisModelResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AnalysisModelResponse.

        分析任务类型，转换计算（transform）、聚合计算（aggregate）、流计算（stream）

        :param type: The type of this AnalysisModelResponse.
        :type type: str
        """
        self._type = type

    @property
    def transform(self):
        r"""Gets the transform of this AnalysisModelResponse.

        :return: The transform of this AnalysisModelResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.TransformModel`
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        r"""Sets the transform of this AnalysisModelResponse.

        :param transform: The transform of this AnalysisModelResponse.
        :type transform: :class:`huaweicloudsdkiotanalytics.v1.TransformModel`
        """
        self._transform = transform

    @property
    def aggregate(self):
        r"""Gets the aggregate of this AnalysisModelResponse.

        :return: The aggregate of this AnalysisModelResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.AggregateModel`
        """
        return self._aggregate

    @aggregate.setter
    def aggregate(self, aggregate):
        r"""Sets the aggregate of this AnalysisModelResponse.

        :param aggregate: The aggregate of this AnalysisModelResponse.
        :type aggregate: :class:`huaweicloudsdkiotanalytics.v1.AggregateModel`
        """
        self._aggregate = aggregate

    @property
    def stream(self):
        r"""Gets the stream of this AnalysisModelResponse.

        :return: The stream of this AnalysisModelResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.StreamModel`
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this AnalysisModelResponse.

        :param stream: The stream of this AnalysisModelResponse.
        :type stream: :class:`huaweicloudsdkiotanalytics.v1.StreamModel`
        """
        self._stream = stream

    @property
    def analysis_id(self):
        r"""Gets the analysis_id of this AnalysisModelResponse.

        分析任务ID

        :return: The analysis_id of this AnalysisModelResponse.
        :rtype: str
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        r"""Sets the analysis_id of this AnalysisModelResponse.

        分析任务ID

        :param analysis_id: The analysis_id of this AnalysisModelResponse.
        :type analysis_id: str
        """
        self._analysis_id = analysis_id

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
        if not isinstance(other, AnalysisModelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
