# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalysisResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'analysis_id': 'str',
        'name': 'str',
        'display_name': 'str',
        'type': 'str',
        'transform': 'TransformResponse',
        'aggregate': 'AggregateResponse',
        'stream': 'StreamResponse'
    }

    attribute_map = {
        'analysis_id': 'analysis_id',
        'name': 'name',
        'display_name': 'display_name',
        'type': 'type',
        'transform': 'transform',
        'aggregate': 'aggregate',
        'stream': 'stream'
    }

    def __init__(self, analysis_id=None, name=None, display_name=None, type=None, transform=None, aggregate=None, stream=None):
        """AnalysisResponse

        The model defined in huaweicloud sdk

        :param analysis_id: 分析任务ID
        :type analysis_id: str
        :param name: 分析任务名称
        :type name: str
        :param display_name: 分析任务显示名称
        :type display_name: str
        :param type: 分析任务类型，转换计算（transform）、聚合计算（aggregate）、流计算（stream）
        :type type: str
        :param transform: 
        :type transform: :class:`huaweicloudsdkiotanalytics.v1.TransformResponse`
        :param aggregate: 
        :type aggregate: :class:`huaweicloudsdkiotanalytics.v1.AggregateResponse`
        :param stream: 
        :type stream: :class:`huaweicloudsdkiotanalytics.v1.StreamResponse`
        """
        
        

        self._analysis_id = None
        self._name = None
        self._display_name = None
        self._type = None
        self._transform = None
        self._aggregate = None
        self._stream = None
        self.discriminator = None

        if analysis_id is not None:
            self.analysis_id = analysis_id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if type is not None:
            self.type = type
        if transform is not None:
            self.transform = transform
        if aggregate is not None:
            self.aggregate = aggregate
        if stream is not None:
            self.stream = stream

    @property
    def analysis_id(self):
        """Gets the analysis_id of this AnalysisResponse.

        分析任务ID

        :return: The analysis_id of this AnalysisResponse.
        :rtype: str
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        """Sets the analysis_id of this AnalysisResponse.

        分析任务ID

        :param analysis_id: The analysis_id of this AnalysisResponse.
        :type analysis_id: str
        """
        self._analysis_id = analysis_id

    @property
    def name(self):
        """Gets the name of this AnalysisResponse.

        分析任务名称

        :return: The name of this AnalysisResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalysisResponse.

        分析任务名称

        :param name: The name of this AnalysisResponse.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this AnalysisResponse.

        分析任务显示名称

        :return: The display_name of this AnalysisResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AnalysisResponse.

        分析任务显示名称

        :param display_name: The display_name of this AnalysisResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """Gets the type of this AnalysisResponse.

        分析任务类型，转换计算（transform）、聚合计算（aggregate）、流计算（stream）

        :return: The type of this AnalysisResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AnalysisResponse.

        分析任务类型，转换计算（transform）、聚合计算（aggregate）、流计算（stream）

        :param type: The type of this AnalysisResponse.
        :type type: str
        """
        self._type = type

    @property
    def transform(self):
        """Gets the transform of this AnalysisResponse.


        :return: The transform of this AnalysisResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.TransformResponse`
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this AnalysisResponse.


        :param transform: The transform of this AnalysisResponse.
        :type transform: :class:`huaweicloudsdkiotanalytics.v1.TransformResponse`
        """
        self._transform = transform

    @property
    def aggregate(self):
        """Gets the aggregate of this AnalysisResponse.


        :return: The aggregate of this AnalysisResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.AggregateResponse`
        """
        return self._aggregate

    @aggregate.setter
    def aggregate(self, aggregate):
        """Sets the aggregate of this AnalysisResponse.


        :param aggregate: The aggregate of this AnalysisResponse.
        :type aggregate: :class:`huaweicloudsdkiotanalytics.v1.AggregateResponse`
        """
        self._aggregate = aggregate

    @property
    def stream(self):
        """Gets the stream of this AnalysisResponse.


        :return: The stream of this AnalysisResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.StreamResponse`
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this AnalysisResponse.


        :param stream: The stream of this AnalysisResponse.
        :type stream: :class:`huaweicloudsdkiotanalytics.v1.StreamResponse`
        """
        self._stream = stream

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
        if not isinstance(other, AnalysisResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
