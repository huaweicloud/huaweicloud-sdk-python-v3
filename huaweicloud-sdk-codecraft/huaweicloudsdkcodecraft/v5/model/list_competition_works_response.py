# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCompetitionWorksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'works': 'list[ListWorksResponseModel]',
        'total': 'int'
    }

    attribute_map = {
        'works': 'works',
        'total': 'total'
    }

    def __init__(self, works=None, total=None):
        """ListCompetitionWorksResponse

        The model defined in huaweicloud sdk

        :param works: 作品列表
        :type works: list[:class:`huaweicloudsdkcodecraft.v5.ListWorksResponseModel`]
        :param total: 作品总数
        :type total: int
        """
        
        super(ListCompetitionWorksResponse, self).__init__()

        self._works = None
        self._total = None
        self.discriminator = None

        if works is not None:
            self.works = works
        if total is not None:
            self.total = total

    @property
    def works(self):
        """Gets the works of this ListCompetitionWorksResponse.

        作品列表

        :return: The works of this ListCompetitionWorksResponse.
        :rtype: list[:class:`huaweicloudsdkcodecraft.v5.ListWorksResponseModel`]
        """
        return self._works

    @works.setter
    def works(self, works):
        """Sets the works of this ListCompetitionWorksResponse.

        作品列表

        :param works: The works of this ListCompetitionWorksResponse.
        :type works: list[:class:`huaweicloudsdkcodecraft.v5.ListWorksResponseModel`]
        """
        self._works = works

    @property
    def total(self):
        """Gets the total of this ListCompetitionWorksResponse.

        作品总数

        :return: The total of this ListCompetitionWorksResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCompetitionWorksResponse.

        作品总数

        :param total: The total of this ListCompetitionWorksResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListCompetitionWorksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
