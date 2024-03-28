# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LineStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_point': 'Point',
        'end_point': 'Point',
        'critical': 'str'
    }

    attribute_map = {
        'start_point': 'startPoint',
        'end_point': 'endPoint',
        'critical': 'critical'
    }

    def __init__(self, start_point=None, end_point=None, critical=None):
        """LineStatus

        The model defined in huaweicloud sdk

        :param start_point: 
        :type start_point: :class:`huaweicloudsdkcce.v3.Point`
        :param end_point: 
        :type end_point: :class:`huaweicloudsdkcce.v3.Point`
        :param critical: 表示是否为关键线路（关键线路未执行无法取消升级流程）
        :type critical: str
        """
        
        

        self._start_point = None
        self._end_point = None
        self._critical = None
        self.discriminator = None

        if start_point is not None:
            self.start_point = start_point
        if end_point is not None:
            self.end_point = end_point
        if critical is not None:
            self.critical = critical

    @property
    def start_point(self):
        """Gets the start_point of this LineStatus.

        :return: The start_point of this LineStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.Point`
        """
        return self._start_point

    @start_point.setter
    def start_point(self, start_point):
        """Sets the start_point of this LineStatus.

        :param start_point: The start_point of this LineStatus.
        :type start_point: :class:`huaweicloudsdkcce.v3.Point`
        """
        self._start_point = start_point

    @property
    def end_point(self):
        """Gets the end_point of this LineStatus.

        :return: The end_point of this LineStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.Point`
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point):
        """Sets the end_point of this LineStatus.

        :param end_point: The end_point of this LineStatus.
        :type end_point: :class:`huaweicloudsdkcce.v3.Point`
        """
        self._end_point = end_point

    @property
    def critical(self):
        """Gets the critical of this LineStatus.

        表示是否为关键线路（关键线路未执行无法取消升级流程）

        :return: The critical of this LineStatus.
        :rtype: str
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this LineStatus.

        表示是否为关键线路（关键线路未执行无法取消升级流程）

        :param critical: The critical of this LineStatus.
        :type critical: str
        """
        self._critical = critical

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
        if not isinstance(other, LineStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
