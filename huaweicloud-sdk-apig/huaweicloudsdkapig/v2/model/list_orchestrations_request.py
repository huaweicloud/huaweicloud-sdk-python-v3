# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrchestrationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'orchestration_name': 'str',
        'precise_search': 'str',
        'orchestration_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'orchestration_name': 'orchestration_name',
        'precise_search': 'precise_search',
        'orchestration_id': 'orchestration_id'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, orchestration_name=None, precise_search=None, orchestration_id=None):
        r"""ListOrchestrationsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param orchestration_name: 编排规则名称。
        :type orchestration_name: str
        :param precise_search: 指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。当前仅支持orchestration_name。
        :type precise_search: str
        :param orchestration_id: 编排规则编号。  支持指定多个编号作为查询条件，多个参数之间使用“,”隔开，支持的查询参数个数与api允许绑定的参数规则上限保持一致，具体请参考产品介绍的“配额说明”章节。
        :type orchestration_id: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._orchestration_name = None
        self._precise_search = None
        self._orchestration_id = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if orchestration_name is not None:
            self.orchestration_name = orchestration_name
        if precise_search is not None:
            self.precise_search = precise_search
        if orchestration_id is not None:
            self.orchestration_id = orchestration_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListOrchestrationsRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListOrchestrationsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListOrchestrationsRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListOrchestrationsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListOrchestrationsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListOrchestrationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOrchestrationsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListOrchestrationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOrchestrationsRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListOrchestrationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOrchestrationsRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListOrchestrationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def orchestration_name(self):
        r"""Gets the orchestration_name of this ListOrchestrationsRequest.

        编排规则名称。

        :return: The orchestration_name of this ListOrchestrationsRequest.
        :rtype: str
        """
        return self._orchestration_name

    @orchestration_name.setter
    def orchestration_name(self, orchestration_name):
        r"""Sets the orchestration_name of this ListOrchestrationsRequest.

        编排规则名称。

        :param orchestration_name: The orchestration_name of this ListOrchestrationsRequest.
        :type orchestration_name: str
        """
        self._orchestration_name = orchestration_name

    @property
    def precise_search(self):
        r"""Gets the precise_search of this ListOrchestrationsRequest.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。当前仅支持orchestration_name。

        :return: The precise_search of this ListOrchestrationsRequest.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        r"""Sets the precise_search of this ListOrchestrationsRequest.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。当前仅支持orchestration_name。

        :param precise_search: The precise_search of this ListOrchestrationsRequest.
        :type precise_search: str
        """
        self._precise_search = precise_search

    @property
    def orchestration_id(self):
        r"""Gets the orchestration_id of this ListOrchestrationsRequest.

        编排规则编号。  支持指定多个编号作为查询条件，多个参数之间使用“,”隔开，支持的查询参数个数与api允许绑定的参数规则上限保持一致，具体请参考产品介绍的“配额说明”章节。

        :return: The orchestration_id of this ListOrchestrationsRequest.
        :rtype: str
        """
        return self._orchestration_id

    @orchestration_id.setter
    def orchestration_id(self, orchestration_id):
        r"""Sets the orchestration_id of this ListOrchestrationsRequest.

        编排规则编号。  支持指定多个编号作为查询条件，多个参数之间使用“,”隔开，支持的查询参数个数与api允许绑定的参数规则上限保持一致，具体请参考产品介绍的“配额说明”章节。

        :param orchestration_id: The orchestration_id of this ListOrchestrationsRequest.
        :type orchestration_id: str
        """
        self._orchestration_id = orchestration_id

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
        if not isinstance(other, ListOrchestrationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
