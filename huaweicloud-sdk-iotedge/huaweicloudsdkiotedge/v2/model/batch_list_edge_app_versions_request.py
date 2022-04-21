# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListEdgeAppVersionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'version': 'str',
        'offset': 'int',
        'limit': 'int',
        'ai_card_type': 'str',
        'arch': 'str',
        'state': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'version': 'version',
        'offset': 'offset',
        'limit': 'limit',
        'ai_card_type': 'ai_card_type',
        'arch': 'arch',
        'state': 'state'
    }

    def __init__(self, edge_app_id=None, version=None, offset=None, limit=None, ai_card_type=None, arch=None, state=None):
        """BatchListEdgeAppVersionsRequest

        The model defined in huaweicloud sdk

        :param edge_app_id: 应用版本,应用内版本唯一。
        :type edge_app_id: str
        :param version: 应用版本搜索关键字
        :type version: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: int
        :param limit: 每页记录数，默认值为10，取值区间为1-1000
        :type limit: int
        :param ai_card_type: ai加速卡类型
        :type ai_card_type: str
        :param arch: 支持架构
        :type arch: str
        :param state: 应用版本状态
        :type state: str
        """
        
        

        self._edge_app_id = None
        self._version = None
        self._offset = None
        self._limit = None
        self._ai_card_type = None
        self._arch = None
        self._state = None
        self.discriminator = None

        self.edge_app_id = edge_app_id
        if version is not None:
            self.version = version
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if ai_card_type is not None:
            self.ai_card_type = ai_card_type
        if arch is not None:
            self.arch = arch
        if state is not None:
            self.state = state

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this BatchListEdgeAppVersionsRequest.

        应用版本,应用内版本唯一。

        :return: The edge_app_id of this BatchListEdgeAppVersionsRequest.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this BatchListEdgeAppVersionsRequest.

        应用版本,应用内版本唯一。

        :param edge_app_id: The edge_app_id of this BatchListEdgeAppVersionsRequest.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def version(self):
        """Gets the version of this BatchListEdgeAppVersionsRequest.

        应用版本搜索关键字

        :return: The version of this BatchListEdgeAppVersionsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BatchListEdgeAppVersionsRequest.

        应用版本搜索关键字

        :param version: The version of this BatchListEdgeAppVersionsRequest.
        :type version: str
        """
        self._version = version

    @property
    def offset(self):
        """Gets the offset of this BatchListEdgeAppVersionsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this BatchListEdgeAppVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BatchListEdgeAppVersionsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this BatchListEdgeAppVersionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this BatchListEdgeAppVersionsRequest.

        每页记录数，默认值为10，取值区间为1-1000

        :return: The limit of this BatchListEdgeAppVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this BatchListEdgeAppVersionsRequest.

        每页记录数，默认值为10，取值区间为1-1000

        :param limit: The limit of this BatchListEdgeAppVersionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def ai_card_type(self):
        """Gets the ai_card_type of this BatchListEdgeAppVersionsRequest.

        ai加速卡类型

        :return: The ai_card_type of this BatchListEdgeAppVersionsRequest.
        :rtype: str
        """
        return self._ai_card_type

    @ai_card_type.setter
    def ai_card_type(self, ai_card_type):
        """Sets the ai_card_type of this BatchListEdgeAppVersionsRequest.

        ai加速卡类型

        :param ai_card_type: The ai_card_type of this BatchListEdgeAppVersionsRequest.
        :type ai_card_type: str
        """
        self._ai_card_type = ai_card_type

    @property
    def arch(self):
        """Gets the arch of this BatchListEdgeAppVersionsRequest.

        支持架构

        :return: The arch of this BatchListEdgeAppVersionsRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this BatchListEdgeAppVersionsRequest.

        支持架构

        :param arch: The arch of this BatchListEdgeAppVersionsRequest.
        :type arch: str
        """
        self._arch = arch

    @property
    def state(self):
        """Gets the state of this BatchListEdgeAppVersionsRequest.

        应用版本状态

        :return: The state of this BatchListEdgeAppVersionsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BatchListEdgeAppVersionsRequest.

        应用版本状态

        :param state: The state of this BatchListEdgeAppVersionsRequest.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, BatchListEdgeAppVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
