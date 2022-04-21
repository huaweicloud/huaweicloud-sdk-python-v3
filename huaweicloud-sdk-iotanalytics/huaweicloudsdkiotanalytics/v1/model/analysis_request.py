# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalysisRequest:

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
        'transform': 'DTTransformRequest',
        'aggregate': 'DTAggregateRequest',
        'stream': 'DTStreamRequest'
    }

    attribute_map = {
        'name': 'name',
        'transform': 'transform',
        'aggregate': 'aggregate',
        'stream': 'stream'
    }

    def __init__(self, name=None, transform=None, aggregate=None, stream=None):
        """AnalysisRequest

        The model defined in huaweicloud sdk

        :param name: 分析任务名，必须是模型中已存在的
        :type name: str
        :param transform: 
        :type transform: :class:`huaweicloudsdkiotanalytics.v1.DTTransformRequest`
        :param aggregate: 
        :type aggregate: :class:`huaweicloudsdkiotanalytics.v1.DTAggregateRequest`
        :param stream: 
        :type stream: :class:`huaweicloudsdkiotanalytics.v1.DTStreamRequest`
        """
        
        

        self._name = None
        self._transform = None
        self._aggregate = None
        self._stream = None
        self.discriminator = None

        self.name = name
        if transform is not None:
            self.transform = transform
        if aggregate is not None:
            self.aggregate = aggregate
        if stream is not None:
            self.stream = stream

    @property
    def name(self):
        """Gets the name of this AnalysisRequest.

        分析任务名，必须是模型中已存在的

        :return: The name of this AnalysisRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalysisRequest.

        分析任务名，必须是模型中已存在的

        :param name: The name of this AnalysisRequest.
        :type name: str
        """
        self._name = name

    @property
    def transform(self):
        """Gets the transform of this AnalysisRequest.


        :return: The transform of this AnalysisRequest.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DTTransformRequest`
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this AnalysisRequest.


        :param transform: The transform of this AnalysisRequest.
        :type transform: :class:`huaweicloudsdkiotanalytics.v1.DTTransformRequest`
        """
        self._transform = transform

    @property
    def aggregate(self):
        """Gets the aggregate of this AnalysisRequest.


        :return: The aggregate of this AnalysisRequest.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DTAggregateRequest`
        """
        return self._aggregate

    @aggregate.setter
    def aggregate(self, aggregate):
        """Sets the aggregate of this AnalysisRequest.


        :param aggregate: The aggregate of this AnalysisRequest.
        :type aggregate: :class:`huaweicloudsdkiotanalytics.v1.DTAggregateRequest`
        """
        self._aggregate = aggregate

    @property
    def stream(self):
        """Gets the stream of this AnalysisRequest.


        :return: The stream of this AnalysisRequest.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DTStreamRequest`
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this AnalysisRequest.


        :param stream: The stream of this AnalysisRequest.
        :type stream: :class:`huaweicloudsdkiotanalytics.v1.DTStreamRequest`
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
        if not isinstance(other, AnalysisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
