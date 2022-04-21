# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelineTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'region_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'region_id': 'region_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, region_id=None, offset=None, limit=None):
        """ListPipelineTemplatesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言类型 中文:zh-cn 英文:en-us
        :type x_language: str
        :param region_id: 区域id
        :type region_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，默认0
        :type offset: int
        :param limit: 每页显示的条目数量，默认10
        :type limit: int
        """
        
        

        self._x_language = None
        self._region_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.region_id = region_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListPipelineTemplatesRequest.

        语言类型 中文:zh-cn 英文:en-us

        :return: The x_language of this ListPipelineTemplatesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListPipelineTemplatesRequest.

        语言类型 中文:zh-cn 英文:en-us

        :param x_language: The x_language of this ListPipelineTemplatesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def region_id(self):
        """Gets the region_id of this ListPipelineTemplatesRequest.

        区域id

        :return: The region_id of this ListPipelineTemplatesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListPipelineTemplatesRequest.

        区域id

        :param region_id: The region_id of this ListPipelineTemplatesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def offset(self):
        """Gets the offset of this ListPipelineTemplatesRequest.

        偏移量，表示从此偏移量开始查询，默认0

        :return: The offset of this ListPipelineTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPipelineTemplatesRequest.

        偏移量，表示从此偏移量开始查询，默认0

        :param offset: The offset of this ListPipelineTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPipelineTemplatesRequest.

        每页显示的条目数量，默认10

        :return: The limit of this ListPipelineTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPipelineTemplatesRequest.

        每页显示的条目数量，默认10

        :param limit: The limit of this ListPipelineTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListPipelineTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
