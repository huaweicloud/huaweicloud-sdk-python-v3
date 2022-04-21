# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AreaDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'area': 'str',
        'summary': 'list[TimeValue]',
        'detail': 'list[AreaTimeValue]'
    }

    attribute_map = {
        'area': 'area',
        'summary': 'summary',
        'detail': 'detail'
    }

    def __init__(self, area=None, summary=None, detail=None):
        """AreaDetail

        The model defined in huaweicloud sdk

        :param area: 各个计费大区名称，例如CN
        :type area: str
        :param summary: 时间戳及相应时间的指标数值
        :type summary: list[:class:`huaweicloudsdklive.v2.TimeValue`]
        :param detail: 各个大区下的具体省份、区域、国家的时间戳及相应时间的指标数值
        :type detail: list[:class:`huaweicloudsdklive.v2.AreaTimeValue`]
        """
        
        

        self._area = None
        self._summary = None
        self._detail = None
        self.discriminator = None

        self.area = area
        self.summary = summary
        self.detail = detail

    @property
    def area(self):
        """Gets the area of this AreaDetail.

        各个计费大区名称，例如CN

        :return: The area of this AreaDetail.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this AreaDetail.

        各个计费大区名称，例如CN

        :param area: The area of this AreaDetail.
        :type area: str
        """
        self._area = area

    @property
    def summary(self):
        """Gets the summary of this AreaDetail.

        时间戳及相应时间的指标数值

        :return: The summary of this AreaDetail.
        :rtype: list[:class:`huaweicloudsdklive.v2.TimeValue`]
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this AreaDetail.

        时间戳及相应时间的指标数值

        :param summary: The summary of this AreaDetail.
        :type summary: list[:class:`huaweicloudsdklive.v2.TimeValue`]
        """
        self._summary = summary

    @property
    def detail(self):
        """Gets the detail of this AreaDetail.

        各个大区下的具体省份、区域、国家的时间戳及相应时间的指标数值

        :return: The detail of this AreaDetail.
        :rtype: list[:class:`huaweicloudsdklive.v2.AreaTimeValue`]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this AreaDetail.

        各个大区下的具体省份、区域、国家的时间戳及相应时间的指标数值

        :param detail: The detail of this AreaDetail.
        :type detail: list[:class:`huaweicloudsdklive.v2.AreaTimeValue`]
        """
        self._detail = detail

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
        if not isinstance(other, AreaDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
