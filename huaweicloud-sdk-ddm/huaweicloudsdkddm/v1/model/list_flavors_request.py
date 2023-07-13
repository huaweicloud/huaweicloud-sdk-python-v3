# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'engine_id': 'engine_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, engine_id=None, offset=None, limit=None):
        """ListFlavorsRequest

        The model defined in huaweicloud sdk

        :param engine_id: 引擎id,通过查询DDM引擎信息接口获取。
        :type engine_id: str
        :param offset: 分页参数：起始值 [大于等于0] 。默认值是0。
        :type offset: int
        :param limit: 分页参数：每页多少条 [大于0且小于等于128]。默认值是128。
        :type limit: int
        """
        
        

        self._engine_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.engine_id = engine_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def engine_id(self):
        """Gets the engine_id of this ListFlavorsRequest.

        引擎id,通过查询DDM引擎信息接口获取。

        :return: The engine_id of this ListFlavorsRequest.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this ListFlavorsRequest.

        引擎id,通过查询DDM引擎信息接口获取。

        :param engine_id: The engine_id of this ListFlavorsRequest.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def offset(self):
        """Gets the offset of this ListFlavorsRequest.

        分页参数：起始值 [大于等于0] 。默认值是0。

        :return: The offset of this ListFlavorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFlavorsRequest.

        分页参数：起始值 [大于等于0] 。默认值是0。

        :param offset: The offset of this ListFlavorsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListFlavorsRequest.

        分页参数：每页多少条 [大于0且小于等于128]。默认值是128。

        :return: The limit of this ListFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFlavorsRequest.

        分页参数：每页多少条 [大于0且小于等于128]。默认值是128。

        :param limit: The limit of this ListFlavorsRequest.
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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
