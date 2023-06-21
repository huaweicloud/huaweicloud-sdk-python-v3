# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTechnicalAssetsStatisticRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'tag': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'tag': 'tag',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, workspace=None, tag=None, offset=None, limit=None):
        """ShowTechnicalAssetsStatisticRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param tag: 标签名，指定标签名称可以获取此标签对应技术资产的统计信息。
        :type tag: str
        :param offset: 分页参数，查询偏移量，默认查询所有
        :type offset: int
        :param limit: 分页参数，每页数量，默认查询所有
        :type limit: int
        """
        
        

        self._workspace = None
        self._tag = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.workspace = workspace
        if tag is not None:
            self.tag = tag
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def workspace(self):
        """Gets the workspace of this ShowTechnicalAssetsStatisticRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ShowTechnicalAssetsStatisticRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowTechnicalAssetsStatisticRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ShowTechnicalAssetsStatisticRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def tag(self):
        """Gets the tag of this ShowTechnicalAssetsStatisticRequest.

        标签名，指定标签名称可以获取此标签对应技术资产的统计信息。

        :return: The tag of this ShowTechnicalAssetsStatisticRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ShowTechnicalAssetsStatisticRequest.

        标签名，指定标签名称可以获取此标签对应技术资产的统计信息。

        :param tag: The tag of this ShowTechnicalAssetsStatisticRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def offset(self):
        """Gets the offset of this ShowTechnicalAssetsStatisticRequest.

        分页参数，查询偏移量，默认查询所有

        :return: The offset of this ShowTechnicalAssetsStatisticRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowTechnicalAssetsStatisticRequest.

        分页参数，查询偏移量，默认查询所有

        :param offset: The offset of this ShowTechnicalAssetsStatisticRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowTechnicalAssetsStatisticRequest.

        分页参数，每页数量，默认查询所有

        :return: The limit of this ShowTechnicalAssetsStatisticRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowTechnicalAssetsStatisticRequest.

        分页参数，每页数量，默认查询所有

        :param limit: The limit of this ShowTechnicalAssetsStatisticRequest.
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
        if not isinstance(other, ShowTechnicalAssetsStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
