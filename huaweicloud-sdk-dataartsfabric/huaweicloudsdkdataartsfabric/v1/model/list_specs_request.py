# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpecsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'spec_types': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'scenario': 'SpecScenario'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'spec_types': 'spec_types',
        'offset': 'offset',
        'limit': 'limit',
        'scenario': 'scenario'
    }

    def __init__(self, spec_code=None, spec_types=None, offset=None, limit=None, scenario=None):
        r"""ListSpecsRequest

        The model defined in huaweicloud sdk

        :param spec_code: 规格编码
        :type spec_code: str
        :param spec_types: 通过资源规格类型检索
        :type spec_types: list[str]
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。
        :type offset: int
        :param limit: 指定每一页返回的最大条目数，取值范围[1,100]，默认为10。
        :type limit: int
        :param scenario: 规格使用场景，不填表示不限制： COMPUTE: 用于购买Ray计算资源时配置的物理节点规格 ENDPOINT: 用于创建Endpoint时配置的资源组规格大小
        :type scenario: :class:`huaweicloudsdkdataartsfabric.v1.SpecScenario`
        """
        
        

        self._spec_code = None
        self._spec_types = None
        self._offset = None
        self._limit = None
        self._scenario = None
        self.discriminator = None

        if spec_code is not None:
            self.spec_code = spec_code
        if spec_types is not None:
            self.spec_types = spec_types
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if scenario is not None:
            self.scenario = scenario

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ListSpecsRequest.

        规格编码

        :return: The spec_code of this ListSpecsRequest.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ListSpecsRequest.

        规格编码

        :param spec_code: The spec_code of this ListSpecsRequest.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def spec_types(self):
        r"""Gets the spec_types of this ListSpecsRequest.

        通过资源规格类型检索

        :return: The spec_types of this ListSpecsRequest.
        :rtype: list[str]
        """
        return self._spec_types

    @spec_types.setter
    def spec_types(self, spec_types):
        r"""Sets the spec_types of this ListSpecsRequest.

        通过资源规格类型检索

        :param spec_types: The spec_types of this ListSpecsRequest.
        :type spec_types: list[str]
        """
        self._spec_types = spec_types

    @property
    def offset(self):
        r"""Gets the offset of this ListSpecsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :return: The offset of this ListSpecsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSpecsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :param offset: The offset of this ListSpecsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSpecsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :return: The limit of this ListSpecsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSpecsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :param limit: The limit of this ListSpecsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def scenario(self):
        r"""Gets the scenario of this ListSpecsRequest.

        规格使用场景，不填表示不限制： COMPUTE: 用于购买Ray计算资源时配置的物理节点规格 ENDPOINT: 用于创建Endpoint时配置的资源组规格大小

        :return: The scenario of this ListSpecsRequest.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.SpecScenario`
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        r"""Sets the scenario of this ListSpecsRequest.

        规格使用场景，不填表示不限制： COMPUTE: 用于购买Ray计算资源时配置的物理节点规格 ENDPOINT: 用于创建Endpoint时配置的资源组规格大小

        :param scenario: The scenario of this ListSpecsRequest.
        :type scenario: :class:`huaweicloudsdkdataartsfabric.v1.SpecScenario`
        """
        self._scenario = scenario

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
        if not isinstance(other, ListSpecsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
