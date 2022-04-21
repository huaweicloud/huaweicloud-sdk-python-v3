# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKeysRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'marker': 'str',
        'key_state': 'str',
        'key_spec': 'str',
        'enterprise_project_id': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'key_state': 'key_state',
        'key_spec': 'key_spec',
        'enterprise_project_id': 'enterprise_project_id',
        'sequence': 'sequence'
    }

    def __init__(self, limit=None, marker=None, key_state=None, key_spec=None, enterprise_project_id=None, sequence=None):
        """ListKeysRequestBody

        The model defined in huaweicloud sdk

        :param limit: 指定查询返回记录条数，如果指定查询记录条数小于存在的条数，响应参数“truncated”将返回“true”，表示存在分页。取值在密钥最大个数范围以内。例如：100
        :type limit: str
        :param marker: 分页查询起始位置标识。分页查询收到的响应参数“truncated”为“true”时，可以发送连续的请求获取更多的记录条数，“marker”设置为响应的next_marker的值。例如：10
        :type marker: str
        :param key_state: 密钥状态，满足正则匹配“^[1-5]{1}$”，枚举如下：  - “1”表示待激活状态  - “2”表示启用状态  - “3”表示禁用状态  - “4”表示计划删除状态  - “5”表示等待导入状态
        :type key_state: str
        :param key_spec: 密钥生成算法，默认为“AES_256”。查询所有（包含非对称）密钥需要指定参数“ALL”。  - AES_256  - SM4  - RSA_2048  - RSA_3072  - RSA_4096  - EC_P256  - EC_P384  - SM2  - ALL
        :type key_spec: str
        :param enterprise_project_id: 企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件. - 取值为“all” - 取值为“0” - 满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”
        :type enterprise_project_id: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        """
        
        

        self._limit = None
        self._marker = None
        self._key_state = None
        self._key_spec = None
        self._enterprise_project_id = None
        self._sequence = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if key_state is not None:
            self.key_state = key_state
        if key_spec is not None:
            self.key_spec = key_spec
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if sequence is not None:
            self.sequence = sequence

    @property
    def limit(self):
        """Gets the limit of this ListKeysRequestBody.

        指定查询返回记录条数，如果指定查询记录条数小于存在的条数，响应参数“truncated”将返回“true”，表示存在分页。取值在密钥最大个数范围以内。例如：100

        :return: The limit of this ListKeysRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListKeysRequestBody.

        指定查询返回记录条数，如果指定查询记录条数小于存在的条数，响应参数“truncated”将返回“true”，表示存在分页。取值在密钥最大个数范围以内。例如：100

        :param limit: The limit of this ListKeysRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListKeysRequestBody.

        分页查询起始位置标识。分页查询收到的响应参数“truncated”为“true”时，可以发送连续的请求获取更多的记录条数，“marker”设置为响应的next_marker的值。例如：10

        :return: The marker of this ListKeysRequestBody.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListKeysRequestBody.

        分页查询起始位置标识。分页查询收到的响应参数“truncated”为“true”时，可以发送连续的请求获取更多的记录条数，“marker”设置为响应的next_marker的值。例如：10

        :param marker: The marker of this ListKeysRequestBody.
        :type marker: str
        """
        self._marker = marker

    @property
    def key_state(self):
        """Gets the key_state of this ListKeysRequestBody.

        密钥状态，满足正则匹配“^[1-5]{1}$”，枚举如下：  - “1”表示待激活状态  - “2”表示启用状态  - “3”表示禁用状态  - “4”表示计划删除状态  - “5”表示等待导入状态

        :return: The key_state of this ListKeysRequestBody.
        :rtype: str
        """
        return self._key_state

    @key_state.setter
    def key_state(self, key_state):
        """Sets the key_state of this ListKeysRequestBody.

        密钥状态，满足正则匹配“^[1-5]{1}$”，枚举如下：  - “1”表示待激活状态  - “2”表示启用状态  - “3”表示禁用状态  - “4”表示计划删除状态  - “5”表示等待导入状态

        :param key_state: The key_state of this ListKeysRequestBody.
        :type key_state: str
        """
        self._key_state = key_state

    @property
    def key_spec(self):
        """Gets the key_spec of this ListKeysRequestBody.

        密钥生成算法，默认为“AES_256”。查询所有（包含非对称）密钥需要指定参数“ALL”。  - AES_256  - SM4  - RSA_2048  - RSA_3072  - RSA_4096  - EC_P256  - EC_P384  - SM2  - ALL

        :return: The key_spec of this ListKeysRequestBody.
        :rtype: str
        """
        return self._key_spec

    @key_spec.setter
    def key_spec(self, key_spec):
        """Sets the key_spec of this ListKeysRequestBody.

        密钥生成算法，默认为“AES_256”。查询所有（包含非对称）密钥需要指定参数“ALL”。  - AES_256  - SM4  - RSA_2048  - RSA_3072  - RSA_4096  - EC_P256  - EC_P384  - SM2  - ALL

        :param key_spec: The key_spec of this ListKeysRequestBody.
        :type key_spec: str
        """
        self._key_spec = key_spec

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListKeysRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件. - 取值为“all” - 取值为“0” - 满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :return: The enterprise_project_id of this ListKeysRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListKeysRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件. - 取值为“all” - 取值为“0” - 满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :param enterprise_project_id: The enterprise_project_id of this ListKeysRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def sequence(self):
        """Gets the sequence of this ListKeysRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this ListKeysRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this ListKeysRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this ListKeysRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

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
        if not isinstance(other, ListKeysRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
