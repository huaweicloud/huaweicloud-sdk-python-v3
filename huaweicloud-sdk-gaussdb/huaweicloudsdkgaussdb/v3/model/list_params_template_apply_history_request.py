# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListParamsTemplateApplyHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'config_id': 'config_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, config_id=None, limit=None, offset=None):
        """ListParamsTemplateApplyHistoryRequest

        The model defined in huaweicloud sdk

        :param config_id: 参数组ID。
        :type config_id: str
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        """
        
        

        self._config_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.config_id = config_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def config_id(self):
        """Gets the config_id of this ListParamsTemplateApplyHistoryRequest.

        参数组ID。

        :return: The config_id of this ListParamsTemplateApplyHistoryRequest.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this ListParamsTemplateApplyHistoryRequest.

        参数组ID。

        :param config_id: The config_id of this ListParamsTemplateApplyHistoryRequest.
        :type config_id: str
        """
        self._config_id = config_id

    @property
    def limit(self):
        """Gets the limit of this ListParamsTemplateApplyHistoryRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListParamsTemplateApplyHistoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListParamsTemplateApplyHistoryRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListParamsTemplateApplyHistoryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListParamsTemplateApplyHistoryRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListParamsTemplateApplyHistoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListParamsTemplateApplyHistoryRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListParamsTemplateApplyHistoryRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListParamsTemplateApplyHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
