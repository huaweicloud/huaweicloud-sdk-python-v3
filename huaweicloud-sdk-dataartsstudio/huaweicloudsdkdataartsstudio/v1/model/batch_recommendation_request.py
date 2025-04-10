# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRecommendationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recommendations': 'list[Recommendation]',
        'guids': 'list[str]',
        'add_type': 'str'
    }

    attribute_map = {
        'recommendations': 'recommendations',
        'guids': 'guids',
        'add_type': 'add_type'
    }

    def __init__(self, recommendations=None, guids=None, add_type=None):
        r"""BatchRecommendationRequest

        The model defined in huaweicloud sdk

        :param recommendations: 标签信息。
        :type recommendations: list[:class:`huaweicloudsdkdataartsstudio.v1.Recommendation`]
        :param guids: 资产guid。
        :type guids: list[str]
        :param add_type: 添加资产类型。cover：覆盖  追加：append。默认追加。
        :type add_type: str
        """
        
        

        self._recommendations = None
        self._guids = None
        self._add_type = None
        self.discriminator = None

        if recommendations is not None:
            self.recommendations = recommendations
        if guids is not None:
            self.guids = guids
        if add_type is not None:
            self.add_type = add_type

    @property
    def recommendations(self):
        r"""Gets the recommendations of this BatchRecommendationRequest.

        标签信息。

        :return: The recommendations of this BatchRecommendationRequest.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Recommendation`]
        """
        return self._recommendations

    @recommendations.setter
    def recommendations(self, recommendations):
        r"""Sets the recommendations of this BatchRecommendationRequest.

        标签信息。

        :param recommendations: The recommendations of this BatchRecommendationRequest.
        :type recommendations: list[:class:`huaweicloudsdkdataartsstudio.v1.Recommendation`]
        """
        self._recommendations = recommendations

    @property
    def guids(self):
        r"""Gets the guids of this BatchRecommendationRequest.

        资产guid。

        :return: The guids of this BatchRecommendationRequest.
        :rtype: list[str]
        """
        return self._guids

    @guids.setter
    def guids(self, guids):
        r"""Sets the guids of this BatchRecommendationRequest.

        资产guid。

        :param guids: The guids of this BatchRecommendationRequest.
        :type guids: list[str]
        """
        self._guids = guids

    @property
    def add_type(self):
        r"""Gets the add_type of this BatchRecommendationRequest.

        添加资产类型。cover：覆盖  追加：append。默认追加。

        :return: The add_type of this BatchRecommendationRequest.
        :rtype: str
        """
        return self._add_type

    @add_type.setter
    def add_type(self, add_type):
        r"""Sets the add_type of this BatchRecommendationRequest.

        添加资产类型。cover：覆盖  追加：append。默认追加。

        :param add_type: The add_type of this BatchRecommendationRequest.
        :type add_type: str
        """
        self._add_type = add_type

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
        if not isinstance(other, BatchRecommendationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
