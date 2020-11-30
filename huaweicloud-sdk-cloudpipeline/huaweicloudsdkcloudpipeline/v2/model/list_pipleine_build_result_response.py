# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPipleineBuildResultResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'total': 'int',
        'build_results': 'list[PipelineBuildResult]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total',
        'build_results': 'build_results'
    }

    def __init__(self, offset=None, limit=None, total=None, build_results=None):
        """ListPipleineBuildResultResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._offset = None
        self._limit = None
        self._total = None
        self._build_results = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if build_results is not None:
            self.build_results = build_results

    @property
    def offset(self):
        """Gets the offset of this ListPipleineBuildResultResponse.

        偏移量,表示从此偏移量开始查询,offset大于等于0

        :return: The offset of this ListPipleineBuildResultResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPipleineBuildResultResponse.

        偏移量,表示从此偏移量开始查询,offset大于等于0

        :param offset: The offset of this ListPipleineBuildResultResponse.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPipleineBuildResultResponse.

        每次查询的条目数量

        :return: The limit of this ListPipleineBuildResultResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPipleineBuildResultResponse.

        每次查询的条目数量

        :param limit: The limit of this ListPipleineBuildResultResponse.
        :type: int
        """
        self._limit = limit

    @property
    def total(self):
        """Gets the total of this ListPipleineBuildResultResponse.

        总条目数量

        :return: The total of this ListPipleineBuildResultResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListPipleineBuildResultResponse.

        总条目数量

        :param total: The total of this ListPipleineBuildResultResponse.
        :type: int
        """
        self._total = total

    @property
    def build_results(self):
        """Gets the build_results of this ListPipleineBuildResultResponse.

        执行状况数据列表

        :return: The build_results of this ListPipleineBuildResultResponse.
        :rtype: list[PipelineBuildResult]
        """
        return self._build_results

    @build_results.setter
    def build_results(self, build_results):
        """Sets the build_results of this ListPipleineBuildResultResponse.

        执行状况数据列表

        :param build_results: The build_results of this ListPipleineBuildResultResponse.
        :type: list[PipelineBuildResult]
        """
        self._build_results = build_results

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListPipleineBuildResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
