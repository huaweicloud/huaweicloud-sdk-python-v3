# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceParamResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'updated': 'str',
        'configuration_parameter': 'list[ConfigurationParameterList]',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'updated': 'updated',
        'configuration_parameter': 'configuration_parameter',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, updated=None, configuration_parameter=None, offset=None, limit=None, total=None):
        """ShowInstanceParamResponse

        The model defined in huaweicloud sdk

        :param updated: DDM参数最后更新时间。
        :type updated: str
        :param configuration_parameter: DDM实例参数信息列表的集合。
        :type configuration_parameter: list[:class:`huaweicloudsdkddm.v1.ConfigurationParameterList`]
        :param offset: 分页参数: 起始值。
        :type offset: int
        :param limit: 分页参数：每页多少条。
        :type limit: int
        :param total: 集合总数
        :type total: int
        """
        
        super(ShowInstanceParamResponse, self).__init__()

        self._updated = None
        self._configuration_parameter = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if updated is not None:
            self.updated = updated
        if configuration_parameter is not None:
            self.configuration_parameter = configuration_parameter
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def updated(self):
        """Gets the updated of this ShowInstanceParamResponse.

        DDM参数最后更新时间。

        :return: The updated of this ShowInstanceParamResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowInstanceParamResponse.

        DDM参数最后更新时间。

        :param updated: The updated of this ShowInstanceParamResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def configuration_parameter(self):
        """Gets the configuration_parameter of this ShowInstanceParamResponse.

        DDM实例参数信息列表的集合。

        :return: The configuration_parameter of this ShowInstanceParamResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.ConfigurationParameterList`]
        """
        return self._configuration_parameter

    @configuration_parameter.setter
    def configuration_parameter(self, configuration_parameter):
        """Sets the configuration_parameter of this ShowInstanceParamResponse.

        DDM实例参数信息列表的集合。

        :param configuration_parameter: The configuration_parameter of this ShowInstanceParamResponse.
        :type configuration_parameter: list[:class:`huaweicloudsdkddm.v1.ConfigurationParameterList`]
        """
        self._configuration_parameter = configuration_parameter

    @property
    def offset(self):
        """Gets the offset of this ShowInstanceParamResponse.

        分页参数: 起始值。

        :return: The offset of this ShowInstanceParamResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowInstanceParamResponse.

        分页参数: 起始值。

        :param offset: The offset of this ShowInstanceParamResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowInstanceParamResponse.

        分页参数：每页多少条。

        :return: The limit of this ShowInstanceParamResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowInstanceParamResponse.

        分页参数：每页多少条。

        :param limit: The limit of this ShowInstanceParamResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        """Gets the total of this ShowInstanceParamResponse.

        集合总数

        :return: The total of this ShowInstanceParamResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowInstanceParamResponse.

        集合总数

        :param total: The total of this ShowInstanceParamResponse.
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
        if not isinstance(other, ShowInstanceParamResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
