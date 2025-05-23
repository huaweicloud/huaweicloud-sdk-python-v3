# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrchestrationAttachedApisRequest:

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
        'orchestration_id': 'str',
        'api_name': 'str',
        'api_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'orchestration_id': 'orchestration_id',
        'api_name': 'api_name',
        'api_id': 'api_id'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, orchestration_id=None, api_name=None, api_id=None):
        r"""ListOrchestrationAttachedApisRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param orchestration_id: 编排规则编号
        :type orchestration_id: str
        :param api_name: API名称。
        :type api_name: str
        :param api_id: API编号。
        :type api_id: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._orchestration_id = None
        self._api_name = None
        self._api_id = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.orchestration_id = orchestration_id
        if api_name is not None:
            self.api_name = api_name
        if api_id is not None:
            self.api_id = api_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListOrchestrationAttachedApisRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListOrchestrationAttachedApisRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListOrchestrationAttachedApisRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListOrchestrationAttachedApisRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListOrchestrationAttachedApisRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListOrchestrationAttachedApisRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOrchestrationAttachedApisRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListOrchestrationAttachedApisRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOrchestrationAttachedApisRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListOrchestrationAttachedApisRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOrchestrationAttachedApisRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListOrchestrationAttachedApisRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def orchestration_id(self):
        r"""Gets the orchestration_id of this ListOrchestrationAttachedApisRequest.

        编排规则编号

        :return: The orchestration_id of this ListOrchestrationAttachedApisRequest.
        :rtype: str
        """
        return self._orchestration_id

    @orchestration_id.setter
    def orchestration_id(self, orchestration_id):
        r"""Sets the orchestration_id of this ListOrchestrationAttachedApisRequest.

        编排规则编号

        :param orchestration_id: The orchestration_id of this ListOrchestrationAttachedApisRequest.
        :type orchestration_id: str
        """
        self._orchestration_id = orchestration_id

    @property
    def api_name(self):
        r"""Gets the api_name of this ListOrchestrationAttachedApisRequest.

        API名称。

        :return: The api_name of this ListOrchestrationAttachedApisRequest.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        r"""Sets the api_name of this ListOrchestrationAttachedApisRequest.

        API名称。

        :param api_name: The api_name of this ListOrchestrationAttachedApisRequest.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def api_id(self):
        r"""Gets the api_id of this ListOrchestrationAttachedApisRequest.

        API编号。

        :return: The api_id of this ListOrchestrationAttachedApisRequest.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this ListOrchestrationAttachedApisRequest.

        API编号。

        :param api_id: The api_id of this ListOrchestrationAttachedApisRequest.
        :type api_id: str
        """
        self._api_id = api_id

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
        if not isinstance(other, ListOrchestrationAttachedApisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
