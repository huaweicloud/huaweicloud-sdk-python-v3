# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'engine_name': 'str',
        'engine_version': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, engine_name=None, engine_version=None, offset=None, limit=None):
        """ListFlavorInfosRequest

        The model defined in huaweicloud sdk

        :param engine_name: 数据库版本类型。取值为“DDS-Community”。
        :type engine_name: str
        :param engine_version: 数据库版本号。
        :type engine_version: str
        :param offset: 索引位置，偏移量。   - 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。   - 取值必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询规格信息上限值。   - 取值范围: 1~100。   - 不传该参数时，默认查询前100条规格信息。
        :type limit: int
        """
        
        

        self._engine_name = None
        self._engine_version = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def engine_name(self):
        """Gets the engine_name of this ListFlavorInfosRequest.

        数据库版本类型。取值为“DDS-Community”。

        :return: The engine_name of this ListFlavorInfosRequest.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this ListFlavorInfosRequest.

        数据库版本类型。取值为“DDS-Community”。

        :param engine_name: The engine_name of this ListFlavorInfosRequest.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        """Gets the engine_version of this ListFlavorInfosRequest.

        数据库版本号。

        :return: The engine_version of this ListFlavorInfosRequest.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ListFlavorInfosRequest.

        数据库版本号。

        :param engine_version: The engine_version of this ListFlavorInfosRequest.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def offset(self):
        """Gets the offset of this ListFlavorInfosRequest.

        索引位置，偏移量。   - 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。   - 取值必须为数字，不能为负数。

        :return: The offset of this ListFlavorInfosRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFlavorInfosRequest.

        索引位置，偏移量。   - 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。   - 取值必须为数字，不能为负数。

        :param offset: The offset of this ListFlavorInfosRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListFlavorInfosRequest.

        查询规格信息上限值。   - 取值范围: 1~100。   - 不传该参数时，默认查询前100条规格信息。

        :return: The limit of this ListFlavorInfosRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFlavorInfosRequest.

        查询规格信息上限值。   - 取值范围: 1~100。   - 不传该参数时，默认查询前100条规格信息。

        :param limit: The limit of this ListFlavorInfosRequest.
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
        if not isinstance(other, ListFlavorInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
