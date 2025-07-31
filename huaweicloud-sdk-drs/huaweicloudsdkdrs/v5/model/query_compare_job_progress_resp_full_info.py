# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCompareJobProgressRespFullInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'progress': 'float',
        'src_speed': 'str',
        'recheck_entities': 'int'
    }

    attribute_map = {
        'progress': 'progress',
        'src_speed': 'src_speed',
        'recheck_entities': 'recheck_entities'
    }

    def __init__(self, progress=None, src_speed=None, recheck_entities=None):
        r"""QueryCompareJobProgressRespFullInfo

        The model defined in huaweicloud sdk

        :param progress: 全量数据对比进度，单位为%。
        :type progress: float
        :param src_speed: 全量数据对比速率。
        :type src_speed: str
        :param recheck_entities: 差异待复查行数。
        :type recheck_entities: int
        """
        
        

        self._progress = None
        self._src_speed = None
        self._recheck_entities = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if src_speed is not None:
            self.src_speed = src_speed
        if recheck_entities is not None:
            self.recheck_entities = recheck_entities

    @property
    def progress(self):
        r"""Gets the progress of this QueryCompareJobProgressRespFullInfo.

        全量数据对比进度，单位为%。

        :return: The progress of this QueryCompareJobProgressRespFullInfo.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this QueryCompareJobProgressRespFullInfo.

        全量数据对比进度，单位为%。

        :param progress: The progress of this QueryCompareJobProgressRespFullInfo.
        :type progress: float
        """
        self._progress = progress

    @property
    def src_speed(self):
        r"""Gets the src_speed of this QueryCompareJobProgressRespFullInfo.

        全量数据对比速率。

        :return: The src_speed of this QueryCompareJobProgressRespFullInfo.
        :rtype: str
        """
        return self._src_speed

    @src_speed.setter
    def src_speed(self, src_speed):
        r"""Sets the src_speed of this QueryCompareJobProgressRespFullInfo.

        全量数据对比速率。

        :param src_speed: The src_speed of this QueryCompareJobProgressRespFullInfo.
        :type src_speed: str
        """
        self._src_speed = src_speed

    @property
    def recheck_entities(self):
        r"""Gets the recheck_entities of this QueryCompareJobProgressRespFullInfo.

        差异待复查行数。

        :return: The recheck_entities of this QueryCompareJobProgressRespFullInfo.
        :rtype: int
        """
        return self._recheck_entities

    @recheck_entities.setter
    def recheck_entities(self, recheck_entities):
        r"""Sets the recheck_entities of this QueryCompareJobProgressRespFullInfo.

        差异待复查行数。

        :param recheck_entities: The recheck_entities of this QueryCompareJobProgressRespFullInfo.
        :type recheck_entities: int
        """
        self._recheck_entities = recheck_entities

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
        if not isinstance(other, QueryCompareJobProgressRespFullInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
